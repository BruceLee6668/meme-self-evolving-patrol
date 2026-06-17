from __future__ import annotations

import hashlib
import math
import re
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .dexscreener_client import DexScreenerClient
from .geckoterminal_client import GeckoTerminalClient

CHAIN_MAP = {
    "bsc": {"dex": "bsc", "gecko": "bsc", "label": "BSC"},
    "solana": {"dex": "solana", "gecko": "solana", "label": "SOL"},
}

# v0.4: keeps v0.3 output and adds chain preflight + Smart Wallet weekly-cache integration in main.py.
SEARCH_QUERIES = [
    "four meme bsc",
    "four.meme",
    "pumpfun solana",
    "pump fun",
    "pumpswap",
    "meme bsc",
    "meme solana",
    "pancakeswap meme",
    "raydium meme",
    "meteora meme",
    "bnb meme",
    "solana meme",
]

STABLE_QUOTES = {"USDT", "USDC", "WBNB", "BNB", "SOL", "WSOL"}
COMMON_AMBIGUOUS_SYMBOLS = {
    "MEME", "MOON", "DOG", "CAT", "PEPE", "AI", "BTC", "ETH", "BNB", "SOL", "USDT", "USDC", "WBNB", "WSOL"
}


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except Exception:
        return default


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(float(value))
    except Exception:
        return default


def _round_or_none(v: Any, digits: int = 4) -> Optional[float]:
    try:
        if v is None:
            return None
        return round(float(v), digits)
    except Exception:
        return None


def _pair_key(pair: Dict[str, Any]) -> str:
    chain = pair.get("chainId") or pair.get("chain") or "unknown"
    pair_addr = pair.get("pairAddress") or pair.get("address") or pair.get("id") or ""
    base = (pair.get("baseToken") or {}).get("address") or pair.get("base_token_address") or ""
    raw = f"{chain}:{pair_addr}:{base}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _norm_address(addr: Any) -> str:
    return str(addr or "").strip().lower()


def _norm_symbol(v: Any) -> str:
    s = str(v or "UNKNOWN").strip().upper()
    # Remove noisy symbols so Gecko-only and Dex rows can bridge when they are likely the same token.
    s = re.sub(r"[^A-Z0-9_.$-]", "", s)
    return s or "UNKNOWN"




def _extract_gecko_token_address(pool: Dict[str, Any], network: str) -> Tuple[Optional[str], str]:
    """Best-effort token address extraction for GeckoTerminal pool payloads.

    GeckoTerminal pool objects usually expose base token through relationships such as
    data.id = "bsc_0x..." or "solana_<mint>". If the relationship is absent, keep it
    unavailable rather than inventing a contract address.
    """
    relationships = pool.get("relationships") or {}
    base = relationships.get("base_token") or {}
    data = base.get("data") or {}
    raw_id = str(data.get("id") or "").strip()
    if raw_id:
        prefix = f"{network}_"
        if raw_id.startswith(prefix):
            return raw_id[len(prefix):], "geckoterminal_relationship"
        if "_" in raw_id:
            return raw_id.split("_", 1)[1], "geckoterminal_relationship"
        return raw_id, "geckoterminal_relationship"
    return None, "unavailable"


def _contract_url(chain: Any, address: Any) -> Optional[str]:
    addr = str(address or "").strip()
    if not addr:
        return None
    if chain == "bsc":
        return f"https://bscscan.com/token/{addr}"
    if chain == "solana":
        return f"https://solscan.io/token/{addr}"
    return None


def _short_address(address: Any) -> str:
    addr = str(address or "").strip()
    if not addr:
        return "不可用"
    if len(addr) <= 14:
        return addr
    return f"{addr[:6]}...{addr[-6:]}"


def _liquidity_tier(lp: Any, strategy: Dict[str, Any]) -> str:
    th = strategy.get("thresholds", {})
    lpv = _safe_float(lp)
    micro_max = _safe_float(th.get("liquidity_tier_micro_max_usd"), 100_000)
    early_max = _safe_float(th.get("liquidity_tier_early_max_usd"), 750_000)
    liquid_max = _safe_float(th.get("liquidity_tier_liquid_max_usd"), 5_000_000)
    if lpv <= 0:
        return "Unknown"
    if lpv < micro_max:
        return "Micro"
    if lpv < early_max:
        return "Early"
    if lpv < liquid_max:
        return "Liquid"
    return "Mature"


def _needs_chain_verify(c: Dict[str, Any]) -> Tuple[bool, str, bool]:
    """Return (needs_chain_verify, reason, emergency_precision_check)."""
    status = c.get("classification")
    lp = _safe_float(c.get("liquidity_usd"))
    vol = _safe_float(c.get("volume_24h_usd"))
    ratio = c.get("volume_lp_ratio")
    chg24 = abs(_safe_float(c.get("price_change_24h_pct")))
    buys = _safe_int(c.get("buys_24h"))
    sells = _safe_int(c.get("sells_24h"))
    has_addr = bool(c.get("token_address"))

    reasons = []
    if status in {"主观察", "次观察"}:
        reasons.append("观察池候选需要链上Swap/钱包留存确认")
    if not has_addr:
        reasons.append("缺少合约地址，需补地址后才能链上确认")
    if c.get("multi_pool_conflict"):
        reasons.append("多池数据冲突，需链上/聚合源复核")
    if status == "PVP风险池":
        reasons.append("PVP候选仅记录，非紧急精查")

    emergency = (
        status == "主观察"
        and has_addr
        and lp >= 100_000
        and vol >= 50_000
        and chg24 <= 25
        and (ratio is None or _safe_float(ratio) <= 8)
        and buys > sells
        and not c.get("multi_pool_conflict")
    )
    if emergency:
        reasons.append("满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突")
    return bool(reasons), "；".join(reasons) if reasons else "暂不需要", emergency


def _token_identity(c: Dict[str, Any]) -> str:
    chain = c.get("chain") or "unknown"
    addr = _norm_address(c.get("token_address"))
    if addr:
        return f"{chain}:addr:{addr}"
    symbol = _norm_symbol(c.get("token"))
    name = _norm_symbol(str(c.get("token_name") or symbol).split("/")[0])
    return f"{chain}:sym:{symbol}:{name}"


def normalize_dex_pair(pair: Dict[str, Any], source: str = "dexscreener") -> Optional[Dict[str, Any]]:
    chain = pair.get("chainId")
    if chain not in {"bsc", "solana"}:
        return None

    base_token = pair.get("baseToken") or {}
    quote_token = pair.get("quoteToken") or {}
    liquidity = pair.get("liquidity") or {}
    volume = pair.get("volume") or {}
    txns = pair.get("txns") or {}
    price_change = pair.get("priceChange") or {}

    token_symbol = base_token.get("symbol") or base_token.get("name") or "UNKNOWN"
    token_name = base_token.get("name") or token_symbol
    token_address = base_token.get("address") or ""
    pair_address = pair.get("pairAddress") or ""
    dex_id = pair.get("dexId") or "unknown"

    volume_24h = _safe_float(volume.get("h24"))
    liquidity_usd = _safe_float(liquidity.get("usd"))
    price_usd = _safe_float(pair.get("priceUsd"))
    price_change_1h = _safe_float(price_change.get("h1"))
    price_change_6h = _safe_float(price_change.get("h6"))
    price_change_24h = _safe_float(price_change.get("h24"))

    buys_24h = _safe_int((txns.get("h24") or {}).get("buys"))
    sells_24h = _safe_int((txns.get("h24") or {}).get("sells"))
    buys_1h = _safe_int((txns.get("h1") or {}).get("buys"))
    sells_1h = _safe_int((txns.get("h1") or {}).get("sells"))
    txns_24h = buys_24h + sells_24h

    age_hours = None
    pair_created_at = pair.get("pairCreatedAt")
    if pair_created_at:
        try:
            created_ms = int(pair_created_at)
            created_dt = datetime.fromtimestamp(created_ms / 1000, tz=timezone.utc)
            age_hours = (datetime.now(timezone.utc) - created_dt).total_seconds() / 3600
        except Exception:
            age_hours = None

    quote_symbol = quote_token.get("symbol")
    symbol_norm = _norm_symbol(token_symbol)
    return {
        "source": source,
        "chain": chain,
        "chain_label": CHAIN_MAP[chain]["label"],
        "dex_id": dex_id,
        "token": token_symbol,
        "token_symbol_norm": symbol_norm,
        "token_name": token_name,
        "token_address": token_address,
        "contract_address": token_address,
        "contract_address_source": "dexscreener_base_token" if token_address else "unavailable",
        "contract_url": _contract_url(chain, token_address),
        "pair_address": pair_address,
        "quote_symbol": quote_symbol,
        "url": pair.get("url"),
        "price_usd": price_usd,
        "liquidity_usd": liquidity_usd,
        "volume_24h_usd": volume_24h,
        "volume_6h_usd": _safe_float(volume.get("h6")),
        "volume_1h_usd": _safe_float(volume.get("h1")),
        "price_change_1h_pct": price_change_1h,
        "price_change_6h_pct": price_change_6h,
        "price_change_24h_pct": price_change_24h,
        "buys_24h": buys_24h,
        "sells_24h": sells_24h,
        "buys_1h": buys_1h,
        "sells_1h": sells_1h,
        "txns_24h": txns_24h,
        "age_hours": age_hours,
        "volume_lp_ratio": volume_24h / liquidity_usd if liquidity_usd > 0 else None,
        "market_cap": _safe_float(pair.get("marketCap")),
        "fdv": _safe_float(pair.get("fdv")),
        "raw_pair_key": _pair_key(pair),
        "is_stable_quote": quote_symbol in STABLE_QUOTES if quote_symbol else False,
    }


def normalize_gecko_pool(pool: Dict[str, Any], network: str) -> Optional[Dict[str, Any]]:
    attrs = pool.get("attributes") or {}
    name = attrs.get("name") or "UNKNOWN"
    address = attrs.get("address") or pool.get("id", "").split("_")[-1]
    token_symbol = name.split("/")[0].strip() if "/" in name else name
    liquidity_usd = _safe_float(attrs.get("reserve_in_usd"))
    volume_usd = attrs.get("volume_usd") or {}
    price_change = attrs.get("price_change_percentage") or {}
    tx_count = attrs.get("transactions") or {}

    buys_24h = _safe_int(((tx_count.get("h24") or {}).get("buys")))
    sells_24h = _safe_int(((tx_count.get("h24") or {}).get("sells")))
    volume_24h = _safe_float(volume_usd.get("h24"))

    token_address, token_address_source = _extract_gecko_token_address(pool, network)

    return {
        "source": "geckoterminal",
        "chain": network,
        "chain_label": CHAIN_MAP.get(network, {}).get("label", network.upper()),
        "dex_id": attrs.get("dex_id") or "unknown",
        "token": token_symbol,
        "token_symbol_norm": _norm_symbol(token_symbol),
        "token_name": name,
        "token_address": token_address,
        "contract_address": token_address,
        "contract_address_source": token_address_source,
        "contract_url": _contract_url(network, token_address),
        "pair_address": address,
        "quote_symbol": None,
        "url": None,
        "price_usd": _safe_float(attrs.get("base_token_price_usd")),
        "liquidity_usd": liquidity_usd,
        "volume_24h_usd": volume_24h,
        "volume_6h_usd": _safe_float(volume_usd.get("h6")),
        "volume_1h_usd": _safe_float(volume_usd.get("h1")),
        "price_change_1h_pct": _safe_float(price_change.get("h1")),
        "price_change_6h_pct": _safe_float(price_change.get("h6")),
        "price_change_24h_pct": _safe_float(price_change.get("h24")),
        "buys_24h": buys_24h,
        "sells_24h": sells_24h,
        "buys_1h": _safe_int(((tx_count.get("h1") or {}).get("buys"))),
        "sells_1h": _safe_int(((tx_count.get("h1") or {}).get("sells"))),
        "txns_24h": buys_24h + sells_24h,
        "age_hours": None,
        "volume_lp_ratio": volume_24h / liquidity_usd if liquidity_usd > 0 else None,
        "market_cap": _safe_float(attrs.get("market_cap_usd")),
        "fdv": _safe_float(attrs.get("fdv_usd")),
        "raw_pair_key": f"gecko:{network}:{address}",
        "is_stable_quote": False,
    }


def _log_score(value: float, floor: float, cap: float, max_score: int) -> int:
    if value <= floor:
        return 0
    value = min(value, cap)
    if cap <= floor:
        return 0
    return int(round((math.log10(value) - math.log10(floor)) / (math.log10(cap) - math.log10(floor)) * max_score))


def _is_mature_pool(c: Dict[str, Any], strategy: Dict[str, Any]) -> Tuple[bool, List[str]]:
    th = strategy.get("thresholds", {})
    max_lp_main = _safe_float(th.get("max_lp_main_usd"), 5_000_000)
    max_fdv_main = _safe_float(th.get("max_fdv_main_usd"), 80_000_000)
    max_mcap_main = _safe_float(th.get("max_mcap_main_usd"), 80_000_000)
    mature_lp_warning = _safe_float(th.get("mature_lp_warning_usd"), 10_000_000)
    mature_market_warning = _safe_float(th.get("mature_market_warning_usd"), 120_000_000)

    lp = _safe_float(c.get("liquidity_usd"))
    fdv = _safe_float(c.get("fdv"))
    mcap = _safe_float(c.get("market_cap"))
    reasons = []
    if lp > max_lp_main:
        reasons.append("LP超过早期Alpha主榜上限")
    if fdv and fdv > max_fdv_main:
        reasons.append("FDV超过早期Alpha主榜上限")
    if mcap and mcap > max_mcap_main:
        reasons.append("市值超过早期Alpha主榜上限")
    if lp > mature_lp_warning:
        reasons.append("成熟大池")
    if (fdv and fdv > mature_market_warning) or (mcap and mcap > mature_market_warning):
        reasons.append("成熟大市值")
    return bool(reasons), reasons


def score_candidate(c: Dict[str, Any], strategy: Dict[str, Any]) -> Tuple[str, str, int, Dict[str, Any], List[str]]:
    th = strategy.get("thresholds", {})
    min_lp_main = _safe_float(th.get("min_lp_main_usd"), 100000)
    min_lp_secondary = _safe_float(th.get("min_lp_secondary_usd"), 50000)
    max_bottom_change = _safe_float(th.get("max_24h_change_bottom_pct"), 80)
    young_hours = _safe_float(th.get("young_token_hours"), 6)
    young_pump = _safe_float(th.get("young_token_pump_pct"), 100)
    pvp_warn = _safe_float(th.get("pvp_volume_lp_warning"), 8)
    pvp_exclude = _safe_float(th.get("pvp_volume_lp_exclude"), 20)
    min_volume = _safe_float(th.get("min_volume_24h_usd"), 50000)
    max_ratio_main = _safe_float(th.get("max_volume_lp_ratio_main"), 8)

    lp = _safe_float(c.get("liquidity_usd"))
    vol = _safe_float(c.get("volume_24h_usd"))
    chg24 = _safe_float(c.get("price_change_24h_pct"))
    chg6 = _safe_float(c.get("price_change_6h_pct"))
    chg1 = _safe_float(c.get("price_change_1h_pct"))
    age = c.get("age_hours")
    ratio = c.get("volume_lp_ratio")
    buys = _safe_int(c.get("buys_24h"))
    sells = _safe_int(c.get("sells_24h"))
    txns = buys + sells

    flags: List[str] = []
    reason_parts: List[str] = []

    # v0.2: avoid over-rewarding very mature LP. Use capped score and separate maturity penalty.
    liquidity_score = _log_score(lp, 10_000, 1_500_000, 20)
    volume_score = _log_score(vol, 10_000, 3_000_000, 17)

    abs24 = abs(chg24)
    if abs24 <= 8:
        bottom_score = 22
        reason_parts.append("24H接近横盘")
    elif abs24 <= 25:
        bottom_score = 17
        reason_parts.append("24H波动可控")
    elif abs24 <= max_bottom_change:
        bottom_score = 8
        reason_parts.append("24H未过热但已明显波动")
    else:
        bottom_score = 0
        flags.append("24H涨跌幅过热")

    if txns > 0:
        buy_ratio = buys / txns
        if buy_ratio >= 0.62:
            buy_balance_score = 12
            reason_parts.append("买入笔数占优")
        elif buy_ratio >= 0.52:
            buy_balance_score = 8
            reason_parts.append("买卖略偏买入")
        elif buy_ratio >= 0.45:
            buy_balance_score = 3
            reason_parts.append("买卖基本均衡")
        else:
            buy_balance_score = 0
            flags.append("卖出笔数占优")
    else:
        buy_ratio = None
        buy_balance_score = 0
        flags.append("交易笔数缺失")

    risk_penalty = 0
    if lp < min_lp_secondary:
        risk_penalty += 10
        flags.append("LP偏薄")
    if lp < min_lp_main:
        reason_parts.append("LP未达主观察门槛")
    else:
        reason_parts.append("LP达主观察门槛")

    if vol < min_volume:
        risk_penalty += 8
        flags.append("24H成交不足")
    else:
        reason_parts.append("24H成交合格")

    if ratio is not None:
        if ratio > pvp_exclude:
            risk_penalty += 30
            flags.append("Volume/LP极端偏高")
        elif ratio > pvp_warn:
            risk_penalty += 18
            flags.append("Volume/LP偏高")
        elif ratio <= max_ratio_main:
            reason_parts.append("Volume/LP未失真")
    else:
        risk_penalty += 3
        flags.append("Volume/LP缺失")

    if age is not None and age < young_hours and max(chg1, chg6, chg24) > young_pump:
        risk_penalty += 25
        flags.append("年轻币短期暴拉")

    if not c.get("is_stable_quote") and str(c.get("source", "")).startswith("dexscreener"):
        risk_penalty += 3
        flags.append("非主流报价池")

    is_mature, mature_reasons = _is_mature_pool(c, strategy)
    if is_mature:
        risk_penalty += 12
        flags.extend(mature_reasons)

    base = 24
    score = base + liquidity_score + volume_score + bottom_score + buy_balance_score - risk_penalty
    score = max(0, min(100, int(round(score))))

    hard_pvp = any(f in flags for f in ["Volume/LP极端偏高", "年轻币短期暴拉"])
    soft_pvp = any(f in flags for f in ["Volume/LP偏高"])

    can_main = (
        lp >= min_lp_main
        and vol >= min_volume
        and abs(chg24) <= max_bottom_change
        and (ratio is None or ratio <= max_ratio_main)
        and not hard_pvp
        and not soft_pvp
        and not is_mature
        and score >= 76
    )

    if hard_pvp or (lp < min_lp_secondary and (ratio or 0) > pvp_warn):
        status = "PVP风险池"
    elif is_mature and score >= 58:
        status = "成熟池观察"
    elif can_main:
        status = "主观察"
    elif score >= 64 and lp >= min_lp_secondary and not hard_pvp:
        status = "次观察"
    elif score >= 50:
        status = "低优先观察"
    else:
        status = "放弃/仅记录"

    components = {
        "liquidity_score": liquidity_score,
        "volume_score": volume_score,
        "bottom_score": bottom_score,
        "buy_balance_score": buy_balance_score,
        "risk_penalty": risk_penalty,
        "buy_ratio": _round_or_none(buy_ratio, 4),
        "mature_pool": is_mature,
    }
    reason = "；".join(reason_parts + flags) if reason_parts or flags else "无明确优势"
    return status, reason, score, components, flags


def merge_multi_pool_candidates(candidates: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merge multi-pool records.

    v0.2 adds symbol bridge merging: GeckoTerminal rows often lack token address,
    while DEXScreener rows have it. If chain+symbol match and symbol is not a common
    ambiguous ticker, merge them to reduce duplicate outputs such as TOESCOIN/KINS.
    """
    initial: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for c in candidates:
        initial[_token_identity(c)].append(c)

    # Build bridge: chain + normalized symbol -> all groups with that symbol.
    by_symbol: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    for key, items in initial.items():
        if not items:
            continue
        symbol = _norm_symbol(items[0].get("token"))
        chain = items[0].get("chain") or "unknown"
        by_symbol[(chain, symbol)].append(key)

    final_groups: List[List[Dict[str, Any]]] = []
    used = set()
    for key, items in initial.items():
        if key in used:
            continue
        chain = items[0].get("chain") or "unknown"
        symbol = _norm_symbol(items[0].get("token"))
        bridge_keys = by_symbol.get((chain, symbol), [])
        # Only bridge non-ambiguous symbols to avoid merging unrelated MEME/PEPE/MOON tickers.
        if symbol not in COMMON_AMBIGUOUS_SYMBOLS and len(bridge_keys) > 1:
            merged_items: List[Dict[str, Any]] = []
            for bk in bridge_keys:
                merged_items.extend(initial[bk])
                used.add(bk)
            for mi in merged_items:
                mi["symbol_bridge_merged"] = True
            final_groups.append(merged_items)
        else:
            used.add(key)
            final_groups.append(items)

    merged: List[Dict[str, Any]] = []
    for items in final_groups:
        best = sorted(
            items,
            key=lambda x: (_safe_float(x.get("liquidity_usd")), _safe_float(x.get("volume_24h_usd"))),
            reverse=True,
        )[0].copy()

        # v0.3: contract address is first-class output. If the representative
        # pool lacks it but another merged row has it, copy the best available one.
        address_items = [i for i in items if i.get("token_address")]
        if address_items and not best.get("token_address"):
            addr_src_item = sorted(address_items, key=lambda x: (_safe_float(x.get("liquidity_usd")), _safe_float(x.get("volume_24h_usd"))), reverse=True)[0]
            best["token_address"] = addr_src_item.get("token_address")
            best["contract_address"] = addr_src_item.get("token_address")
            best["contract_address_source"] = addr_src_item.get("contract_address_source")
            best["contract_url"] = _contract_url(best.get("chain"), best.get("token_address"))
        else:
            best["contract_address"] = best.get("token_address")
            best["contract_url"] = _contract_url(best.get("chain"), best.get("token_address"))

        pool_count = len(items)
        sources = sorted(set(str(i.get("source")) for i in items if i.get("source")))
        dexes = sorted(set(str(i.get("dex_id")) for i in items if i.get("dex_id")))
        total_lp = sum(_safe_float(i.get("liquidity_usd")) for i in items)
        total_vol = sum(_safe_float(i.get("volume_24h_usd")) for i in items)
        max_price = max((_safe_float(i.get("price_usd")) for i in items), default=0)
        min_price = min((_safe_float(i.get("price_usd")) for i in items if _safe_float(i.get("price_usd")) > 0), default=0)
        price_spread_pct = ((max_price - min_price) / min_price * 100) if min_price > 0 else None

        best["pool_count"] = pool_count
        best["pool_sources"] = sources
        best["pool_dexes"] = dexes
        best["aggregate_liquidity_usd"] = total_lp
        best["aggregate_volume_24h_usd"] = total_vol
        best["multi_pool_price_spread_pct"] = _round_or_none(price_spread_pct, 2)
        best["symbol_bridge_merged"] = any(i.get("symbol_bridge_merged") for i in items)
        best["token_addresses"] = sorted(set(str(i.get("token_address")) for i in items if i.get("token_address")))
        best["address_available"] = bool(best.get("token_address"))
        best["top_pools"] = [
            {
                "source": i.get("source"),
                "dex_id": i.get("dex_id"),
                "pair_address": i.get("pair_address"),
                "token_address": i.get("token_address"),
                "contract_address_source": i.get("contract_address_source"),
                "liquidity_usd": _round_or_none(i.get("liquidity_usd"), 2),
                "volume_24h_usd": _round_or_none(i.get("volume_24h_usd"), 2),
                "price_usd": i.get("price_usd"),
                "url": i.get("url"),
            }
            for i in sorted(items, key=lambda x: _safe_float(x.get("liquidity_usd")), reverse=True)[:5]
        ]
        if pool_count > 1:
            best["multi_pool_note"] = "多池合并：以最大LP池为代表，聚合LP/成交仅作参考"
        if price_spread_pct is not None and price_spread_pct > 20 and pool_count > 1:
            best["multi_pool_conflict"] = True
        else:
            best["multi_pool_conflict"] = False
        merged.append(best)
    return merged


def apply_main_watchlist_cap(candidates: List[Dict[str, Any]], strategy: Dict[str, Any]) -> None:
    max_main = int(strategy.get("thresholds", {}).get("max_main_watchlist", 5))
    mains = [c for c in candidates if c.get("classification") == "主观察"]
    mains_sorted = sorted(mains, key=lambda x: x.get("score", 0), reverse=True)
    allowed_ids = {id(c) for c in mains_sorted[:max_main]}
    for c in mains:
        if id(c) not in allowed_ids:
            c["classification"] = "次观察"
            c["classification_reason"] = (c.get("classification_reason") or "") + "；主观察数量限制，降为次观察"
            c["operation_conclusion"] = "次观察，不直接进攻"


def build_candidate_notes(c: Dict[str, Any]) -> None:
    status = c.get("classification")
    c["smart_money_judgment"] = "钱包级数据不可用；当前仅代理指标"
    c["smart_money_source"] = "proxy_metrics_only"
    c["smart_money_source_status"] = "proxy_only_ave_weekly_cache_not_connected"

    if c.get("multi_pool_conflict"):
        c["confidence"] = "Low"
        c["smart_money_judgment"] += "；多池数据存在冲突，降置信度"
    elif status == "主观察":
        c["confidence"] = "Medium-Low"
    elif status == "成熟池观察":
        c["confidence"] = "Low"
        c["smart_money_judgment"] += "；资产偏成熟，不按早期吸筹处理"
    else:
        c["confidence"] = "Low"

    mapping = {
        "主观察": "保留主观察，等待链上钱包留存确认；不因代理指标直接买入",
        "次观察": "次观察，等成交/LP结构继续改善",
        "成熟池观察": "成熟池观察，不占用早期Alpha主榜",
        "低优先观察": "低优先观察，不追高",
        "PVP风险池": "只记录热度，不进入主榜",
        "放弃/仅记录": "暂不参与",
    }
    c["operation_conclusion"] = mapping.get(status, "暂不参与")


def _class_priority(c: Dict[str, Any]) -> Tuple[int, int]:
    order = {
        "主观察": 50,
        "次观察": 40,
        "PVP风险池": 35,
        "成熟池观察": 30,
        "低优先观察": 20,
        "放弃/仅记录": 10,
    }
    return (order.get(c.get("classification"), 0), int(c.get("score", 0)))


def scan_free_sources(strategy: Dict[str, Any]) -> Dict[str, Any]:
    run_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_status: Dict[str, Any] = {}
    raw_candidates: List[Dict[str, Any]] = []

    dex = DexScreenerClient()
    gecko = GeckoTerminalClient()
    th = strategy.get("thresholds", {})
    profile_limit = int(th.get("profile_expand_limit", 30))
    boost_limit = int(th.get("boost_expand_limit", 25))
    search_limit = int(th.get("search_pair_limit_per_query", 15))

    try:
        profiles = dex.token_profiles_latest()
        source_status["dexscreener_profiles"] = {"ok": True, "count": len(profiles), "expanded": min(len(profiles), profile_limit)}
        for p in profiles[:profile_limit]:
            chain_id = p.get("chainId")
            token_addr = p.get("tokenAddress")
            if chain_id in {"bsc", "solana"} and token_addr:
                try:
                    for pair in dex.token_pairs(chain_id, token_addr)[:5]:
                        norm = normalize_dex_pair(pair, "dexscreener_profile_expand")
                        if norm:
                            raw_candidates.append(norm)
                except Exception:
                    continue
    except Exception as exc:  # noqa: BLE001
        source_status["dexscreener_profiles"] = {"ok": False, "error": str(exc)}

    try:
        boosts = dex.token_boosts_latest()
        source_status["dexscreener_boosts"] = {"ok": True, "count": len(boosts), "expanded": min(len(boosts), boost_limit)}
        for b in boosts[:boost_limit]:
            chain_id = b.get("chainId")
            token_addr = b.get("tokenAddress")
            if chain_id in {"bsc", "solana"} and token_addr:
                try:
                    for pair in dex.token_pairs(chain_id, token_addr)[:5]:
                        norm = normalize_dex_pair(pair, "dexscreener_boost_expand")
                        if norm:
                            raw_candidates.append(norm)
                except Exception:
                    continue
    except Exception as exc:  # noqa: BLE001
        source_status["dexscreener_boosts"] = {"ok": False, "error": str(exc)}

    search_count = 0
    for q in SEARCH_QUERIES:
        try:
            pairs = dex.search_pairs(q)
            search_count += len(pairs)
            for pair in pairs[:search_limit]:
                norm = normalize_dex_pair(pair, "dexscreener_search")
                if norm:
                    raw_candidates.append(norm)
        except Exception:
            continue
    source_status["dexscreener_search"] = {"ok": True, "count": search_count}

    for network in ["bsc", "solana"]:
        try:
            pools = gecko.trending_pools(network)
            source_status[f"geckoterminal_{network}_trending"] = {"ok": True, "count": len(pools)}
            for pool in pools[:10]:
                norm = normalize_gecko_pool(pool, network)
                if norm:
                    raw_candidates.append(norm)
        except Exception as exc:  # noqa: BLE001
            source_status[f"geckoterminal_{network}_trending"] = {"ok": False, "error": str(exc)}

    merged = merge_multi_pool_candidates(raw_candidates)
    for c in merged:
        status, reason, score, components, flags = score_candidate(c, strategy)
        c["classification"] = status
        c["classification_reason"] = reason
        c["score"] = score
        c["score_components"] = components
        c["risk_flags"] = flags
        c["volume_lp_ratio"] = _round_or_none(c.get("volume_lp_ratio"), 4)
        c["age_hours"] = _round_or_none(c.get("age_hours"), 2)
        c["liquidity_tier"] = _liquidity_tier(c.get("liquidity_usd"), strategy)
        needs_verify, verify_reason, emergency_check = _needs_chain_verify(c)
        c["needs_chain_verify"] = needs_verify
        c["chain_verify_reason"] = verify_reason
        c["emergency_precision_check"] = emergency_check
        build_candidate_notes(c)

    # Cap main watchlist first, then preserve a visible PVP pool in output.
    apply_main_watchlist_cap(merged, strategy)

    max_candidates = int(th.get("max_candidates", 25))
    pvp_keep = int(th.get("pvp_keep_limit", 8))
    main_secondary = [c for c in merged if c.get("classification") in {"主观察", "次观察"}]
    pvp = [c for c in merged if c.get("classification") == "PVP风险池"]
    mature = [c for c in merged if c.get("classification") == "成熟池观察"]
    low = [c for c in merged if c.get("classification") not in {"主观察", "次观察", "PVP风险池", "成熟池观察"}]

    main_secondary = sorted(main_secondary, key=lambda x: x.get("score", 0), reverse=True)
    pvp = sorted(pvp, key=lambda x: (_safe_float(x.get("volume_24h_usd")), x.get("score", 0)), reverse=True)[:pvp_keep]
    mature = sorted(mature, key=lambda x: x.get("score", 0), reverse=True)
    low = sorted(low, key=lambda x: x.get("score", 0), reverse=True)

    candidates = (main_secondary + pvp + mature + low)[:max_candidates]
    candidates = sorted(candidates, key=_class_priority, reverse=True)

    summary = {
        "raw_pair_count": len(raw_candidates),
        "merged_token_count": len(merged),
        "returned_candidate_count": len(candidates),
        "main_watch_count": sum(1 for c in candidates if c.get("classification") == "主观察"),
        "secondary_watch_count": sum(1 for c in candidates if c.get("classification") == "次观察"),
        "mature_count": sum(1 for c in candidates if c.get("classification") == "成熟池观察"),
        "pvp_count": sum(1 for c in candidates if c.get("classification") == "PVP风险池"),
        "low_priority_count": sum(1 for c in candidates if c.get("classification") == "低优先观察"),
        "multi_pool_count": sum(1 for c in candidates if c.get("pool_count", 1) > 1),
        "multi_pool_conflict_count": sum(1 for c in candidates if c.get("multi_pool_conflict")),
        "symbol_bridge_merge_count": sum(1 for c in candidates if c.get("symbol_bridge_merged")),
        "contract_address_available_count": sum(1 for c in candidates if c.get("token_address")),
        "contract_address_missing_count": sum(1 for c in candidates if not c.get("token_address")),
        "micro_tier_count": sum(1 for c in candidates if c.get("liquidity_tier") == "Micro"),
        "early_tier_count": sum(1 for c in candidates if c.get("liquidity_tier") == "Early"),
        "liquid_tier_count": sum(1 for c in candidates if c.get("liquidity_tier") == "Liquid"),
        "mature_tier_count": sum(1 for c in candidates if c.get("liquidity_tier") == "Mature"),
        "needs_chain_verify_count": sum(1 for c in candidates if c.get("needs_chain_verify")),
        "emergency_precision_check_count": sum(1 for c in candidates if c.get("emergency_precision_check")),
    }

    return {
        "snapshot_id": f"scan_{run_time.replace(':', '').replace('-', '').replace('Z', 'UTC')}",
        "version": strategy.get("version", "unknown"),
        "run_time_utc": run_time,
        "s0_anchor": strategy.get("s0_anchor"),
        "source_status": source_status,
        "summary": summary,
        "candidates": candidates,
        "data_limitations": [
            "This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.",
            "AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.",
            "S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.",
            "Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.",
            "v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.",
            "Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.",
        ],
    }

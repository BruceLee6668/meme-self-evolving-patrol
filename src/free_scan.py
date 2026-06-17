from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from .dexscreener_client import DexScreenerClient
from .geckoterminal_client import GeckoTerminalClient

CHAIN_MAP = {
    "bsc": {"dex": "bsc", "gecko": "bsc", "label": "BSC"},
    "solana": {"dex": "solana", "gecko": "solana", "label": "SOL"},
}

SEARCH_QUERIES = [
    "four meme bsc",
    "four.meme",
    "pumpfun solana",
    "pump fun",
    "pumpswap",
    "meme bsc",
    "meme solana",
]


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except Exception:
        return default


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        if value is None:
            return default
        return int(float(value))
    except Exception:
        return default


def _pair_key(pair: Dict[str, Any]) -> str:
    chain = pair.get("chainId") or pair.get("chain") or "unknown"
    pair_addr = pair.get("pairAddress") or pair.get("address") or pair.get("id") or ""
    base = (pair.get("baseToken") or {}).get("address") or pair.get("base_token_address") or ""
    raw = f"{chain}:{pair_addr}:{base}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


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

    return {
        "source": source,
        "chain": chain,
        "chain_label": CHAIN_MAP[chain]["label"],
        "dex_id": dex_id,
        "token": token_symbol,
        "token_name": token_name,
        "token_address": token_address,
        "pair_address": pair_address,
        "quote_symbol": quote_token.get("symbol"),
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
        "txns_24h": txns_24h,
        "age_hours": age_hours,
        "volume_lp_ratio": volume_24h / liquidity_usd if liquidity_usd > 0 else None,
        "market_cap": _safe_float(pair.get("marketCap")),
        "fdv": _safe_float(pair.get("fdv")),
        "raw_pair_key": _pair_key(pair),
    }


def normalize_gecko_pool(pool: Dict[str, Any], network: str) -> Optional[Dict[str, Any]]:
    attrs = pool.get("attributes") or {}
    rel = pool.get("relationships") or {}
    name = attrs.get("name") or "UNKNOWN"
    address = attrs.get("address") or pool.get("id", "").split("_")[-1]
    # Gecko often names pools like TOKEN / QUOTE.
    token_symbol = name.split("/")[0].strip() if "/" in name else name
    liquidity_usd = _safe_float(attrs.get("reserve_in_usd"))
    volume_usd = attrs.get("volume_usd") or {}
    price_change = attrs.get("price_change_percentage") or {}
    tx_count = attrs.get("transactions") or {}

    buys_24h = _safe_int(((tx_count.get("h24") or {}).get("buys")))
    sells_24h = _safe_int(((tx_count.get("h24") or {}).get("sells")))
    volume_24h = _safe_float(volume_usd.get("h24"))

    return {
        "source": "geckoterminal",
        "chain": network,
        "chain_label": CHAIN_MAP.get(network, {}).get("label", network.upper()),
        "dex_id": attrs.get("dex_id") or "unknown",
        "token": token_symbol,
        "token_name": name,
        "token_address": None,
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
        "txns_24h": buys_24h + sells_24h,
        "age_hours": None,
        "volume_lp_ratio": volume_24h / liquidity_usd if liquidity_usd > 0 else None,
        "market_cap": _safe_float(attrs.get("market_cap_usd")),
        "fdv": _safe_float(attrs.get("fdv_usd")),
        "raw_pair_key": f"gecko:{network}:{address}",
    }


def classify_candidate(c: Dict[str, Any], strategy: Dict[str, Any]) -> Tuple[str, str, int]:
    th = strategy.get("thresholds", {})
    min_lp = _safe_float(th.get("min_lp_main_usd"), 100000)
    max_bottom_change = _safe_float(th.get("max_24h_change_bottom_pct"), 80)
    young_hours = _safe_float(th.get("young_token_hours"), 6)
    young_pump = _safe_float(th.get("young_token_pump_pct"), 100)
    pvp_warn = _safe_float(th.get("pvp_volume_lp_warning"), 8)
    pvp_exclude = _safe_float(th.get("pvp_volume_lp_exclude"), 20)

    lp = _safe_float(c.get("liquidity_usd"))
    vol = _safe_float(c.get("volume_24h_usd"))
    chg24 = _safe_float(c.get("price_change_24h_pct"))
    chg1 = _safe_float(c.get("price_change_1h_pct"))
    age = c.get("age_hours")
    ratio = c.get("volume_lp_ratio")
    buys = _safe_int(c.get("buys_24h"))
    sells = _safe_int(c.get("sells_24h"))

    status = "观察"
    reason_parts: List[str] = []
    score = 50

    if lp >= min_lp:
        score += 15
        reason_parts.append("LP达主观察门槛")
    else:
        score -= 12
        reason_parts.append("LP低于主观察门槛")

    if vol >= _safe_float(th.get("min_volume_24h_usd"), 50000):
        score += 10
        reason_parts.append("24H成交合格")
    else:
        score -= 8
        reason_parts.append("24H成交不足")

    if abs(chg24) <= max_bottom_change:
        score += 8
        reason_parts.append("24H涨幅未过热")
    else:
        score -= 15
        reason_parts.append("24H涨幅过高/过热")

    if buys > sells and buys + sells > 0:
        score += 5
        reason_parts.append("买入笔数多于卖出")
    elif sells > buys:
        score -= 5
        reason_parts.append("卖出笔数多于买入")

    if ratio is not None:
        if ratio > pvp_exclude:
            score -= 25
            status = "PVP风险池"
            reason_parts.append("Volume/LP极端偏高")
        elif ratio > pvp_warn:
            score -= 12
            status = "PVP风险池"
            reason_parts.append("Volume/LP偏高")
        else:
            score += 5
            reason_parts.append("Volume/LP未失真")

    if age is not None and age < young_hours and max(chg1, chg24) > young_pump:
        score -= 20
        status = "PVP风险池"
        reason_parts.append("年轻币短期暴拉")

    if status != "PVP风险池":
        if score >= 75:
            status = "主观察"
        elif score >= 60:
            status = "低优先观察"
        else:
            status = "放弃/仅记录"

    return status, "；".join(reason_parts), max(0, min(100, score))


def dedupe_candidates(candidates: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for c in candidates:
        key = c.get("token_address") or c.get("pair_address") or c.get("raw_pair_key")
        chain = c.get("chain")
        dedupe_key = f"{chain}:{key}"
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        out.append(c)
    return out


def scan_free_sources(strategy: Dict[str, Any]) -> Dict[str, Any]:
    run_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_status: Dict[str, Any] = {}
    candidates: List[Dict[str, Any]] = []

    dex = DexScreenerClient()
    gecko = GeckoTerminalClient()

    try:
        profiles = dex.token_profiles_latest()
        source_status["dexscreener_profiles"] = {"ok": True, "count": len(profiles), "note": "profiles counted only in v0 to control calls"}
    except Exception as exc:  # noqa: BLE001
        source_status["dexscreener_profiles"] = {"ok": False, "error": str(exc)}

    try:
        boosts = dex.token_boosts_latest()
        source_status["dexscreener_boosts"] = {"ok": True, "count": len(boosts)}
        for b in boosts[:10]:
            chain_id = b.get("chainId")
            token_addr = b.get("tokenAddress")
            if chain_id in {"bsc", "solana"} and token_addr:
                try:
                    for pair in dex.token_pairs(chain_id, token_addr)[:3]:
                        norm = normalize_dex_pair(pair, "dexscreener_boost_expand")
                        if norm:
                            candidates.append(norm)
                except Exception:
                    continue
    except Exception as exc:  # noqa: BLE001
        source_status["dexscreener_boosts"] = {"ok": False, "error": str(exc)}

    search_count = 0
    for q in SEARCH_QUERIES:
        try:
            pairs = dex.search_pairs(q)
            search_count += len(pairs)
            for pair in pairs[:10]:
                norm = normalize_dex_pair(pair, "dexscreener_search")
                if norm:
                    candidates.append(norm)
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
                    candidates.append(norm)
        except Exception as exc:  # noqa: BLE001
            source_status[f"geckoterminal_{network}_trending"] = {"ok": False, "error": str(exc)}

    deduped = dedupe_candidates(candidates)
    for c in deduped:
        status, reason, score = classify_candidate(c, strategy)
        c["classification"] = status
        c["classification_reason"] = reason
        c["score"] = score
        c["smart_money_judgment"] = "钱包级数据不可用；当前仅代理指标"
        c["smart_money_source"] = "proxy_metrics_only"
        c["confidence"] = "Low" if "PVP" in status or c.get("smart_money_source") == "proxy_metrics_only" else "Medium"
        c["operation_conclusion"] = {
            "主观察": "保留主观察，等待链上钱包留存确认",
            "低优先观察": "低优先观察，不追高",
            "PVP风险池": "只记录热度，不进入主榜",
            "放弃/仅记录": "暂不参与",
        }.get(status, "暂不参与")

    max_candidates = int(strategy.get("thresholds", {}).get("max_candidates", 25))
    sorted_candidates = sorted(deduped, key=lambda x: x.get("score", 0), reverse=True)[:max_candidates]

    return {
        "snapshot_id": f"scan_{run_time.replace(':', '').replace('-', '').replace('Z', 'UTC')}",
        "run_time_utc": run_time,
        "s0_anchor": strategy.get("s0_anchor"),
        "source_status": source_status,
        "candidates": sorted_candidates,
        "data_limitations": [
            "This v0 scan uses free public sources only.",
            "AVE Smart Money weekly cache is not connected in v0.",
            "S0 exact historical replay is not implemented in v0; candidates are marked with current metrics only.",
            "Wallet-level buy/sell retention is not implemented in v0."
        ]
    }

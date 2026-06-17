from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from typing import Any, Dict, List
from urllib import request

from .smart_wallet_cache import match_smart_wallets

TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _rpc_post(url: str, payload: Dict[str, Any], timeout: int = 15) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 - configured public RPC endpoints only
        return json.loads(resp.read().decode("utf-8"))


def _hex_to_int(value: Any) -> int | None:
    try:
        return int(str(value), 16)
    except Exception:
        return None


def _topic_addr(topic: Any) -> str | None:
    s = str(topic or "")
    if not s.startswith("0x") or len(s) < 42:
        return None
    return "0x" + s[-40:]


def _bsc_transfer_activity(token_address: str, pair_address: str | None, rpc_url: str, lookback_blocks: int, max_logs: int) -> Dict[str, Any]:
    try:
        block_res = _rpc_post(rpc_url, {"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber", "params": []})
        latest = _hex_to_int(block_res.get("result"))
        if latest is None:
            return {"status": "failed", "error": "cannot_read_latest_block"}
        from_block = max(0, latest - lookback_blocks)
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getLogs",
            "params": [{
                "address": token_address,
                "fromBlock": hex(from_block),
                "toBlock": "latest",
                "topics": [TRANSFER_TOPIC],
            }],
        }
        res = _rpc_post(rpc_url, payload)
        logs = res.get("result") or []
        if not isinstance(logs, list):
            return {"status": "failed", "error": str(res.get("error") or "unexpected_result")[:180]}
        logs = logs[:max_logs]
        pair_l = str(pair_address or "").lower()
        from_counter: Counter[str] = Counter()
        to_counter: Counter[str] = Counter()
        buy_like_receivers: Counter[str] = Counter()
        sell_like_senders: Counter[str] = Counter()
        for lg in logs:
            topics = lg.get("topics") or []
            if len(topics) < 3:
                continue
            from_addr = _topic_addr(topics[1])
            to_addr = _topic_addr(topics[2])
            if not from_addr or not to_addr:
                continue
            from_l = from_addr.lower()
            to_l = to_addr.lower()
            from_counter[from_l] += 1
            to_counter[to_l] += 1
            if pair_l and from_l == pair_l and to_l != pair_l:
                buy_like_receivers[to_l] += 1
            if pair_l and to_l == pair_l and from_l != pair_l:
                sell_like_senders[from_l] += 1
        active_wallets = set(from_counter.keys()) | set(to_counter.keys())
        return {
            "status": "checked",
            "latest_block": latest,
            "from_block": from_block,
            "lookback_blocks": lookback_blocks,
            "raw_log_count": len(logs),
            "unique_active_wallet_count": len(active_wallets),
            "top_receivers": [{"wallet_address": k, "transfer_count": v} for k, v in to_counter.most_common(10)],
            "top_senders": [{"wallet_address": k, "transfer_count": v} for k, v in from_counter.most_common(10)],
            "buy_like_receivers": [{"wallet_address": k, "transfer_count": v} for k, v in buy_like_receivers.most_common(10)],
            "sell_like_senders": [{"wallet_address": k, "transfer_count": v} for k, v in sell_like_senders.most_common(10)],
            "limitation": "BSC v0.5 uses ERC20 Transfer logs. Pair-to-wallet is buy-like and wallet-to-pair is sell-like only when pair_address is available; this is not full swap decoding.",
        }
    except Exception as exc:  # noqa: BLE001
        return {"status": "failed", "error": str(exc)[:180]}


def analyze_wallet_behavior(snapshot: Dict[str, Any], strategy: Dict[str, Any], smart_cache: Dict[str, Any], chain_verify: Dict[str, Any]) -> Dict[str, Any]:
    cfg = strategy.get("wallet_behavior") or {}
    enabled = bool(cfg.get("enabled", True))
    max_candidates = int(cfg.get("max_candidates_per_run", 8))
    lookback_blocks = int(cfg.get("bsc_transfer_lookback_blocks", 300))
    max_logs = int(cfg.get("bsc_max_logs_per_token", 250))
    bsc_rpc = os.getenv("BSC_RPC_URL") or (strategy.get("chain_verify") or {}).get("bsc_rpc_url") or "https://bsc-dataseed.binance.org/"

    candidates = snapshot.get("candidates", [])
    targets = [c for c in candidates if c.get("classification") == "主观察" or c.get("emergency_precision_check")]
    targets = sorted(targets, key=lambda c: (bool(c.get("emergency_precision_check")), int(c.get("score") or 0)), reverse=True)[:max_candidates]

    results: List[Dict[str, Any]] = []
    hit_total = 0
    if not enabled:
        return {
            "version": "0.5.0-wallet-behavior-prep",
            "run_time_utc": _now(),
            "status": "disabled",
            "checked_count": 0,
            "smart_wallet_hit_count": 0,
            "results": [],
            "limitations": ["wallet_behavior.enabled=false"],
        }

    for c in targets:
        chain = c.get("chain")
        addr = c.get("token_address") or c.get("contract_address")
        pair = c.get("pair_address")
        result: Dict[str, Any] = {
            "token": c.get("token"),
            "chain": chain,
            "token_address": addr,
            "pair_address": pair,
            "classification": c.get("classification"),
            "score": c.get("score"),
            "checked_at": _now(),
        }
        if not addr:
            result.update({"status": "address_missing", "behavior_level": "none"})
        elif chain == "bsc":
            activity = _bsc_transfer_activity(addr, pair, bsc_rpc, lookback_blocks, max_logs)
            active_addresses = []
            for key in ("top_receivers", "top_senders", "buy_like_receivers", "sell_like_senders"):
                for row in activity.get(key) or []:
                    active_addresses.append(row.get("wallet_address"))
            hits = match_smart_wallets("bsc", active_addresses, smart_cache)
            hit_total += len(hits)
            result.update({
                "status": activity.get("status"),
                "behavior_level": "bsc_transfer_activity_v0.5",
                "activity": activity,
                "smart_wallet_hits": hits,
                "smart_wallet_hit_count": len(hits),
                "smart_wallet_cache_status": smart_cache.get("status"),
            })
        elif chain == "solana":
            result.update({
                "status": "signature_sample_only",
                "behavior_level": "solana_swap_retention_not_parsed_v0.5",
                "smart_wallet_hits": [],
                "smart_wallet_hit_count": 0,
                "smart_wallet_cache_status": smart_cache.get("status"),
                "limitation": "SOL v0.5 keeps address/signature preflight. Full wallet behavior requires Helius enhanced transactions or parsed token balance diffs in the next version.",
            })
        else:
            result.update({"status": "unsupported_chain", "behavior_level": "none"})
        results.append(result)

    by_addr = {f"{r.get('chain')}:{str(r.get('token_address')).lower()}": r for r in results if r.get("token_address")}
    for c in candidates:
        key = f"{c.get('chain')}:{str(c.get('token_address') or c.get('contract_address')).lower()}"
        r = by_addr.get(key)
        if not r:
            c["wallet_behavior_status"] = "not_checked_this_run"
            c["smart_wallet_hit_count"] = 0
            continue
        c["wallet_behavior_status"] = r.get("status")
        c["wallet_behavior_level"] = r.get("behavior_level")
        c["smart_wallet_hit_count"] = r.get("smart_wallet_hit_count", 0)
        if r.get("smart_wallet_hit_count", 0) > 0:
            c["smart_money_source_status"] = "ave_weekly_cache_hit_plus_chain_behavior"
            c["smart_money_judgment"] = str(c.get("smart_money_judgment") or "") + "；本轮链上行为命中AVE缓存钱包，需人工复核买卖方向和留存"
        elif smart_cache.get("status") == "active":
            c["smart_money_judgment"] = str(c.get("smart_money_judgment") or "") + "；本轮行为未命中AVE缓存钱包"

    return {
        "version": "0.5.0-wallet-behavior-prep",
        "run_time_utc": _now(),
        "status": "checked",
        "checked_count": len(results),
        "bsc_transfer_checked_count": sum(1 for r in results if r.get("behavior_level") == "bsc_transfer_activity_v0.5"),
        "solana_signature_only_count": sum(1 for r in results if r.get("chain") == "solana"),
        "smart_wallet_hit_count": hit_total,
        "smart_wallet_cache_status": smart_cache.get("status"),
        "results": results,
        "limitations": [
            "v0.5 BSC只解析ERC20 Transfer样本，不等同于完整Swap路径。",
            "pair_address可用时，pair->wallet视为buy-like，wallet->pair视为sell-like；仍需后续完整Swap/Router/CEX解析。",
            "SOL当前仍为签名/账户预检，完整留存需要Helius增强交易或解析token balance diff。",
            "Smart Wallet身份来自AVE周缓存；缓存为空或过期时不能高置信判断聪明钱。",
        ],
    }

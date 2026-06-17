from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List
from urllib import request


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _rpc_post(url: str, payload: Dict[str, Any], timeout: int = 12) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 - configured public RPC endpoints only
        return json.loads(resp.read().decode("utf-8"))


def _bsc_get_code(address: str, rpc_url: str) -> Dict[str, Any]:
    try:
        res = _rpc_post(rpc_url, {"jsonrpc": "2.0", "id": 1, "method": "eth_getCode", "params": [address, "latest"]})
        code = res.get("result")
        ok = isinstance(code, str) and code not in {"0x", ""}
        return {"ok": ok, "contract_exists": ok, "rpc_reachable": True, "error": None if ok else "empty_code"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "contract_exists": None, "rpc_reachable": False, "error": str(exc)[:160]}


def _solana_get_account(address: str, rpc_url: str) -> Dict[str, Any]:
    try:
        res = _rpc_post(rpc_url, {"jsonrpc": "2.0", "id": 1, "method": "getAccountInfo", "params": [address, {"encoding": "jsonParsed"}]})
        value = (res.get("result") or {}).get("value")
        ok = value is not None
        owner = (value or {}).get("owner") if isinstance(value, dict) else None
        return {"ok": ok, "account_exists": ok, "rpc_reachable": True, "owner": owner, "error": None if ok else "account_not_found"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "account_exists": None, "rpc_reachable": False, "owner": None, "error": str(exc)[:160]}


def _solana_signature_sample(address: str, rpc_url: str, limit: int = 5) -> Dict[str, Any]:
    try:
        res = _rpc_post(rpc_url, {"jsonrpc": "2.0", "id": 1, "method": "getSignaturesForAddress", "params": [address, {"limit": limit}]})
        sigs = res.get("result") or []
        return {"ok": True, "signature_sample_count": len(sigs), "latest_signatures": [s.get("signature") for s in sigs[:limit] if isinstance(s, dict)]}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "signature_sample_count": None, "latest_signatures": [], "error": str(exc)[:160]}


def verify_candidates(snapshot: Dict[str, Any], strategy: Dict[str, Any]) -> Dict[str, Any]:
    """v0.4 lightweight on-chain verification.

    This is deliberately limited to address/account existence and signature preflight.
    It does not yet parse swaps or wallet retention. That parsing belongs to v0.6+.
    """
    candidates = snapshot.get("candidates", [])
    max_verify = int(strategy.get("chain_verify", {}).get("max_candidates_per_run", 12))
    bsc_rpc = os.getenv("BSC_RPC_URL") or strategy.get("chain_verify", {}).get("bsc_rpc_url") or "https://bsc-dataseed.binance.org/"
    helius_key = os.getenv("HELIUS_API_KEY")
    sol_rpc = os.getenv("SOLANA_RPC_URL") or (f"https://mainnet.helius-rpc.com/?api-key={helius_key}" if helius_key else "https://api.mainnet-beta.solana.com")

    targets = [c for c in candidates if c.get("needs_chain_verify") or c.get("emergency_precision_check")]
    targets = sorted(targets, key=lambda c: (bool(c.get("emergency_precision_check")), int(c.get("score") or 0)), reverse=True)[:max_verify]

    results: List[Dict[str, Any]] = []
    by_key: Dict[str, Dict[str, Any]] = {}
    for c in targets:
        chain = c.get("chain")
        addr = c.get("token_address") or c.get("contract_address")
        token = c.get("token")
        key = f"{chain}:{str(addr).lower()}"
        base = {
            "token": token,
            "chain": chain,
            "token_address": addr,
            "classification": c.get("classification"),
            "score": c.get("score"),
            "emergency_precision_check": bool(c.get("emergency_precision_check")),
            "verified_at": _now(),
            "verify_level": "address_preflight_v0.4",
            "swap_retention_parsed": False,
        }
        if not addr:
            base.update({"status": "address_missing", "ok": False, "reason": "缺少合约地址，无法链上确认"})
        elif chain == "bsc":
            r = _bsc_get_code(addr, bsc_rpc)
            base.update({"status": "verified" if r.get("ok") else "failed", "bsc_contract": r})
        elif chain == "solana":
            r = _solana_get_account(addr, sol_rpc)
            sig = _solana_signature_sample(addr, sol_rpc, limit=5) if r.get("ok") else {"ok": False, "signature_sample_count": None, "latest_signatures": []}
            base.update({"status": "verified" if r.get("ok") else "failed", "solana_account": r, "solana_signature_sample": sig, "helius_used": bool(helius_key)})
        else:
            base.update({"status": "unsupported_chain", "ok": False, "reason": "不支持的链"})
        results.append(base)
        by_key[key] = base

    # Attach compact verification status back to candidates.
    for c in candidates:
        addr = c.get("token_address") or c.get("contract_address")
        key = f"{c.get('chain')}:{str(addr).lower()}"
        r = by_key.get(key)
        if r:
            c["chain_verify_status"] = r.get("status")
            c["chain_verify_level"] = r.get("verify_level")
            c["chain_verify_summary"] = "地址/账户预检通过，尚未解析Swap留存" if r.get("status") == "verified" else "链上预检失败或地址缺失"
        else:
            c["chain_verify_status"] = "not_checked_this_run"
            c["chain_verify_level"] = "not_checked"
            c["chain_verify_summary"] = "本轮未进入预检名额，等待后续精查"

    ok_count = sum(1 for r in results if r.get("status") == "verified")
    return {
        "version": "0.5.0-chain-preflight-plus-wallet-behavior",
        "run_time_utc": _now(),
        "checked_count": len(results),
        "verified_count": ok_count,
        "failed_count": len(results) - ok_count,
        "bsc_rpc_configured": bool(bsc_rpc),
        "solana_rpc_configured": bool(sol_rpc),
        "helius_configured": bool(helius_key),
        "results": results,
        "limitations": [
            "v0.5链上预检仍只做地址/账户存在性与SOL签名样本；钱包行为样本由wallet_behavior_latest.json承接。",
            "完整钱包买入、卖出、留存、转Router/CEX需要v0.6继续实现。",
            "未配置HELIUS_API_KEY时，SOL使用公共RPC，可能限速或返回不稳定。",
        ],
    }

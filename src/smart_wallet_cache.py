from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

CACHE_VERSION = "0.4.1-smart-wallet-cache"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except Exception:
        return None


def load_smart_wallet_cache(path: Path, valid_days: int = 7) -> Dict[str, Any]:
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    else:
        data = {}

    wallets = data.get("wallets") if isinstance(data.get("wallets"), list) else []
    last_refresh = data.get("last_refresh_at")
    refreshed_dt = _parse_time(last_refresh)
    is_stale = True
    age_days = None
    if refreshed_dt:
        age_days = (datetime.now(timezone.utc) - refreshed_dt).total_seconds() / 86400
        is_stale = age_days > valid_days

    by_key = {}
    for w in wallets:
        chain = str(w.get("chain") or "unknown").lower()
        addr = str(w.get("wallet_address") or "").strip().lower()
        if addr:
            by_key[f"{chain}:{addr}"] = w

    return {
        "version": data.get("version", CACHE_VERSION),
        "source": data.get("source", "AVE_weekly_cache"),
        "last_refresh_at": last_refresh,
        "valid_days": valid_days,
        "age_days": round(age_days, 2) if age_days is not None else None,
        "is_stale": is_stale,
        "wallet_count": len(by_key),
        "wallets": list(by_key.values()),
        "wallets_by_key": by_key,
        "status": "active" if wallets and not is_stale else ("stale" if wallets else "empty"),
    }


def write_smart_wallet_cache(path: Path, cache: Dict[str, Any]) -> None:
    payload = {k: v for k, v in cache.items() if k != "wallets_by_key"}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def upsert_ave_smart_wallets(existing: Dict[str, Any], new_wallets: Iterable[Dict[str, Any]], related_token: str | None = None) -> Dict[str, Any]:
    """Merge AVE smart-wallet rows into persistent cache.

    Existing wallet labels are not deleted when absent from a new AVE response; they remain
    in cache and can later be marked stale by cache age. New rows update label/profile fields
    and last_refresh_at/last_seen_at.
    """
    now = _now()
    by_key = dict(existing.get("wallets_by_key") or {})
    for row in new_wallets:
        addr = str(row.get("wallet_address") or row.get("address") or row.get("wallet") or "").strip()
        chain = str(row.get("chain") or "unknown").lower()
        if not addr:
            continue
        key = f"{chain}:{addr.lower()}"
        old = by_key.get(key, {})
        related = set(old.get("related_tokens") or [])
        if related_token:
            related.add(related_token)
        for token in row.get("related_tokens") or []:
            related.add(str(token))
        labels = row.get("labels") or row.get("label") or old.get("labels") or []
        if isinstance(labels, str):
            labels = [labels]
        risk_flags = row.get("risk_flags") or old.get("risk_flags") or []
        if isinstance(risk_flags, str):
            risk_flags = [risk_flags]
        by_key[key] = {
            "wallet_address": addr,
            "chain": chain,
            "labels": labels,
            "profile": row.get("profile") or old.get("profile") or {},
            "source": "AVE",
            "confidence": row.get("confidence") or old.get("confidence") or "medium",
            "first_seen_at": old.get("first_seen_at") or now,
            "last_refresh_at": now,
            "last_seen_at": now,
            "related_tokens": sorted(related),
            "risk_flags": risk_flags,
            "status": "active",
        }

    return {
        "version": CACHE_VERSION,
        "source": "AVE_weekly_cache",
        "last_refresh_at": now,
        "valid_days": existing.get("valid_days", 7),
        "wallet_count": len(by_key),
        "wallets": list(by_key.values()),
        "wallets_by_key": by_key,
        "status": "active" if by_key else "empty",
        "is_stale": False if by_key else True,
        "age_days": 0 if by_key else None,
    }


def smart_money_status_for_candidate(candidate: Dict[str, Any], cache: Dict[str, Any]) -> Dict[str, Any]:
    """Return smart-money source metadata for hourly output.

    v0.4 does not yet connect wallet events to specific wallets; this function reports cache
    availability and leaves candidate-level identity as proxy unless chain verification later
    supplies wallet addresses.
    """
    if cache.get("status") == "empty":
        return {
            "source": "proxy_metrics_only_no_ave_cache",
            "cache_status": "empty",
            "cache_age_days": None,
            "judgment": "未接入AVE周缓存；只能用DEX/链上代理指标，不能标记真实吸筹",
            "confidence_cap": "Low",
        }
    if cache.get("is_stale"):
        return {
            "source": "ave_weekly_cache_stale_plus_proxy",
            "cache_status": "stale",
            "cache_age_days": cache.get("age_days"),
            "judgment": "AVE周缓存已过期；仅可低置信参考，需刷新后再判断聪明钱包身份",
            "confidence_cap": "Low",
        }
    return {
        "source": "ave_weekly_cache_available_plus_proxy",
        "cache_status": "active",
        "cache_age_days": cache.get("age_days"),
        "judgment": "AVE周缓存可用，但本轮尚未把具体买卖钱包映射到候选；仍需链上Swap留存确认",
        "confidence_cap": "Medium",
    }

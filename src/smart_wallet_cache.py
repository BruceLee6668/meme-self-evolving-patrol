from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

CACHE_VERSION = "0.5.0-smart-wallet-cache"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except Exception:
        return None


def _norm_addr(addr: Any) -> str:
    return str(addr or "").strip().lower()


def wallet_key(chain: Any, address: Any) -> str:
    return f"{str(chain or 'unknown').lower()}:{_norm_addr(address)}"


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple) or isinstance(value, set):
        return list(value)
    return [value]


def _unique_strings(values: Iterable[Any]) -> List[str]:
    out: List[str] = []
    seen = set()
    for v in values:
        s = str(v).strip()
        if not s:
            continue
        k = s.lower()
        if k not in seen:
            seen.add(k)
            out.append(s)
    return out


def _derive_status(wallet: Dict[str, Any], valid_days: int) -> str:
    current = str(wallet.get("status") or "active").lower()
    refreshed = _parse_time(wallet.get("last_refresh_at"))
    if not refreshed:
        return current if current in {"stale", "expired"} else "stale"
    age_days = (datetime.now(timezone.utc) - refreshed).total_seconds() / 86400
    if age_days > valid_days * 2:
        return "expired"
    if age_days > valid_days:
        return "stale"
    if current in {"expired", "stale"} and age_days <= valid_days:
        return "active"
    return current or "active"


def normalize_ave_wallet_row(row: Dict[str, Any], default_chain: str | None = None, related_token: str | None = None) -> Dict[str, Any] | None:
    """Normalize flexible AVE wallet rows without assuming a single undocumented schema."""
    addr = (
        row.get("wallet_address")
        or row.get("address")
        or row.get("wallet")
        or row.get("owner")
        or row.get("account")
        or row.get("holder")
    )
    addr = str(addr or "").strip()
    if not addr:
        return None
    chain = str(row.get("chain") or row.get("network") or default_chain or "unknown").lower()
    labels = row.get("labels") or row.get("label") or row.get("tags") or row.get("tag") or row.get("type") or []
    risk_flags = row.get("risk_flags") or row.get("risks") or row.get("risk") or []
    confidence = row.get("confidence") or row.get("score") or row.get("rank") or "medium"
    related = _as_list(row.get("related_tokens"))
    if related_token:
        related.append(related_token)
    return {
        "wallet_address": addr,
        "chain": chain,
        "labels": _unique_strings(_as_list(labels)),
        "profile": row.get("profile") or {
            k: v for k, v in row.items()
            if k not in {"wallet_address", "address", "wallet", "owner", "account", "holder", "labels", "label", "tags", "tag", "risk_flags", "risks", "risk"}
        },
        "source": "AVE",
        "confidence": confidence,
        "related_tokens": _unique_strings(related),
        "risk_flags": _unique_strings(_as_list(risk_flags)),
        "status": "active",
    }


def load_smart_wallet_cache(path: Path, valid_days: int = 7) -> Dict[str, Any]:
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            data = {}
    else:
        data = {}

    wallets_in = data.get("wallets") if isinstance(data.get("wallets"), list) else []
    by_key: Dict[str, Dict[str, Any]] = {}
    for w in wallets_in:
        chain = str(w.get("chain") or "unknown").lower()
        addr = _norm_addr(w.get("wallet_address"))
        if not addr:
            continue
        cleaned = dict(w)
        cleaned["chain"] = chain
        cleaned["status"] = _derive_status(cleaned, valid_days)
        by_key[wallet_key(chain, addr)] = cleaned

    last_refresh = data.get("last_refresh_at")
    refreshed_dt = _parse_time(last_refresh)
    age_days = None
    is_stale = True
    if refreshed_dt:
        age_days = (datetime.now(timezone.utc) - refreshed_dt).total_seconds() / 86400
        is_stale = age_days > valid_days

    active_count = sum(1 for w in by_key.values() if w.get("status") == "active")
    stale_count = sum(1 for w in by_key.values() if w.get("status") == "stale")
    expired_count = sum(1 for w in by_key.values() if w.get("status") == "expired")
    status = "active" if by_key and not is_stale else ("stale" if by_key else "empty")
    return {
        "version": data.get("version", CACHE_VERSION),
        "source": data.get("source", "AVE_weekly_cache"),
        "last_refresh_at": last_refresh,
        "valid_days": valid_days,
        "age_days": round(age_days, 2) if age_days is not None else None,
        "is_stale": is_stale,
        "wallet_count": len(by_key),
        "active_wallet_count": active_count,
        "stale_wallet_count": stale_count,
        "expired_wallet_count": expired_count,
        "wallets": list(by_key.values()),
        "wallets_by_key": by_key,
        "status": status,
        "refresh_mode": data.get("refresh_mode", "not_refreshed"),
    }


def write_smart_wallet_cache(path: Path, cache: Dict[str, Any]) -> None:
    payload = {k: v for k, v in cache.items() if k != "wallets_by_key"}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def upsert_ave_smart_wallets(
    existing: Dict[str, Any],
    new_wallets: Iterable[Dict[str, Any]],
    related_token: str | None = None,
    refresh_scope: str = "incremental",
    default_chain: str | None = None,
) -> Dict[str, Any]:
    """Merge AVE smart-wallet rows into persistent cache.

    Missing wallets are not deleted. If refresh_scope='full', wallets absent from the
    latest response are marked stale instead of being removed.
    """
    now = _now()
    by_key: Dict[str, Dict[str, Any]] = dict(existing.get("wallets_by_key") or {})
    seen_keys = set()

    for row in new_wallets:
        norm = normalize_ave_wallet_row(row, default_chain=default_chain, related_token=related_token)
        if not norm:
            continue
        key = wallet_key(norm.get("chain"), norm.get("wallet_address"))
        seen_keys.add(key)
        old = by_key.get(key, {})
        related = _unique_strings(_as_list(old.get("related_tokens")) + _as_list(norm.get("related_tokens")))
        labels = _unique_strings(_as_list(old.get("labels")) + _as_list(norm.get("labels")))
        risk_flags = _unique_strings(_as_list(old.get("risk_flags")) + _as_list(norm.get("risk_flags")))
        profile = old.get("profile") if isinstance(old.get("profile"), dict) else {}
        incoming_profile = norm.get("profile") if isinstance(norm.get("profile"), dict) else {}
        profile = {**profile, **incoming_profile}
        by_key[key] = {
            "wallet_address": norm.get("wallet_address"),
            "chain": norm.get("chain"),
            "labels": labels,
            "profile": profile,
            "source": "AVE",
            "confidence": norm.get("confidence") or old.get("confidence") or "medium",
            "first_seen_at": old.get("first_seen_at") or now,
            "last_refresh_at": now,
            "last_seen_at": now,
            "related_tokens": related,
            "risk_flags": risk_flags,
            "status": "active",
        }

    if refresh_scope == "full":
        for key, old in list(by_key.items()):
            if key not in seen_keys and old.get("source") == "AVE":
                old = dict(old)
                old["status"] = "stale"
                old["stale_reason"] = "not_returned_in_latest_full_ave_refresh"
                by_key[key] = old

    valid_days = int(existing.get("valid_days", 7))
    wallets = list(by_key.values())
    active_count = sum(1 for w in wallets if w.get("status") == "active")
    stale_count = sum(1 for w in wallets if w.get("status") == "stale")
    expired_count = sum(1 for w in wallets if w.get("status") == "expired")
    return {
        "version": CACHE_VERSION,
        "source": "AVE_weekly_cache",
        "last_refresh_at": now if wallets else existing.get("last_refresh_at"),
        "valid_days": valid_days,
        "age_days": 0 if wallets else existing.get("age_days"),
        "is_stale": False if wallets else True,
        "wallet_count": len(by_key),
        "active_wallet_count": active_count,
        "stale_wallet_count": stale_count,
        "expired_wallet_count": expired_count,
        "wallets": wallets,
        "wallets_by_key": by_key,
        "status": "active" if by_key else "empty",
        "refresh_mode": f"ave_{refresh_scope}_merge",
    }


def match_smart_wallets(chain: str, addresses: Sequence[Any], cache: Dict[str, Any]) -> List[Dict[str, Any]]:
    by_key: Dict[str, Dict[str, Any]] = cache.get("wallets_by_key") or {}
    hits: List[Dict[str, Any]] = []
    seen = set()
    for addr in addresses:
        key = wallet_key(chain, addr)
        if key in seen:
            continue
        seen.add(key)
        w = by_key.get(key)
        if w:
            hits.append({
                "wallet_address": w.get("wallet_address"),
                "chain": w.get("chain"),
                "labels": w.get("labels") or [],
                "confidence": w.get("confidence"),
                "status": w.get("status"),
                "risk_flags": w.get("risk_flags") or [],
                "last_refresh_at": w.get("last_refresh_at"),
            })
    return hits


def smart_money_status_for_candidate(candidate: Dict[str, Any], cache: Dict[str, Any]) -> Dict[str, Any]:
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
        "source": "ave_weekly_cache_available_plus_chain_behavior",
        "cache_status": "active",
        "cache_age_days": cache.get("age_days"),
        "judgment": "AVE周缓存可用；小时级仍需链上行为映射来确认该钱包本轮是否买入/留存",
        "confidence_cap": "Medium",
    }

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from string import Template
from typing import Any, Dict, Iterable, List
from urllib import parse, request

from .smart_wallet_cache import load_smart_wallet_cache, upsert_ave_smart_wallets, write_smart_wallet_cache

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
CACHE_PATH = OUTPUT_DIR / "smart_wallet_cache.json"
RAW_PATH = OUTPUT_DIR / "ave_raw_smart_money.json"
CONFIG_PATH = ROOT / "config" / "strategy_config.json"
LATEST_SNAPSHOT = OUTPUT_DIR / "latest_snapshot.json"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: Dict[str, Any]) -> Dict[str, Any]:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _extract_wallet_rows(payload: Any) -> List[Dict[str, Any]]:
    """Extract wallet-like rows from several common API response shapes."""
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("wallets", "smart_wallets", "smartMoney", "smart_money", "holders", "data", "result", "rows", "list"):
        value = payload.get(key)
        if isinstance(value, list):
            return [x for x in value if isinstance(x, dict)]
        if isinstance(value, dict):
            nested = _extract_wallet_rows(value)
            if nested:
                return nested
    return []


def _format_endpoint(template: str, candidate: Dict[str, Any]) -> str:
    token_address = str(candidate.get("token_address") or candidate.get("contract_address") or "")
    params = {
        "chain": candidate.get("chain") or "",
        "chain_label": candidate.get("chain_label") or "",
        "token": candidate.get("token") or "",
        "token_address": token_address,
        "address": token_address,
        "pair_address": candidate.get("pair_address") or "",
    }
    safe_params = {k: parse.quote(str(v), safe="") for k, v in params.items()}
    # Supports both Python .format() and shell-like ${token_address} templates.
    try:
        return template.format(**safe_params)
    except Exception:
        return Template(template).safe_substitute(**safe_params)


def _http_get_json(url: str, api_key: str | None, auth_header: str, timeout: int = 20) -> Dict[str, Any]:
    headers = {"Accept": "application/json", "User-Agent": "meme-self-evolving-patrol/0.5"}
    if api_key:
        if auth_header.lower() == "authorization":
            headers["Authorization"] = api_key if api_key.lower().startswith("bearer ") else f"Bearer {api_key}"
        else:
            headers[auth_header] = api_key
    req = request.Request(url, headers=headers, method="GET")
    with request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 - endpoint is user-configured via GitHub Secrets
        text = resp.read().decode("utf-8")
        return json.loads(text)


def _candidate_targets(snapshot: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    candidates = snapshot.get("candidates") if isinstance(snapshot.get("candidates"), list) else []
    targets = [c for c in candidates if c.get("token_address") and (c.get("classification") == "主观察" or c.get("emergency_precision_check"))]
    return sorted(targets, key=lambda c: (bool(c.get("emergency_precision_check")), int(c.get("score") or 0)), reverse=True)[:limit]


def _merge_raw_rows(existing: Dict[str, Any], raw: Dict[str, Any], valid_days: int) -> Dict[str, Any] | None:
    rows: List[Dict[str, Any]] = []
    if isinstance(raw.get("wallets"), list):
        rows = raw["wallets"]
    elif isinstance(raw.get("responses"), list):
        for res in raw.get("responses") or []:
            rows.extend(_extract_wallet_rows(res.get("payload")))
    if not rows:
        return None
    updated = upsert_ave_smart_wallets(existing, rows, refresh_scope=str(raw.get("refresh_scope") or "incremental"))
    updated["valid_days"] = valid_days
    updated["refresh_mode"] = "merged_from_ave_raw_or_response_rows"
    return updated


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    strategy = read_json(CONFIG_PATH, {})
    smart_cfg = strategy.get("smart_money") or {}
    ave_cfg = smart_cfg.get("ave_api") or {}
    valid_days = int(smart_cfg.get("ave_cache_valid_days", 7))
    existing = load_smart_wallet_cache(CACHE_PATH, valid_days=valid_days)

    api_key = os.getenv("AVE_API_KEY")
    endpoint_template = os.getenv("AVE_SMART_WALLET_ENDPOINT_TEMPLATE") or ave_cfg.get("smart_wallet_endpoint_template")
    auth_header = os.getenv("AVE_AUTH_HEADER") or ave_cfg.get("auth_header") or "X-API-KEY"
    target_limit = int(os.getenv("AVE_TARGET_LIMIT") or ave_cfg.get("target_limit", 12))
    refresh_scope = os.getenv("AVE_REFRESH_SCOPE") or ave_cfg.get("refresh_scope") or "incremental"

    latest = read_json(LATEST_SNAPSHOT, {})
    targets = _candidate_targets(latest, target_limit)
    raw_out: Dict[str, Any] = {
        "version": "0.5.0-ave-weekly-cache-refresh",
        "run_time_utc": _now(),
        "api_key_present": bool(api_key),
        "endpoint_template_configured": bool(endpoint_template),
        "auth_header": auth_header if auth_header.lower() != "authorization" else "Authorization",
        "target_count": len(targets),
        "refresh_scope": refresh_scope,
        "responses": [],
        "wallets": [],
        "status": "not_started",
        "limitations": [
            "AVE endpoint is configurable. The code does not hard-code an undocumented AVE path.",
            "If endpoint is not configured, the workflow preserves existing cache and can still merge manually supplied output/ave_raw_smart_money.json rows.",
        ],
    }

    collected_rows: List[Dict[str, Any]] = []
    if endpoint_template and api_key and targets:
        for c in targets:
            url = _format_endpoint(endpoint_template, c)
            safe_url = url.replace(api_key, "***") if api_key else url
            item = {
                "token": c.get("token"),
                "chain": c.get("chain"),
                "token_address": c.get("token_address"),
                "endpoint": safe_url,
                "status": "pending",
            }
            try:
                payload = _http_get_json(url, api_key=api_key, auth_header=auth_header)
                rows = _extract_wallet_rows(payload)
                for r in rows:
                    r.setdefault("chain", c.get("chain"))
                    related = r.get("related_tokens") or []
                    if isinstance(related, list):
                        if c.get("token_address") not in related:
                            related.append(c.get("token_address"))
                        r["related_tokens"] = related
                collected_rows.extend(rows)
                item.update({"status": "ok", "wallet_rows": len(rows), "payload": payload})
            except Exception as exc:  # noqa: BLE001
                item.update({"status": "failed", "error": str(exc)[:240]})
            raw_out["responses"].append(item)
        raw_out["wallets"] = collected_rows
        raw_out["status"] = "queried_configured_endpoint"
    else:
        raw_out["status"] = "endpoint_or_key_not_configured"

    # Also merge rows already present in RAW_PATH, so users can manually drop AVE export rows.
    manual_raw = read_json(RAW_PATH, {})
    manual_rows = []
    if isinstance(manual_raw.get("wallets"), list):
        manual_rows = manual_raw["wallets"]
    collected_rows.extend(manual_rows)
    raw_out["manual_wallet_rows_merged"] = len(manual_rows)

    if collected_rows:
        updated = upsert_ave_smart_wallets(existing, collected_rows, refresh_scope=refresh_scope)
        updated["valid_days"] = valid_days
        updated["refresh_mode"] = "ave_endpoint_or_raw_json_merge_v0.5"
        updated["ave_api_key_present"] = bool(api_key)
        updated["endpoint_template_configured"] = bool(endpoint_template)
        write_smart_wallet_cache(CACHE_PATH, updated)
        raw_out["merged_wallet_rows"] = len(collected_rows)
        raw_out["cache_wallet_count_after_merge"] = updated.get("wallet_count")
        raw_out["cache_status_after_merge"] = updated.get("status")
        print(f"Merged {len(collected_rows)} AVE smart-wallet rows into {CACHE_PATH}")
    else:
        # Preserve existing cache and still write canonical structure.
        write_smart_wallet_cache(CACHE_PATH, existing)
        raw_out["merged_wallet_rows"] = 0
        raw_out["cache_wallet_count_after_merge"] = existing.get("wallet_count", 0)
        raw_out["cache_status_after_merge"] = existing.get("status")
        print("No AVE wallet rows collected. Cache preserved.")

    write_json(RAW_PATH, raw_out)


if __name__ == "__main__":
    main()

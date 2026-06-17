from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .free_scan import scan_free_sources
from .chain_verify import verify_candidates
from .report_writer import build_report
from .self_evolver import evaluate_strategy_patch
from .smart_wallet_cache import load_smart_wallet_cache, write_smart_wallet_cache

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "strategy_config.json"
OUTPUT_DIR = ROOT / "output"
LATEST_SNAPSHOT = OUTPUT_DIR / "latest_snapshot.json"
PREVIOUS_SNAPSHOT = OUTPUT_DIR / "previous_snapshot.json"
LATEST_REPORT = OUTPUT_DIR / "latest_report.md"
STRATEGY_PATCH = OUTPUT_DIR / "strategy_patch.json"
CHAIN_VERIFY_LATEST = OUTPUT_DIR / "chain_verify_latest.json"
SMART_WALLET_CACHE = OUTPUT_DIR / "smart_wallet_cache.json"
HISTORY_DIR = OUTPUT_DIR / "history"


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


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    strategy = read_json(CONFIG_PATH, {})
    previous = read_json(LATEST_SNAPSHOT, {"status": "no_previous_snapshot"})

    # Move previous latest to previous_snapshot before writing new one.
    write_json(PREVIOUS_SNAPSHOT, previous)

    snapshot = scan_free_sources(strategy)

    # v0.4: read weekly AVE smart-wallet cache and add chain-address preflight.
    valid_days = int((strategy.get("smart_money") or {}).get("ave_cache_valid_days", 7))
    smart_cache = load_smart_wallet_cache(SMART_WALLET_CACHE, valid_days=valid_days)
    # v0.4.1: always persist/refresh the cache file, even when AVE is not configured.
    # This guarantees output/smart_wallet_cache.json exists for downstream readers.
    write_smart_wallet_cache(SMART_WALLET_CACHE, smart_cache)
    snapshot["smart_wallet_cache_status"] = {
        "status": smart_cache.get("status"),
        "wallet_count": smart_cache.get("wallet_count"),
        "last_refresh_at": smart_cache.get("last_refresh_at"),
        "age_days": smart_cache.get("age_days"),
        "is_stale": smart_cache.get("is_stale"),
        "valid_days": smart_cache.get("valid_days"),
    }
    for c in snapshot.get("candidates", []):
        if smart_cache.get("status") == "active":
            c["smart_money_source_status"] = "ave_weekly_cache_available_plus_proxy"
            c["smart_money_judgment"] = str(c.get("smart_money_judgment", "")) + "；AVE周缓存可用，等待链上钱包映射"
        elif smart_cache.get("status") == "stale":
            c["smart_money_source_status"] = "ave_weekly_cache_stale_plus_proxy"
            c["smart_money_judgment"] = str(c.get("smart_money_judgment", "")) + "；AVE周缓存过期，不作高置信依据"
        else:
            c["smart_money_source_status"] = "proxy_only_no_ave_cache"

    chain_verify = verify_candidates(snapshot, strategy)
    snapshot["chain_verify"] = {k: v for k, v in chain_verify.items() if k != "results"}
    patch = evaluate_strategy_patch(snapshot, previous, strategy)

    write_json(CHAIN_VERIFY_LATEST, chain_verify)
    write_json(LATEST_SNAPSHOT, snapshot)
    write_json(STRATEGY_PATCH, patch)

    history_file = HISTORY_DIR / f"{snapshot['snapshot_id']}.json"
    write_json(history_file, snapshot)

    report = build_report(snapshot, previous, strategy, patch)
    LATEST_REPORT.write_text(report, encoding="utf-8")

    print(f"Generated snapshot: {LATEST_SNAPSHOT}")
    print(f"Generated report: {LATEST_REPORT}")
    print(f"Candidates: {len(snapshot.get('candidates', []))}")


if __name__ == "__main__":
    main()

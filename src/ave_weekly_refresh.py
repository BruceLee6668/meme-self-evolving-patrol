from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List

from .smart_wallet_cache import load_smart_wallet_cache, upsert_ave_smart_wallets, write_smart_wallet_cache

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
CACHE_PATH = OUTPUT_DIR / "smart_wallet_cache.json"
RAW_PATH = OUTPUT_DIR / "ave_raw_smart_money.json"
CONFIG_PATH = ROOT / "config" / "strategy_config.json"


def read_json(path: Path, default: Dict[str, Any]) -> Dict[str, Any]:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    strategy = read_json(CONFIG_PATH, {})
    valid_days = int((strategy.get("smart_money") or {}).get("ave_cache_valid_days", 7))
    existing = load_smart_wallet_cache(CACHE_PATH, valid_days=valid_days)

    # v0.4 keeps the workflow safe: if AVE key/endpoints are not configured, do not fail.
    # If output/ave_raw_smart_money.json exists, merge it. Later versions can replace this
    # with direct AVE endpoints once the exact API payload is confirmed.
    ave_key = os.getenv("AVE_API_KEY")
    raw = read_json(RAW_PATH, {})
    rows: List[Dict[str, Any]] = []
    if isinstance(raw.get("wallets"), list):
        rows = raw["wallets"]

    if rows:
        updated = upsert_ave_smart_wallets(existing, rows)
        updated["refresh_mode"] = "merged_from_ave_raw_smart_money_json"
        updated["ave_api_key_present"] = bool(ave_key)
        write_smart_wallet_cache(CACHE_PATH, updated)
        print(f"Merged {len(rows)} AVE smart-wallet rows into {CACHE_PATH}")
    else:
        # Preserve existing cache. Write bootstrap file if absent.
        if not CACHE_PATH.exists():
            write_smart_wallet_cache(CACHE_PATH, existing)
        print("No AVE raw wallet rows found. Cache preserved. Set AVE_API_KEY and implement endpoint mapping in v0.5, or place rows in output/ave_raw_smart_money.json.")


if __name__ == "__main__":
    main()

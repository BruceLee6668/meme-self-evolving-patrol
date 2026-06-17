from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .free_scan import scan_free_sources
from .report_writer import build_report
from .self_evolver import evaluate_strategy_patch

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "strategy_config.json"
OUTPUT_DIR = ROOT / "output"
LATEST_SNAPSHOT = OUTPUT_DIR / "latest_snapshot.json"
PREVIOUS_SNAPSHOT = OUTPUT_DIR / "previous_snapshot.json"
LATEST_REPORT = OUTPUT_DIR / "latest_report.md"
STRATEGY_PATCH = OUTPUT_DIR / "strategy_patch.json"
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
    patch = evaluate_strategy_patch(snapshot, previous, strategy)

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

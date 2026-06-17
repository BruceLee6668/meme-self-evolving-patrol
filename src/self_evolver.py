from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def evaluate_strategy_patch(snapshot: Dict[str, Any], previous: Dict[str, Any], strategy: Dict[str, Any]) -> Dict[str, Any]:
    """Conservative strategy patcher.

    v0 avoids aggressive auto-tuning. It only records whether a change is suggested.
    Later versions can persist modifications to strategy_config.json when enough history exists.
    """
    candidates = snapshot.get("candidates", [])
    if not candidates:
        return {
            "has_patch": False,
            "patches": [],
            "summary": "无候选，暂不调整策略",
            "no_patch_reason": "数据样本不足",
            "evaluated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        }

    pvp_count = sum(1 for c in candidates if c.get("classification") == "PVP风险池")
    total = len(candidates)
    pvp_ratio = pvp_count / total if total else 0

    # In v0, produce patch suggestions but do not change strategy automatically unless extremely noisy.
    if pvp_ratio > 0.8 and total >= 10:
        return {
            "has_patch": True,
            "patches": [
                {
                    "field": "thresholds.pvp_volume_lp_warning",
                    "old_value": strategy.get("thresholds", {}).get("pvp_volume_lp_warning"),
                    "new_value": strategy.get("thresholds", {}).get("pvp_volume_lp_warning"),
                    "reason": "PVP候选占比过高，但v0先不自动改阈值，只提示继续观察",
                    "impact": "下轮继续严格分离PVP，不放宽主观察池",
                    "writeback_type": "logical_confirmation_only",
                }
            ],
            "summary": "确认PVP过滤继续生效；v0不改变数值阈值",
            "evaluated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        }

    return {
        "has_patch": False,
        "patches": [],
        "summary": "本轮无充分数据支持策略变更",
        "no_patch_reason": "候选结构未显示明显阈值失效",
        "evaluated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }

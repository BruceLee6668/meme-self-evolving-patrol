from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def evaluate_strategy_patch(snapshot: Dict[str, Any], previous: Dict[str, Any], strategy: Dict[str, Any]) -> Dict[str, Any]:
    """Conservative strategy patcher.

    v0.1 focuses on structural quality: multi-pool merge, capped main watchlist,
    richer scoring. It still avoids aggressive numeric threshold writeback until
    we have several successful runs.
    """
    candidates = snapshot.get("candidates", [])
    summary = snapshot.get("summary", {})
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    if not candidates:
        return {
            "has_patch": False,
            "patches": [],
            "summary": "无候选，暂不调整策略",
            "no_patch_reason": "数据样本不足",
            "evaluated_at": now,
        }

    pvp_count = summary.get("pvp_count", sum(1 for c in candidates if c.get("classification") == "PVP风险池"))
    main_count = summary.get("main_watch_count", sum(1 for c in candidates if c.get("classification") == "主观察"))
    total = len(candidates)
    pvp_ratio = pvp_count / total if total else 0
    conflict_count = summary.get("multi_pool_conflict_count", 0)

    patches = []

    if pvp_ratio > 0.75 and total >= 10:
        patches.append({
            "field": "discovery_focus",
            "old_value": "broad_hot_trending",
            "new_value": "keep_pvp_separated_and_focus_on_lp_quality",
            "reason": "PVP候选占比过高，说明热榜噪声仍大",
            "impact": "下轮继续限制高换手币进入主观察，不放宽Volume/LP阈值",
            "writeback_type": "logical_confirmation_only",
        })

    if main_count > strategy.get("thresholds", {}).get("max_main_watchlist", 5):
        patches.append({
            "field": "thresholds.max_main_watchlist",
            "old_value": strategy.get("thresholds", {}).get("max_main_watchlist"),
            "new_value": strategy.get("thresholds", {}).get("max_main_watchlist"),
            "reason": "主观察候选仍然过多，但v0.1已做数量上限，暂不继续降低",
            "impact": "保持主榜稀缺，避免17个主观察的问题复发",
            "writeback_type": "logical_confirmation_only",
        })

    if conflict_count > 0:
        patches.append({
            "field": "multi_pool_conflict_policy",
            "old_value": "soft_check",
            "new_value": "confidence_downgrade",
            "reason": "本轮存在多池数据冲突，不能用单池数据给高置信判断",
            "impact": "多池价格/LP冲突的币降置信度，不直接升级主观察",
            "writeback_type": "logical_confirmation_only",
        })

    if patches:
        return {
            "has_patch": True,
            "patches": patches,
            "summary": "本轮确认结构性规则：PVP分离、多池冲突降置信、主榜保持稀缺",
            "evaluated_at": now,
        }

    return {
        "has_patch": False,
        "patches": [],
        "summary": "本轮无充分数据支持数值阈值变更",
        "no_patch_reason": "v0.1结构修正后先累计多轮样本，再做数值阈值调整",
        "evaluated_at": now,
    }

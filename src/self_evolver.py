from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict


def evaluate_strategy_patch(snapshot: Dict[str, Any], previous: Dict[str, Any], strategy: Dict[str, Any]) -> Dict[str, Any]:
    """Conservative strategy patcher.

    v0.2 focuses on structural quality: early-alpha range filtering, stronger
    duplicate merging, visible PVP pool, and mature-pool separation. It avoids
    aggressive numeric threshold changes until several runs confirm direction.
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
    mature_count = summary.get("mature_count", sum(1 for c in candidates if c.get("classification") == "成熟池观察"))
    total = len(candidates)
    pvp_ratio = pvp_count / total if total else 0
    mature_ratio = mature_count / total if total else 0
    conflict_count = summary.get("multi_pool_conflict_count", 0)
    symbol_bridge_count = summary.get("symbol_bridge_merge_count", 0)

    patches = []

    if pvp_count == 0 and total >= 20:
        patches.append({
            "field": "pvp_visibility_policy",
            "old_value": "pvp_may_be_hidden_by_score_sorting",
            "new_value": "include_top_pvp_in_output",
            "reason": "上一版PVP风险池可能被排序挤出报告，本轮v0.2要求保留可见PVP池",
            "impact": "下轮继续强制展示PVP风险候选，便于观察噪声和假阳性",
            "writeback_type": "logical_confirmation_only",
        })

    if pvp_ratio > 0.65 and total >= 10:
        patches.append({
            "field": "discovery_focus",
            "old_value": "broad_hot_trending",
            "new_value": "keep_pvp_separated_and_focus_on_lp_quality",
            "reason": "PVP候选占比过高，说明热榜噪声仍大",
            "impact": "下轮继续限制高换手币进入主观察，不放宽Volume/LP阈值",
            "writeback_type": "logical_confirmation_only",
        })

    if mature_count > 0:
        patches.append({
            "field": "early_alpha_range_filter",
            "old_value": "not_strict_enough",
            "new_value": "mature_pool_separation",
            "reason": "检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜",
            "impact": "成熟大池进入成熟池观察，不作为底部MEME扫货主观察",
            "writeback_type": "logical_confirmation_only",
        })

    if main_count > strategy.get("thresholds", {}).get("max_main_watchlist", 5):
        patches.append({
            "field": "thresholds.max_main_watchlist",
            "old_value": strategy.get("thresholds", {}).get("max_main_watchlist"),
            "new_value": strategy.get("thresholds", {}).get("max_main_watchlist"),
            "reason": "主观察候选仍然过多，但v0.2已做数量上限，暂不继续降低",
            "impact": "保持主榜稀缺，避免过多主观察的问题复发",
            "writeback_type": "logical_confirmation_only",
        })

    if conflict_count > 0:
        patches.append({
            "field": "multi_pool_conflict_policy",
            "old_value": "confidence_downgrade",
            "new_value": "confidence_downgrade_plus_representative_largest_lp_pool",
            "reason": "本轮存在多池数据冲突，不能用单池数据给高置信判断",
            "impact": "多池价格/LP冲突的币降置信度，不直接升级主观察",
            "writeback_type": "logical_confirmation_only",
        })

    if symbol_bridge_count > 0:
        patches.append({
            "field": "symbol_bridge_merge_policy",
            "old_value": "address_only_or_gecko_symbol_fallback",
            "new_value": "bridge_gecko_only_rows_to_dex_rows_when_symbol_is_non_ambiguous",
            "reason": "本轮存在symbol桥接合并，说明重复输出问题正在被修正",
            "impact": "减少同一Token在主观察/次观察中重复出现",
            "writeback_type": "logical_confirmation_only",
        })

    if patches:
        return {
            "has_patch": True,
            "patches": patches,
            "summary": "本轮确认结构性规则：早期Alpha区间过滤、PVP可见分层、多池冲突降置信、重复合并增强",
            "evaluated_at": now,
        }

    return {
        "has_patch": False,
        "patches": [],
        "summary": "本轮无充分数据支持数值阈值变更",
        "no_patch_reason": "v0.2结构修正后先累计多轮样本，再做数值阈值调整",
        "evaluated_at": now,
    }

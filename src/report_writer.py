from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List


def _fmt_money(v: Any) -> str:
    try:
        x = float(v)
    except Exception:
        return "-"
    if x >= 1_000_000:
        return f"${x/1_000_000:.2f}M"
    if x >= 1_000:
        return f"${x/1_000:.1f}K"
    return f"${x:.2f}"


def _fmt_pct(v: Any) -> str:
    try:
        return f"{float(v):+.2f}%"
    except Exception:
        return "-"


def candidate_rows(candidates: List[Dict[str, Any]], limit: int = 10) -> str:
    if not candidates:
        return "| Token | 链 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |\n|---|---|---|---|---|---|---|\n| - | - | 无候选 | - | - | - | - |"
    lines = [
        "| Token | 链 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |",
        "|---|---|---|---|---|---|---|",
    ]
    for c in candidates[:limit]:
        metrics = (
            f"Score {c.get('score', '-')}; "
            f"LP {_fmt_money(c.get('liquidity_usd'))}; "
            f"Vol24H {_fmt_money(c.get('volume_24h_usd'))}; "
            f"24H {_fmt_pct(c.get('price_change_24h_pct'))}; "
            f"V/LP {c.get('volume_lp_ratio') if c.get('volume_lp_ratio') is not None else '-'}"
        )
        url = c.get("url")
        token = c.get("token") or "UNKNOWN"
        if url:
            token_cell = f"[{token}]({url})"
        else:
            token_cell = token
        lines.append(
            f"| {token_cell} | {c.get('chain_label') or c.get('chain')} | {c.get('classification')} | {metrics} | "
            f"{c.get('smart_money_judgment')} | {c.get('smart_money_source')} | {c.get('operation_conclusion')} |"
        )
    return "\n".join(lines)


def build_report(snapshot: Dict[str, Any], previous: Dict[str, Any], strategy: Dict[str, Any], patch: Dict[str, Any]) -> str:
    run_time = snapshot.get("run_time_utc") or datetime.now(timezone.utc).isoformat()
    candidates = snapshot.get("candidates", [])
    prev_candidates = previous.get("candidates", []) if isinstance(previous, dict) else []

    main_count = sum(1 for c in candidates if c.get("classification") == "主观察")
    pvp_count = sum(1 for c in candidates if c.get("classification") == "PVP风险池")

    lines = []
    lines.append("# 自我进化轮巡")
    lines.append("")
    lines.append(f"**本轮时间 UTC：** {run_time}")
    lines.append(f"**S0 时间锚点：** {strategy.get('s0_anchor', {}).get('jst', '-')}")
    lines.append("")
    lines.append("## 一句话结论")
    if main_count > 0:
        lines.append(f"本轮发现 {main_count} 个主观察候选，但 v0 还未接入钱包级确认，不能直接定义为真实聪明钱吸筹。")
    else:
        lines.append("本轮没有出现可直接确认的“干净底部聪明钱扫货”。")
    lines.append("")

    lines.append("## 第一部分：生成结果表格")
    lines.append("")
    lines.append("### A. 上次记录结果表")
    if previous.get("status") == "no_previous_snapshot" or not prev_candidates:
        lines.append("| Token | 链 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |")
        lines.append("|---|---|---|---|---|---|---|")
        lines.append("| - | - | 上次记录不可用 | 第一次或无有效 previous_snapshot | - | - | - |")
    else:
        lines.append(candidate_rows(prev_candidates, limit=10))
    lines.append("")

    lines.append("### B. 本轮扫描结果表")
    lines.append(candidate_rows(candidates, limit=15))
    lines.append("")

    lines.append("## 第二部分：逻辑复盘表格")
    lines.append("")
    lines.append("### A. 上次逻辑总结表")
    lines.append("| 逻辑项 | 上次规则 | 本轮验证 |")
    lines.append("|---|---|---|")
    lines.append("| 主观察门槛 | LP >= $100K | 继续保留，低 LP 候选不进主榜 |")
    lines.append("| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | 继续保留，防止高换手误判 |")
    lines.append("| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | v0 未接 AVE，仅代理指标，置信度低 |")
    lines.append("")

    lines.append("### B. 本轮逻辑总结表")
    lines.append("| 逻辑项 | 本轮结果 | 判断 |")
    lines.append("|---|---|---|")
    lines.append(f"| 主观察候选 | {main_count} 个 | 需后续链上钱包留存确认 |")
    lines.append(f"| PVP风险池 | {pvp_count} 个 | PVP分层正常工作 |")
    lines.append("| S0对比 | v0 尚未做精确历史回放 | 后续用 GeckoTerminal OHLCV / 链上数据补齐 |")
    lines.append("| Smart Money | v0 仅代理指标 | 不允许标记真实吸筹 |")
    lines.append("")

    lines.append("### C. 本轮优化调整表")
    lines.append("| 调整项 | 触发原因 | 对下轮筛选影响 |")
    lines.append("|---|---|---|")
    if patch.get("has_patch"):
        for p in patch.get("patches", []):
            lines.append(f"| {p.get('field')} | {p.get('reason')} | {p.get('impact')} |")
    else:
        lines.append("| 暂无自动调整 | v0 首轮/数据不足 | 维持当前策略，继续累计样本 |")
    lines.append("")

    lines.append("### D. 挖掘策略调优表")
    lines.append("| 项目 | 本轮判断 |")
    lines.append("|---|---|")
    lines.append("| 当前挖掘策略是否有效 | 部分有效：可完成免费源候选发现和PVP初筛 |")
    lines.append("| 主要问题 | 缺少钱包级数据、AVE周缓存、链上Swap留存和S0精确回放 |")
    lines.append("| 假阳性风险 | 仍然存在，尤其是Net Buys/交易笔数代理指标 |")
    lines.append("| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |")
    lines.append("| 下轮挖掘方向 | 先验证免费源稳定性，再接BSC/SOL链上确认与AVE周缓存 |")
    lines.append("")

    lines.append("## 第三部分：策略回写确认")
    lines.append("")
    lines.append("| 项目 | 状态 |")
    lines.append("|---|---|")
    lines.append(f"| 是否已将本轮优化策略写回主定时策略 | {'是' if patch.get('has_patch') else '否'} |")
    lines.append(f"| 写回内容摘要 | {patch.get('summary', '本轮无策略变更')} |")
    lines.append(f"| 下轮是否生效 | {'是' if patch.get('has_patch') else '维持原策略'} |")
    lines.append(f"| 未写回原因 | {patch.get('no_patch_reason', '-') if not patch.get('has_patch') else '-'} |")
    lines.append("")

    lines.append("## 数据源状态")
    lines.append("| 数据源 | 状态 |")
    lines.append("|---|---|")
    for src, st in snapshot.get("source_status", {}).items():
        lines.append(f"| {src} | {st} |")
    lines.append("")
    lines.append("## 数据限制")
    for item in snapshot.get("data_limitations", []):
        lines.append(f"- {item}")

    return "\n".join(lines)

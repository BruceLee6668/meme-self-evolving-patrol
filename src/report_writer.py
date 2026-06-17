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


def _fmt_ratio(v: Any) -> str:
    try:
        return f"{float(v):.2f}x"
    except Exception:
        return "-"


def _short_address(addr: Any) -> str:
    a = str(addr or "").strip()
    if not a:
        return "不可用"
    if len(a) <= 14:
        return a
    return f"{a[:6]}...{a[-6:]}"


def _addr_cell(c: Dict[str, Any]) -> str:
    addr = c.get("token_address") or c.get("contract_address")
    if not addr:
        return "不可用"
    url = c.get("contract_url")
    short = _short_address(addr)
    return f"[{short}]({url})" if url else short


def _core_metrics(c: Dict[str, Any]) -> str:
    comp = c.get("score_components") or {}
    return (
        f"Score {c.get('score','-')}; "
        f"Tier {c.get('liquidity_tier','-')}; "
        f"LP {_fmt_money(c.get('liquidity_usd'))}; "
        f"Vol24H {_fmt_money(c.get('volume_24h_usd'))}; "
        f"24H {_fmt_pct(c.get('price_change_24h_pct'))}; "
        f"V/LP {_fmt_ratio(c.get('volume_lp_ratio'))}; "
        f"池数 {c.get('pool_count', 1)}; "
        f"分项 L{comp.get('liquidity_score','-')}/V{comp.get('volume_score','-')}/B{comp.get('bottom_score','-')}/Buy{comp.get('buy_balance_score','-')}/Risk-{comp.get('risk_penalty','-')}"
    )


def candidate_rows(candidates: List[Dict[str, Any]], limit: int = 10) -> str:
    if not candidates:
        return "| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |\n|---|---|---|---|---|---|---|---|\n| - | - | - | 无候选 | - | - | - | - |"
    lines = [
        "| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for c in candidates[:limit]:
        url = c.get("url")
        token = c.get("token") or "UNKNOWN"
        token_cell = f"[{token}]({url})" if url else token
        sm_source = c.get("smart_money_source_status") or c.get("smart_money_source") or "-"
        lines.append(
            f"| {token_cell} | {c.get('chain_label') or c.get('chain')} | {_addr_cell(c)} | {c.get('classification')} | {_core_metrics(c)} | "
            f"{c.get('smart_money_judgment')} | {sm_source} | {c.get('operation_conclusion')} |"
        )
    return "\n".join(lines)


def detail_rows(candidates: List[Dict[str, Any]], classification: str, limit: int = 8) -> str:
    rows = [c for c in candidates if c.get("classification") == classification]
    if not rows:
        return "| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |\n|---|---|---|---|---|---|\n| - | - | - | 无 | - | - |"
    lines = [
        "| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |",
        "|---|---|---|---|---|---|",
    ]
    for c in rows[:limit]:
        token = c.get("token") or "UNKNOWN"
        token_cell = f"[{token}]({c.get('url')})" if c.get("url") else token
        reason = c.get("classification_reason") or "-"
        lines.append(f"| {token_cell} | {c.get('chain_label') or c.get('chain')} | {_addr_cell(c)} | {reason} | {_core_metrics(c)} | {c.get('operation_conclusion')} |")
    return "\n".join(lines)


def chain_verify_rows(candidates: List[Dict[str, Any]], limit: int = 10) -> str:
    rows = [c for c in candidates if c.get("needs_chain_verify") or c.get("emergency_precision_check")]
    if not rows:
        return "| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 原因 |\n|---|---|---|---|---|---|\n| - | - | - | 否 | 否 | 无 |"
    rows = sorted(rows, key=lambda c: (bool(c.get("emergency_precision_check")), c.get("score", 0)), reverse=True)
    lines = [
        "| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 原因 |",
        "|---|---|---|---|---|---|",
    ]
    for c in rows[:limit]:
        token = c.get("token") or "UNKNOWN"
        token_cell = f"[{token}]({c.get('url')})" if c.get("url") else token
        lines.append(
            f"| {token_cell} | {c.get('chain_label') or c.get('chain')} | {_addr_cell(c)} | "
            f"{'是' if c.get('needs_chain_verify') else '否'} | {'是' if c.get('emergency_precision_check') else '否'} | {c.get('chain_verify_reason','-')} |"
        )
    return "\n".join(lines)


def _summary_rows(snapshot: Dict[str, Any]) -> str:
    s = snapshot.get("summary") or {}
    return "\n".join([
        "| 指标 | 数量 |",
        "|---|---:|",
        f"| 原始池子记录 | {s.get('raw_pair_count', 0)} |",
        f"| 合并后Token | {s.get('merged_token_count', 0)} |",
        f"| 输出候选 | {s.get('returned_candidate_count', 0)} |",
        f"| 主观察 | {s.get('main_watch_count', 0)} |",
        f"| 次观察 | {s.get('secondary_watch_count', 0)} |",
        f"| PVP风险池 | {s.get('pvp_count', 0)} |",
        f"| 成熟池观察 | {s.get('mature_count', 0)} |",
        f"| 低优先观察 | {s.get('low_priority_count', 0)} |",
        f"| 多池Token | {s.get('multi_pool_count', 0)} |",
        f"| 多池冲突 | {s.get('multi_pool_conflict_count', 0)} |",
        f"| Symbol桥接合并 | {s.get('symbol_bridge_merge_count', 0)} |",
        f"| 合约地址可用 | {s.get('contract_address_available_count', 0)} |",
        f"| 合约地址缺失 | {s.get('contract_address_missing_count', 0)} |",
        f"| Micro层 | {s.get('micro_tier_count', 0)} |",
        f"| Early层 | {s.get('early_tier_count', 0)} |",
        f"| Liquid层 | {s.get('liquid_tier_count', 0)} |",
        f"| Mature层 | {s.get('mature_tier_count', 0)} |",
        f"| 需要链上确认 | {s.get('needs_chain_verify_count', 0)} |",
        f"| 紧急精查候选 | {s.get('emergency_precision_check_count', 0)} |",
    ])


def build_report(snapshot: Dict[str, Any], previous: Dict[str, Any], strategy: Dict[str, Any], patch: Dict[str, Any]) -> str:
    run_time = snapshot.get("run_time_utc") or datetime.now(timezone.utc).isoformat()
    candidates = snapshot.get("candidates", [])
    prev_candidates = previous.get("candidates", []) if isinstance(previous, dict) else []
    summary = snapshot.get("summary") or {}

    main_count = summary.get("main_watch_count", sum(1 for c in candidates if c.get("classification") == "主观察"))
    pvp_count = summary.get("pvp_count", sum(1 for c in candidates if c.get("classification") == "PVP风险池"))
    mature_count = summary.get("mature_count", sum(1 for c in candidates if c.get("classification") == "成熟池观察"))
    merged_count = summary.get("merged_token_count", len(candidates))
    addr_ok = summary.get("contract_address_available_count", 0)
    addr_missing = summary.get("contract_address_missing_count", 0)

    lines = []
    lines.append("# 自我进化轮巡")
    lines.append("")
    lines.append(f"**本轮时间 UTC：** {run_time}")
    lines.append(f"**版本：** {snapshot.get('version', strategy.get('version', '-'))}")
    lines.append(f"**S0 时间锚点：** {strategy.get('s0_anchor', {}).get('jst', '-')}")
    lines.append("")
    lines.append("## 一句话结论")
    if main_count > 0:
        lines.append(f"本轮从 {merged_count} 个合并Token中筛出 {main_count} 个主观察候选。v0.3已把合约地址作为主输出字段，并增加Micro/Early/Liquid/Mature分层、PVP明细、成熟池明细和链上确认标记。")
    else:
        lines.append("本轮没有出现可直接确认的“干净底部聪明钱扫货”。")
    lines.append(f"合约地址可用 {addr_ok} 个，缺失 {addr_missing} 个；缺失地址的候选不能进入后续链上精查。")
    lines.append("")

    lines.append("## 本轮扫描摘要")
    lines.append(_summary_rows(snapshot))
    lines.append("")

    lines.append("## 第一部分：生成结果表格")
    lines.append("")
    lines.append("### A. 上次记录结果表")
    if previous.get("status") == "no_previous_snapshot" or not prev_candidates:
        lines.append("| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |")
        lines.append("|---|---|---|---|---|---|---|---|")
        lines.append("| - | - | - | 上次记录不可用 | 第一次或无有效 previous_snapshot | - | - | - |")
    else:
        lines.append(candidate_rows(prev_candidates, limit=10))
    lines.append("")

    lines.append("### B. 本轮扫描结果表")
    lines.append(candidate_rows(candidates, limit=15))
    lines.append("")

    lines.append("### C. PVP风险池明细表")
    lines.append(detail_rows(candidates, "PVP风险池", limit=8))
    lines.append("")

    lines.append("### D. 成熟池观察明细表")
    lines.append(detail_rows(candidates, "成熟池观察", limit=8))
    lines.append("")

    lines.append("### E. 链上确认/紧急精查表")
    lines.append(chain_verify_rows(candidates, limit=10))
    lines.append("")

    lines.append("## 第二部分：逻辑复盘表格")
    lines.append("")
    lines.append("### A. 上次逻辑总结表")
    lines.append("| 逻辑项 | 上次规则 | 本轮验证 |")
    lines.append("|---|---|---|")
    lines.append("| 主观察门槛 | LP >= $100K，且非PVP，且不过成熟 | v0.3继续保留，并新增LP层级避免不同阶段候选混在一起 |")
    lines.append("| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | v0.3增加PVP明细表，风险不再黑箱隐藏 |")
    lines.append("| 多池处理 | symbol bridge合并，以最大LP池为代表 | v0.3保留，并继续标注多池冲突 |")
    lines.append("| 合约地址 | v0.2未在主表强制展示 | v0.3强制展示合约地址；缺失时标注不可用 |")
    lines.append("| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | 仍未接AVE，当前只用代理指标，置信度低 |")
    lines.append("")

    lines.append("### B. 本轮逻辑总结表")
    lines.append("| 逻辑项 | 本轮结果 | 判断 |")
    lines.append("|---|---|---|")
    lines.append(f"| 主观察候选 | {main_count} 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |")
    lines.append(f"| PVP风险池 | {pvp_count} 个 | v0.3已单独展示明细，便于判断噪声来源 |")
    lines.append(f"| 成熟池观察 | {mature_count} 个 | 成熟资产不占早期Alpha主榜 |")
    lines.append(f"| 合约地址覆盖 | 可用 {addr_ok}，缺失 {addr_missing} | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |")
    lines.append(f"| LP层级 | Micro {summary.get('micro_tier_count',0)} / Early {summary.get('early_tier_count',0)} / Liquid {summary.get('liquid_tier_count',0)} / Mature {summary.get('mature_tier_count',0)} | 下一步可以按层级分别设置进攻规则 |")
    lines.append("| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |")
    lines.append("| Smart Money | 仅代理指标 | 不允许标记真实吸筹 |")
    lines.append("")

    lines.append("### C. 本轮优化调整表")
    lines.append("| 调整项 | 触发原因 | 对下轮筛选影响 |")
    lines.append("|---|---|---|")
    if patch.get("has_patch"):
        for p in patch.get("patches", []):
            lines.append(f"| {p.get('field')} | {p.get('reason')} | {p.get('impact')} |")
    else:
        lines.append("| 暂无自动数值调整 | v0.3先做输出结构和字段完整性增强，不轻易改阈值 | 维持当前策略，继续累计样本 |")
    lines.append("")

    lines.append("### D. 挖掘策略调优表")
    lines.append("| 项目 | 本轮判断 |")
    lines.append("|---|---|")
    lines.append("| 当前挖掘策略是否有效 | 部分有效：免费源可发现候选，v0.3能展示合约地址、PVP明细、成熟池明细和链上确认需求 |")
    lines.append("| 主要问题 | 缺少钱包级数据、AVE周缓存、链上Swap留存和S0精确回放；合约地址缺失候选无法精查 |")
    lines.append("| 假阳性风险 | 已降低，但代理指标仍可能误判买盘质量 |")
    lines.append("| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |")
    lines.append("| 候选来源调整 | 暂不新增外部源，下一步优先接BSC/SOL链上精查，并用合约地址作为入口 |")
    lines.append("| 阈值调整 | 暂不改数值；先按Micro/Early/Liquid/Mature层级观察不同阶段表现 |")
    lines.append("| 下轮挖掘方向 | 主观察必须有合约地址；PVP和成熟池继续单独展示；优先推进BSC RPC/Helius链上确认 |")
    lines.append("")

    lines.append("## 第三部分：策略回写确认")
    lines.append("")
    lines.append("| 项目 | 状态 |")
    lines.append("|---|---|")
    lines.append(f"| 是否已将本轮优化策略写回主定时策略 | {'是' if patch.get('has_patch') else '否'} |")
    lines.append(f"| 写回内容摘要 | {patch.get('summary', '本轮无策略变更')} |")
    lines.append(f"| 下轮是否生效 | {'是' if patch.get('has_patch') else '维持v0.3策略'} |")
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

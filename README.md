# meme-self-evolving-patrol

BSC + SOL MEME 自我进化轮巡。

## 当前版本

`v0.1.1-free-sources-quality-filter`

本版本仍只接免费公开数据源：

- DEXScreener：候选发现、价格、LP、成交、涨跌、多池数据
- GeckoTerminal：Trending pools / 后续补 OHLCV

尚未接入：

- AVE Smart Money 周缓存
- Helius / Solana 交易解析
- BSC RPC Swap 解析
- 精确 S0 历史回放

## v0.1.1 修正点

相比 v0：

1. **主观察数量压缩**：新增 `max_main_watchlist=5`，避免一次输出 17 个主观察。
2. **多池合并**：同一 Token 多个池子会按 Token 合并，以最大 LP 池作为代表。
3. **多池冲突降置信**：价格/LP/成交冲突明显时，标记 `multi_pool_conflict`。
4. **评分分项拆开**：输出 Liquidity / Volume / Bottom / Buy / Risk 分项，避免大量候选同分。
5. **更严格 PVP 隔离**：Volume/LP 过高、年轻币暴拉，默认进入 PVP 风险池。

## 输出文件

每次 GitHub Actions 跑完，会更新：

- `output/latest_snapshot.json`
- `output/previous_snapshot.json`
- `output/latest_report.md`
- `output/strategy_patch.json`
- `output/history/*.json`

## GitHub Actions

`.github/workflows/hourly_patrol.yml` 已配置：

- 手动触发：`workflow_dispatch`
- 每小时整点触发：`schedule cron: 0 * * * *`

## 下一步计划

1. 接 BSC RPC，确认 BSC 大额 Swap 和钱包留存。
2. 接 Helius Free，确认 SOL 交易解析。
3. 接 AVE 每周 Smart Money 缓存。
4. 增加 S0 精确历史回放。

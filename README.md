# meme-self-evolving-patrol

BSC + SOL MEME 自我进化轮巡。

## 当前版本

`v0.3.0-contract-address-tier-detail`

当前版本在 v0.2 基础上继续增强报告可交易性和后续链上精查入口。

### 已接入免费公开数据源

- DEXScreener：候选发现、价格、LP、成交、涨跌、多池数据、合约地址
- GeckoTerminal：Trending pools / 后续补 OHLCV

### v0.3 新增能力

- **合约地址强制输出**：主结果表、PVP明细、成熟池明细都显示合约地址；BSC 链接到 BscScan，SOL 链接到 Solscan。
- **合约地址来源标记**：DEXScreener baseToken / GeckoTerminal relationship / unavailable。
- **LP层级分离**：Micro / Early / Liquid / Mature，避免不同成熟度候选混在一起。
- **PVP风险池明细表**：不再只显示数量，明确列出哪些币被降级为 PVP。
- **成熟池观察明细表**：百万级/成熟资产不占早期 Alpha 主榜，但保留观察。
- **链上确认/紧急精查表**：生成 `needs_chain_verify`、`chain_verify_reason`、`emergency_precision_check` 字段，为后续 BSC RPC / Helius 接入准备。
- **Smart Money 数据源状态**：当前仍为代理指标，后续接 AVE 周缓存和本地钱包评分。

## 尚未接入

- AVE Smart Money 周缓存
- Helius / Solana 交易解析
- BSC RPC Swap 解析
- S0 精确历史回放
- 钱包买后留存与胜率评分

## 输出文件

每次 GitHub Actions 跑完，会更新：

- `output/latest_snapshot.json`
- `output/previous_snapshot.json`
- `output/latest_report.md`
- `output/strategy_patch.json`
- `output/history/*.json`

## 运行方式

GitHub Actions：

- 每小时整点自动运行
- 支持手动 `Run workflow`

## 下一步建议

v0.4 优先接入链上确认：

1. BSC RPC：解析 PancakeSwap Swap / LP / 大额买卖。
2. Helius Free：解析 SOL Pump/Raydium/Meteora 交易。
3. 用合约地址作为精查入口，补充钱包留存和大额买卖。

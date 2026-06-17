# meme-self-evolving-patrol

BSC + SOL MEME 自我进化轮巡。

## 当前版本

`v0.2.0-alpha-range-dedupe-pvp`

当前版本仍以免费公开数据源为主：

- DEXScreener：候选发现、价格、LP、成交、涨跌、多池数据
- GeckoTerminal：Trending pools / 后续补 OHLCV

v0.2 重点修正：

- 增加早期 Alpha 区间过滤：过大 LP / 过大 FDV / 过成熟资产不再占用主观察榜。
- 强化 Gecko-only 与 DEXScreener 地址行之间的 symbol bridge 合并，减少 TOESCOIN / KINS 这类重复输出。
- 保留可见 PVP 风险池，不再因为分数排序被挤出报告。
- 把成熟池观察、主观察、次观察、PVP风险池分层输出。
- 继续保留策略回写、逻辑复盘、挖掘策略调优表。

尚未接入：

- AVE Smart Money 周缓存
- Helius / Solana 交易解析
- BSC RPC Swap 解析
- 精确 S0 历史回放

## 输出文件

每次 GitHub Actions 跑完，会更新：

- `output/latest_snapshot.json`
- `output/previous_snapshot.json`
- `output/latest_report.md`
- `output/strategy_patch.json`
- `output/history/*.json`

ChatGPT 后续读取 Raw URL：

```text
https://raw.githubusercontent.com/BruceLee6668/meme-self-evolving-patrol/main/output/latest_snapshot.json
https://raw.githubusercontent.com/BruceLee6668/meme-self-evolving-patrol/main/output/latest_report.md
https://raw.githubusercontent.com/BruceLee6668/meme-self-evolving-patrol/main/config/strategy_config.json
```

## 手动运行

```bash
pip install -r requirements.txt
python -m src.main
```

## GitHub Actions

`.github/workflows/hourly_patrol.yml` 会每小时整点自动运行，也可以在 GitHub Actions 页面手动点击 `Run workflow`。

## 后续阶段

1. v0.2 先稳定免费源扫描质量。
2. 接 Helius Free 做 SOL 交易解析。
3. 接 BSC RPC 做 BSC Swap / LP / 钱包留存。
4. 接 AVE，每周更新 Smart Money 缓存。
5. 将策略调优结果写回 `config/strategy_config.json`。

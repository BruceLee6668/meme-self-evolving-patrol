# meme-self-evolving-patrol

BSC + SOL MEME 自我进化轮巡。

## 当前版本

`v0.1.0-free-sources`

当前版本先接入免费公开数据源：

- DEXScreener：候选发现、价格、LP、成交、涨跌、多池数据
- GeckoTerminal：Trending pools / 后续补 OHLCV

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

1. 先跑通免费源扫描。
2. 接 Helius Free 做 SOL 交易解析。
3. 接 BSC RPC 做 BSC Swap / LP / 钱包留存。
4. 接 AVE，每周更新 Smart Money 缓存。
5. 将策略调优结果写回 `config/strategy_config.json`。

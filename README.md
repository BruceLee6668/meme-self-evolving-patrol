# meme-self-evolving-patrol

BSC + SOL MEME 自我进化轮巡。

## 当前版本

`v0.4.1-output-persistence-fix`

## v0.4.1 新增/修复能力

- 保留 v0.3 的合约地址输出、LP分层、PVP明细表、成熟池明细表、链上确认标记。
- 新增 **BSC/SOL 链上地址预检**：
  - BSC：通过 RPC `eth_getCode` 检查合约是否存在。
  - SOL：通过 RPC `getAccountInfo` 检查 token/account 是否存在，并取少量签名样本。
- 新增 **Smart Wallet Cache 持久化结构**：
  - `output/smart_wallet_cache.json`
  - AVE Smart Money 钱包标签每周刷新一次。
  - 每小时轮巡只读取缓存，不每小时调用 AVE。
- 新增 **AVE周缓存刷新workflow**：
  - `.github/workflows/weekly_ave_refresh.yml`
  - 默认每周一 UTC 00:00 运行，也可以手动运行。
- 新增 **链上预检结果文件**：
  - `output/chain_verify_latest.json`


## v0.4.1 修复点

- 强制生成 `output/chain_verify_latest.json`：即使RPC失败或未配置，也输出标准空结构。
- 强制生成 `output/smart_wallet_cache.json`：即使AVE未配置，也输出标准空缓存结构。
- Workflow提交方式改为 `git add -A output config`，避免新增文件没有被提交。
- 报告底部限制说明更新为v0.4.1当前状态，不再残留v0.3表述。

## 当前已接入数据源

- DEXScreener：候选发现、价格、LP、成交、涨跌、多池数据。
- GeckoTerminal：Trending pools / 后续 OHLCV 预留。
- BSC RPC：v0.4 合约存在性预检。
- Solana RPC / Helius：v0.4 账户存在性预检；如配置 `HELIUS_API_KEY`，优先使用 Helius RPC。

## 尚未完成

- BSC/SOL Swap 方向解析。
- 钱包买入后 30m/1h 留存判断。
- Router/CEX 出货路径追踪。
- AVE 真实接口映射。v0.4 先完成缓存结构与周更workflow，v0.5 再接实际接口。
- S0 精确历史回放。

## 输出文件

每次 GitHub Actions 跑完，会更新：

- `output/latest_snapshot.json`
- `output/previous_snapshot.json`
- `output/latest_report.md`
- `output/strategy_patch.json`
- `output/chain_verify_latest.json`
- `output/history/*.json`

AVE周缓存相关：

- `output/smart_wallet_cache.json`
- `output/ave_raw_smart_money.json`

## GitHub Secrets

当前可选配置：

| Secret | 用途 | 是否必须 |
|---|---|---|
| `HELIUS_API_KEY` | SOL RPC增强查询 | 否 |
| `BSC_RPC_URL` | 自定义BSC RPC | 否 |
| `SOLANA_RPC_URL` | 自定义Solana RPC | 否 |
| `AVE_API_KEY` | 后续AVE周缓存刷新 | v0.5后需要 |

## 使用方式

1. 上传代码到仓库根目录。
2. 进入 Actions。
3. 手动运行 `自我进化轮巡`。
4. 查看 `output/latest_report.md`。
5. 可选：配置 `HELIUS_API_KEY`，提高 SOL 预检稳定性。
6. 后续配置 `AVE_API_KEY` 后，每周运行 `AVE Smart Wallet 周缓存刷新`。

## 关键原则

- 不把 Net Buys 为正直接等同于 Smart Money 吸筹。
- AVE Smart Money 标签只周更，不每小时刷新。
- 每小时轮巡负责行情、LP、成交、PVP、多池、链上预检。
- Smart 钱包身份来自周缓存；当前买卖行为来自链上/DEX小时级数据。
- AVE刷新时保存 smart wallet 地址、标签、画像、置信度、关联Token和风险标签；失效标签不直接删除，只标记 stale/expired。

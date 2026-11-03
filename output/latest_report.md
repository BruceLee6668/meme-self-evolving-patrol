# 自我进化轮巡

**本轮时间 UTC：** 2026-11-03T07:28:47Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 144 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 244 |
| 合并后Token | 144 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 3 |
| 多池Token | 8 |
| 多池冲突 | 5 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 8 |
| Mature层 | 0 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2405，刷新时间 2026-11-02T03:39:47Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 0 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 86; Tier Liquid; LP $1.20M; Vol24H $891.2K; 24H -5.97%; V/LP 0.75x; 池数 1; 分项 L19/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 85; Tier Early; LP $369.7K; Vol24H $2.27M; 24H -3.64%; V/LP 6.14x; 池数 1; 分项 L14/V16/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 78; Tier Liquid; LP $787.8K; Vol24H $508.9K; 24H -8.62%; V/LP 0.65x; 池数 1; 分项 L17/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [NODF](https://dexscreener.com/solana/exulh1zrmfj1gpct8de8hbzqbgrtinalusjldegbmifd) | SOL | [gHeaay...AUpump](https://solscan.io/token/gHeaaywtSrrYWNGf6fAWifNNxnoM8HTE15zFmAUpump) | 次观察 | Score 75; Tier Early; LP $312.5K; Vol24H $160.2K; 24H +17.69%; V/LP 0.51x; 池数 1; 分项 L14/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 次观察 | Score 71; Tier Early; LP $538.0K; Vol24H $1.56M; 24H -38.36%; V/LP 2.91x; 池数 1; 分项 L16/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 69; Tier Early; LP $198.6K; Vol24H $169.6K; 24H +9.46%; V/LP 0.85x; 池数 1; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [KOROSUKE](https://dexscreener.com/solana/8rentt13xhjnxyr7fyf7qhsjskazsqhu2xjskqngw3vt) | SOL | [7ha4HF...Gbpump](https://solscan.io/token/7ha4HFgdvkXaDcR2biCsuBpoCZzoLSRjb5we34Gbpump) | 次观察 | Score 69; Tier Liquid; LP $1.36M; Vol24H $665.0K; 24H +2903.00%; V/LP 0.49x; 池数 1; 分项 L20/V13/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 69; Tier Early; LP $436.9K; Vol24H $265.5K; 24H +19.69%; V/LP 0.61x; 池数 1; 分项 L15/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 67; Tier Early; LP $153.5K; Vol24H $60.8K; 24H -1.56%; V/LP 0.40x; 池数 3; 分项 L11/V5/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GTA](https://dexscreener.com/solana/5isvs31h7hmdggmyuvzmhdsywv7cydd6czjtbqzctlii) | SOL | [BsbsB3...uLpump](https://solscan.io/token/BsbsB3WLq7vbY5En3MBCAsTrcwaCxNKY2Mp5pGuLpump) | 次观察 | Score 66; Tier Early; LP $110.0K; Vol24H $104.4K; 24H +19.71%; V/LP 0.95x; 池数 6; 分项 L10/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 主观察 | Score 83; Tier Early; LP $337.8K; Vol24H $1.41M; 24H +1.06%; V/LP 4.17x; 池数 2; 分项 L14/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 主观察 | Score 82; Tier Liquid; LP $1.19M; Vol24H $1.03M; 24H -9.26%; V/LP 0.86x; 池数 2; 分项 L19/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 80; Tier Early; LP $351.4K; Vol24H $2.37M; 24H -21.18%; V/LP 6.75x; 池数 2; 分项 L14/V16/B17/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [NODF](https://dexscreener.com/solana/exulh1zrmfj1gpct8de8hbzqbgrtinalusjldegbmifd) | SOL | [gHeaay...AUpump](https://solscan.io/token/gHeaaywtSrrYWNGf6fAWifNNxnoM8HTE15zFmAUpump) | 次观察 | Score 75; Tier Early; LP $320.3K; Vol24H $158.8K; 24H +17.38%; V/LP 0.50x; 池数 1; 分项 L14/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 次观察 | Score 75; Tier Early; LP $474.1K; Vol24H $1.86M; 24H -50.86%; V/LP 3.93x; 池数 1; 分项 L15/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 72; Tier Early; LP $144.9K; Vol24H $122.4K; 24H +0.03%; V/LP 0.84x; 池数 1; 分项 L11/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GTA](https://dexscreener.com/solana/5isvs31h7hmdggmyuvzmhdsywv7cydd6czjtbqzctlii) | SOL | [BsbsB3...uLpump](https://solscan.io/token/BsbsB3WLq7vbY5En3MBCAsTrcwaCxNKY2Mp5pGuLpump) | 次观察 | Score 71; Tier Early; LP $110.5K; Vol24H $96.1K; 24H +7.55%; V/LP 0.87x; 池数 5; 分项 L10/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 次观察 | Score 71; Tier Early; LP $185.6K; Vol24H $1.44M; 24H +8.13%; V/LP 7.75x; 池数 1; 分项 L12/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 70; Tier Early; LP $178.4K; Vol24H $183.8K; 24H -10.83%; V/LP 1.03x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 68; Tier Early; LP $432.4K; Vol24H $205.4K; 24H +16.36%; V/LP 0.47x; 池数 1; 分项 L15/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 34; Tier Liquid; LP $1.15M; Vol24H $24.37M; 24H -27.79%; V/LP 21.24x; 池数 1; 分项 L19/V17/B8/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | PVP风险池 | Score 29; Tier Liquid; LP $1.13M; Vol24H $26.02M; 24H -28.61%; V/LP 23.01x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MAMESUKE | SOL | [SCGBBn...gFSTNK](https://solscan.io/token/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK) | PVP风险池 | Score 28; Tier Micro; LP $90.6K; Vol24H $3.82M; 24H +1128.32%; V/LP 42.21x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAPY](https://dexscreener.com/solana/7jyz7ykqvvrhcjrmkhzs1z6fup16pkpcwonvdnkqrert) | SOL | [5DnWmS...8avg2g](https://solscan.io/token/5DnWmSL9t3YqK5MeYq8ozJpna46VcdePWzHvyN8avg2g) | PVP风险池 | Score 26; Tier Micro; LP $60.2K; Vol24H $5.73M; 24H +895.00%; V/LP 95.26x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| STEALTH | SOL | [GoDSW3...xzBmoA](https://solscan.io/token/GoDSW31bTxfkoup9yA1qcGGx9RMXdTEWgApv3xzBmoA) | PVP风险池 | Score 26; Tier Micro; LP $30.6K; Vol24H $678.1K; 24H -19.32%; V/LP 22.15x; 池数 1; 分项 L4/V13/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 34; Tier Liquid; LP $1.15M; Vol24H $24.37M; 24H -27.79%; V/LP 21.24x; 池数 1; 分项 L19/V17/B8/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限 | Score 29; Tier Liquid; LP $1.13M; Vol24H $26.02M; 24H -28.61%; V/LP 23.01x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| MAMESUKE | SOL | [SCGBBn...gFSTNK](https://solscan.io/token/SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $90.6K; Vol24H $3.82M; 24H +1128.32%; V/LP 42.21x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CAPY](https://dexscreener.com/solana/7jyz7ykqvvrhcjrmkhzs1z6fup16pkpcwonvdnkqrert) | SOL | [5DnWmS...8avg2g](https://solscan.io/token/5DnWmSL9t3YqK5MeYq8ozJpna46VcdePWzHvyN8avg2g) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $60.2K; Vol24H $5.73M; 24H +895.00%; V/LP 95.26x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| STEALTH | SOL | [GoDSW3...xzBmoA](https://solscan.io/token/GoDSW31bTxfkoup9yA1qcGGx9RMXdTEWgApv3xzBmoA) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 26; Tier Micro; LP $30.6K; Vol24H $678.1K; 24H -19.32%; V/LP 22.15x; 池数 1; 分项 L4/V13/B17/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [PumpFun](https://dexscreener.com/solana/333wjud7rmkrtwwtxqdzedrobhj8dgjq8anbsg3pqakq) | SOL | [9X5UwH...Yspump](https://solscan.io/token/9X5UwHT7gWSPtAH5yeEzrLHqv3Nedmhy3HyZN3Yspump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $19.1K; Vol24H $680.4K; 24H +62.13%; V/LP 35.62x; 池数 8; 分项 L3/V13/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| PEACE | SOL | [BngAfL...8Epump](https://solscan.io/token/BngAfLZxaWN2QvpFhRbUHydYGr8zA7YTSA178G8Epump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $17.1K; Vol24H $1.41M; 24H -88.21%; V/LP 82.68x; 池数 1; 分项 L2/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [SPHERE](https://dexscreener.com/solana/hmcvp73epenjn2jdhqbws6syn56abcmpugdgouqznuok) | SOL | [31SYoq...fDpump](https://solscan.io/token/31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $63.3K; Vol24H $1.79M; 24H +1069.00%; V/LP 28.30x; 池数 4; 分项 L7/V15/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 82; Tier Liquid; LP $1.93M; Vol24H $1.90M; 24H -5.03%; V/LP 0.98x; 池数 1; 分项 L20/V16/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Q | BSC | [0xc07e...690589](https://bscscan.com/token/0xc07e1300dc138601fa6b0b59f8d0fa477e690589) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.07M; Vol24H $7.75M; 24H -4.43%; V/LP 7.23x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [AODF](https://dexscreener.com/solana/cbyxncob6ckhnbkv6um7dnewomb4jmqb5httuvs5u5eu) | SOL | [GePXef...MRpump](https://solscan.io/token/GePXefzRNUT92fcn5u8VfXpPPc9BhCmyPefKW2MRpump) | 24H波动可控；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.24M; Vol24H $179.3K; 24H +11.04%; V/LP 0.14x; 池数 1; 分项 L19/V9/B17/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARIA | BSC | [0x5d3a...555238](https://bscscan.com/token/0x5d3a12c42e5372b2cc3264ab3cdcf660a1555238) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限 | Score 60; Tier Liquid; LP $1.67M; Vol24H $9.99M; 24H +39.31%; V/LP 5.97x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [NODF](https://dexscreener.com/solana/exulh1zrmfj1gpct8de8hbzqbgrtinalusjldegbmifd) | SOL | [gHeaay...AUpump](https://solscan.io/token/gHeaaywtSrrYWNGf6fAWifNNxnoM8HTE15zFmAUpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| JAGENT | BSC | [0x8e64...e4ae15](https://bscscan.com/token/0x8e6442663a4f8c50b6132c68d42a30e7dfe4ae15) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GTA](https://dexscreener.com/solana/5isvs31h7hmdggmyuvzmhdsywv7cydd6czjtbqzctlii) | SOL | [BsbsB3...uLpump](https://solscan.io/token/BsbsB3WLq7vbY5En3MBCAsTrcwaCxNKY2Mp5pGuLpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

## 第二部分：逻辑复盘表格

### A. 上次逻辑总结表
| 逻辑项 | 上次规则 | 本轮验证 |
|---|---|---|
| 主观察门槛 | LP >= $100K，且非PVP，且不过成熟 | v0.3继续保留，并新增LP层级避免不同阶段候选混在一起 |
| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | v0.3增加PVP明细表，风险不再黑箱隐藏 |
| 多池处理 | symbol bridge合并，以最大LP池为代表 | v0.3保留，并继续标注多池冲突 |
| 合约地址 | v0.2未在主表强制展示 | v0.3强制展示合约地址；缺失时标注不可用 |
| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | v0.5已支持AVE周缓存接口框架与本地持久保存；缓存为空/过期时仍为低置信，命中后也要看链上行为 |

### B. 本轮逻辑总结表
| 逻辑项 | 本轮结果 | 判断 |
|---|---|---|
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 8 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |
| multi_pool_conflict_policy | 本轮存在多池数据冲突，不能用单池数据给高置信判断 | 多池价格/LP冲突的币降置信度，不直接升级主观察 |
| symbol_bridge_merge_policy | 本轮存在symbol桥接合并，说明重复输出问题正在被修正 | 减少同一Token在主观察/次观察中重复出现 |

### D. 挖掘策略调优表
| 项目 | 本轮判断 |
|---|---|
| 当前挖掘策略是否有效 | 部分有效：免费源可发现候选，v0.5能展示合约地址、PVP明细、成熟池明细、链上地址预检、AVE缓存状态和钱包行为样本 |
| 主要问题 | AVE接口已做可配置接入框架，BSC已做Transfer行为样本；仍缺完整Swap路径、钱包买后留存、Router/CEX出货和S0精确回放 |
| 假阳性风险 | 已降低，但代理指标仍可能误判买盘质量 |
| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |
| 候选来源调整 | 暂不新增高频外部源，下一步把v0.5 Transfer样本升级为完整Swap解析、钱包留存和Router/CEX路径 |
| 阈值调整 | 暂不改数值；先按Micro/Early/Liquid/Mature层级观察不同阶段表现 |
| 下轮挖掘方向 | 主观察必须有合约地址；优先对emergency_precision_check做完整Swap留存解析；AVE只周更保存Smart Wallet身份库，每小时只映射当前链上行为 |

## 第三部分：策略回写确认

| 项目 | 状态 |
|---|---|
| 是否已将本轮优化策略写回主定时策略 | 是 |
| 写回内容摘要 | 本轮确认结构性规则：合约地址强制展示、LP层级分离、PVP/成熟池明细、链上确认标记、早期Alpha过滤、多池冲突降置信 |
| 下轮是否生效 | 是 |
| 未写回原因 | - |

## 数据源状态
| 数据源 | 状态 |
|---|---|
| dexscreener_profiles | {'ok': True, 'count': 30, 'expanded': 30} |
| dexscreener_boosts | {'ok': True, 'count': 30, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 330} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
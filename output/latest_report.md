# 自我进化轮巡

**本轮时间 UTC：** 2026-06-17T21:56:18Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 137 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 281 |
| 合并后Token | 137 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 3 |
| 多池Token | 11 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 2 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 200，刷新时间 2026-06-17T17:59:17Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 6 个，BSC Transfer样本 3 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 88; Tier Early; LP $362.5K; Vol24H $2.35M; 24H +3.79%; V/LP 6.49x; 池数 2; 分项 L14/V16/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 87; Tier Liquid; LP $2.38M; Vol24H $764.5K; 24H +1.57%; V/LP 0.32x; 池数 1; 分项 L20/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SPACE | BSC | [0x87ac...2bdc00](https://bscscan.com/token/0x87acfa3fd7a6e0d48677d070644d76905c2bdc00) | 主观察 | Score 86; Tier Liquid; LP $2.55M; Vol24H $14.09M; 24H -0.14%; V/LP 5.52x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 85; Tier Liquid; LP $2.34M; Vol24H $101.2K; 24H +1.76%; V/LP 0.04x; 池数 1; 分项 L20/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 主观察 | Score 82; Tier Early; LP $167.7K; Vol24H $868.6K; 24H -0.34%; V/LP 5.18x; 池数 4; 分项 L11/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 76; Tier Early; LP $117.0K; Vol24H $153.9K; 24H -2.85%; V/LP 1.32x; 池数 1; 分项 L10/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [LOA](https://dexscreener.com/solana/enymbpwxnvj7ebav3d9stticmidtm658lorfqvlwvscf) | SOL | [EhHyfj...qjpump](https://solscan.io/token/EhHyfjRwj2jhmSE7GW5uJfizaLcNDa5C4HWPiSqjpump) | 次观察 | Score 74; Tier Early; LP $120.7K; Vol24H $290.3K; 24H -4.29%; V/LP 2.40x; 池数 4; 分项 L10/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WORLDCUP | SOL | [33eum8...T5pump](https://solscan.io/token/33eum82LaAhtv5YkUq1BdwEviSErH5CnFxqVNLT5pump) | 次观察 | Score 73; Tier Early; LP $149.0K; Vol24H $902.4K; 24H +21.76%; V/LP 6.05x; 池数 3; 分项 L11/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 73; Tier Early; LP $382.6K; Vol24H $1.16M; 24H +16.53%; V/LP 3.04x; 池数 2; 分项 L15/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SOL777](https://dexscreener.com/solana/e218zbtuprkk8xaqwa2fjflhxfa749towuqj4bxvnjuk) | SOL | [23Y1bU...hDpump](https://solscan.io/token/23Y1bUqVcJsvWH9WpVJfj1xDozq2GdKbEhRSdGhDpump) | 次观察 | Score 69; Tier Micro; LP $94.1K; Vol24H $88.1K; 24H +0.58%; V/LP 0.94x; 池数 1; 分项 L9/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 88; Tier Liquid; LP $2.99M; Vol24H $1.23M; 24H -7.00%; V/LP 0.41x; 池数 1; 分项 L20/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 87; Tier Liquid; LP $2.34M; Vol24H $724.9K; 24H -3.40%; V/LP 0.31x; 池数 2; 分项 L20/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.16M; Vol24H $5.63M; 24H -0.96%; V/LP 4.87x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 83; Tier Early; LP $355.9K; Vol24H $2.23M; 24H +8.85%; V/LP 6.25x; 池数 2; 分项 L14/V16/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 主观察 | Score 81; Tier Liquid; LP $1.47M; Vol24H $7.18M; 24H +19.16%; V/LP 4.89x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 76; Tier Early; LP $115.8K; Vol24H $129.6K; 24H -4.03%; V/LP 1.12x; 池数 1; 分项 L10/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 72; Tier Early; LP $372.5K; Vol24H $1.16M; 24H +10.57%; V/LP 3.10x; 池数 2; 分项 L14/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Merlin](https://dexscreener.com/solana/a2hnwknfbhit3hvymk2gueqc4yqpgwt9hamptjwd4cap) | SOL | [AvxFBj...4bpump](https://solscan.io/token/AvxFBjWydMYWD7C8pHzSkGxNYAFWr7aNBbAKm84bpump) | 次观察 | Score 70; Tier Early; LP $125.0K; Vol24H $341.8K; 24H -13.25%; V/LP 2.74x; 池数 7; 分项 L10/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 70; Tier Early; LP $199.6K; Vol24H $1.05M; 24H +53.53%; V/LP 5.28x; 池数 5; 分项 L12/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 65; Tier Liquid; LP $977.5K; Vol24H $3.6K; 24H -1.14%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WORLDCUP | SOL | [33eum8...T5pump](https://solscan.io/token/33eum82LaAhtv5YkUq1BdwEviSErH5CnFxqVNLT5pump) | 次观察 | Score 64; Tier Early; LP $145.2K; Vol24H $818.7K; 24H +30.82%; V/LP 5.64x; 池数 3; 分项 L11/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SPACEMOON | BSC | [0xf255...527777](https://bscscan.com/token/0xf2557688c18cab42bec4b5b053e05e3482527777) | PVP风险池 | Score 48; Tier Early; LP $179.6K; Vol24H $4.88M; 24H +12.31%; V/LP 27.14x; 池数 1; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 44; Tier Early; LP $272.0K; Vol24H $6.36M; 24H -15.82%; V/LP 23.38x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/edexqsn8ndyudusndngmybr9czevkbvxjb2vpfmvo6x3) | SOL | [6KDh3w...G7pump](https://solscan.io/token/6KDh3wLSZMg37nnU7prtKZr7Rut7WQGSf33Vp1G7pump) | PVP风险池 | Score 35; Tier Micro; LP $89.2K; Vol24H $2.32M; 24H +58.14%; V/LP 26.02x; 池数 1; 分项 L9/V16/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [OGFLOKI](https://dexscreener.com/solana/8drpkoihx9ybrmaw7nttpixvifsz3bnjv9guzb8fbasy) | SOL | [4gZ8BD...sGpump](https://solscan.io/token/4gZ8BDrhDcRjw9gDWEGeTyLT4iFejVoxVxdQFYsGpump) | PVP风险池 | Score 34; Tier Micro; LP $35.5K; Vol24H $1.41M; 24H -0.23%; V/LP 39.60x; 池数 2; 分项 L5/V15/B22/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SPACEMOON | BSC | [0xf255...527777](https://bscscan.com/token/0xf2557688c18cab42bec4b5b053e05e3482527777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 48; Tier Early; LP $179.6K; Vol24H $4.88M; 24H +12.31%; V/LP 27.14x; 池数 1; 分项 L12/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $272.0K; Vol24H $6.36M; 24H -15.82%; V/LP 23.38x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/edexqsn8ndyudusndngmybr9czevkbvxjb2vpfmvo6x3) | SOL | [6KDh3w...G7pump](https://solscan.io/token/6KDh3wLSZMg37nnU7prtKZr7Rut7WQGSf33Vp1G7pump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $89.2K; Vol24H $2.32M; 24H +58.14%; V/LP 26.02x; 池数 1; 分项 L9/V16/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [OGFLOKI](https://dexscreener.com/solana/8drpkoihx9ybrmaw7nttpixvifsz3bnjv9guzb8fbasy) | SOL | [4gZ8BD...sGpump](https://solscan.io/token/4gZ8BDrhDcRjw9gDWEGeTyLT4iFejVoxVxdQFYsGpump) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 34; Tier Micro; LP $35.5K; Vol24H $1.41M; 24H -0.23%; V/LP 39.60x; 池数 2; 分项 L5/V15/B22/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| MEEP | SOL | [8jvtfe...e3pump](https://solscan.io/token/8jvtfeVTJQsrQ3L4kjQmRcXJ1iSFQMmkjkCqPUe3pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $72.4K; Vol24H $2.09M; 24H +21037.74%; V/LP 28.88x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [YASMINE](https://dexscreener.com/solana/hvh5akrdoamxsgab2jjks168dytsmep4mtyh56msfdu7) | SOL | [9UdVwU...3tpump](https://solscan.io/token/9UdVwUYHbVAVD6p4oFfRqZBVD4gNAp62PErkqC3tpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $55.0K; Vol24H $1.35M; 24H +620.00%; V/LP 24.50x; 池数 2; 分项 L7/V15/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |
| [RIV](https://dexscreener.com/solana/97afimzdusore6l9e4drqbwj2tqeui5xfuuokwyxkqhv) | SOL | [HREUDW...dPpump](https://solscan.io/token/HREUDWzLtmJrMjav48RY9iPRJr9r8KoTBLjWNjdPpump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $40.8K; Vol24H $1.64M; 24H +344.00%; V/LP 40.22x; 池数 4; 分项 L6/V15/B0/Buy0/Risk-65 | 只记录热度，不进入主榜 |
| OILMAXXING | SOL | [FFRQbb...LLpump](https://solscan.io/token/FFRQbb9KaXomHrBKrtJ7UxrqSTxDGk8WLjacqnLLpump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；LP偏薄；Volume/LP极端偏高 | Score 0; Tier Micro; LP $6.3K; Vol24H $1.11M; 24H -97.00%; V/LP 176.15x; 池数 1; 分项 L0/V14/B0/Buy0/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 76; Tier Liquid; LP $1.22M; Vol24H $1.36M; 24H -1.91%; V/LP 1.11x; 池数 2; 分项 L19/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $61.70M; Vol24H $6.34M; 24H -5.63%; V/LP 0.10x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 64; Tier Mature; LP $9.03M; Vol24H $327.7K; 24H -4.66%; V/LP 0.04x; 池数 1; 分项 L20/V10/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Merlin](https://dexscreener.com/solana/a2hnwknfbhit3hvymk2gueqc4yqpgwt9hamptjwd4cap) | SOL | [AvxFBj...4bpump](https://solscan.io/token/AvxFBjWydMYWD7C8pHzSkGxNYAFWr7aNBbAKm84bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 6 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
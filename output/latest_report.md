# 自我进化轮巡

**本轮时间 UTC：** 2026-07-20T17:55:12Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 99 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 221 |
| 合并后Token | 99 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 1 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 5 |
| 多池Token | 10 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 10 |
| Liquid层 | 4 |
| Mature层 | 3 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 84; Tier Early; LP $311.3K; Vol24H $634.9K; 24H -5.39%; V/LP 2.04x; 池数 1; 分项 L14/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 71; Tier Liquid; LP $930.6K; Vol24H $205.5K; 24H -18.09%; V/LP 0.22x; 池数 1; 分项 L18/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 52; Tier Early; LP $507.4K; Vol24H $12.52M; 24H +0.52%; V/LP 24.68x; 池数 1; 分项 L16/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Agamemnon](https://dexscreener.com/solana/636bkx7ugs6vdb9fhajdwfdi4afuphdarrtw2ntvueag) | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | PVP风险池 | Score 50; Tier Micro; LP $85.3K; Vol24H $5.52M; 24H +3.49%; V/LP 64.67x; 池数 2; 分项 L9/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 37; Tier Liquid; LP $1.01M; Vol24H $46.16M; 24H -8.47%; V/LP 45.69x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 屎币 | BSC | [0xe14b...354444](https://bscscan.com/token/0xe14b77ce30250cf94182b7019020fa00e7354444) | PVP风险池 | Score 36; Tier Micro; LP $95.5K; Vol24H $4.35M; 24H -41.45%; V/LP 45.56x; 池数 43; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| JACOBIAN | SOL | [5UoWze...L7pump](https://solscan.io/token/5UoWzex7rVky9ZSHGQXQgAPsm8jDZQMFBGqch8L7pump) | PVP风险池 | Score 26; Tier Micro; LP $57.0K; Vol24H $5.11M; 24H +1228.32%; V/LP 89.68x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $131.0K; Vol24H $6.76M; 24H +62.12%; V/LP 51.64x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FABLE | SOL | [93tRm6...Ntpump](https://solscan.io/token/93tRm6L1bNr15FTjnYUazRh4J3Ths2bL84myCBNtpump) | PVP风险池 | Score 18; Tier Micro; LP $19.6K; Vol24H $1.53M; 24H +77.62%; V/LP 78.29x; 池数 1; 分项 L3/V15/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| nice | SOL | [A3NaYD...FmAUS9](https://solscan.io/token/A3NaYDFxepZCXurb2LZouaPREHZ21SMfY3zgrwFmAUS9) | PVP风险池 | Score 14; Tier Micro; LP $34.2K; Vol24H $4.79M; 24H +411.94%; V/LP 139.90x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 84; Tier Early; LP $305.6K; Vol24H $626.4K; 24H -3.79%; V/LP 2.05x; 池数 1; 分项 L14/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 80; Tier Liquid; LP $1.28M; Vol24H $4.48M; 24H -8.92%; V/LP 3.51x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 主观察 | Score 76; Tier Early; LP $147.3K; Vol24H $583.7K; 24H +24.90%; V/LP 3.96x; 池数 5; 分项 L11/V12/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 73; Tier Early; LP $144.3K; Vol24H $770.4K; 24H +11.43%; V/LP 5.34x; 池数 1; 分项 L11/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 51; Tier Early; LP $478.3K; Vol24H $12.97M; 24H +1.10%; V/LP 27.13x; 池数 1; 分项 L15/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | PVP风险池 | Score 46; Tier Early; LP $125.3K; Vol24H $3.64M; 24H -16.37%; V/LP 29.07x; 池数 1; 分项 L10/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 37; Tier Liquid; LP $984.1K; Vol24H $38.86M; 24H -18.32%; V/LP 39.49x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | PVP风险池 | Score 35; Tier Micro; LP $69.0K; Vol24H $4.28M; 24H -71.26%; V/LP 61.96x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $132.8K; Vol24H $5.63M; 24H +37.57%; V/LP 42.40x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| JACOBIAN | SOL | [5UoWze...L7pump](https://solscan.io/token/5UoWzex7rVky9ZSHGQXQgAPsm8jDZQMFBGqch8L7pump) | PVP风险池 | Score 15; Tier Micro; LP $46.7K; Vol24H $5.59M; 24H +769.38%; V/LP 119.49x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [nice](https://dexscreener.com/solana/4dtsp9bx38gwytmdpgmqu5yx5bkatrfck1akgn1pujjm) | SOL | [A3NaYD...FmAUS9](https://solscan.io/token/A3NaYDFxepZCXurb2LZouaPREHZ21SMfY3zgrwFmAUS9) | PVP风险池 | Score 14; Tier Micro; LP $31.4K; Vol24H $4.88M; 24H +273.00%; V/LP 155.43x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MOGCHILL](https://dexscreener.com/solana/7m3epma4iubcknhl4fytstwrkus1qymbelucwpafyrpx) | SOL | [5v4Apa...kNpump](https://solscan.io/token/5v4Apahd9MZVUWt5qn5MV4ZsbsuRWavbvfmmwVkNpump) | PVP风险池 | Score 1; Tier Micro; LP $74.7K; Vol24H $2.26M; 24H +2446.00%; V/LP 30.31x; 池数 2; 分项 L8/V16/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $51.46M; Vol24H $3.44M; 24H -0.80%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 74; Tier Liquid; LP $1.43M; Vol24H $6.74M; 24H -1.00%; V/LP 4.72x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 71; Tier Mature; LP $16.95M; Vol24H $76.07M; 24H -0.10%; V/LP 4.49x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Early; LP $478.3K; Vol24H $12.97M; 24H +1.10%; V/LP 27.13x; 池数 1; 分项 L15/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 46; Tier Early; LP $125.3K; Vol24H $3.64M; 24H -16.37%; V/LP 29.07x; 池数 1; 分项 L10/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 37; Tier Liquid; LP $984.1K; Vol24H $38.86M; 24H -18.32%; V/LP 39.49x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $69.0K; Vol24H $4.28M; 24H -71.26%; V/LP 61.96x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 20; Tier Early; LP $132.8K; Vol24H $5.63M; 24H +37.57%; V/LP 42.40x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| JACOBIAN | SOL | [5UoWze...L7pump](https://solscan.io/token/5UoWzex7rVky9ZSHGQXQgAPsm8jDZQMFBGqch8L7pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $46.7K; Vol24H $5.59M; 24H +769.38%; V/LP 119.49x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [nice](https://dexscreener.com/solana/4dtsp9bx38gwytmdpgmqu5yx5bkatrfck1akgn1pujjm) | SOL | [A3NaYD...FmAUS9](https://solscan.io/token/A3NaYDFxepZCXurb2LZouaPREHZ21SMfY3zgrwFmAUS9) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $31.4K; Vol24H $4.88M; 24H +273.00%; V/LP 155.43x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MOGCHILL](https://dexscreener.com/solana/7m3epma4iubcknhl4fytstwrkus1qymbelucwpafyrpx) | SOL | [5v4Apa...kNpump](https://solscan.io/token/5v4Apahd9MZVUWt5qn5MV4ZsbsuRWavbvfmmwVkNpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 1; Tier Micro; LP $74.7K; Vol24H $2.26M; 24H +2446.00%; V/LP 30.31x; 池数 2; 分项 L8/V16/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.46M; Vol24H $3.44M; 24H -0.80%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.43M; Vol24H $6.74M; 24H -1.00%; V/LP 4.72x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.95M; Vol24H $76.07M; 24H -0.10%; V/LP 4.49x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.16M; Vol24H $3.51M; 24H +23.48%; V/LP 1.62x; 池数 2; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [KIM](https://dexscreener.com/solana/b38qwnqtah775zktfh3tmnzguzjqtxtvqmrzrju1y3r) | SOL | [L8VV5T...1tpump](https://solscan.io/token/L8VV5THQCh7oN37TwgVRRSVqb5FuPydXS9Roy1tpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 8 / Early 10 / Liquid 4 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 335} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
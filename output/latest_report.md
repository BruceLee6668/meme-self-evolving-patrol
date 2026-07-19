# 自我进化轮巡

**本轮时间 UTC：** 2026-07-19T10:22:36Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 227 |
| 合并后Token | 101 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 8 |
| 多池Token | 8 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 8 |
| Liquid层 | 10 |
| Mature层 | 2 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.31M; Vol24H $3.34M; 24H -0.17%; V/LP 2.56x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 主观察 | Score 79; Tier Early; LP $155.6K; Vol24H $1.24M; 24H +2.34%; V/LP 7.94x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NTFS | SOL | [NTFSzF...nhmBe7](https://solscan.io/token/NTFSzFdqyjt4babasFp6RxsQj8QLs6xYYKcQMnhmBe7) | 主观察 | Score 78; Tier Early; LP $186.2K; Vol24H $490.7K; 24H +6.64%; V/LP 2.63x; 池数 2; 分项 L12/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 76; Tier Early; LP $312.3K; Vol24H $666.4K; 24H +24.31%; V/LP 2.13x; 池数 6; 分项 L14/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 71; Tier Liquid; LP $1.16M; Vol24H $2.83M; 24H +66.64%; V/LP 2.44x; 池数 2; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 次观察 | Score 65; Tier Liquid; LP $1.17M; Vol24H $474.70; 24H +1.30%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TRADOOR | BSC | [0x9123...09f492](https://bscscan.com/token/0x9123400446a56176eb1b6be9ee5cf703e409f492) | 次观察 | Score 65; Tier Early; LP $714.0K; Vol24H $7.79M; 24H -2.71%; V/LP 10.92x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 64; Tier Liquid; LP $1.95M; Vol24H $31.8K; 24H +2.07%; V/LP 0.02x; 池数 1; 分项 L20/V3/B22/Buy3/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 64; Tier Early; LP $313.0K; Vol24H $1.31M; 24H +26.82%; V/LP 4.19x; 池数 1; 分项 L14/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 43; Tier Liquid; LP $1.05M; Vol24H $91.38M; 24H -3.51%; V/LP 86.91x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 72; Tier Early; LP $293.6K; Vol24H $1.33M; 24H +22.58%; V/LP 4.54x; 池数 1; 分项 L13/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 次观察 | Score 69; Tier Liquid; LP $1.17M; Vol24H $398.60; 24H +1.38%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 68; Tier Early; LP $158.5K; Vol24H $827.5K; 24H +11.15%; V/LP 5.22x; 池数 1; 分项 L11/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 65; Tier Early; LP $328.0K; Vol24H $357.9K; 24H +50.06%; V/LP 1.09x; 池数 6; 分项 L14/V11/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TRADOOR | BSC | [0x9123...09f492](https://bscscan.com/token/0x9123400446a56176eb1b6be9ee5cf703e409f492) | 次观察 | Score 65; Tier Early; LP $710.4K; Vol24H $7.17M; 24H -5.19%; V/LP 10.09x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 56; Tier Liquid; LP $2.55M; Vol24H $150.00M; 24H -0.09%; V/LP 58.71x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 43; Tier Liquid; LP $1.06M; Vol24H $75.65M; 24H +5.74%; V/LP 71.68x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | PVP风险池 | Score 42; Tier Early; LP $141.8K; Vol24H $11.83M; 24H -12.80%; V/LP 83.48x; 池数 1; 分项 L11/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Mouse](https://dexscreener.com/solana/4mt1pvmbzenlbkq4onj7syoxmmbin2sp2vqtd8tdzecl) | SOL | [3wwU3n...K2pump](https://solscan.io/token/3wwU3njdLCT3ebRUrTFeHwKG6zamiiCKwmpShSK2pump) | PVP风险池 | Score 37; Tier Micro; LP $49.3K; Vol24H $5.18M; 24H +1.72%; V/LP 105.17x; 池数 2; 分项 L6/V17/B22/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 36; Tier Early; LP $324.7K; Vol24H $15.52M; 24H -42.01%; V/LP 47.80x; 池数 2; 分项 L14/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOLdiers](https://dexscreener.com/solana/b4jm2z5daqncjtsfm4f8v5pc88ka8fk3oycswefsq9br) | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 30; Tier Early; LP $165.9K; Vol24H $4.88M; 24H +97.97%; V/LP 29.40x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Benny | SOL | [2mGS6W...Lqpump](https://solscan.io/token/2mGS6WWuDy1xNQuCo7irzH3iT4SsSeSaA3oJ5NLqpump) | PVP风险池 | Score 14; Tier Micro; LP $32.9K; Vol24H $4.65M; 24H +314.00%; V/LP 141.07x; 池数 3; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 11; Tier Early; LP $104.0K; Vol24H $4.37M; 24H +94.73%; V/LP 42.05x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 71; Tier Mature; LP $16.71M; Vol24H $46.21M; 24H +0.03%; V/LP 2.77x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 69; Tier Liquid; LP $2.05M; Vol24H $8.17M; 24H +9.28%; V/LP 3.98x; 池数 2; 分项 L20/V17/B17/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Liquid; LP $2.55M; Vol24H $150.00M; 24H -0.09%; V/LP 58.71x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 43; Tier Liquid; LP $1.06M; Vol24H $75.65M; 24H +5.74%; V/LP 71.68x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $141.8K; Vol24H $11.83M; 24H -12.80%; V/LP 83.48x; 池数 1; 分项 L11/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Mouse](https://dexscreener.com/solana/4mt1pvmbzenlbkq4onj7syoxmmbin2sp2vqtd8tdzecl) | SOL | [3wwU3n...K2pump](https://solscan.io/token/3wwU3njdLCT3ebRUrTFeHwKG6zamiiCKwmpShSK2pump) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 37; Tier Micro; LP $49.3K; Vol24H $5.18M; 24H +1.72%; V/LP 105.17x; 池数 2; 分项 L6/V17/B22/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Early; LP $324.7K; Vol24H $15.52M; 24H -42.01%; V/LP 47.80x; 池数 2; 分项 L14/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [SOLdiers](https://dexscreener.com/solana/b4jm2z5daqncjtsfm4f8v5pc88ka8fk3oycswefsq9br) | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $165.9K; Vol24H $4.88M; 24H +97.97%; V/LP 29.40x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Benny | SOL | [2mGS6W...Lqpump](https://solscan.io/token/2mGS6WWuDy1xNQuCo7irzH3iT4SsSeSaA3oJ5NLqpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $32.9K; Vol24H $4.65M; 24H +314.00%; V/LP 141.07x; 池数 3; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 11; Tier Early; LP $104.0K; Vol24H $4.37M; 24H +94.73%; V/LP 42.05x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.71M; Vol24H $46.21M; 24H +0.03%; V/LP 2.77x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.05M; Vol24H $8.17M; 24H +9.28%; V/LP 3.98x; 池数 2; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.49M; Vol24H $7.96M; 24H -10.66%; V/LP 5.33x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；成熟大池 | Score 59; Tier Mature; LP $20.01M; Vol24H $15.2K; 24H +1.76%; V/LP 0.00x; 池数 1; 分项 L20/V1/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TRADOOR | BSC | [0x9123...09f492](https://bscscan.com/token/0x9123400446a56176eb1b6be9ee5cf703e409f492) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Mouse](https://dexscreener.com/solana/4mt1pvmbzenlbkq4onj7syoxmmbin2sp2vqtd8tdzecl) | SOL | [3wwU3n...K2pump](https://solscan.io/token/3wwU3njdLCT3ebRUrTFeHwKG6zamiiCKwmpShSK2pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| - | - | - | 本轮无钱包行为样本 | - | 0 | - |

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
| 主观察候选 | 0 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 8 / Liquid 10 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
| dexscreener_search | {'ok': True, 'count': 332} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
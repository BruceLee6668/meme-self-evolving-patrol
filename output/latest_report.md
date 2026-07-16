# 自我进化轮巡

**本轮时间 UTC：** 2026-07-16T19:58:40Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 110 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 208 |
| 合并后Token | 110 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 4 |
| 多池Token | 6 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 5 |
| Liquid层 | 9 |
| Mature层 | 3 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 5 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 2 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 主观察 | Score 85; Tier Liquid; LP $1.18M; Vol24H $136.4K; 24H +1.22%; V/LP 0.12x; 池数 1; 分项 L19/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.31M; Vol24H $6.51M; 24H +5.28%; V/LP 4.96x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 主观察 | Score 84; Tier Liquid; LP $1.26M; Vol24H $120.5K; 24H -1.29%; V/LP 0.10x; 池数 1; 分项 L19/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 主观察 | Score 81; Tier Liquid; LP $1.58M; Vol24H $6.61M; 24H -21.39%; V/LP 4.20x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 主观察 | Score 78; Tier Early; LP $712.5K; Vol24H $5.43M; 24H +10.82%; V/LP 7.63x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 75; Tier Early; LP $294.4K; Vol24H $521.8K; 24H -11.38%; V/LP 1.77x; 池数 5; 分项 L14/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 69; Tier Early; LP $151.1K; Vol24H $1.16M; 24H -19.16%; V/LP 7.69x; 池数 2; 分项 L11/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 37; Tier Early; LP $129.1K; Vol24H $7.41M; 24H -40.98%; V/LP 57.36x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TrumpCoin | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | PVP风险池 | Score 29; Tier Early; LP $112.6K; Vol24H $4.88M; 24H +120.86%; V/LP 43.37x; 池数 7; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CASHCOW](https://dexscreener.com/solana/dczlne5pnsilipetgcluljzahnrxjiqygkb4jbytdipq) | SOL | [D6ytjM...HNpump](https://solscan.io/token/D6ytjMdBBPoV8nsRHJhvrkpwF7sgVBYd7PufkRHNpump) | PVP风险池 | Score 25; Tier Micro; LP $67.8K; Vol24H $1.55M; 24H +602.00%; V/LP 22.78x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 87; Tier Liquid; LP $1.87M; Vol24H $186.7K; 24H +1.15%; V/LP 0.10x; 池数 1; 分项 L20/V9/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 主观察 | Score 85; Tier Liquid; LP $1.18M; Vol24H $136.4K; 24H +1.22%; V/LP 0.12x; 池数 1; 分项 L19/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.29M; Vol24H $6.51M; 24H +1.13%; V/LP 5.03x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 主观察 | Score 84; Tier Liquid; LP $1.26M; Vol24H $120.5K; 24H -1.29%; V/LP 0.10x; 池数 1; 分项 L19/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 主观察 | Score 81; Tier Liquid; LP $1.57M; Vol24H $6.52M; 24H -20.05%; V/LP 4.16x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 次观察 | Score 78; Tier Early; LP $716.6K; Vol24H $5.61M; 24H +10.05%; V/LP 7.82x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 75; Tier Early; LP $294.4K; Vol24H $484.1K; 24H -2.78%; V/LP 1.64x; 池数 5; 分项 L14/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [febu](https://dexscreener.com/solana/68nvmrvpyxgjgbgh2p92e93syhjcbe6qocizrqoqdjcb) | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 69; Tier Early; LP $155.7K; Vol24H $1.04M; 24H -21.73%; V/LP 6.71x; 池数 2; 分项 L11/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 64; Tier Micro; LP $75.4K; Vol24H $106.1K; 24H +4.74%; V/LP 1.41x; 池数 1; 分项 L8/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 37; Tier Early; LP $121.2K; Vol24H $4.21M; 24H -35.28%; V/LP 34.70x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 29; Tier Liquid; LP $1.26M; Vol24H $27.16M; 24H +37.25%; V/LP 21.53x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | PVP风险池 | Score 28; Tier Early; LP $105.5K; Vol24H $4.93M; 24H +131.00%; V/LP 46.75x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CASHCOW](https://dexscreener.com/solana/dczlne5pnsilipetgcluljzahnrxjiqygkb4jbytdipq) | SOL | [D6ytjM...HNpump](https://solscan.io/token/D6ytjMdBBPoV8nsRHJhvrkpwF7sgVBYd7PufkRHNpump) | PVP风险池 | Score 25; Tier Micro; LP $72.9K; Vol24H $1.62M; 24H +708.00%; V/LP 22.18x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CUBEMAN](https://dexscreener.com/solana/4z3zkjiksbxgr7pvkfsjbuk2gmkhmttfaghmgwpago8d) | SOL | [HVRtNe...efpump](https://solscan.io/token/HVRtNeFPrDcAA9Yu3WrTEdCsTLGJiYDiQbqjg3efpump) | PVP风险池 | Score 25; Tier Micro; LP $70.1K; Vol24H $1.59M; 24H +2408.00%; V/LP 22.69x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HOMIE](https://dexscreener.com/solana/5fg5azit5ed8paz12vdtttmgxw5monsutyxjwa2w6qdy) | SOL | [E7vTVL...srpump](https://solscan.io/token/E7vTVLLaxV3y68cpnDx2Q7ExeznhWgJKwPziKDsrpump) | PVP风险池 | Score 18; Tier Micro; LP $53.5K; Vol24H $3.38M; 24H +1120.00%; V/LP 63.18x; 池数 1; 分项 L7/V17/B0/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $121.2K; Vol24H $4.21M; 24H -35.28%; V/LP 34.70x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限 | Score 29; Tier Liquid; LP $1.26M; Vol24H $27.16M; 24H +37.25%; V/LP 21.53x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $105.5K; Vol24H $4.93M; 24H +131.00%; V/LP 46.75x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CASHCOW](https://dexscreener.com/solana/dczlne5pnsilipetgcluljzahnrxjiqygkb4jbytdipq) | SOL | [D6ytjM...HNpump](https://solscan.io/token/D6ytjMdBBPoV8nsRHJhvrkpwF7sgVBYd7PufkRHNpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $72.9K; Vol24H $1.62M; 24H +708.00%; V/LP 22.18x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CUBEMAN](https://dexscreener.com/solana/4z3zkjiksbxgr7pvkfsjbuk2gmkhmttfaghmgwpago8d) | SOL | [HVRtNe...efpump](https://solscan.io/token/HVRtNeFPrDcAA9Yu3WrTEdCsTLGJiYDiQbqjg3efpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $70.1K; Vol24H $1.59M; 24H +2408.00%; V/LP 22.69x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HOMIE](https://dexscreener.com/solana/5fg5azit5ed8paz12vdtttmgxw5monsutyxjwa2w6qdy) | SOL | [E7vTVL...srpump](https://solscan.io/token/E7vTVLLaxV3y68cpnDx2Q7ExeznhWgJKwPziKDsrpump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高 | Score 18; Tier Micro; LP $53.5K; Vol24H $3.38M; 24H +1120.00%; V/LP 63.18x; 池数 1; 分项 L7/V17/B0/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| BARRON | SOL | [GqQc4t...fNpump](https://solscan.io/token/GqQc4tjs6RkZt1EdsehKLZvNDTpZc9n3UHGxnbfNpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $32.2K; Vol24H $3.46M; 24H +328.20%; V/LP 107.38x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [bet](https://dexscreener.com/solana/ehgman1uem5ypafxphg5hbzopzqxvskhuceucg7r7xt7) | SOL | [He6pEC...Kqpump](https://solscan.io/token/He6pECrSVi123qabQJRiGEonMbBZ7e8PZ9NmUxKqpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $40.3K; Vol24H $1.66M; 24H +670.00%; V/LP 41.17x; 池数 1; 分项 L6/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.03M; Vol24H $13.13M; 24H +5.76%; V/LP 6.47x; 池数 3; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $52.60M; Vol24H $3.31M; 24H -0.12%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.68M; Vol24H $54.83M; 24H -0.02%; V/LP 3.29x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| XPIN | BSC | [0xd955...3d31a6](https://bscscan.com/token/0xd955c9ba56fb1ab30e34766e252a97ccce3d31a6) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $940.6K; Vol24H $1.49M; 24H -6.32%; V/LP 1.59x; 池数 1; 分项 L18/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [febu](https://dexscreener.com/solana/68nvmrvpyxgjgbgh2p92e93syhjcbe6qocizrqoqdjcb) | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 5 / Liquid 9 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |

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
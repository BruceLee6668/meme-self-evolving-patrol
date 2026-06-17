# 自我进化轮巡

**本轮时间 UTC：** 2026-06-17T17:09:35Z
**版本：** 0.3.0-contract-address-tier-detail
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 131 个合并Token中筛出 5 个主观察候选。v0.3已把合约地址作为主输出字段，并增加Micro/Early/Liquid/Mature分层、PVP明细、成熟池明细和链上确认标记。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 278 |
| 合并后Token | 131 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 12 |
| PVP风险池 | 8 |
| 成熟池观察 | 0 |
| 低优先观察 | 0 |
| 多池Token | 7 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 9 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 0 |
| 需要链上确认 | 25 |
| 紧急精查候选 | 8 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| - | - | - | 上次记录不可用 | 第一次或无有效 previous_snapshot | - | - | - |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 87; Tier Liquid; LP $2.41M; Vol24H $815.2K; 24H +0.15%; V/LP 0.34x; 池数 1; 分项 L20/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 86; Tier Liquid; LP $2.32M; Vol24H $135.3K; 24H +4.82%; V/LP 0.06x; 池数 1; 分项 L20/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SPACE | BSC | [0x87ac...2bdc00](https://bscscan.com/token/0x87acfa3fd7a6e0d48677d070644d76905c2bdc00) | 主观察 | Score 86; Tier Liquid; LP $2.54M; Vol24H $15.13M; 24H +0.16%; V/LP 5.95x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.17M; Vol24H $5.09M; 24H +1.36%; V/LP 4.34x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 主观察 | Score 84; Tier Liquid; LP $1.94M; Vol24H $79.4K; 24H -3.30%; V/LP 0.04x; 池数 1; 分项 L20/V6/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 83; Tier Early; LP $370.6K; Vol24H $2.27M; 24H +11.84%; V/LP 6.12x; 池数 2; 分项 L14/V16/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，不直接进攻 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 83; Tier Early; LP $251.4K; Vol24H $552.4K; 24H -1.19%; V/LP 2.20x; 池数 1; 分项 L13/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，不直接进攻 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 82; Tier Early; LP $173.9K; Vol24H $926.1K; 24H -7.40%; V/LP 5.33x; 池数 1; 分项 L11/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，不直接进攻 |
| WORLDCUP | SOL | [33eum8...T5pump](https://solscan.io/token/33eum82LaAhtv5YkUq1BdwEviSErH5CnFxqVNLT5pump) | 次观察 | Score 78; Tier Early; LP $146.9K; Vol24H $829.4K; 24H +2.67%; V/LP 5.65x; 池数 4; 分项 L11/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度 | proxy_only_ave_weekly_cache_not_connected | 次观察，不直接进攻 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 77; Tier Early; LP $119.0K; Vol24H $206.9K; 24H -0.51%; V/LP 1.74x; 池数 1; 分项 L10/V9/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，不直接进攻 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 73; Tier Early; LP $389.2K; Vol24H $1.23M; 24H +13.99%; V/LP 3.17x; 池数 2; 分项 L15/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，等成交/LP结构继续改善 |
| [LOA](https://dexscreener.com/solana/enymbpwxnvj7ebav3d9stticmidtm658lorfqvlwvscf) | SOL | [EhHyfj...qjpump](https://solscan.io/token/EhHyfjRwj2jhmSE7GW5uJfizaLcNDa5C4HWPiSqjpump) | 次观察 | Score 69; Tier Early; LP $116.3K; Vol24H $321.1K; 24H +7.56%; V/LP 2.76x; 池数 4; 分项 L10/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度 | proxy_only_ave_weekly_cache_not_connected | 次观察，等成交/LP结构继续改善 |
| [USBC](https://dexscreener.com/solana/e98eyybmtmbkxwycnrdbcdkj6hfas3hzxg2lkdq1htd) | SOL | [EA6jvQ...FPpump](https://solscan.io/token/EA6jvQhjR2iMkRaVy9P9drM2ExowaFZWGn3Uo8FPpump) | 次观察 | Score 67; Tier Micro; LP $54.2K; Vol24H $365.2K; 24H -13.87%; V/LP 6.73x; 池数 1; 分项 L7/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，等成交/LP结构继续改善 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | [BiywH8...sypump](https://solscan.io/token/BiywH8Eq2CbGhwMHKwCnfTiccWJwN7r1Q4Qn9hsypump) | 次观察 | Score 66; Tier Micro; LP $71.4K; Vol24H $180.3K; 24H -3.19%; V/LP 2.52x; 池数 1; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，等成交/LP结构继续改善 |
| [OGDOGE](https://dexscreener.com/solana/6wgsajrfy9fxgxkzrfns3rnt2yrgmhrs1xafpmkr8ykd) | SOL | [utLyQQ...oGdoge](https://solscan.io/token/utLyQQCPvjuCc6zeaXdsFeEC3JNdxKS3vxaZWoGdoge) | 次观察 | Score 66; Tier Early; LP $238.7K; Vol24H $2.84M; 24H -0.87%; V/LP 11.88x; 池数 2; 分项 L13/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标 | proxy_only_ave_weekly_cache_not_connected | 次观察，等成交/LP结构继续改善 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SPACEMOON | BSC | [0xf255...527777](https://bscscan.com/token/0xf2557688c18cab42bec4b5b053e05e3482527777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $217.5K; Vol24H $5.96M; 24H +14231.08%; V/LP 27.41x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/edexqsn8ndyudusndngmybr9czevkbvxjb2vpfmvo6x3) | SOL | [6KDh3w...G7pump](https://solscan.io/token/6KDh3wLSZMg37nnU7prtKZr7Rut7WQGSf33Vp1G7pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $102.9K; Vol24H $2.53M; 24H +528.00%; V/LP 24.62x; 池数 2; 分项 L9/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MEEP | SOL | [8jvtfe...e3pump](https://solscan.io/token/8jvtfeVTJQsrQ3L4kjQmRcXJ1iSFQMmkjkCqPUe3pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Micro; LP $52.4K; Vol24H $1.54M; 24H +11059.76%; V/LP 29.45x; 池数 1; 分项 L7/V15/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| OGFLOKI | SOL | [4gZ8BD...sGpump](https://solscan.io/token/4gZ8BDrhDcRjw9gDWEGeTyLT4iFejVoxVxdQFYsGpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $42.8K; Vol24H $2.43M; 24H +760.64%; V/LP 56.79x; 池数 2; 分项 L6/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [SNDK69](https://dexscreener.com/solana/hx7dm1fslf2vevb6b3szgvvxs5vbh48pqn9sbyznypsu) | SOL | [851JK2...Ltpump](https://solscan.io/token/851JK2La49dwLjKzWsoDpTddsue4d7ct9SedgYLtpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $33.5K; Vol24H $1.23M; 24H +426.00%; V/LP 36.83x; 池数 1; 分项 L5/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| OILMAXXING | SOL | [FFRQbb...LLpump](https://solscan.io/token/FFRQbb9KaXomHrBKrtJ7UxrqSTxDGk8WLjacqnLLpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $6.5K; Vol24H $2.43M; 24H -98.41%; V/LP 373.19x; 池数 1; 分项 L0/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [JOE](https://dexscreener.com/solana/8b6cmnmdfjzmn5csocu8vgajtucneqtuqkadq6z3zzij) | SOL | [Az1sNB...Djpump](https://solscan.io/token/Az1sNBBe6H97oNVi4zXDosgFHN8hWnCf1QsDDJDjpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 7; Tier Micro; LP $42.3K; Vol24H $1.20M; 24H +782.00%; V/LP 28.43x; 池数 1; 分项 L6/V14/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| UPLON | SOL | [HyH42s...uypump](https://solscan.io/token/HyH42sG6X5VsU4pd6d89D3SqJQ6hqppzNgoBYUuypump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 6; Tier Micro; LP $4.7K; Vol24H $1.05M; 24H -98.84%; V/LP 222.59x; 池数 1; 分项 L0/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| - | - | - | 无 | - | - |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 原因 |
|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SPACE | BSC | [0x87ac...2bdc00](https://bscscan.com/token/0x87acfa3fd7a6e0d48677d070644d76905c2bdc00) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TOESCOIN | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 是 | 是 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | 观察池候选需要链上Swap/钱包留存确认 |
| WORLDCUP | SOL | [33eum8...T5pump](https://solscan.io/token/33eum82LaAhtv5YkUq1BdwEviSErH5CnFxqVNLT5pump) | 是 | 否 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |

## 第二部分：逻辑复盘表格

### A. 上次逻辑总结表
| 逻辑项 | 上次规则 | 本轮验证 |
|---|---|---|
| 主观察门槛 | LP >= $100K，且非PVP，且不过成熟 | v0.3继续保留，并新增LP层级避免不同阶段候选混在一起 |
| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | v0.3增加PVP明细表，风险不再黑箱隐藏 |
| 多池处理 | symbol bridge合并，以最大LP池为代表 | v0.3保留，并继续标注多池冲突 |
| 合约地址 | v0.2未在主表强制展示 | v0.3强制展示合约地址；缺失时标注不可用 |
| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | 仍未接AVE，当前只用代理指标，置信度低 |

### B. 本轮逻辑总结表
| 逻辑项 | 本轮结果 | 判断 |
|---|---|---|
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 0 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 9 / Early 10 / Liquid 6 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| Smart Money | 仅代理指标 | 不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.3已生成确认标记 | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| multi_pool_conflict_policy | 本轮存在多池数据冲突，不能用单池数据给高置信判断 | 多池价格/LP冲突的币降置信度，不直接升级主观察 |
| symbol_bridge_merge_policy | 本轮存在symbol桥接合并，说明重复输出问题正在被修正 | 减少同一Token在主观察/次观察中重复出现 |

### D. 挖掘策略调优表
| 项目 | 本轮判断 |
|---|---|
| 当前挖掘策略是否有效 | 部分有效：免费源可发现候选，v0.3能展示合约地址、PVP明细、成熟池明细和链上确认需求 |
| 主要问题 | 缺少钱包级数据、AVE周缓存、链上Swap留存和S0精确回放；合约地址缺失候选无法精查 |
| 假阳性风险 | 已降低，但代理指标仍可能误判买盘质量 |
| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |
| 候选来源调整 | 暂不新增外部源，下一步优先接BSC/SOL链上精查，并用合约地址作为入口 |
| 阈值调整 | 暂不改数值；先按Micro/Early/Liquid/Mature层级观察不同阶段表现 |
| 下轮挖掘方向 | 主观察必须有合约地址；PVP和成熟池继续单独展示；优先推进BSC RPC/Helius链上确认 |

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
| dexscreener_boosts | {'ok': True, 'count': 28, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.3 scan uses free public sources only.
- AVE Smart Money weekly cache is not connected yet.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet.
- v0.3 adds contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
# 自我进化轮巡

**本轮时间 UTC：** 2026-08-08T08:33:10Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 135 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 256 |
| 合并后Token | 135 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 4 |
| 多池Token | 7 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 2 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 81; Tier Early; LP $543.5K; Vol24H $2.17M; 24H +12.17%; V/LP 3.99x; 池数 1; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $1.09M; Vol24H $381.7K; 24H +19.71%; V/LP 0.35x; 池数 1; 分项 L19/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 78; Tier Liquid; LP $2.46M; Vol24H $1.03M; 24H +11.34%; V/LP 0.42x; 池数 1; 分项 L20/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NEEGY | SOL | [6oGuFD...22pump](https://solscan.io/token/6oGuFDbEeaSzTcvrmmd2MqfNYwHKXFoN7regcR22pump) | 次观察 | Score 74; Tier Early; LP $164.4K; Vol24H $990.3K; 24H +24.64%; V/LP 6.02x; 池数 1; 分项 L11/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 次观察 | Score 72; Tier Early; LP $448.8K; Vol24H $860.3K; 24H +56.96%; V/LP 1.92x; 池数 1; 分项 L15/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 71; Tier Liquid; LP $2.00M; Vol24H $58.4K; 24H +1.61%; V/LP 0.03x; 池数 1; 分项 L20/V5/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 68; Tier Early; LP $121.4K; Vol24H $55.0K; 24H +14.72%; V/LP 0.45x; 池数 1; 分项 L10/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 次观察 | Score 68; Tier Micro; LP $59.5K; Vol24H $262.9K; 24H +0.67%; V/LP 4.42x; 池数 6; 分项 L7/V10/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 66; Tier Liquid; LP $1.00M; Vol24H $9.39M; 24H -10.16%; V/LP 9.36x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Deod | BSC | [0x3510...61683e](https://bscscan.com/token/0x3510fbbc13090f991ffa523527113a166161683e) | 次观察 | Score 66; Tier Micro; LP $71.0K; Vol24H $60.2K; 24H +13.78%; V/LP 0.85x; 池数 1; 分项 L8/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 81; Tier Early; LP $540.6K; Vol24H $2.19M; 24H +9.65%; V/LP 4.06x; 池数 1; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 80; Tier Liquid; LP $2.05M; Vol24H $379.1K; 24H +0.00%; V/LP 0.18x; 池数 2; 分项 L20/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $1.09M; Vol24H $392.1K; 24H +19.33%; V/LP 0.36x; 池数 1; 分项 L19/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 78; Tier Liquid; LP $2.53M; Vol24H $1.20M; 24H +18.95%; V/LP 0.47x; 池数 1; 分项 L20/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 次观察 | Score 72; Tier Early; LP $445.1K; Vol24H $859.0K; 24H +54.94%; V/LP 1.93x; 池数 1; 分项 L15/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 68; Tier Early; LP $122.0K; Vol24H $55.3K; 24H +13.83%; V/LP 0.45x; 池数 1; 分项 L10/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 次观察 | Score 68; Tier Micro; LP $60.2K; Vol24H $265.8K; 24H +2.37%; V/LP 4.41x; 池数 6; 分项 L7/V10/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 66; Tier Liquid; LP $1.01M; Vol24H $9.37M; 24H -10.36%; V/LP 9.27x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Deod | BSC | [0x3510...61683e](https://bscscan.com/token/0x3510fbbc13090f991ffa523527113a166161683e) | 次观察 | Score 66; Tier Micro; LP $70.8K; Vol24H $56.8K; 24H +15.02%; V/LP 0.80x; 池数 1; 分项 L8/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 次观察 | Score 66; Tier Early; LP $426.3K; Vol24H $2.06M; 24H +72.84%; V/LP 4.84x; 池数 1; 分项 L15/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GWEI | BSC | [0x3011...2f7d49](https://bscscan.com/token/0x30117e4bc17d7b044194b76a38365c53b72f7d49) | PVP风险池 | Score 51; Tier Liquid; LP $1.54M; Vol24H $32.92M; 24H +11.00%; V/LP 21.31x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | PVP风险池 | Score 44; Tier Early; LP $279.5K; Vol24H $8.19M; 24H +16.97%; V/LP 29.30x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [goon](https://dexscreener.com/solana/d4zqhsrbsfw6g9gtb1p4j3ws2uxwedumrzcdjgsqukbn) | SOL | [3c32HT...ugpump](https://solscan.io/token/3c32HTEvDVQC71irgNwQ6HX69Kw387V1aWBn76ugpump) | PVP风险池 | Score 36; Tier Micro; LP $40.0K; Vol24H $2.51M; 24H +1.74%; V/LP 62.83x; 池数 6; 分项 L6/V16/B22/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bStocks | BSC | [0x244b...fd7777](https://bscscan.com/token/0x244b112cf746e62a5df723cbde9906a6defd7777) | PVP风险池 | Score 30; Tier Early; LP $153.2K; Vol24H $7.22M; 24H +3687.97%; V/LP 47.14x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Tanisha | SOL | [7U3io2...m2pump](https://solscan.io/token/7U3io2T7S9ce2hpyLCejHBDQV5Q4UEDAPeshxSm2pump) | PVP风险池 | Score 28; Tier Micro; LP $15.8K; Vol24H $4.12M; 24H +17.71%; V/LP 260.87x; 池数 1; 分项 L2/V17/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| GWEI | BSC | [0x3011...2f7d49](https://bscscan.com/token/0x30117e4bc17d7b044194b76a38365c53b72f7d49) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.54M; Vol24H $32.92M; 24H +11.00%; V/LP 21.31x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $279.5K; Vol24H $8.19M; 24H +16.97%; V/LP 29.30x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [goon](https://dexscreener.com/solana/d4zqhsrbsfw6g9gtb1p4j3ws2uxwedumrzcdjgsqukbn) | SOL | [3c32HT...ugpump](https://solscan.io/token/3c32HTEvDVQC71irgNwQ6HX69Kw387V1aWBn76ugpump) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 36; Tier Micro; LP $40.0K; Vol24H $2.51M; 24H +1.74%; V/LP 62.83x; 池数 6; 分项 L6/V16/B22/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| bStocks | BSC | [0x244b...fd7777](https://bscscan.com/token/0x244b112cf746e62a5df723cbde9906a6defd7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $153.2K; Vol24H $7.22M; 24H +3687.97%; V/LP 47.14x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Tanisha | SOL | [7U3io2...m2pump](https://solscan.io/token/7U3io2T7S9ce2hpyLCejHBDQV5Q4UEDAPeshxSm2pump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 28; Tier Micro; LP $15.8K; Vol24H $4.12M; 24H +17.71%; V/LP 260.87x; 池数 1; 分项 L2/V17/B17/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Frohorse](https://dexscreener.com/solana/5elnx7mtk6ttrmvfgxj3utk8wxtbq81kzruhflehrhvq) | SOL | [9p84TE...uMpump](https://solscan.io/token/9p84TE2ZwH8PXU7QMvj8ieK3TWodZPdCjpE8Q2uMpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.9K; Vol24H $5.37M; 24H +1339.00%; V/LP 85.32x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| ENES | SOL | [BJWHLm...THpump](https://solscan.io/token/BJWHLmtbabbby7LstVRvo4Q39oER9C1TrzR3gpTHpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $20.3K; Vol24H $2.74M; 24H +105.88%; V/LP 135.07x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [RUBY](https://dexscreener.com/solana/d3cavwpt4vutxzntypqaxpbxsmpa2fjoudpkxctwpdw2) | SOL | [JBKWfC...8cpump](https://solscan.io/token/JBKWfCwhW91RvkZb1S9HL8x59YuBbnVFxgwpkx8cpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $40.7K; Vol24H $3.20M; 24H +731.00%; V/LP 78.65x; 池数 10; 分项 L6/V17/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.99M; Vol24H $645.7K; 24H +5.17%; V/LP 0.32x; 池数 2; 分项 L20/V12/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $8.10M; Vol24H $20.93M; 24H +11.95%; V/LP 2.58x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 66; Tier Mature; LP $11.26M; Vol24H $1.28M; 24H +9.82%; V/LP 0.11x; 池数 3; 分项 L20/V14/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Deod | BSC | [0x3510...61683e](https://bscscan.com/token/0x3510fbbc13090f991ffa523527113a166161683e) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 7 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
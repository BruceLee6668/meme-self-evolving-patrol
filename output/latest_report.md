# 自我进化轮巡

**本轮时间 UTC：** 2026-07-05T20:52:57Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 321 |
| 合并后Token | 120 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 5 |
| 多池Token | 15 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 406，刷新时间 2026-06-29T02:42:54Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| DADDY | SOL | [4Cnk9E...9epump](https://solscan.io/token/4Cnk9EPnW5ixfLZatCPJjDB1PUtcRpVVgTQukm9epump) | 主观察 | Score 83; Tier Liquid; LP $1.22M; Vol24H $1.50M; 24H -14.31%; V/LP 1.23x; 池数 1; 分项 L19/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 72; Tier Early; LP $241.9K; Vol24H $245.1K; 24H -12.23%; V/LP 1.01x; 池数 1; 分项 L13/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 70; Tier Micro; LP $66.4K; Vol24H $167.8K; 24H +6.99%; V/LP 2.53x; 池数 2; 分项 L8/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 次观察 | Score 70; Tier Early; LP $187.7K; Vol24H $1.16M; 24H +13.25%; V/LP 6.17x; 池数 1; 分项 L12/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 68; Tier Early; LP $205.4K; Vol24H $550.2K; 24H +30.67%; V/LP 2.68x; 池数 5; 分项 L12/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 65; Tier Early; LP $187.8K; Vol24H $693.4K; 24H -34.01%; V/LP 3.69x; 池数 5; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | PVP风险池 | Score 41; Tier Early; LP $309.3K; Vol24H $8.73M; 24H -48.52%; V/LP 28.22x; 池数 3; 分项 L14/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 40; Tier Liquid; LP $953.0K; Vol24H $19.53M; 24H +34.54%; V/LP 20.49x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 37; Tier Liquid; LP $870.3K; Vol24H $36.88M; 24H +74455.22%; V/LP 42.38x; 池数 1; 分项 L18/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 36; Tier Liquid; LP $773.8K; Vol24H $66.29M; 24H +30483.41%; V/LP 85.66x; 池数 5; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 70; Tier Early; LP $222.8K; Vol24H $237.6K; 24H -23.94%; V/LP 1.07x; 池数 5; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 68; Tier Early; LP $206.7K; Vol24H $536.9K; 24H +25.87%; V/LP 2.60x; 池数 1; 分项 L12/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 次观察 | Score 67; Tier Early; LP $201.5K; Vol24H $1.40M; 24H +31.16%; V/LP 6.96x; 池数 6; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 65; Tier Early; LP $185.0K; Vol24H $666.3K; 24H -30.21%; V/LP 3.60x; 池数 5; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 64; Tier Micro; LP $65.4K; Vol24H $163.8K; 24H -12.55%; V/LP 2.51x; 池数 2; 分项 L7/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 次观察 | Score 64; Tier Early; LP $110.2K; Vol24H $303.9K; 24H -21.64%; V/LP 2.76x; 池数 1; 分项 L10/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 49; Tier Liquid; LP $923.5K; Vol24H $19.76M; 24H +21.22%; V/LP 21.40x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | PVP风险池 | Score 41; Tier Early; LP $322.2K; Vol24H $8.16M; 24H -43.21%; V/LP 25.34x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COBRA](https://dexscreener.com/solana/9nrjcz8arsdujx5bl7rwnnppsiwfhmepvwdhb9cq2eav) | SOL | [D6sA8h...LWpump](https://solscan.io/token/D6sA8hKpreRfWEqLRo2fyx5UpmcHeEmGsQ1UndLWpump) | PVP风险池 | Score 37; Tier Early; LP $123.5K; Vol24H $4.60M; 24H -61.60%; V/LP 37.25x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 36; Tier Liquid; LP $788.2K; Vol24H $69.10M; 24H +29742.96%; V/LP 87.67x; 池数 2; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 36; Tier Liquid; LP $784.3K; Vol24H $43.57M; 24H +57545.23%; V/LP 55.55x; 池数 1; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HEYI | BSC | [0x4ce6...a24444](https://bscscan.com/token/0x4ce634563bb2f72961483357dc31b4c146a24444) | PVP风险池 | Score 30; Tier Early; LP $156.6K; Vol24H $9.29M; 24H +3458.50%; V/LP 59.31x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TOLY | SOL | [CvqxZz...dKpump](https://solscan.io/token/CvqxZzFZqDKSpD1bNSkwQ6j9stSCBVgQ9GT4tLdKpump) | PVP风险池 | Score 28; Tier Micro; LP $99.1K; Vol24H $6.49M; 24H +662.67%; V/LP 65.43x; 池数 6; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEMJAK](https://dexscreener.com/solana/9dhas5v2jtvonyzuhrzylszarha7b15zvx793mvnyx57) | SOL | [BKbf1L...qypump](https://solscan.io/token/BKbf1L2TETrPuJdJeHTFCdSrCE8DDRdzm1DBDgqypump) | PVP风险池 | Score 1; Tier Micro; LP $61.6K; Vol24H $6.04M; 24H +933.00%; V/LP 98.08x; 池数 5; 分项 L7/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 74; Tier Liquid; LP $3.25M; Vol24H $24.44M; 24H -15.77%; V/LP 7.51x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $923.5K; Vol24H $19.76M; 24H +21.22%; V/LP 21.40x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 41; Tier Early; LP $322.2K; Vol24H $8.16M; 24H -43.21%; V/LP 25.34x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [COBRA](https://dexscreener.com/solana/9nrjcz8arsdujx5bl7rwnnppsiwfhmepvwdhb9cq2eav) | SOL | [D6sA8h...LWpump](https://solscan.io/token/D6sA8hKpreRfWEqLRo2fyx5UpmcHeEmGsQ1UndLWpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $123.5K; Vol24H $4.60M; 24H -61.60%; V/LP 37.25x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 36; Tier Liquid; LP $788.2K; Vol24H $69.10M; 24H +29742.96%; V/LP 87.67x; 池数 2; 分项 L17/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 36; Tier Liquid; LP $784.3K; Vol24H $43.57M; 24H +57545.23%; V/LP 55.55x; 池数 1; 分项 L17/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| HEYI | BSC | [0x4ce6...a24444](https://bscscan.com/token/0x4ce634563bb2f72961483357dc31b4c146a24444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $156.6K; Vol24H $9.29M; 24H +3458.50%; V/LP 59.31x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TOLY | SOL | [CvqxZz...dKpump](https://solscan.io/token/CvqxZzFZqDKSpD1bNSkwQ6j9stSCBVgQ9GT4tLdKpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $99.1K; Vol24H $6.49M; 24H +662.67%; V/LP 65.43x; 池数 6; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ANSEMJAK](https://dexscreener.com/solana/9dhas5v2jtvonyzuhrzylszarha7b15zvx793mvnyx57) | SOL | [BKbf1L...qypump](https://solscan.io/token/BKbf1L2TETrPuJdJeHTFCdSrCE8DDRdzm1DBDgqypump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 1; Tier Micro; LP $61.6K; Vol24H $6.04M; 24H +933.00%; V/LP 98.08x; 池数 5; 分项 L7/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.25M; Vol24H $24.44M; 24H -15.77%; V/LP 7.51x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.25M; Vol24H $907.9K; 24H -0.61%; V/LP 0.73x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 66; Tier Mature; LP $5.34M; Vol24H $5.51M; 24H -19.34%; V/LP 1.03x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/3wsaser1eupbegmp6vptcmwg38xsvmjuwa2oqhbt3vyb) | SOL | [99kDGD...nhCSAZ](https://solscan.io/token/99kDGDi5Q655ctCAsxfyGSnws8qUwx3KPHF3t5nhCSAZ) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [COBRA](https://dexscreener.com/solana/9nrjcz8arsdujx5bl7rwnnppsiwfhmepvwdhb9cq2eav) | SOL | [D6sA8h...LWpump](https://solscan.io/token/D6sA8hKpreRfWEqLRo2fyx5UpmcHeEmGsQ1UndLWpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 347} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
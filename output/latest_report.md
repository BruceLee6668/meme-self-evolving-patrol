# 自我进化轮巡

**本轮时间 UTC：** 2026-07-15T17:11:37Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 117 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 208 |
| 合并后Token | 117 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 5 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 10 |
| Early层 | 8 |
| Liquid层 | 3 |
| Mature层 | 4 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 2 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.29M; Vol24H $6.07M; 24H +0.25%; V/LP 4.70x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 主观察 | Score 78; Tier Early; LP $703.7K; Vol24H $3.72M; 24H +20.05%; V/LP 5.29x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 72; Tier Early; LP $288.3K; Vol24H $1.78M; 24H +38.28%; V/LP 6.19x; 池数 2; 分项 L13/V15/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 70; Tier Early; LP $287.8K; Vol24H $162.6K; 24H -13.24%; V/LP 0.57x; 池数 1; 分项 L13/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 次观察 | Score 67; Tier Early; LP $583.8K; Vol24H $2.43M; 24H +30.10%; V/LP 4.17x; 池数 1; 分项 L16/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DARK](https://dexscreener.com/solana/dymkfevepticznbnsmtnvrjrzinoxyzujdblzgtxqdfb) | SOL | [3LgNCF...CPdArK](https://solscan.io/token/3LgNCFW7KjV34TePFih6wRtcWb7mSSByPLsRMxCPdArK) | 次观察 | Score 64; Tier Early; LP $121.5K; Vol24H $149.1K; 24H -7.12%; V/LP 1.23x; 池数 4; 分项 L10/V8/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Flea | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | PVP风险池 | Score 43; Tier Micro; LP $54.5K; Vol24H $3.60M; 24H -15.83%; V/LP 66.03x; 池数 2; 分项 L7/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 33; Tier Early; LP $152.4K; Vol24H $4.49M; 24H -39.67%; V/LP 29.47x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | PVP风险池 | Score 28; Tier Micro; LP $90.2K; Vol24H $8.51M; 24H -79.93%; V/LP 94.40x; 池数 1; 分项 L9/V17/B8/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| brain | SOL | [9oDndF...Skpump](https://solscan.io/token/9oDndFiC7RW42vZcmSzacTKMWE9kgeqnzwXDGLSkpump) | PVP风险池 | Score 28; Tier Micro; LP $54.1K; Vol24H $1.88M; 24H -68.33%; V/LP 34.68x; 池数 2; 分项 L7/V16/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.28M; Vol24H $6.28M; 24H -1.76%; V/LP 4.90x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 主观察 | Score 78; Tier Early; LP $690.5K; Vol24H $4.25M; 24H +12.99%; V/LP 6.15x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 72; Tier Early; LP $275.8K; Vol24H $1.59M; 24H +28.80%; V/LP 5.78x; 池数 1; 分项 L13/V15/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 70; Tier Early; LP $287.2K; Vol24H $159.6K; 24H -17.13%; V/LP 0.56x; 池数 1; 分项 L13/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 次观察 | Score 67; Tier Early; LP $580.2K; Vol24H $2.34M; 24H +36.12%; V/LP 4.04x; 池数 1; 分项 L16/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 66; Tier Early; LP $143.6K; Vol24H $212.6K; 24H -7.42%; V/LP 1.48x; 池数 2; 分项 L11/V9/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 32; Tier Early; LP $137.4K; Vol24H $4.28M; 24H -50.82%; V/LP 31.15x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | PVP风险池 | Score 28; Tier Micro; LP $92.8K; Vol24H $8.07M; 24H -72.44%; V/LP 87.03x; 池数 1; 分项 L9/V17/B8/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | PVP风险池 | Score 23; Tier Early; LP $101.2K; Vol24H $4.08M; 24H +4730.08%; V/LP 40.31x; 池数 2; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Robbinghood | SOL | [6fkhFE...Tspump](https://solscan.io/token/6fkhFEPL1KjipJkAuJg6gCQmHsnvwfhJXUyjV2Tspump) | PVP风险池 | Score 21; Tier Micro; LP $30.9K; Vol24H $2.43M; 24H -30.69%; V/LP 78.74x; 池数 2; 分项 L5/V16/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Flea](https://dexscreener.com/solana/6aau4je3caa3gogza1tonkcuutfrzestwfg5wa3hu8km) | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | PVP风险池 | Score 20; Tier Micro; LP $51.7K; Vol24H $2.34M; 24H +108.00%; V/LP 45.24x; 池数 2; 分项 L7/V16/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 13; Tier Micro; LP $84.7K; Vol24H $223.57M; 24H -99.98%; V/LP 2638.36x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOLdiers](https://dexscreener.com/solana/b4jm2z5daqncjtsfm4f8v5pc88ka8fk3oycswefsq9br) | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 3; Tier Micro; LP $98.5K; Vol24H $12.93M; 24H +2922.00%; V/LP 131.19x; 池数 3; 分项 L9/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | PVP风险池 | Score 0; Tier Micro; LP $20.3K; Vol24H $113.43M; 24H -99.98%; V/LP 5585.01x; 池数 1; 分项 L3/V17/B0/Buy3/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $52.64M; Vol24H $3.06M; 24H -0.27%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 32; Tier Early; LP $137.4K; Vol24H $4.28M; 24H -50.82%; V/LP 31.15x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | 24H未过热但已明显波动；LP未达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高 | Score 28; Tier Micro; LP $92.8K; Vol24H $8.07M; 24H -72.44%; V/LP 87.03x; 池数 1; 分项 L9/V17/B8/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 23; Tier Early; LP $101.2K; Vol24H $4.08M; 24H +4730.08%; V/LP 40.31x; 池数 2; 分项 L9/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Robbinghood | SOL | [6fkhFE...Tspump](https://solscan.io/token/6fkhFEPL1KjipJkAuJg6gCQmHsnvwfhJXUyjV2Tspump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 21; Tier Micro; LP $30.9K; Vol24H $2.43M; 24H -30.69%; V/LP 78.74x; 池数 2; 分项 L5/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Flea](https://dexscreener.com/solana/6aau4je3caa3gogza1tonkcuutfrzestwfg5wa3hu8km) | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 20; Tier Micro; LP $51.7K; Vol24H $2.34M; 24H +108.00%; V/LP 45.24x; 池数 2; 分项 L7/V16/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 13; Tier Micro; LP $84.7K; Vol24H $223.57M; 24H -99.98%; V/LP 2638.36x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-45 | 只记录热度，不进入主榜 |
| [SOLdiers](https://dexscreener.com/solana/b4jm2z5daqncjtsfm4f8v5pc88ka8fk3oycswefsq9br) | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $98.5K; Vol24H $12.93M; 24H +2922.00%; V/LP 131.19x; 池数 3; 分项 L9/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 0; Tier Micro; LP $20.3K; Vol24H $113.43M; 24H -99.98%; V/LP 5585.01x; 池数 1; 分项 L3/V17/B0/Buy3/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $52.64M; Vol24H $3.06M; 24H -0.27%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.35M; Vol24H $9.85M; 24H -11.03%; V/LP 4.18x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BSB | BSC | [0x595d...4679cc](https://bscscan.com/token/0x595deaad1eb5476ff1e649fdb7efc36f1e4679cc) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $9.84M; Vol24H $16.44M; 24H -19.52%; V/LP 1.67x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $1.62M; Vol24H $3.62M; 24H -11.03%; V/LP 2.24x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；成熟大池 | Score 62; Tier Mature; LP $20.46M; Vol24H $34.3K; 24H +0.43%; V/LP 0.00x; 池数 1; 分项 L20/V4/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/41jj12f5ojtm9wpptrwuixmwvg1y95tv7j32wxjcpyqk) | SOL | [EyNbAt...ojFKa6](https://solscan.io/token/EyNbAt2aavE1SbEpmKCLxniHGKez9KqF93zwvAojFKa6) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 2 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 10 / Early 8 / Liquid 3 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
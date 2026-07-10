# 自我进化轮巡

**本轮时间 UTC：** 2026-07-10T02:29:32Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 104 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 243 |
| 合并后Token | 104 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 8 |
| 多池Token | 5 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 11 |
| Liquid层 | 5 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 主观察 | Score 86; Tier Liquid; LP $4.49M; Vol24H $13.90M; 24H +10.14%; V/LP 3.09x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [MAME](https://dexscreener.com/bsc/0x924f1a4422a89900faafa3f886721fdccd6e086a) | BSC | [0xe92F...c42302](https://bscscan.com/token/0xe92F7Fe3EAf61DF28b7B75f3FaAB199333c42302) | 主观察 | Score 85; Tier Liquid; LP $864.2K; Vol24H $671.5K; 24H +2.96%; V/LP 0.78x; 池数 2; 分项 L18/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 主观察 | Score 78; Tier Early; LP $217.5K; Vol24H $635.3K; 24H -5.12%; V/LP 2.92x; 池数 6; 分项 L12/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 主观察 | Score 76; Tier Early; LP $119.3K; Vol24H $506.4K; 24H +2.05%; V/LP 4.24x; 池数 5; 分项 L10/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 次观察 | Score 69; Tier Micro; LP $89.4K; Vol24H $417.4K; 24H -24.22%; V/LP 4.67x; 池数 1; 分项 L9/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | PVP风险池 | Score 50; Tier Early; LP $126.5K; Vol24H $4.63M; 24H +8.88%; V/LP 36.58x; 池数 1; 分项 L10/V17/B17/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 39; Tier Liquid; LP $3.01M; Vol24H $137.65M; 24H -20.82%; V/LP 45.73x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DEXBULL](https://dexscreener.com/solana/9x3m3xwffzejdsjb9znsqdw5pooq5q7wurb3rsmbmcoj) | SOL | [6xCtR2...tqpump](https://solscan.io/token/6xCtR2Eq1VumsoRdNutcfSQfLMk7xUa2BrMx18tqpump) | PVP风险池 | Score 32; Tier Early; LP $135.9K; Vol24H $2.83M; 24H +63.89%; V/LP 20.85x; 池数 2; 分项 L10/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AVAJAK](https://dexscreener.com/solana/cw3k643xazzflhtuygkdq1zx2etettnu4bus73whazc5) | SOL | [HnkB6c...d4pump](https://solscan.io/token/HnkB6cP2fEZE6KwdHwLEdEEDT8J5kUGPL1wFRqd4pump) | PVP风险池 | Score 31; Tier Micro; LP $73.2K; Vol24H $3.24M; 24H +2298.00%; V/LP 44.25x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANIF](https://dexscreener.com/solana/clmwpdywqbkbq9prsuj3dbkxqxigf6jtrnfbr8vwrq6e) | SOL | [HcFUgX...Q3pump](https://solscan.io/token/HcFUgXHEJWjZfDFvyFXDfVRkq5VTzJCfXNpJtcQ3pump) | PVP风险池 | Score 30; Tier Micro; LP $78.6K; Vol24H $2.17M; 24H +1422.00%; V/LP 27.68x; 池数 1; 分项 L8/V16/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 主观察 | Score 91; Tier Liquid; LP $4.36M; Vol24H $13.57M; 24H +2.60%; V/LP 3.11x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 81; Tier Early; LP $192.2K; Vol24H $441.5K; 24H +7.57%; V/LP 2.30x; 池数 5; 分项 L12/V11/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 次观察 | Score 69; Tier Micro; LP $89.7K; Vol24H $378.5K; 24H -16.37%; V/LP 4.22x; 池数 1; 分项 L9/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| HOOD | SOL | [h5NciP...yBhood](https://solscan.io/token/h5NciPdMZ5QCB5BYETJMYBMpVx9ZuitR6HcVjyBhood) | 次观察 | Score 68; Tier Early; LP $251.4K; Vol24H $1.76M; 24H -27.92%; V/LP 7.02x; 池数 1; 分项 L13/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 次观察 | Score 67; Tier Early; LP $180.2K; Vol24H $1.32M; 24H -30.42%; V/LP 7.31x; 池数 1; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 次观察 | Score 65; Tier Early; LP $187.1K; Vol24H $757.1K; 24H -27.80%; V/LP 4.05x; 池数 1; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FOMO](https://dexscreener.com/solana/9qwpxcsessoy6nacsyivmptpeyqxa8hwd2ofpjd4vrxp) | SOL | [BDdzUj...w3pump](https://solscan.io/token/BDdzUjksj1J4bSnMveQ5tV9Up8A9c6YS1tHrxNw3pump) | 次观察 | Score 64; Tier Micro; LP $55.3K; Vol24H $367.5K; 24H +7.67%; V/LP 6.65x; 池数 3; 分项 L7/V11/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | PVP风险池 | Score 42; Tier Early; LP $145.9K; Vol24H $4.83M; 24H +33.97%; V/LP 33.07x; 池数 1; 分项 L11/V17/B8/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 39; Tier Liquid; LP $3.02M; Vol24H $133.33M; 24H -17.06%; V/LP 44.18x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANIF](https://dexscreener.com/solana/clmwpdywqbkbq9prsuj3dbkxqxigf6jtrnfbr8vwrq6e) | SOL | [HcFUgX...Q3pump](https://solscan.io/token/HcFUgXHEJWjZfDFvyFXDfVRkq5VTzJCfXNpJtcQ3pump) | PVP风险池 | Score 32; Tier Micro; LP $88.0K; Vol24H $2.65M; 24H +1750.00%; V/LP 30.10x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZBULL | BSC | [0xcd1a...2e4444](https://bscscan.com/token/0xcd1a9dbbc041386902c96717f0ce1d4a0e2e4444) | PVP风险池 | Score 27; Tier Micro; LP $74.8K; Vol24H $4.77M; 24H +322.49%; V/LP 63.85x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | PVP风险池 | Score 24; Tier Early; LP $110.0K; Vol24H $3.26M; 24H +200.29%; V/LP 29.59x; 池数 2; 分项 L10/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEXBULL | SOL | [6xCtR2...tqpump](https://solscan.io/token/6xCtR2Eq1VumsoRdNutcfSQfLMk7xUa2BrMx18tqpump) | PVP风险池 | Score 24; Tier Early; LP $134.3K; Vol24H $2.81M; 24H +117.47%; V/LP 20.91x; 池数 2; 分项 L10/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AVAJAK](https://dexscreener.com/solana/cw3k643xazzflhtuygkdq1zx2etettnu4bus73whazc5) | SOL | [HnkB6c...d4pump](https://solscan.io/token/HnkB6cP2fEZE6KwdHwLEdEEDT8J5kUGPL1wFRqd4pump) | PVP风险池 | Score 19; Tier Micro; LP $48.8K; Vol24H $3.38M; 24H +945.00%; V/LP 69.21x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Bullscan | SOL | [J5Zogn...MrH2J7](https://solscan.io/token/J5ZognFJEepsWsCQPmqVchvEvsUMomEkxd8LbMrH2J7) | PVP风险池 | Score 13; Tier Micro; LP $44.7K; Vol24H $1.69M; 24H +806.91%; V/LP 37.90x; 池数 1; 分项 L6/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $145.9K; Vol24H $4.83M; 24H +33.97%; V/LP 33.07x; 池数 1; 分项 L11/V17/B8/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $3.02M; Vol24H $133.33M; 24H -17.06%; V/LP 44.18x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [ANIF](https://dexscreener.com/solana/clmwpdywqbkbq9prsuj3dbkxqxigf6jtrnfbr8vwrq6e) | SOL | [HcFUgX...Q3pump](https://solscan.io/token/HcFUgXHEJWjZfDFvyFXDfVRkq5VTzJCfXNpJtcQ3pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Micro; LP $88.0K; Vol24H $2.65M; 24H +1750.00%; V/LP 30.10x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| CZBULL | BSC | [0xcd1a...2e4444](https://bscscan.com/token/0xcd1a9dbbc041386902c96717f0ce1d4a0e2e4444) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $74.8K; Vol24H $4.77M; 24H +322.49%; V/LP 63.85x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Early; LP $110.0K; Vol24H $3.26M; 24H +200.29%; V/LP 29.59x; 池数 2; 分项 L10/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| DEXBULL | SOL | [6xCtR2...tqpump](https://solscan.io/token/6xCtR2Eq1VumsoRdNutcfSQfLMk7xUa2BrMx18tqpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Early; LP $134.3K; Vol24H $2.81M; 24H +117.47%; V/LP 20.91x; 池数 2; 分项 L10/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [AVAJAK](https://dexscreener.com/solana/cw3k643xazzflhtuygkdq1zx2etettnu4bus73whazc5) | SOL | [HnkB6c...d4pump](https://solscan.io/token/HnkB6cP2fEZE6KwdHwLEdEEDT8J5kUGPL1wFRqd4pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $48.8K; Vol24H $3.38M; 24H +945.00%; V/LP 69.21x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| Bullscan | SOL | [J5Zogn...MrH2J7](https://solscan.io/token/J5ZognFJEepsWsCQPmqVchvEvsUMomEkxd8LbMrH2J7) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $44.7K; Vol24H $1.69M; 24H +806.91%; V/LP 37.90x; 池数 1; 分项 L6/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 76; Tier Mature; LP $217.20M; Vol24H $146.19M; 24H +3.56%; V/LP 0.67x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $3.79M; Vol24H $5.20M; 24H +14.61%; V/LP 1.37x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| HOOD | SOL | [h5NciP...yBhood](https://solscan.io/token/h5NciPdMZ5QCB5BYETJMYBMpVx9ZuitR6HcVjyBhood) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FOMO](https://dexscreener.com/solana/9qwpxcsessoy6nacsyivmptpeyqxa8hwd2ofpjd4vrxp) | SOL | [BDdzUj...w3pump](https://solscan.io/token/BDdzUjksj1J4bSnMveQ5tV9Up8A9c6YS1tHrxNw3pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [ANIF](https://dexscreener.com/solana/clmwpdywqbkbq9prsuj3dbkxqxigf6jtrnfbr8vwrq6e) | SOL | [HcFUgX...Q3pump](https://solscan.io/token/HcFUgXHEJWjZfDFvyFXDfVRkq5VTzJCfXNpJtcQ3pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 11 / Liquid 5 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 337} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
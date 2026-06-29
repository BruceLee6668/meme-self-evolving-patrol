# 自我进化轮巡

**本轮时间 UTC：** 2026-06-29T19:01:41Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 140 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 315 |
| 合并后Token | 140 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 4 |
| 多池Token | 11 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 5 |
| Liquid层 | 7 |
| Mature层 | 5 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 406，刷新时间 2026-06-29T02:42:54Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 86; Tier Early; LP $319.1K; Vol24H $1.13M; 24H +1.62%; V/LP 3.53x; 池数 5; 分项 L14/V14/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 75; Tier Early; LP $363.4K; Vol24H $2.58M; 24H +21.34%; V/LP 7.09x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 68; Tier Liquid; LP $1.43M; Vol24H $13.57M; 24H +5.61%; V/LP 9.49x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [REX](https://dexscreener.com/solana/8xzxttcfq49n5awdmtlaok7mkmz65aaatpqryd9m1jl7) | SOL | [CmQJNJ...f7pump](https://solscan.io/token/CmQJNJ185pjzQoebPbcqZu1kTykHxJbn4gER1Af7pump) | 次观察 | Score 67; Tier Micro; LP $57.7K; Vol24H $71.6K; 24H +0.50%; V/LP 1.24x; 池数 2; 分项 L7/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 次观察 | Score 66; Tier Micro; LP $91.9K; Vol24H $142.3K; 24H +11.10%; V/LP 1.55x; 池数 2; 分项 L9/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | PVP风险池 | Score 43; Tier Liquid; LP $1.23M; Vol24H $26.84M; 24H +9.33%; V/LP 21.80x; 池数 4; 分项 L19/V17/B17/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 熊猫头 | BSC | [0xf352...194444](https://bscscan.com/token/0xf3525965a4ad3ca0ac13f4d2f237113691194444) | PVP风险池 | Score 43; Tier Early; LP $191.6K; Vol24H $4.95M; 24H +10.02%; V/LP 25.82x; 池数 13; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEM | BSC | [0xab9d...0f026f](https://bscscan.com/token/0xab9d1148f111c6f6516174143ea7244d000f026f) | PVP风险池 | Score 42; Tier Liquid; LP $2.25M; Vol24H $191.12M; 24H +77.09%; V/LP 85.05x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | PVP风险池 | Score 30; Tier Liquid; LP $1.58M; Vol24H $51.41M; 24H +34.24%; V/LP 32.44x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FLORK | BSC | [0x09db...134444](https://bscscan.com/token/0x09db6885551ab1d4a9fa484d9b4b9fe899134444) | PVP风险池 | Score 30; Tier Early; LP $177.5K; Vol24H $3.86M; 24H +765.96%; V/LP 21.72x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 主观察 | Score 84; Tier Liquid; LP $1.00M; Vol24H $517.0K; 24H +3.58%; V/LP 0.51x; 池数 1; 分项 L18/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 75; Tier Early; LP $380.4K; Vol24H $2.51M; 24H +24.64%; V/LP 6.60x; 池数 1; 分项 L15/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 71; Tier Early; LP $231.2K; Vol24H $173.6K; 24H +0.88%; V/LP 0.75x; 池数 5; 分项 L13/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.43M; Vol24H $1.8K; 24H +5.03%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 68; Tier Liquid; LP $1.43M; Vol24H $13.29M; 24H +6.82%; V/LP 9.29x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 次观察 | Score 66; Tier Micro; LP $94.7K; Vol24H $154.6K; 24H +14.84%; V/LP 1.63x; 池数 2; 分项 L9/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 65; Tier Liquid; LP $1.40M; Vol24H $34.0K; 24H +10.14%; V/LP 0.02x; 池数 1; 分项 L20/V4/B17/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 熊猫头 | BSC | [0xf352...194444](https://bscscan.com/token/0xf3525965a4ad3ca0ac13f4d2f237113691194444) | PVP风险池 | Score 48; Tier Early; LP $185.2K; Vol24H $3.79M; 24H -2.23%; V/LP 20.45x; 池数 6; 分项 L12/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEM | BSC | [0xab9d...0f026f](https://bscscan.com/token/0xab9d1148f111c6f6516174143ea7244d000f026f) | PVP风险池 | Score 34; Tier Liquid; LP $2.49M; Vol24H $189.76M; 24H +240.49%; V/LP 76.31x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | PVP风险池 | Score 30; Tier Liquid; LP $1.60M; Vol24H $52.68M; 24H +29.36%; V/LP 32.92x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FLORK | BSC | [0x09db...134444](https://bscscan.com/token/0x09db6885551ab1d4a9fa484d9b4b9fe899134444) | PVP风险池 | Score 30; Tier Early; LP $164.2K; Vol24H $5.04M; 24H +1070.53%; V/LP 30.70x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TATE | SOL | [CuGJf6...sGpump](https://solscan.io/token/CuGJf6cfDfMh4UxVgNJ5KFQ6v8Wv3qrqop6cFKsGpump) | PVP风险池 | Score 28; Tier Micro; LP $96.3K; Vol24H $2.71M; 24H +2941.63%; V/LP 28.16x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLCAT](https://dexscreener.com/solana/hh6ajghbw5err8rj9kc51zazvrchjvvranc2w8sy6g7j) | SOL | [CkAuhM...tspump](https://solscan.io/token/CkAuhMagnem2iukGwApsfw1ypWETWDdKFD1Xrrtspump) | PVP风险池 | Score 23; Tier Micro; LP $84.2K; Vol24H $4.05M; 24H +1333.00%; V/LP 48.11x; 池数 6; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | PVP风险池 | Score 23; Tier Micro; LP $43.2K; Vol24H $2.73M; 24H -68.72%; V/LP 63.31x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEMHOUSE | SOL | [5RNsaR...pjpump](https://solscan.io/token/5RNsaRw3vDsZ9T1cHgNfGWGcK84GoAYRJcpW5Jpjpump) | PVP风险池 | Score 13; Tier Micro; LP $6.4K; Vol24H $3.38M; 24H -97.79%; V/LP 532.33x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| 熊猫头 | BSC | [0xf352...194444](https://bscscan.com/token/0xf3525965a4ad3ca0ac13f4d2f237113691194444) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 48; Tier Early; LP $185.2K; Vol24H $3.79M; 24H -2.23%; V/LP 20.45x; 池数 6; 分项 L12/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| ANSEM | BSC | [0xab9d...0f026f](https://bscscan.com/token/0xab9d1148f111c6f6516174143ea7244d000f026f) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Liquid; LP $2.49M; Vol24H $189.76M; 24H +240.49%; V/LP 76.31x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；市值超过早期Alpha主榜上限 | Score 30; Tier Liquid; LP $1.60M; Vol24H $52.68M; 24H +29.36%; V/LP 32.92x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| FLORK | BSC | [0x09db...134444](https://bscscan.com/token/0x09db6885551ab1d4a9fa484d9b4b9fe899134444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $164.2K; Vol24H $5.04M; 24H +1070.53%; V/LP 30.70x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TATE | SOL | [CuGJf6...sGpump](https://solscan.io/token/CuGJf6cfDfMh4UxVgNJ5KFQ6v8Wv3qrqop6cFKsGpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $96.3K; Vol24H $2.71M; 24H +2941.63%; V/LP 28.16x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BULLCAT](https://dexscreener.com/solana/hh6ajghbw5err8rj9kc51zazvrchjvvranc2w8sy6g7j) | SOL | [CkAuhM...tspump](https://solscan.io/token/CkAuhMagnem2iukGwApsfw1ypWETWDdKFD1Xrrtspump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 23; Tier Micro; LP $84.2K; Vol24H $4.05M; 24H +1333.00%; V/LP 48.11x; 池数 6; 分项 L9/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $43.2K; Vol24H $2.73M; 24H -68.72%; V/LP 63.31x; 池数 2; 分项 L6/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| ANSEMHOUSE | SOL | [5RNsaR...pjpump](https://solscan.io/token/5RNsaRw3vDsZ9T1cHgNfGWGcK84GoAYRJcpW5Jpjpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $6.4K; Vol24H $3.38M; 24H -97.79%; V/LP 532.33x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 76; Tier Mature; LP $66.23M; Vol24H $168.05M; 24H -1.24%; V/LP 2.54x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 76; Tier Liquid; LP $1.12M; Vol24H $1.35M; 24H +4.87%; V/LP 1.20x; 池数 2; 分项 L19/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $19.39M; Vol24H $111.3K; 24H +4.13%; V/LP 0.01x; 池数 1; 分项 L20/V7/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $167.38M; Vol24H $281.08M; 24H -3.77%; V/LP 1.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| VELVET | BSC | [0x8b19...8c1488](https://bscscan.com/token/0x8b194370825e37b33373e74a41009161808c1488) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 67; Tier Mature; LP $6.87M; Vol24H $1.50M; 24H -9.89%; V/LP 0.22x; 池数 1; 分项 L20/V15/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 66; Tier Mature; LP $7.82M; Vol24H $10.75M; 24H -18.32%; V/LP 1.37x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| 熊猫头 | BSC | [0xf352...194444](https://bscscan.com/token/0xf3525965a4ad3ca0ac13f4d2f237113691194444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 1 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 5 / Liquid 7 / Mature 5 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 331} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
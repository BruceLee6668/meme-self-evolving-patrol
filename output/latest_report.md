# 自我进化轮巡

**本轮时间 UTC：** 2026-07-07T13:14:37Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 122 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 335 |
| 合并后Token | 122 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 9 |
| 多池Token | 10 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 11 |
| Liquid层 | 5 |
| Mature层 | 1 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 次观察 | Score 67; Tier Early; LP $345.9K; Vol24H $5.89M; 24H +6.89%; V/LP 17.03x; 池数 2; 分项 L14/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 67; Tier Early; LP $171.0K; Vol24H $628.6K; 24H -8.06%; V/LP 3.68x; 池数 3; 分项 L11/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 67; Tier Liquid; LP $1.25M; Vol24H $24.33M; 24H +1.63%; V/LP 19.40x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 次观察 | Score 64; Tier Early; LP $169.4K; Vol24H $212.2K; 24H -12.61%; V/LP 1.25x; 池数 6; 分项 L11/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 54; Tier Liquid; LP $960.5K; Vol24H $19.86M; 24H +24.62%; V/LP 20.68x; 池数 1; 分项 L18/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 48; Tier Early; LP $206.7K; Vol24H $13.54M; 24H -12.50%; V/LP 65.50x; 池数 2; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 42; Tier Early; LP $441.0K; Vol24H $9.87M; 24H -39.90%; V/LP 22.37x; 池数 1; 分项 L15/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | PVP风险池 | Score 31; Tier Early; LP $191.5K; Vol24H $12.35M; 24H +12182.00%; V/LP 64.47x; 池数 4; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BIF | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | PVP风险池 | Score 30; Tier Early; LP $168.6K; Vol24H $6.25M; 24H +179.13%; V/LP 37.06x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [₿en Todar](https://dexscreener.com/bsc/0xa29cf2b91bbb91e04fd71853721e0dd1bc4fd716) | BSC | [0x2d6B...a34444](https://bscscan.com/token/0x2d6BcD0A33ed491193878B8deC10789eCea34444) | PVP风险池 | Score 29; Tier Early; LP $136.0K; Vol24H $5.97M; 24H +2202.00%; V/LP 43.88x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.28M; Vol24H $6.51M; 24H -4.04%; V/LP 5.09x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BABYCZ | BSC | [0xc7ae...9e4444](https://bscscan.com/token/0xc7aeb1a936fcf98cfe4dd552f6cbf48ac19e4444) | 次观察 | Score 73; Tier Micro; LP $51.9K; Vol24H $153.8K; 24H +3.15%; V/LP 2.96x; 池数 1; 分项 L7/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 68; Tier Early; LP $439.4K; Vol24H $7.69M; 24H -2.42%; V/LP 17.50x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 67; Tier Early; LP $167.7K; Vol24H $556.9K; 24H -14.09%; V/LP 3.32x; 池数 3; 分项 L11/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 65; Tier Early; LP $267.3K; Vol24H $499.1K; 24H -25.36%; V/LP 1.87x; 池数 5; 分项 L13/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 54; Tier Early; LP $239.0K; Vol24H $13.56M; 24H -4.52%; V/LP 56.76x; 池数 2; 分项 L13/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | PVP风险池 | Score 34; Tier Micro; LP $62.8K; Vol24H $4.41M; 24H -50.58%; V/LP 70.22x; 池数 4; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 31; Tier Early; LP $215.7K; Vol24H $4.75M; 24H +477.63%; V/LP 22.00x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | PVP风险池 | Score 30; Tier Early; LP $146.1K; Vol24H $12.67M; 24H +6993.00%; V/LP 86.68x; 池数 3; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Freedom of meme](https://dexscreener.com/bsc/0x749abdc68bd5aa38df26e5906af379d32a629084) | BSC | [0xD1B4...914444](https://bscscan.com/token/0xD1B4d656a283973D6b0818211d159C94AC914444) | PVP风险池 | Score 27; Tier Micro; LP $81.4K; Vol24H $6.28M; 24H +861.00%; V/LP 77.19x; 池数 6; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SAYLOR | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | PVP风险池 | Score 23; Tier Micro; LP $17.6K; Vol24H $5.52M; 24H -67.27%; V/LP 313.07x; 池数 1; 分项 L2/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 21; Tier Early; LP $170.9K; Vol24H $5.98M; 24H -46.90%; V/LP 35.00x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Vaaland | SOL | [6uYAQy...YCpump](https://solscan.io/token/6uYAQyXYMQ5sTNPRZmYSVMGTAzgkTrK5mGtHpPYCpump) | PVP风险池 | Score 9; Tier Micro; LP $5.4K; Vol24H $4.07M; 24H -98.19%; V/LP 749.58x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $18.11M; Vol24H $11.11M; 24H +2.75%; V/LP 0.61x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 74; Tier Liquid; LP $3.52M; Vol24H $20.60M; 24H +8.08%; V/LP 5.85x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 54; Tier Early; LP $239.0K; Vol24H $13.56M; 24H -4.52%; V/LP 56.76x; 池数 2; 分项 L13/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 34; Tier Micro; LP $62.8K; Vol24H $4.41M; 24H -50.58%; V/LP 70.22x; 池数 4; 分项 L7/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $215.7K; Vol24H $4.75M; 24H +477.63%; V/LP 22.00x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $146.1K; Vol24H $12.67M; 24H +6993.00%; V/LP 86.68x; 池数 3; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Freedom of meme](https://dexscreener.com/bsc/0x749abdc68bd5aa38df26e5906af379d32a629084) | BSC | [0xD1B4...914444](https://bscscan.com/token/0xD1B4d656a283973D6b0818211d159C94AC914444) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $81.4K; Vol24H $6.28M; 24H +861.00%; V/LP 77.19x; 池数 6; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| SAYLOR | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $17.6K; Vol24H $5.52M; 24H -67.27%; V/LP 313.07x; 池数 1; 分项 L2/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 21; Tier Early; LP $170.9K; Vol24H $5.98M; 24H -46.90%; V/LP 35.00x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Vaaland | SOL | [6uYAQy...YCpump](https://solscan.io/token/6uYAQyXYMQ5sTNPRZmYSVMGTAzgkTrK5mGtHpPYCpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $5.4K; Vol24H $4.07M; 24H -98.19%; V/LP 749.58x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $18.11M; Vol24H $11.11M; 24H +2.75%; V/LP 0.61x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.52M; Vol24H $20.60M; 24H +8.08%; V/LP 5.85x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $1.57M; Vol24H $2.86M; 24H +5.61%; V/LP 1.82x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BABYCZ | BSC | [0xc7ae...9e4444](https://bscscan.com/token/0xc7aeb1a936fcf98cfe4dd552f6cbf48ac19e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [BABYANSEM](https://dexscreener.com/solana/47pknd3jk4mmyckwpszbxbnshbzqhqtlch71fkntbnlb) | SOL | [DLvuaz...M5pump](https://solscan.io/token/DLvuaz18bKnh1hEaCZsZ5NgJi7wYFm5RvgZVA2M5pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 11 / Liquid 5 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 338} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
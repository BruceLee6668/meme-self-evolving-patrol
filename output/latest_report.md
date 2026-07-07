# 自我进化轮巡

**本轮时间 UTC：** 2026-07-07T10:21:46Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 358 |
| 合并后Token | 124 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 7 |
| 多池Token | 13 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 12 |
| Liquid层 | 5 |
| Mature层 | 1 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [BIGBANG](https://dexscreener.com/bsc/0xc7bd925d6bbe7ebb44acafcb9b099b516889b811) | BSC | [0xFDD5...455555](https://bscscan.com/token/0xFDD599f3DE302355bAa301E861062A8C11455555) | 次观察 | Score 74; Tier Early; LP $123.4K; Vol24H $409.9K; 24H +15.77%; V/LP 3.32x; 池数 1; 分项 L10/V11/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 次观察 | Score 69; Tier Early; LP $175.2K; Vol24H $192.7K; 24H -3.94%; V/LP 1.10x; 池数 1; 分项 L11/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 68; Tier Early; LP $169.2K; Vol24H $665.5K; 24H -21.85%; V/LP 3.93x; 池数 5; 分项 L11/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [unc](https://dexscreener.com/solana/bwfzkx1pmpvwxammwtrizvowzzzgifeyuyw6ee51shly) | SOL | [ACtfUW...xkpump](https://solscan.io/token/ACtfUWtgvaXrQGNMiohTusi5jcx5RJf5zwu9aAxkpump) | 次观察 | Score 66; Tier Early; LP $169.2K; Vol24H $81.2K; 24H -8.26%; V/LP 0.48x; 池数 5; 分项 L11/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 54; Tier Early; LP $259.9K; Vol24H $14.07M; 24H -1.52%; V/LP 54.14x; 池数 2; 分项 L13/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 45; Tier Liquid; LP $942.0K; Vol24H $23.84M; 24H +41.29%; V/LP 25.31x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 42; Tier Early; LP $461.5K; Vol24H $15.90M; 24H -62.85%; V/LP 34.45x; 池数 1; 分项 L15/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BIF](https://dexscreener.com/solana/6wjspkymm4uq7qekcnfsu9jq7pf3zzjbmhw6efabmexc) | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | PVP风险池 | Score 31; Tier Early; LP $184.2K; Vol24H $6.71M; 24H +1354.00%; V/LP 36.44x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | PVP风险池 | Score 30; Tier Early; LP $166.7K; Vol24H $11.63M; 24H +9353.00%; V/LP 69.76x; 池数 5; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FREEDOM | BSC | [0x9c11...1d4444](https://bscscan.com/token/0x9c118268a9bf6328b62ebf7d2be035fbc01d4444) | PVP风险池 | Score 28; Tier Early; LP $102.6K; Vol24H $6.41M; 24H +1637.79%; V/LP 62.47x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
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
| SAYLOR | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | PVP风险池 | Score 18; Tier Micro; LP $34.4K; Vol24H $5.55M; 24H +103.61%; V/LP 161.35x; 池数 2; 分项 L5/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Freedom of meme](https://dexscreener.com/bsc/0x749abdc68bd5aa38df26e5906af379d32a629084) | BSC | [0xD1B4...914444](https://bscscan.com/token/0xD1B4d656a283973D6b0818211d159C94AC914444) | PVP风险池 | Score 4; Tier Early; LP $131.1K; Vol24H $5.66M; 24H +2290.00%; V/LP 43.17x; 池数 4; 分项 L10/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $18.08M; Vol24H $11.70M; 24H +0.93%; V/LP 0.65x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 74; Tier Liquid; LP $3.48M; Vol24H $22.76M; 24H +14.53%; V/LP 6.53x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 成熟池观察 | Score 71; Tier Liquid; LP $1.59M; Vol24H $2.89M; 24H +5.37%; V/LP 1.82x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 54; Tier Liquid; LP $960.5K; Vol24H $19.86M; 24H +24.62%; V/LP 20.68x; 池数 1; 分项 L18/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 48; Tier Early; LP $206.7K; Vol24H $13.54M; 24H -12.50%; V/LP 65.50x; 池数 2; 分项 L12/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $441.0K; Vol24H $9.87M; 24H -39.90%; V/LP 22.37x; 池数 1; 分项 L15/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $191.5K; Vol24H $12.35M; 24H +12182.00%; V/LP 64.47x; 池数 4; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BIF | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $168.6K; Vol24H $6.25M; 24H +179.13%; V/LP 37.06x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [₿en Todar](https://dexscreener.com/bsc/0xa29cf2b91bbb91e04fd71853721e0dd1bc4fd716) | BSC | [0x2d6B...a34444](https://bscscan.com/token/0x2d6BcD0A33ed491193878B8deC10789eCea34444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $136.0K; Vol24H $5.97M; 24H +2202.00%; V/LP 43.88x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| SAYLOR | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 18; Tier Micro; LP $34.4K; Vol24H $5.55M; 24H +103.61%; V/LP 161.35x; 池数 2; 分项 L5/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [Freedom of meme](https://dexscreener.com/bsc/0x749abdc68bd5aa38df26e5906af379d32a629084) | BSC | [0xD1B4...914444](https://bscscan.com/token/0xD1B4d656a283973D6b0818211d159C94AC914444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 4; Tier Early; LP $131.1K; Vol24H $5.66M; 24H +2290.00%; V/LP 43.17x; 池数 4; 分项 L10/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $18.08M; Vol24H $11.70M; 24H +0.93%; V/LP 0.65x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.48M; Vol24H $22.76M; 24H +14.53%; V/LP 6.53x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $1.59M; Vol24H $2.89M; 24H +5.37%; V/LP 1.82x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| BIF | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [₿en Todar](https://dexscreener.com/bsc/0xa29cf2b91bbb91e04fd71853721e0dd1bc4fd716) | BSC | [0x2d6B...a34444](https://bscscan.com/token/0x2d6BcD0A33ed491193878B8deC10789eCea34444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

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
| LP层级 | Micro 6 / Early 12 / Liquid 5 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
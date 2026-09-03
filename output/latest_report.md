# 自我进化轮巡

**本轮时间 UTC：** 2026-09-03T19:34:39Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 123 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 212 |
| 合并后Token | 123 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 9 |
| 多池Token | 9 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 9 |
| Early层 | 9 |
| Liquid层 | 6 |
| Mature层 | 1 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1174，刷新时间 2026-08-31T02:36:52Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $1.91M; Vol24H $4.13M; 24H +15.54%; V/LP 2.17x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 82; Tier Liquid; LP $2.05M; Vol24H $129.8K; 24H +0.00%; V/LP 0.06x; 池数 1; 分项 L20/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| FLORK | BSC | [0xf405...4d7777](https://bscscan.com/token/0xf40592daacb3e5abf358789f5688c0b4f64d7777) | 次观察 | Score 74; Tier Early; LP $681.0K; Vol24H $4.77M; 24H +41.49%; V/LP 7.01x; 池数 1; 分项 L17/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 71; Tier Early; LP $426.7K; Vol24H $2.36M; 24H +44.29%; V/LP 5.54x; 池数 1; 分项 L15/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [fone](https://dexscreener.com/solana/3dcwhqjp6jbtjpq8ga335hwgsqvs7uqmdmex7igjmnpj) | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 次观察 | Score 66; Tier Liquid; LP $802.6K; Vol24H $7.95M; 24H +14.46%; V/LP 9.91x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| HEMI | BSC | [0x5ffd...5afc5b](https://bscscan.com/token/0x5ffd0eadc186af9512542d0d5e5eafc65d5afc5b) | 次观察 | Score 65; Tier Early; LP $671.5K; Vol24H $12.02M; 24H +7.74%; V/LP 17.91x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 44; Tier Liquid; LP $2.00M; Vol24H $94.52M; 24H +5.55%; V/LP 47.24x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Pumpooor | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | PVP风险池 | Score 40; Tier Micro; LP $98.0K; Vol24H $4.35M; 24H +59.39%; V/LP 44.36x; 池数 2; 分项 L9/V17/B8/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SOLCAT | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | PVP风险池 | Score 38; Tier Early; LP $144.1K; Vol24H $3.27M; 24H -38.43%; V/LP 22.68x; 池数 2; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | PVP风险池 | Score 27; Tier Micro; LP $81.4K; Vol24H $2.57M; 24H +627.00%; V/LP 31.62x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $1.92M; Vol24H $4.23M; 24H +19.66%; V/LP 2.20x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| FLORK | BSC | [0xf405...4d7777](https://bscscan.com/token/0xf40592daacb3e5abf358789f5688c0b4f64d7777) | 主观察 | Score 83; Tier Early; LP $625.8K; Vol24H $4.66M; 24H +11.43%; V/LP 7.45x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 82; Tier Liquid; LP $2.05M; Vol24H $151.8K; 24H -0.34%; V/LP 0.07x; 池数 1; 分项 L20/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 71; Tier Early; LP $419.0K; Vol24H $2.24M; 24H +44.06%; V/LP 5.36x; 池数 1; 分项 L15/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [fone](https://dexscreener.com/solana/3dcwhqjp6jbtjpq8ga335hwgsqvs7uqmdmex7igjmnpj) | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 次观察 | Score 65; Tier Liquid; LP $768.6K; Vol24H $6.57M; 24H -14.57%; V/LP 8.55x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 39; Tier Liquid; LP $2.14M; Vol24H $90.06M; 24H -10.63%; V/LP 42.10x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOLCAT](https://dexscreener.com/solana/6imhrymyu5xogj5w7yveymb5o5yfyavxxveozwpbu5ix) | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | PVP风险池 | Score 36; Tier Early; LP $115.7K; Vol24H $2.34M; 24H -27.01%; V/LP 20.24x; 池数 2; 分项 L10/V16/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | PVP风险池 | Score 28; Tier Micro; LP $89.1K; Vol24H $2.69M; 24H +859.00%; V/LP 30.17x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | PVP风险池 | Score 27; Tier Micro; LP $49.2K; Vol24H $5.50M; 24H -71.15%; V/LP 111.89x; 池数 2; 分项 L6/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | PVP风险池 | Score 26; Tier Early; LP $607.8K; Vol24H $21.93M; 24H +75.06%; V/LP 36.09x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BEN](https://dexscreener.com/solana/dkj8pa8oyrntmp3un7p4jwt9pmbabcgc9mgybotz8jek) | SOL | [43uJZG...Rmpump](https://solscan.io/token/43uJZGxfZcsiL29k1vpwd7H6up5qgMAoU1aMb5Rmpump) | PVP风险池 | Score 26; Tier Micro; LP $61.7K; Vol24H $3.73M; 24H +459.00%; V/LP 60.50x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [POGGERS](https://dexscreener.com/solana/4vcbccqjnfdcsenqmeujcp3w8xdneudtgdcanaaduuee) | SOL | [49FXK7...AFqrcK](https://solscan.io/token/49FXK7sSJT9f6c9WQ36VsaN73XmBiCQfgsELTqAFqrcK) | PVP风险池 | Score 25; Tier Micro; LP $55.9K; Vol24H $2.20M; 24H +814.00%; V/LP 39.32x; 池数 1; 分项 L7/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COIN](https://dexscreener.com/solana/vizuabynwpywfzxcetkxxhm1raoelrfbgy6vz6eu4zp) | SOL | [5jNB5Y...kmpump](https://solscan.io/token/5jNB5YFamqs3iifyhs34ERox2En3EBc1v5CdgHkmpump) | PVP风险池 | Score 14; Tier Micro; LP $39.1K; Vol24H $3.16M; 24H +318.00%; V/LP 80.76x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 79; Tier Liquid; LP $2.88M; Vol24H $3.34M; 24H +3.81%; V/LP 1.16x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $26.20M; Vol24H $23.72M; 24H +5.52%; V/LP 0.91x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $2.14M; Vol24H $90.06M; 24H -10.63%; V/LP 42.10x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [SOLCAT](https://dexscreener.com/solana/6imhrymyu5xogj5w7yveymb5o5yfyavxxveozwpbu5ix) | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Early; LP $115.7K; Vol24H $2.34M; 24H -27.01%; V/LP 20.24x; 池数 2; 分项 L10/V16/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $89.1K; Vol24H $2.69M; 24H +859.00%; V/LP 30.17x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 27; Tier Micro; LP $49.2K; Vol24H $5.50M; 24H -71.15%; V/LP 111.89x; 池数 2; 分项 L6/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 26; Tier Early; LP $607.8K; Vol24H $21.93M; 24H +75.06%; V/LP 36.09x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [BEN](https://dexscreener.com/solana/dkj8pa8oyrntmp3un7p4jwt9pmbabcgc9mgybotz8jek) | SOL | [43uJZG...Rmpump](https://solscan.io/token/43uJZGxfZcsiL29k1vpwd7H6up5qgMAoU1aMb5Rmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $61.7K; Vol24H $3.73M; 24H +459.00%; V/LP 60.50x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [POGGERS](https://dexscreener.com/solana/4vcbccqjnfdcsenqmeujcp3w8xdneudtgdcanaaduuee) | SOL | [49FXK7...AFqrcK](https://solscan.io/token/49FXK7sSJT9f6c9WQ36VsaN73XmBiCQfgsELTqAFqrcK) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $55.9K; Vol24H $2.20M; 24H +814.00%; V/LP 39.32x; 池数 1; 分项 L7/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [COIN](https://dexscreener.com/solana/vizuabynwpywfzxcetkxxhm1raoelrfbgy6vz6eu4zp) | SOL | [5jNB5Y...kmpump](https://solscan.io/token/5jNB5YFamqs3iifyhs34ERox2En3EBc1v5CdgHkmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $39.1K; Vol24H $3.16M; 24H +318.00%; V/LP 80.76x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.88M; Vol24H $3.34M; 24H +3.81%; V/LP 1.16x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $26.20M; Vol24H $23.72M; 24H +5.52%; V/LP 0.91x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| FLORK | BSC | [0xf405...4d7777](https://bscscan.com/token/0xf40592daacb3e5abf358789f5688c0b4f64d7777) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [fone](https://dexscreener.com/solana/3dcwhqjp6jbtjpq8ga335hwgsqvs7uqmdmex7igjmnpj) | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [SOLCAT](https://dexscreener.com/solana/6imhrymyu5xogj5w7yveymb5o5yfyavxxveozwpbu5ix) | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| FLORK | BSC | [0xf405...4d7777](https://bscscan.com/token/0xf40592daacb3e5abf358789f5688c0b4f64d7777) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 9 / Early 9 / Liquid 6 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 334} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
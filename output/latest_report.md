# 自我进化轮巡

**本轮时间 UTC：** 2026-08-18T19:22:56Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 124 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 229 |
| 合并后Token | 124 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 1 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 12 |
| 多池Token | 12 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 12 |
| Early层 | 6 |
| Liquid层 | 5 |
| Mature层 | 2 |
| 需要链上确认 | 10 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1035，刷新时间 2026-08-17T00:45:08Z，是否过期 否 |
| 链上预检 | 本轮检查 10 个，验证通过 3 个，失败 7 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 次观察 | Score 75; Tier Liquid; LP $889.1K; Vol24H $14.65M; 24H +5.00%; V/LP 16.48x; 池数 13; 分项 L18/V17/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 75; Tier Liquid; LP $1.42M; Vol24H $1.49M; 24H +34.66%; V/LP 1.05x; 池数 1; 分项 L20/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 次观察 | Score 72; Tier Early; LP $555.3K; Vol24H $504.5K; 24H +32.19%; V/LP 0.91x; 池数 1; 分项 L16/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 55; Tier Liquid; LP $1.28M; Vol24H $66.17M; 24H -1.30%; V/LP 51.53x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Z](https://dexscreener.com/solana/exormh6uapxi6abtqfnbcbdsdyvnp5zc6cyybzzvuolh) | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | PVP风险池 | Score 49; Tier Micro; LP $83.1K; Vol24H $5.35M; 24H +7.71%; V/LP 64.42x; 池数 2; 分项 L8/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | PVP风险池 | Score 45; Tier Early; LP $328.3K; Vol24H $8.87M; 24H +8.21%; V/LP 27.00x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | PVP风险池 | Score 39; Tier Early; LP $211.5K; Vol24H $15.87M; 24H +41.60%; V/LP 75.06x; 池数 3; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Z500](https://dexscreener.com/solana/2c7palgc7wtqzwr9wa7qt2bthqtdyzcbl6beyfgdsa5e) | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | PVP风险池 | Score 35; Tier Micro; LP $81.9K; Vol24H $5.43M; 24H -74.25%; V/LP 66.30x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | PVP风险池 | Score 27; Tier Micro; LP $77.8K; Vol24H $10.73M; 24H +2163.00%; V/LP 137.99x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 67coin | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | PVP风险池 | Score 26; Tier Micro; LP $59.1K; Vol24H $15.21M; 24H +1142.74%; V/LP 257.53x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 84; Tier Liquid; LP $1.38M; Vol24H $1.53M; 24H +23.68%; V/LP 1.11x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 次观察 | Score 66; Tier Liquid; LP $855.7K; Vol24H $14.49M; 24H +12.49%; V/LP 16.93x; 池数 11; 分项 L18/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EYE | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | PVP风险池 | Score 53; Tier Early; LP $206.5K; Vol24H $13.59M; 24H +7.44%; V/LP 65.82x; 池数 3; 分项 L12/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | PVP风险池 | Score 50; Tier Early; LP $317.8K; Vol24H $8.65M; 24H +5.70%; V/LP 27.21x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | PVP风险池 | Score 35; Tier Micro; LP $77.8K; Vol24H $9.08M; 24H -46.49%; V/LP 116.77x; 池数 1; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Z500 | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | PVP风险池 | Score 35; Tier Micro; LP $79.8K; Vol24H $4.75M; 24H -73.37%; V/LP 59.49x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Z | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | PVP风险池 | Score 35; Tier Micro; LP $78.7K; Vol24H $4.09M; 24H +63.18%; V/LP 51.99x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Qenis](https://dexscreener.com/solana/httde6bsdc3y58owhqayqmersnmwnrzfvdewjymxgax3) | SOL | [EkcTa8...KTpump](https://solscan.io/token/EkcTa8n14fXcHdfvZqCg72cTCutJnnKb19vcHwKTpump) | PVP风险池 | Score 30; Tier Early; LP $172.9K; Vol24H $3.49M; 24H +99.02%; V/LP 20.17x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 67coin | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | PVP风险池 | Score 26; Tier Micro; LP $51.6K; Vol24H $15.29M; 24H +857.27%; V/LP 296.56x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOLLOCKS](https://dexscreener.com/solana/ewlkmz6r2tcvkiep4zzxqybnbxm96yfhmw97csn1zl6p) | SOL | [9MMXQQ...3ghYn7](https://solscan.io/token/9MMXQQhhMhA4yWeTuiv7dkGTeCMzKCGmfmWgVD3ghYn7) | PVP风险池 | Score 14; Tier Micro; LP $36.9K; Vol24H $3.81M; 24H +513.00%; V/LP 103.23x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 74; Tier Liquid; LP $2.39M; Vol24H $3.72M; 24H -21.13%; V/LP 1.56x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $14.14M; Vol24H $7.19M; 24H +0.49%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 74; Tier Mature; LP $70.27M; Vol24H $36.06M; 24H +0.05%; V/LP 0.51x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 低优先观察 | Score 62; Tier Liquid; LP $2.16M; Vol24H $44.7K; 24H +1.16%; V/LP 0.02x; 池数 1; 分项 L20/V4/B22/Buy0/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 低优先观察 | Score 62; Tier Micro; LP $92.0K; Vol24H $210.2K; 24H -23.30%; V/LP 2.28x; 池数 3; 分项 L9/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| EYE | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 53; Tier Early; LP $206.5K; Vol24H $13.59M; 24H +7.44%; V/LP 65.82x; 池数 3; 分项 L12/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 50; Tier Early; LP $317.8K; Vol24H $8.65M; 24H +5.70%; V/LP 27.21x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $77.8K; Vol24H $9.08M; 24H -46.49%; V/LP 116.77x; 池数 1; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Z500 | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $79.8K; Vol24H $4.75M; 24H -73.37%; V/LP 59.49x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Z | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $78.7K; Vol24H $4.09M; 24H +63.18%; V/LP 51.99x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Qenis](https://dexscreener.com/solana/httde6bsdc3y58owhqayqmersnmwnrzfvdewjymxgax3) | SOL | [EkcTa8...KTpump](https://solscan.io/token/EkcTa8n14fXcHdfvZqCg72cTCutJnnKb19vcHwKTpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $172.9K; Vol24H $3.49M; 24H +99.02%; V/LP 20.17x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| 67coin | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $51.6K; Vol24H $15.29M; 24H +857.27%; V/LP 296.56x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BOLLOCKS](https://dexscreener.com/solana/ewlkmz6r2tcvkiep4zzxqybnbxm96yfhmw97csn1zl6p) | SOL | [9MMXQQ...3ghYn7](https://solscan.io/token/9MMXQQhhMhA4yWeTuiv7dkGTeCMzKCGmfmWgVD3ghYn7) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.9K; Vol24H $3.81M; 24H +513.00%; V/LP 103.23x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.39M; Vol24H $3.72M; 24H -21.13%; V/LP 1.56x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $14.14M; Vol24H $7.19M; 24H +0.49%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $70.27M; Vol24H $36.06M; 24H +0.05%; V/LP 0.51x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| EYE | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | 是 | 否 | failed / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Z500 | SOL | [7fDdLy...mfkJBK](https://solscan.io/token/7fDdLy2rmQKsPCkqUXEd1mN7yDfEzArc4VrctWmfkJBK) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Z | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Qenis](https://dexscreener.com/solana/httde6bsdc3y58owhqayqmersnmwnrzfvdewjymxgax3) | SOL | [EkcTa8...KTpump](https://solscan.io/token/EkcTa8n14fXcHdfvZqCg72cTCutJnnKb19vcHwKTpump) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| 67coin | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BOLLOCKS](https://dexscreener.com/solana/ewlkmz6r2tcvkiep4zzxqybnbxm96yfhmw97csn1zl6p) | SOL | [9MMXQQ...3ghYn7](https://solscan.io/token/9MMXQQhhMhA4yWeTuiv7dkGTeCMzKCGmfmWgVD3ghYn7) | 是 | 否 | failed / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 12 / Early 6 / Liquid 5 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 336} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
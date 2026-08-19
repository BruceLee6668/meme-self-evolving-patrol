# 自我进化轮巡

**本轮时间 UTC：** 2026-08-19T02:16:01Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 123 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 256 |
| 合并后Token | 123 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 1 |
| 低优先观察 | 10 |
| 多池Token | 10 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 1 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1035，刷新时间 2026-08-17T00:45:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 89; Tier Liquid; LP $1.35M; Vol24H $1.52M; 24H +7.04%; V/LP 1.13x; 池数 1; 分项 L20/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Qenis](https://dexscreener.com/solana/httde6bsdc3y58owhqayqmersnmwnrzfvdewjymxgax3) | SOL | [EkcTa8...KTpump](https://solscan.io/token/EkcTa8n14fXcHdfvZqCg72cTCutJnnKb19vcHwKTpump) | 次观察 | Score 64; Tier Early; LP $153.0K; Vol24H $2.79M; 24H +6.32%; V/LP 18.25x; 池数 1; 分项 L11/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 55; Tier Liquid; LP $1.29M; Vol24H $68.10M; 24H -1.67%; V/LP 52.82x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | PVP风险池 | Score 50; Tier Early; LP $324.1K; Vol24H $7.52M; 24H +4.72%; V/LP 23.19x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EYE | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | PVP风险池 | Score 39; Tier Early; LP $200.4K; Vol24H $4.34M; 24H -33.67%; V/LP 21.64x; 池数 3; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | PVP风险池 | Score 30; Tier Early; LP $153.9K; Vol24H $4.57M; 24H +148.00%; V/LP 29.67x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAME](https://dexscreener.com/solana/6atbru6gybp1dwb6xejduww8vb8hlvni1tomxlnrfjyr) | SOL | [CU5e2i...skpump](https://solscan.io/token/CU5e2iqWkXKrEHrg6fgoV6uqptEWL9M98oeU4skpump) | PVP风险池 | Score 26; Tier Early; LP $197.2K; Vol24H $4.12M; 24H +677.00%; V/LP 20.92x; 池数 1; 分项 L12/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 67coin | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | PVP风险池 | Score 15; Tier Micro; LP $39.9K; Vol24H $15.63M; 24H +457.59%; V/LP 391.60x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Gorikun](https://dexscreener.com/solana/6jcybpjqrxozz12scbxe1votcpie6uduc1g5kye6pt7k) | SOL | [Drac2H...8Kpump](https://solscan.io/token/Drac2HBT8Fxt9SauZj8yVWUUyZbE5gZ9fNzXqL8Kpump) | PVP风险池 | Score 14; Tier Micro; LP $32.7K; Vol24H $3.74M; 24H +280.00%; V/LP 114.31x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AXE](https://dexscreener.com/solana/a9w9th82joz23fz1m1snofgrm2rnpjtk5hnd8stds8lv) | SOL | [BcMKCe...M5pump](https://solscan.io/token/BcMKCebDM3JJrSJy3WuYdvcbChri49Z1z4GoApM5pump) | PVP风险池 | Score 2; Tier Micro; LP $78.0K; Vol24H $4.15M; 24H +2578.00%; V/LP 53.21x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 84; Tier Liquid; LP $1.34M; Vol24H $1.52M; 24H +10.53%; V/LP 1.14x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CREPE | BSC | [0xeb2b...8d931d](https://bscscan.com/token/0xeb2b7d5691878627eff20492ca7c9a71228d931d) | 次观察 | Score 74; Tier Early; LP $582.2K; Vol24H $202.5K; 24H -11.77%; V/LP 0.35x; 池数 1; 分项 L16/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 次观察 | Score 71; Tier Liquid; LP $940.1K; Vol24H $15.14M; 24H +4.03%; V/LP 16.11x; 池数 18; 分项 L18/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 64; Tier Micro; LP $81.2K; Vol24H $100.9K; 24H -22.08%; V/LP 1.24x; 池数 3; 分项 L8/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 55; Tier Liquid; LP $1.30M; Vol24H $70.52M; 24H -0.91%; V/LP 54.19x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | PVP风险池 | Score 45; Tier Early; LP $324.8K; Vol24H $7.35M; 24H +17.60%; V/LP 22.64x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | PVP风险池 | Score 37; Tier Early; LP $123.5K; Vol24H $4.56M; 24H -25.93%; V/LP 36.90x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | PVP风险池 | Score 34; Tier Early; LP $184.5K; Vol24H $3.79M; 24H -37.36%; V/LP 20.54x; 池数 3; 分项 L12/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Z](https://dexscreener.com/solana/exormh6uapxi6abtqfnbcbdsdyvnp5zc6cyybzzvuolh) | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | PVP风险池 | Score 30; Tier Micro; LP $74.3K; Vol24H $3.00M; 24H +38.51%; V/LP 40.33x; 池数 2; 分项 L8/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AXE](https://dexscreener.com/solana/a9w9th82joz23fz1m1snofgrm2rnpjtk5hnd8stds8lv) | SOL | [BcMKCe...M5pump](https://solscan.io/token/BcMKCebDM3JJrSJy3WuYdvcbChri49Z1z4GoApM5pump) | PVP风险池 | Score 27; Tier Micro; LP $71.0K; Vol24H $4.27M; 24H +2125.00%; V/LP 60.06x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAME](https://dexscreener.com/solana/6atbru6gybp1dwb6xejduww8vb8hlvni1tomxlnrfjyr) | SOL | [CU5e2i...skpump](https://solscan.io/token/CU5e2iqWkXKrEHrg6fgoV6uqptEWL9M98oeU4skpump) | PVP风险池 | Score 25; Tier Early; LP $139.7K; Vol24H $5.17M; 24H +268.00%; V/LP 36.98x; 池数 1; 分项 L11/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [67coin](https://dexscreener.com/solana/6vzyorybzzeltuf6bejjgrekk2eehq2bx2unu3eviblc) | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | PVP风险池 | Score 15; Tier Micro; LP $45.2K; Vol24H $15.77M; 24H +510.00%; V/LP 349.16x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 78; Tier Liquid; LP $2.32M; Vol24H $2.32M; 24H -6.83%; V/LP 1.00x; 池数 2; 分项 L20/V16/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 低优先观察 | Score 62; Tier Liquid; LP $2.15M; Vol24H $44.0K; 24H +1.20%; V/LP 0.02x; 池数 1; 分项 L20/V4/B22/Buy0/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 低优先观察 | Score 60; Tier Early; LP $106.8K; Vol24H $325.9K; 24H +24.22%; V/LP 3.05x; 池数 3; 分项 L9/V10/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 55; Tier Liquid; LP $1.30M; Vol24H $70.52M; 24H -0.91%; V/LP 54.19x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Early; LP $324.8K; Vol24H $7.35M; 24H +17.60%; V/LP 22.64x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $123.5K; Vol24H $4.56M; 24H -25.93%; V/LP 36.90x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 34; Tier Early; LP $184.5K; Vol24H $3.79M; 24H -37.36%; V/LP 20.54x; 池数 3; 分项 L12/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Z](https://dexscreener.com/solana/exormh6uapxi6abtqfnbcbdsdyvnp5zc6cyybzzvuolh) | SOL | [7MQSup...naN3eS](https://solscan.io/token/7MQSupJTpY31HGChEHUAsS1pQhLSrHS5CCsB9bnaN3eS) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 30; Tier Micro; LP $74.3K; Vol24H $3.00M; 24H +38.51%; V/LP 40.33x; 池数 2; 分项 L8/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [AXE](https://dexscreener.com/solana/a9w9th82joz23fz1m1snofgrm2rnpjtk5hnd8stds8lv) | SOL | [BcMKCe...M5pump](https://solscan.io/token/BcMKCebDM3JJrSJy3WuYdvcbChri49Z1z4GoApM5pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $71.0K; Vol24H $4.27M; 24H +2125.00%; V/LP 60.06x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SAME](https://dexscreener.com/solana/6atbru6gybp1dwb6xejduww8vb8hlvni1tomxlnrfjyr) | SOL | [CU5e2i...skpump](https://solscan.io/token/CU5e2iqWkXKrEHrg6fgoV6uqptEWL9M98oeU4skpump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Early; LP $139.7K; Vol24H $5.17M; 24H +268.00%; V/LP 36.98x; 池数 1; 分项 L11/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [67coin](https://dexscreener.com/solana/6vzyorybzzeltuf6bejjgrekk2eehq2bx2unu3eviblc) | SOL | [DLYQBX...2epump](https://solscan.io/token/DLYQBXkRo43Ct96fd9Cr7y5tZP5yQKUBLMTZU92epump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $45.2K; Vol24H $15.77M; 24H +510.00%; V/LP 349.16x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $2.32M; Vol24H $2.32M; 24H -6.83%; V/LP 1.00x; 池数 2; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| CREPE | BSC | [0xeb2b...8d931d](https://bscscan.com/token/0xeb2b7d5691878627eff20492ca7c9a71228d931d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [KIO](https://dexscreener.com/solana/ccye73oa7dqrcs16fht3twevnhtlzrqzwn4c8smdxfwq) | SOL | [7rMnp9...7opump](https://solscan.io/token/7rMnp9EJd61SvNn8LGc7SAJeQxM36oeECKmP2a7opump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [PUMP](https://dexscreener.com/solana/9ww15cehwhuapsr3a2ysu3ilk3vswwbqfp9rzbpvaiph) | SOL | [8FtafP...sC5yBx](https://solscan.io/token/8FtafPHhmYVtKQYrbNs4ZSS2Hwykw5dJ3t1JtGsC5yBx) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| MarsCoin | BSC | [0x1706...6f4444](https://bscscan.com/token/0x1706f1e06c69f3a8cf33cce179d5d78a5c6f4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BULLSHIT](https://dexscreener.com/solana/cd5hdt23sjgud5vtwsv51bmpey2qf9qh5cyswwmjbddq) | SOL | [zj1jpp...F8ry2k](https://solscan.io/token/zj1jpp7QMveWHLs61vL9KMZf254KvW7j4AAmBF8ry2k) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [EYE](https://dexscreener.com/solana/5jm4gnwpt62kphmheet6rjzzfjvsfnxnqdpeugwp2u9q) | SOL | [RmtMAY...KwNDYk](https://solscan.io/token/RmtMAYVTTFv2iK9muMrXEoAnSSsZPPgRPbqZCKwNDYk) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

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
| 成熟池观察 | 1 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 10 / Liquid 6 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
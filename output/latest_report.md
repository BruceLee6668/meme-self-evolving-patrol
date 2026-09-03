# 自我进化轮巡

**本轮时间 UTC：** 2026-09-03T12:29:08Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 124 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 199 |
| 合并后Token | 124 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 8 |
| 多池Token | 9 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 2 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1174，刷新时间 2026-08-31T02:36:52Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 0 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $1.77M; Vol24H $3.91M; 24H -8.96%; V/LP 2.21x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 主观察 | Score 78; Tier Early; LP $365.4K; Vol24H $1.38M; 24H +22.35%; V/LP 3.78x; 池数 1; 分项 L14/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 次观察 | Score 74; Tier Liquid; LP $812.6K; Vol24H $2.18M; 24H +29.32%; V/LP 2.68x; 池数 1; 分项 L18/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WSOLP](https://dexscreener.com/solana/h5gzcmccxdzexzneddgfepjnpyayuyhh6t4cyxt5pdfz) | SOL | [GvUCjm...A1pump](https://solscan.io/token/GvUCjmWSXA5hrTh9smmNA1AU55YCtP9mDLQcrKA1pump) | 次观察 | Score 68; Tier Early; LP $158.7K; Vol24H $164.2K; 24H -10.84%; V/LP 1.03x; 池数 1; 分项 L11/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 次观察 | Score 65; Tier Liquid; LP $777.1K; Vol24H $8.24M; 24H -12.05%; V/LP 10.60x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SME](https://dexscreener.com/bsc/0xb293980374739cfe7b41bbe5f7be31ae86ff18a8) | BSC | [0x36dB...2a0C92](https://bscscan.com/token/0x36dBcBCA106353D49e1E0E8974492fFB862a0C92) | 次观察 | Score 64; Tier Early; LP $356.1K; Vol24H $0.10; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L14/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 48; Tier Liquid; LP $1.11M; Vol24H $23.01M; 24H -4.37%; V/LP 20.82x; 池数 12; 分项 L19/V17/B22/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | PVP风险池 | Score 48; Tier Micro; LP $69.8K; Vol24H $3.15M; 24H -22.23%; V/LP 45.09x; 池数 1; 分项 L8/V17/B17/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEBIT | BSC | [0x6666...83ce49](https://bscscan.com/token/0x66661c7229901f568f16bd1551b3ba826f83ce49) | PVP风险池 | Score 44; Tier Liquid; LP $2.18M; Vol24H $263.62M; 24H -1.55%; V/LP 120.99x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 30; Tier Liquid; LP $1.93M; Vol24H $116.91M; 24H +49.46%; V/LP 60.56x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $1.75M; Vol24H $3.92M; 24H -1.24%; V/LP 2.24x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 77; Tier Liquid; LP $2.05M; Vol24H $172.0K; 24H +0.00%; V/LP 0.08x; 池数 1; 分项 L20/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 71; Tier Early; LP $454.5K; Vol24H $2.14M; 24H +63.26%; V/LP 4.72x; 池数 1; 分项 L15/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Martians](https://dexscreener.com/solana/42srahwlaltsf9uhs8jsjvwjjxj5glbenqcjxkyk4eho) | SOL | [7nLukV...o1pump](https://solscan.io/token/7nLukVng5teXze14rum9v57juXLjUp7JJnCveko1pump) | 次观察 | Score 69; Tier Micro; LP $72.9K; Vol24H $114.1K; 24H +1.73%; V/LP 1.56x; 池数 3; 分项 L8/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WSOLP](https://dexscreener.com/solana/h5gzcmccxdzexzneddgfepjnpyayuyhh6t4cyxt5pdfz) | SOL | [GvUCjm...A1pump](https://solscan.io/token/GvUCjmWSXA5hrTh9smmNA1AU55YCtP9mDLQcrKA1pump) | 次观察 | Score 69; Tier Early; LP $150.4K; Vol24H $213.5K; 24H -18.88%; V/LP 1.42x; 池数 1; 分项 L11/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 次观察 | Score 65; Tier Early; LP $738.9K; Vol24H $7.96M; 24H -13.52%; V/LP 10.78x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | PVP风险池 | Score 40; Tier Micro; LP $99.6K; Vol24H $3.32M; 24H +32.71%; V/LP 33.36x; 池数 7; 分项 L9/V17/B8/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 30; Tier Liquid; LP $1.97M; Vol24H $121.07M; 24H +51.71%; V/LP 61.49x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SOLCAT | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | PVP风险池 | Score 29; Tier Early; LP $134.5K; Vol24H $8.86M; 24H +643.91%; V/LP 65.91x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | PVP风险池 | Score 27; Tier Early; LP $104.2K; Vol24H $2.18M; 24H +1246.00%; V/LP 20.94x; 池数 1; 分项 L9/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HeeHaw](https://dexscreener.com/solana/6qyydc6jgeknfp1fwhiexmyq3jq3sidsyoubjwuto3rm) | SOL | [EEpng7...yTpump](https://solscan.io/token/EEpng77ZPn9FbgbT4xsRjwuxNCcMBYq3HTwEscyTpump) | PVP风险池 | Score 26; Tier Micro; LP $78.3K; Vol24H $1.89M; 24H -80.07%; V/LP 24.12x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | PVP风险池 | Score 25; Tier Early; LP $400.3K; Vol24H $19.09M; 24H +70.11%; V/LP 47.68x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COIN](https://dexscreener.com/solana/vizuabynwpywfzxcetkxxhm1raoelrfbgy6vz6eu4zp) | SOL | [5jNB5Y...kmpump](https://solscan.io/token/5jNB5YFamqs3iifyhs34ERox2En3EBc1v5CdgHkmpump) | PVP风险池 | Score 14; Tier Micro; LP $37.7K; Vol24H $2.85M; 24H +317.00%; V/LP 75.77x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BEN](https://dexscreener.com/solana/dkj8pa8oyrntmp3un7p4jwt9pmbabcgc9mgybotz8jek) | SOL | [43uJZG...Rmpump](https://solscan.io/token/43uJZGxfZcsiL29k1vpwd7H6up5qgMAoU1aMb5Rmpump) | PVP风险池 | Score 2; Tier Micro; LP $73.6K; Vol24H $3.21M; 24H +707.00%; V/LP 43.63x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 79; Tier Liquid; LP $2.69M; Vol24H $2.89M; 24H -6.59%; V/LP 1.08x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Micro; LP $99.6K; Vol24H $3.32M; 24H +32.71%; V/LP 33.36x; 池数 7; 分项 L9/V17/B8/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $1.97M; Vol24H $121.07M; 24H +51.71%; V/LP 61.49x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| SOLCAT | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $134.5K; Vol24H $8.86M; 24H +643.91%; V/LP 65.91x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $104.2K; Vol24H $2.18M; 24H +1246.00%; V/LP 20.94x; 池数 1; 分项 L9/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HeeHaw](https://dexscreener.com/solana/6qyydc6jgeknfp1fwhiexmyq3jq3sidsyoubjwuto3rm) | SOL | [EEpng7...yTpump](https://solscan.io/token/EEpng77ZPn9FbgbT4xsRjwuxNCcMBYq3HTwEscyTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $78.3K; Vol24H $1.89M; 24H -80.07%; V/LP 24.12x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 25; Tier Early; LP $400.3K; Vol24H $19.09M; 24H +70.11%; V/LP 47.68x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [COIN](https://dexscreener.com/solana/vizuabynwpywfzxcetkxxhm1raoelrfbgy6vz6eu4zp) | SOL | [5jNB5Y...kmpump](https://solscan.io/token/5jNB5YFamqs3iifyhs34ERox2En3EBc1v5CdgHkmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $37.7K; Vol24H $2.85M; 24H +317.00%; V/LP 75.77x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [BEN](https://dexscreener.com/solana/dkj8pa8oyrntmp3un7p4jwt9pmbabcgc9mgybotz8jek) | SOL | [43uJZG...Rmpump](https://solscan.io/token/43uJZGxfZcsiL29k1vpwd7H6up5qgMAoU1aMb5Rmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 2; Tier Micro; LP $73.6K; Vol24H $3.21M; 24H +707.00%; V/LP 43.63x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.69M; Vol24H $2.89M; 24H -6.59%; V/LP 1.08x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $25.42M; Vol24H $20.34M; 24H +1.33%; V/LP 0.80x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.94M; Vol24H $6.09M; 24H -2.70%; V/LP 3.13x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Martians](https://dexscreener.com/solana/42srahwlaltsf9uhs8jsjvwjjxj5glbenqcjxkyk4eho) | SOL | [7nLukV...o1pump](https://solscan.io/token/7nLukVng5teXze14rum9v57juXLjUp7JJnCveko1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WSOLP](https://dexscreener.com/solana/h5gzcmccxdzexzneddgfepjnpyayuyhh6t4cyxt5pdfz) | SOL | [GvUCjm...A1pump](https://solscan.io/token/GvUCjmWSXA5hrTh9smmNA1AU55YCtP9mDLQcrKA1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Pumpooor](https://dexscreener.com/solana/3vlpiebr9s31udgbqutz3hetzt5yauk2225iy54npghl) | SOL | [H76u9j...vKpump](https://solscan.io/token/H76u9jTTbMtEF5JGmqXM2wW6xqMXpvTdVyer4RvKpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| SOLCAT | SOL | [HmJDgk...8jpump](https://solscan.io/token/HmJDgky11u77hpBss6D8sjNpYPD5B6fWgSVDj58jpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Shrek](https://dexscreener.com/solana/2mv3euxqb3y5tojt3nbea9noxmb55vcxxjgdqub7d4uo) | SOL | [bykrhk...e8pump](https://solscan.io/token/bykrhkExmjWco2mFxKGX3XPmPVaZB9JJp9MkRe8pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 2 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 6 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
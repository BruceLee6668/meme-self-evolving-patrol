# 自我进化轮巡

**本轮时间 UTC：** 2026-06-29T22:51:27Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 141 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 313 |
| 合并后Token | 141 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 7 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 0 |
| 多池Token | 6 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 6 |
| Liquid层 | 6 |
| Mature层 | 5 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 406，刷新时间 2026-06-29T02:42:54Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 2 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 主观察 | Score 84; Tier Liquid; LP $1.01M; Vol24H $550.8K; 24H +6.02%; V/LP 0.54x; 池数 1; 分项 L18/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 83; Tier Early; LP $565.5K; Vol24H $799.2K; 24H +2.12%; V/LP 1.41x; 池数 1; 分项 L16/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 70; Tier Early; LP $235.3K; Vol24H $154.2K; 24H +1.60%; V/LP 0.66x; 池数 3; 分项 L13/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 69; Tier Micro; LP $72.7K; Vol24H $496.6K; 24H -9.60%; V/LP 6.83x; 池数 1; 分项 L8/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 次观察 | Score 68; Tier Liquid; LP $1.43M; Vol24H $12.83M; 24H +7.61%; V/LP 8.95x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 次观察 | Score 66; Tier Early; LP $514.1K; Vol24H $1.31M; 24H +52.54%; V/LP 2.55x; 池数 6; 分项 L16/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ADA](https://dexscreener.com/solana/rsyt64cs33cvfqxq2kvny13a7isrkke3dbmuc8t9pl8) | SOL | [skDGuS...Ufpump](https://solscan.io/token/skDGuSDyKYGbYTWnMCNcPeDd4vHUxAsMNVVxxUfpump) | 次观察 | Score 66; Tier Micro; LP $83.7K; Vol24H $184.3K; 24H -6.72%; V/LP 2.20x; 池数 2; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 次观察 | Score 66; Tier Micro; LP $94.2K; Vol24H $154.9K; 24H +13.43%; V/LP 1.64x; 池数 2; 分项 L9/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 66; Tier Early; LP $407.5K; Vol24H $2.53M; 24H +59.42%; V/LP 6.21x; 池数 1; 分项 L15/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ANSEM | BSC | [0xab9d...0f026f](https://bscscan.com/token/0xab9d1148f111c6f6516174143ea7244d000f026f) | PVP风险池 | Score 51; Tier Liquid; LP $2.17M; Vol24H $189.44M; 24H +22.42%; V/LP 87.19x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 主观察 | Score 84; Tier Liquid; LP $1.01M; Vol24H $545.0K; 24H +4.82%; V/LP 0.54x; 池数 1; 分项 L18/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 83; Tier Early; LP $565.9K; Vol24H $785.4K; 24H +4.41%; V/LP 1.39x; 池数 1; 分项 L16/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [MANIFEST](https://dexscreener.com/solana/2dvbu5h8jcd37gaxajuz4t77hsjjw22lldutzk7gsa43) | SOL | [BCdwQB...ERpump](https://solscan.io/token/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | 主观察 | Score 78; Tier Liquid; LP $914.2K; Vol24H $1.90M; 24H +12.35%; V/LP 2.08x; 池数 1; 分项 L18/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 74; Tier Early; LP $377.4K; Vol24H $2.42M; 24H -17.71%; V/LP 6.41x; 池数 6; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 74; Tier Micro; LP $67.7K; Vol24H $507.0K; 24H -6.85%; V/LP 7.48x; 池数 1; 分项 L8/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 69; Tier Early; LP $227.6K; Vol24H $136.0K; 24H +0.19%; V/LP 0.60x; 池数 1; 分项 L12/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 次观察 | Score 66; Tier Early; LP $513.9K; Vol24H $1.31M; 24H +50.99%; V/LP 2.55x; 池数 5; 分项 L16/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 次观察 | Score 66; Tier Micro; LP $93.6K; Vol24H $155.3K; 24H +14.93%; V/LP 1.66x; 池数 2; 分项 L9/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 65; Tier Liquid; LP $1.39M; Vol24H $35.3K; 24H +10.00%; V/LP 0.03x; 池数 1; 分项 L20/V4/B17/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 64; Tier Early; LP $300.9K; Vol24H $203.7K; 24H +22.63%; V/LP 0.68x; 池数 1; 分项 L14/V9/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | PVP风险池 | Score 30; Tier Liquid; LP $1.61M; Vol24H $52.58M; 24H +33.78%; V/LP 32.69x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FLORK | BSC | [0x09db...134444](https://bscscan.com/token/0x09db6885551ab1d4a9fa484d9b4b9fe899134444) | PVP风险池 | Score 30; Tier Early; LP $167.4K; Vol24H $5.90M; 24H +730.52%; V/LP 35.23x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TATE | SOL | [CuGJf6...sGpump](https://solscan.io/token/CuGJf6cfDfMh4UxVgNJ5KFQ6v8Wv3qrqop6cFKsGpump) | PVP风险池 | Score 28; Tier Micro; LP $90.2K; Vol24H $2.55M; 24H +107.25%; V/LP 28.23x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Speedrun](https://dexscreener.com/solana/c93imb1xhf9a2kzgaa5kzakhkm3xsrgf9pzhhkhgqiny) | SOL | [PDqSeP...MCpump](https://solscan.io/token/PDqSePtjwXYaruFX7hdujV9wf4X7Z4fu5d2iVMCpump) | PVP风险池 | Score 24; Tier Micro; LP $50.2K; Vol24H $2.38M; 24H +1119.00%; V/LP 47.33x; 池数 1; 分项 L6/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLCAT](https://dexscreener.com/solana/hh6ajghbw5err8rj9kc51zazvrchjvvranc2w8sy6g7j) | SOL | [CkAuhM...tspump](https://solscan.io/token/CkAuhMagnem2iukGwApsfw1ypWETWDdKFD1Xrrtspump) | PVP风险池 | Score 23; Tier Micro; LP $85.4K; Vol24H $5.04M; 24H +1302.00%; V/LP 59.06x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；市值超过早期Alpha主榜上限 | Score 30; Tier Liquid; LP $1.61M; Vol24H $52.58M; 24H +33.78%; V/LP 32.69x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| FLORK | BSC | [0x09db...134444](https://bscscan.com/token/0x09db6885551ab1d4a9fa484d9b4b9fe899134444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $167.4K; Vol24H $5.90M; 24H +730.52%; V/LP 35.23x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TATE | SOL | [CuGJf6...sGpump](https://solscan.io/token/CuGJf6cfDfMh4UxVgNJ5KFQ6v8Wv3qrqop6cFKsGpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $90.2K; Vol24H $2.55M; 24H +107.25%; V/LP 28.23x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Speedrun](https://dexscreener.com/solana/c93imb1xhf9a2kzgaa5kzakhkm3xsrgf9pzhhkhgqiny) | SOL | [PDqSeP...MCpump](https://solscan.io/token/PDqSePtjwXYaruFX7hdujV9wf4X7Z4fu5d2iVMCpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Micro; LP $50.2K; Vol24H $2.38M; 24H +1119.00%; V/LP 47.33x; 池数 1; 分项 L6/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BULLCAT](https://dexscreener.com/solana/hh6ajghbw5err8rj9kc51zazvrchjvvranc2w8sy6g7j) | SOL | [CkAuhM...tspump](https://solscan.io/token/CkAuhMagnem2iukGwApsfw1ypWETWDdKFD1Xrrtspump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 23; Tier Micro; LP $85.4K; Vol24H $5.04M; 24H +1302.00%; V/LP 59.06x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| 🐂🀄️ | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $41.9K; Vol24H $2.46M; 24H -74.67%; V/LP 58.75x; 池数 1; 分项 L6/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| ANSEMHOUSE | SOL | [5RNsaR...pjpump](https://solscan.io/token/5RNsaRw3vDsZ9T1cHgNfGWGcK84GoAYRJcpW5Jpjpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $6.7K; Vol24H $2.55M; 24H -98.01%; V/LP 379.23x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [MMGA](https://dexscreener.com/solana/ekpvebbqhg8rlpar5udxgttbncpvyzn5wwrflkrlv8cu) | SOL | [6eDqAx...dUpump](https://solscan.io/token/6eDqAxts3AZ3cMBPQd3c4D1jzjX1uAQ4Lo53d6dUpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 1; Tier Micro; LP $51.3K; Vol24H $2.88M; 24H +1058.00%; V/LP 56.16x; 池数 11; 分项 L7/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 76; Tier Mature; LP $66.33M; Vol24H $161.00M; 24H -2.95%; V/LP 2.43x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| COAI | BSC | [0x0a8d...836ea5](https://bscscan.com/token/0x0a8d6c86e1bce73fe4d0bd531e1a567306836ea5) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.80M; Vol24H $8.55M; 24H +4.36%; V/LP 4.76x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $19.89M; Vol24H $111.3K; 24H +6.86%; V/LP 0.01x; 池数 1; 分项 L20/V7/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $155.25M; Vol24H $281.74M; 24H -1.97%; V/LP 1.81x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Mature; LP $7.86M; Vol24H $10.26M; 24H -9.58%; V/LP 1.30x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| VELVET | BSC | [0x8b19...8c1488](https://bscscan.com/token/0x8b194370825e37b33373e74a41009161808c1488) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 67; Tier Mature; LP $6.99M; Vol24H $1.42M; 24H -9.66%; V/LP 0.20x; 池数 1; 分项 L20/V15/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $3.70M; Vol24H $19.09M; 24H +42.15%; V/LP 5.15x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [MANIFEST](https://dexscreener.com/solana/2dvbu5h8jcd37gaxajuz4t77hsjjw22lldutzk7gsa43) | SOL | [BCdwQB...ERpump](https://solscan.io/token/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PFP](https://dexscreener.com/solana/gdfcd7l8x1giudfz1wthnheb352k3ni37rswtjgmglpt) | SOL | [5TfqNK...TBpump](https://solscan.io/token/5TfqNKZbn9AnNtzq8bbkyhKgcPGTfNDc9wNzFrTBpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| MAME | BSC | [0xe92f...c42302](https://bscscan.com/token/0xe92f7fe3eaf61df28b7b75f3faab199333c42302) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [MANIFEST](https://dexscreener.com/solana/2dvbu5h8jcd37gaxajuz4t77hsjjw22lldutzk7gsa43) | SOL | [BCdwQB...ERpump](https://solscan.io/token/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 6 / Liquid 6 / Mature 5 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 330} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
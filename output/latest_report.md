# 自我进化轮巡

**本轮时间 UTC：** 2026-10-13T09:59:46Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 235 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 9 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 0 |
| 多池Token | 7 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 1 |
| 需要链上确认 | 20 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1888，刷新时间 2026-10-12T03:31:42Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 3 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 79; Tier Liquid; LP $836.7K; Vol24H $3.61M; 24H -10.33%; V/LP 4.32x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 76; Tier Liquid; LP $1.24M; Vol24H $2.19M; 24H -9.48%; V/LP 1.77x; 池数 1; 分项 L19/V16/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 73; Tier Early; LP $596.3K; Vol24H $2.93M; 24H -54.22%; V/LP 4.92x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| swordcat | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | 次观察 | Score 73; Tier Early; LP $215.2K; Vol24H $645.6K; 24H +6.41%; V/LP 3.00x; 池数 1; 分项 L12/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 69; Tier Early; LP $585.0K; Vol24H $212.4K; 24H -13.33%; V/LP 0.36x; 池数 1; 分项 L16/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 次观察 | Score 69; Tier Early; LP $220.2K; Vol24H $922.3K; 24H -15.17%; V/LP 4.19x; 池数 1; 分项 L12/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CRAWL](https://dexscreener.com/solana/52by9szjr4qenrcgaddfunefw7o1cqfdfs7ve12oe3je) | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | 次观察 | Score 68; Tier Micro; LP $75.3K; Vol24H $360.4K; 24H -16.19%; V/LP 4.78x; 池数 1; 分项 L8/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 68; Tier Early; LP $258.7K; Vol24H $1.55M; 24H -49.82%; V/LP 5.99x; 池数 1; 分项 L13/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 67; Tier Early; LP $355.0K; Vol24H $204.3K; 24H -8.42%; V/LP 0.58x; 池数 1; 分项 L14/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Normie](https://dexscreener.com/solana/4poweghzar3qd2hpbkrkyq8bb3dy7vanszhbq3rsxryh) | SOL | [DzMwAr...LJpump](https://solscan.io/token/DzMwArmdzPqcqgvyqAmTxy79XdA9NwK9mMteqWLJpump) | 次观察 | Score 66; Tier Micro; LP $80.9K; Vol24H $555.3K; 24H +0.68%; V/LP 6.87x; 池数 1; 分项 L8/V12/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 82; Tier Liquid; LP $3.93M; Vol24H $1.93M; 24H -1.82%; V/LP 0.49x; 池数 1; 分项 L20/V16/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 79; Tier Liquid; LP $949.4K; Vol24H $3.24M; 24H -19.40%; V/LP 3.42x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 76; Tier Liquid; LP $1.23M; Vol24H $2.06M; 24H -9.39%; V/LP 1.68x; 池数 1; 分项 L19/V16/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 75; Tier Liquid; LP $1.12M; Vol24H $110.5K; 24H -2.03%; V/LP 0.10x; 池数 1; 分项 L19/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pumpoween](https://dexscreener.com/solana/8nvfb1unnk9adtl5hoof8hahf2rt4glpwx9cteadikhg) | SOL | [5Gefef...vFpump](https://solscan.io/token/5GefefPX1mDs6ZJB1apYmz6fCTCiNJpHturZ9bvFpump) | 次观察 | Score 74; Tier Micro; LP $88.4K; Vol24H $111.1K; 24H +2.63%; V/LP 1.26x; 池数 4; 分项 L9/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [swordcat](https://dexscreener.com/solana/2yagc2iyzt44b5zn5tvk59apban51xgekznqapf2pgn1) | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | 次观察 | Score 72; Tier Early; LP $335.0K; Vol24H $209.9K; 24H -1.04%; V/LP 0.63x; 池数 6; 分项 L14/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 72; Tier Early; LP $415.2K; Vol24H $762.2K; 24H -14.95%; V/LP 1.84x; 池数 1; 分项 L15/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [AODF](https://dexscreener.com/solana/gn6fdn3pcxpd3ccznq37edhiftxzgzxybatqasyk6yf1) | SOL | [2KbRLs...hjpump](https://solscan.io/token/2KbRLsBVEXdF3YJm35yjvCHr8gC5o1wzRzQpbDhjpump) | 次观察 | Score 69; Tier Early; LP $579.9K; Vol24H $178.4K; 24H +10.13%; V/LP 0.31x; 池数 1; 分项 L16/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 69; Tier Early; LP $584.2K; Vol24H $212.4K; 24H -16.58%; V/LP 0.36x; 池数 1; 分项 L16/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 次观察 | Score 67; Tier Early; LP $259.9K; Vol24H $1.13M; 24H -40.95%; V/LP 4.36x; 池数 1; 分项 L13/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 66; Tier Early; LP $559.7K; Vol24H $1.70M; 24H -43.54%; V/LP 3.03x; 池数 1; 分项 L16/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOMO](https://dexscreener.com/solana/5a7qurjlart146jajjype5nh6vlyfpn2qrhuslqbsczy) | SOL | [9XKzy4...hEpump](https://solscan.io/token/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump) | 次观察 | Score 65; Tier Early; LP $107.4K; Vol24H $80.0K; 24H -20.82%; V/LP 0.74x; 池数 2; 分项 L9/V6/B17/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | PVP风险池 | Score 49; Tier Liquid; LP $827.1K; Vol24H $28.78M; 24H -24.30%; V/LP 34.80x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | PVP风险池 | Score 35; Tier Micro; LP $99.2K; Vol24H $2.04M; 24H -36.44%; V/LP 20.58x; 池数 2; 分项 L9/V16/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HIRE](https://dexscreener.com/solana/2u5kdozdrdgyzygrnbtdbejglyeert1fkerqmypbv85p) | SOL | [98AG3z...o1pump](https://solscan.io/token/98AG3zJUawbvDnpgbDhmxpMKva43vtgPLLPSXqo1pump) | PVP风险池 | Score 27; Tier Micro; LP $79.4K; Vol24H $3.30M; 24H +1269.00%; V/LP 41.60x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $827.1K; Vol24H $28.78M; 24H -24.30%; V/LP 34.80x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| DOPE | SOL | [33jENU...CNpump](https://solscan.io/token/33jENUQnjoitkMFpvNJcSHyLAHFWJuHwT6E3E8CNpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $99.2K; Vol24H $2.04M; 24H -36.44%; V/LP 20.58x; 池数 2; 分项 L9/V16/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HIRE](https://dexscreener.com/solana/2u5kdozdrdgyzygrnbtdbejglyeert1fkerqmypbv85p) | SOL | [98AG3z...o1pump](https://solscan.io/token/98AG3zJUawbvDnpgbDhmxpMKva43vtgPLLPSXqo1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $79.4K; Vol24H $3.30M; 24H +1269.00%; V/LP 41.60x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MarsX](https://dexscreener.com/solana/9dsiuydk5efrclk6veywy95nn3jjgbdwnijuacf1pxua) | SOL | [Fak3rJ...2rpump](https://solscan.io/token/Fak3rJEBfR4Vb8DoFpecf6yoxbkkr1gGUH5tdj2rpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $61.7K; Vol24H $2.12M; 24H +730.00%; V/LP 34.33x; 池数 1; 分项 L7/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Solamians | SOL | [8ZP5Cz...Lxpump](https://solscan.io/token/8ZP5CzbPL1fmP8dn1GEmLd8xw1JdudUF5Dk7EpLxpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $33.6K; Vol24H $988.9K; 24H -70.78%; V/LP 29.41x; 池数 1; 分项 L5/V14/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Bear](https://dexscreener.com/solana/cvwvn3tn4aoxkhptlk5enhnynxnhcntq2vmsx35xn1en) | SOL | [49PU6E...RGpump](https://solscan.io/token/49PU6ENTpYc3zkhgCruzCSBzgVAdix5muP2oVzRGpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $14.4K; Vol24H $687.8K; 24H -29.44%; V/LP 47.91x; 池数 5; 分项 L1/V13/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| FIGHT | SOL | [A8JUiZ...DZpump](https://solscan.io/token/A8JUiZLzjGAsKxE74evdspHcuW4hvhPbvryDhaDZpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $3.6K; Vol24H $1.27M; 24H -98.65%; V/LP 350.82x; 池数 1; 分项 L0/V14/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [DADDY](https://dexscreener.com/solana/6wmipykabxgqgqajmnvcqfwyuij1znojn12lpxnzakyd) | SOL | [hnMDBV...RUpump](https://solscan.io/token/hnMDBVtBoFuoE4fq3FU3d1d4MTgXdLayE3wQhRUpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $38.5K; Vol24H $613.7K; 24H +202.00%; V/LP 15.94x; 池数 2; 分项 L5/V12/B0/Buy3/Risk-53 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 76; Tier Liquid; LP $2.24M; Vol24H $272.6K; 24H -6.35%; V/LP 0.12x; 池数 1; 分项 L20/V10/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.85M; Vol24H $7.16M; 24H -11.54%; V/LP 1.86x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.23M; Vol24H $6.69M; 24H +0.60%; V/LP 5.45x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 72; Tier Liquid; LP $2.47M; Vol24H $1.69M; 24H +2.80%; V/LP 0.68x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $57.14M; Vol24H $3.04M; 24H -0.94%; V/LP 0.05x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Pumpoween](https://dexscreener.com/solana/8nvfb1unnk9adtl5hoof8hahf2rt4glpwx9cteadikhg) | SOL | [5Gefef...vFpump](https://solscan.io/token/5GefefPX1mDs6ZJB1apYmz6fCTCiNJpHturZ9bvFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [swordcat](https://dexscreener.com/solana/2yagc2iyzt44b5zn5tvk59apban51xgekznqapf2pgn1) | SOL | [5tCju6...SFpump](https://solscan.io/token/5tCju6YNxHq5zrA6tGndr6F7TK42mpUFmeE31cSFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [AODF](https://dexscreener.com/solana/gn6fdn3pcxpd3ccznq37edhiftxzgzxybatqasyk6yf1) | SOL | [2KbRLs...hjpump](https://solscan.io/token/2KbRLsBVEXdF3YJm35yjvCHr8gC5o1wzRzQpbDhjpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CLAUDIA](https://dexscreener.com/solana/fe7bpdycs74gqicuf14hwgumtopkv1d9mdyvx5btohfr) | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 9 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
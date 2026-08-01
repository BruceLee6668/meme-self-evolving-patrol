# 自我进化轮巡

**本轮时间 UTC：** 2026-08-01T22:49:00Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 138 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 241 |
| 合并后Token | 138 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 6 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 5 |
| Liquid层 | 10 |
| Mature层 | 3 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 782，刷新时间 2026-07-27T02:07:24Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 0 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 80; Tier Early; LP $444.8K; Vol24H $1.91M; 24H -9.63%; V/LP 4.30x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 66; Tier Liquid; LP $1.45M; Vol24H $2.6K; 24H +0.91%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 次观察 | Score 65; Tier Early; LP $684.8K; Vol24H $6.57M; 24H +7.37%; V/LP 9.59x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LUMENA | SOL | [2gYhGa...7ZUory](https://solscan.io/token/2gYhGaFMBiPC2bBibG7yKZk94uJw2fcq6DtpYP7ZUory) | 次观察 | Score 65; Tier Early; LP $157.8K; Vol24H $285.7K; 24H +62.13%; V/LP 1.81x; 池数 1; 分项 L11/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UNTIE](https://dexscreener.com/solana/6qagmfvtvurfawr7z4p4b5puiawj9zzdrbjh3fgxds3d) | SOL | [euXT5w...DKpump](https://solscan.io/token/euXT5wMLfGs1zu2zfgeTUSXhjZNuMMiUZLsLsDKpump) | PVP风险池 | Score 37; Tier Early; LP $122.3K; Vol24H $4.41M; 24H +35.27%; V/LP 36.07x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | PVP风险池 | Score 32; Tier Early; LP $244.8K; Vol24H $27.47M; 24H +8234.99%; V/LP 112.18x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CONTRA | SOL | [EV169n...RQGFg2](https://solscan.io/token/EV169nnxWHQGvDFiz999BUt8XDpcRLmwqkciytRQGFg2) | PVP风险池 | Score 30; Tier Micro; LP $27.8K; Vol24H $4.58M; 24H +12.27%; V/LP 164.79x; 池数 1; 分项 L4/V17/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | PVP风险池 | Score 29; Tier Liquid; LP $1.17M; Vol24H $30.60M; 24H +46.52%; V/LP 26.20x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [STOCKERS](https://dexscreener.com/solana/4zcviz4pe9hy6vlg3fdq2gpug59gkpejkpe69nuc7b3f) | SOL | [CeyZtF...Qppump](https://solscan.io/token/CeyZtFUiYP5oxCZ99urwHMvdCW67cY2yALknfrQppump) | PVP风险池 | Score 20; Tier Micro; LP $54.2K; Vol24H $1.96M; 24H +1668.00%; V/LP 36.20x; 池数 2; 分项 L7/V16/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DAVID](https://dexscreener.com/solana/5gnm6anmf9cfvhiswrklusmtqjxvmex1klvno9bbqzok) | SOL | [8wtdds...6Ppump](https://solscan.io/token/8wtdds5LPt7nu4jKifGpcxysF5AvJ1xCVti2rQ6Ppump) | PVP风险池 | Score 17; Tier Micro; LP $15.0K; Vol24H $1.58M; 24H +25.75%; V/LP 105.26x; 池数 6; 分项 L2/V15/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 80; Tier Early; LP $457.4K; Vol24H $1.82M; 24H -13.03%; V/LP 3.99x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 次观察 | Score 69; Tier Liquid; LP $1.20M; Vol24H $14.59; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 66; Tier Liquid; LP $1.45M; Vol24H $2.6K; 24H +0.91%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LUMENA | SOL | [2gYhGa...7ZUory](https://solscan.io/token/2gYhGaFMBiPC2bBibG7yKZk94uJw2fcq6DtpYP7ZUory) | 次观察 | Score 65; Tier Early; LP $166.1K; Vol24H $285.8K; 24H +73.63%; V/LP 1.72x; 池数 1; 分项 L11/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UNTIE](https://dexscreener.com/solana/6qagmfvtvurfawr7z4p4b5puiawj9zzdrbjh3fgxds3d) | SOL | [euXT5w...DKpump](https://solscan.io/token/euXT5wMLfGs1zu2zfgeTUSXhjZNuMMiUZLsLsDKpump) | PVP风险池 | Score 51; Tier Early; LP $109.3K; Vol24H $4.50M; 24H +4.60%; V/LP 41.16x; 池数 1; 分项 L10/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BRICK](https://dexscreener.com/solana/dbrvbrlni7dk9vqqffn9nel43lbadf5ejydjnsilqwaj) | SOL | [8Byg9w...WQpump](https://solscan.io/token/8Byg9wi43TNzgJpYta6UXxPz3LPe8v6ZwvmWWoWQpump) | PVP风险池 | Score 41; Tier Micro; LP $52.8K; Vol24H $1.66M; 24H +4.82%; V/LP 31.36x; 池数 2; 分项 L7/V15/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | PVP风险池 | Score 32; Tier Early; LP $254.6K; Vol24H $27.56M; 24H +8900.99%; V/LP 108.27x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | PVP风险池 | Score 29; Tier Liquid; LP $1.17M; Vol24H $30.81M; 24H +45.67%; V/LP 26.38x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CONTRA | SOL | [EV169n...RQGFg2](https://solscan.io/token/EV169nnxWHQGvDFiz999BUt8XDpcRLmwqkciytRQGFg2) | PVP风险池 | Score 20; Tier Micro; LP $22.1K; Vol24H $4.49M; 24H +25.88%; V/LP 203.34x; 池数 1; 分项 L3/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [STOCKERS](https://dexscreener.com/solana/4zcviz4pe9hy6vlg3fdq2gpug59gkpejkpe69nuc7b3f) | SOL | [CeyZtF...Qppump](https://solscan.io/token/CeyZtFUiYP5oxCZ99urwHMvdCW67cY2yALknfrQppump) | PVP风险池 | Score 20; Tier Micro; LP $62.0K; Vol24H $2.06M; 24H +2178.00%; V/LP 33.26x; 池数 2; 分项 L7/V16/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CallDog](https://dexscreener.com/solana/b2kmkdo5cfbzpgava6aqcd9bnqvaplxcusuyfs8coilt) | SOL | [8Jqs2L...Mcpump](https://solscan.io/token/8Jqs2Le4HsNUxfEWy44vQaDWrR3gqR3cvSJigDMcpump) | PVP风险池 | Score 12; Tier Micro; LP $31.4K; Vol24H $1.70M; 24H +457.00%; V/LP 54.09x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [:p](https://dexscreener.com/solana/c1v6yumqijuyffeja6n96gdakpgvtcmzkvezotqmzha9) | SOL | [8izw4X...1Apump](https://solscan.io/token/8izw4XNQk4RuJtH88wc1EKQ4RLqGiUqKXZUTS51Apump) | PVP风险池 | Score 12; Tier Micro; LP $35.6K; Vol24H $1.59M; 24H +530.00%; V/LP 44.68x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 79; Tier Mature; LP $36.70M; Vol24H $41.94M; 24H -0.22%; V/LP 1.14x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 72; Tier Liquid; LP $1.99M; Vol24H $1.38M; 24H +8.89%; V/LP 0.69x; 池数 2; 分项 L20/V15/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 69; Tier Liquid; LP $1.35M; Vol24H $5.75M; 24H -8.86%; V/LP 4.26x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [UNTIE](https://dexscreener.com/solana/6qagmfvtvurfawr7z4p4b5puiawj9zzdrbjh3fgxds3d) | SOL | [euXT5w...DKpump](https://solscan.io/token/euXT5wMLfGs1zu2zfgeTUSXhjZNuMMiUZLsLsDKpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Early; LP $109.3K; Vol24H $4.50M; 24H +4.60%; V/LP 41.16x; 池数 1; 分项 L10/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BRICK](https://dexscreener.com/solana/dbrvbrlni7dk9vqqffn9nel43lbadf5ejydjnsilqwaj) | SOL | [8Byg9w...WQpump](https://solscan.io/token/8Byg9wi43TNzgJpYta6UXxPz3LPe8v6ZwvmWWoWQpump) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 41; Tier Micro; LP $52.8K; Vol24H $1.66M; 24H +4.82%; V/LP 31.36x; 池数 2; 分项 L7/V15/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $254.6K; Vol24H $27.56M; 24H +8900.99%; V/LP 108.27x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限 | Score 29; Tier Liquid; LP $1.17M; Vol24H $30.81M; 24H +45.67%; V/LP 26.38x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| CONTRA | SOL | [EV169n...RQGFg2](https://solscan.io/token/EV169nnxWHQGvDFiz999BUt8XDpcRLmwqkciytRQGFg2) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 20; Tier Micro; LP $22.1K; Vol24H $4.49M; 24H +25.88%; V/LP 203.34x; 池数 1; 分项 L3/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [STOCKERS](https://dexscreener.com/solana/4zcviz4pe9hy6vlg3fdq2gpug59gkpejkpe69nuc7b3f) | SOL | [CeyZtF...Qppump](https://solscan.io/token/CeyZtFUiYP5oxCZ99urwHMvdCW67cY2yALknfrQppump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 20; Tier Micro; LP $62.0K; Vol24H $2.06M; 24H +2178.00%; V/LP 33.26x; 池数 2; 分项 L7/V16/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [CallDog](https://dexscreener.com/solana/b2kmkdo5cfbzpgava6aqcd9bnqvaplxcusuyfs8coilt) | SOL | [8Jqs2L...Mcpump](https://solscan.io/token/8Jqs2Le4HsNUxfEWy44vQaDWrR3gqR3cvSJigDMcpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $31.4K; Vol24H $1.70M; 24H +457.00%; V/LP 54.09x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [:p](https://dexscreener.com/solana/c1v6yumqijuyffeja6n96gdakpgvtcmzkvezotqmzha9) | SOL | [8izw4X...1Apump](https://solscan.io/token/8izw4XNQk4RuJtH88wc1EKQ4RLqGiUqKXZUTS51Apump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $35.6K; Vol24H $1.59M; 24H +530.00%; V/LP 44.68x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $36.70M; Vol24H $41.94M; 24H -0.22%; V/LP 1.14x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 72; Tier Liquid; LP $1.99M; Vol24H $1.38M; 24H +8.89%; V/LP 0.69x; 池数 2; 分项 L20/V15/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.35M; Vol24H $5.75M; 24H -8.86%; V/LP 4.26x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；成熟大池 | Score 68; Tier Mature; LP $10.18M; Vol24H $1.21M; 24H -5.18%; V/LP 0.12x; 池数 5; 分项 L20/V14/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；成熟大池 | Score 61; Tier Mature; LP $19.16M; Vol24H $112.5K; 24H -0.41%; V/LP 0.01x; 池数 1; 分项 L20/V7/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 61; Tier Liquid; LP $3.11M; Vol24H $40.50M; 24H -0.97%; V/LP 13.02x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-30 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 59; Tier Liquid; LP $1.13M; Vol24H $6.58M; 24H +32.62%; V/LP 5.80x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| LUMENA | SOL | [2gYhGa...7ZUory](https://solscan.io/token/2gYhGaFMBiPC2bBibG7yKZk94uJw2fcq6DtpYP7ZUory) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UNTIE](https://dexscreener.com/solana/6qagmfvtvurfawr7z4p4b5puiawj9zzdrbjh3fgxds3d) | SOL | [euXT5w...DKpump](https://solscan.io/token/euXT5wMLfGs1zu2zfgeTUSXhjZNuMMiUZLsLsDKpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BRICK](https://dexscreener.com/solana/dbrvbrlni7dk9vqqffn9nel43lbadf5ejydjnsilqwaj) | SOL | [8Byg9w...WQpump](https://solscan.io/token/8Byg9wi43TNzgJpYta6UXxPz3LPe8v6ZwvmWWoWQpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CONTRA | SOL | [EV169n...RQGFg2](https://solscan.io/token/EV169nnxWHQGvDFiz999BUt8XDpcRLmwqkciytRQGFg2) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [STOCKERS](https://dexscreener.com/solana/4zcviz4pe9hy6vlg3fdq2gpug59gkpejkpe69nuc7b3f) | SOL | [CeyZtF...Qppump](https://solscan.io/token/CeyZtFUiYP5oxCZ99urwHMvdCW67cY2yALknfrQppump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 5 / Liquid 10 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
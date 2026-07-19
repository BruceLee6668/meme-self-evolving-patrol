# 自我进化轮巡

**本轮时间 UTC：** 2026-07-19T17:53:58Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 229 |
| 合并后Token | 95 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 7 |
| 多池Token | 6 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 13 |
| Liquid层 | 6 |
| Mature层 | 0 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 主观察 | Score 79; Tier Liquid; LP $949.8K; Vol24H $3.26M; 24H -20.34%; V/LP 3.43x; 池数 2; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ZBT | BSC | [0xfab9...777777](https://bscscan.com/token/0xfab99fcf605fd8f4593edb70a43ba56542777777) | 主观察 | Score 79; Tier Early; LP $429.0K; Vol24H $1.52M; 24H -3.38%; V/LP 3.55x; 池数 1; 分项 L15/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 74; Tier Early; LP $296.5K; Vol24H $1.99M; 24H +14.13%; V/LP 6.70x; 池数 1; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 71; Tier Early; LP $310.6K; Vol24H $138.7K; 24H +16.32%; V/LP 0.45x; 池数 1; 分项 L14/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 54; Tier Liquid; LP $872.3K; Vol24H $104.58M; 24H -1.15%; V/LP 119.89x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 41; Tier Early; LP $295.1K; Vol24H $11.66M; 24H -46.87%; V/LP 39.50x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 38; Tier Liquid; LP $1.06M; Vol24H $83.10M; 24H +8.19%; V/LP 78.29x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOLdiers](https://dexscreener.com/solana/b4jm2z5daqncjtsfm4f8v5pc88ka8fk3oycswefsq9br) | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 38; Tier Early; LP $152.0K; Vol24H $3.42M; 24H +26.77%; V/LP 22.47x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | PVP风险池 | Score 37; Tier Early; LP $131.4K; Vol24H $3.92M; 24H -71.05%; V/LP 29.85x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | PVP风险池 | Score 27; Tier Micro; LP $81.7K; Vol24H $4.28M; 24H +3058.02%; V/LP 52.33x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 75; Tier Early; LP $311.8K; Vol24H $139.6K; 24H +17.67%; V/LP 0.45x; 池数 1; 分项 L14/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 74; Tier Early; LP $294.4K; Vol24H $1.98M; 24H +15.99%; V/LP 6.73x; 池数 1; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ZBT | BSC | [0xfab9...777777](https://bscscan.com/token/0xfab99fcf605fd8f4593edb70a43ba56542777777) | 次观察 | Score 74; Tier Early; LP $427.3K; Vol24H $1.44M; 24H -8.53%; V/LP 3.36x; 池数 1; 分项 L15/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 70; Tier Liquid; LP $965.5K; Vol24H $3.25M; 24H -30.21%; V/LP 3.37x; 池数 2; 分项 L18/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 54; Tier Liquid; LP $831.9K; Vol24H $101.23M; 24H -0.36%; V/LP 121.69x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 40; Tier Early; LP $277.5K; Vol24H $10.72M; 24H -57.22%; V/LP 38.62x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 38; Tier Liquid; LP $1.09M; Vol24H $85.52M; 24H +15.72%; V/LP 78.36x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | PVP风险池 | Score 37; Tier Early; LP $131.8K; Vol24H $3.54M; 24H -68.90%; V/LP 26.83x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Benny | SOL | [2mGS6W...Lqpump](https://solscan.io/token/2mGS6WWuDy1xNQuCo7irzH3iT4SsSeSaA3oJ5NLqpump) | PVP风险池 | Score 33; Tier Micro; LP $16.6K; Vol24H $4.90M; 24H +6.59%; V/LP 295.25x; 池数 1; 分项 L2/V17/B22/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [屎币](https://dexscreener.com/bsc/0xce8c39f18ed145476d4101675e87dfae616b93ea) | BSC | [0xE14B...354444](https://bscscan.com/token/0xE14B77ce30250CF94182b7019020fA00e7354444) | PVP风险池 | Score 29; Tier Early; LP $121.6K; Vol24H $6.00M; 24H +2430.00%; V/LP 49.34x; 池数 29; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | PVP风险池 | Score 29; Tier Early; LP $114.8K; Vol24H $5.03M; 24H +5997.20%; V/LP 43.85x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 12; Tier Early; LP $119.5K; Vol24H $7.10M; 24H +81.70%; V/LP 59.40x; 池数 1; 分项 L10/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 73; Tier Liquid; LP $1.92M; Vol24H $2.33M; 24H +1.42%; V/LP 1.21x; 池数 2; 分项 L20/V16/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 69; Tier Liquid; LP $1.42M; Vol24H $8.18M; 24H -20.14%; V/LP 5.77x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 低优先观察 | Score 62; Tier Early; LP $134.0K; Vol24H $652.3K; 24H -25.07%; V/LP 4.87x; 池数 1; 分项 L10/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 54; Tier Liquid; LP $831.9K; Vol24H $101.23M; 24H -0.36%; V/LP 121.69x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Early; LP $277.5K; Vol24H $10.72M; 24H -57.22%; V/LP 38.62x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 38; Tier Liquid; LP $1.09M; Vol24H $85.52M; 24H +15.72%; V/LP 78.36x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $131.8K; Vol24H $3.54M; 24H -68.90%; V/LP 26.83x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Benny | SOL | [2mGS6W...Lqpump](https://solscan.io/token/2mGS6WWuDy1xNQuCo7irzH3iT4SsSeSaA3oJ5NLqpump) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 33; Tier Micro; LP $16.6K; Vol24H $4.90M; 24H +6.59%; V/LP 295.25x; 池数 1; 分项 L2/V17/B22/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [屎币](https://dexscreener.com/bsc/0xce8c39f18ed145476d4101675e87dfae616b93ea) | BSC | [0xE14B...354444](https://bscscan.com/token/0xE14B77ce30250CF94182b7019020fA00e7354444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $121.6K; Vol24H $6.00M; 24H +2430.00%; V/LP 49.34x; 池数 29; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Agamemnon | SOL | [2cAtqs...rCpump](https://solscan.io/token/2cAtqsRafKS7baN3mvJARhyZiMRdW4fZYNUUWUrCpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $114.8K; Vol24H $5.03M; 24H +5997.20%; V/LP 43.85x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 12; Tier Early; LP $119.5K; Vol24H $7.10M; 24H +81.70%; V/LP 59.40x; 池数 1; 分项 L10/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.92M; Vol24H $2.33M; 24H +1.42%; V/LP 1.21x; 池数 2; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.42M; Vol24H $8.18M; 24H -20.14%; V/LP 5.77x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ZBT | BSC | [0xfab9...777777](https://bscscan.com/token/0xfab99fcf605fd8f4593edb70a43ba56542777777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [WINGIT](https://dexscreener.com/solana/5kc5ssfzhtque628ny3d5z22appt9au16hmx94jexaz5) | SOL | [CVhWiQ...KSpump](https://solscan.io/token/CVhWiQ2SBhpTJ3xAR3ekf3uf8Ns2tNzj3mEtzKSpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Benny | SOL | [2mGS6W...Lqpump](https://solscan.io/token/2mGS6WWuDy1xNQuCo7irzH3iT4SsSeSaA3oJ5NLqpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [屎币](https://dexscreener.com/bsc/0xce8c39f18ed145476d4101675e87dfae616b93ea) | BSC | [0xE14B...354444](https://bscscan.com/token/0xE14B77ce30250CF94182b7019020fA00e7354444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 13 / Liquid 6 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
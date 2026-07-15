# 自我进化轮巡

**本轮时间 UTC：** 2026-07-15T23:54:23Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 126 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 229 |
| 合并后Token | 126 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 6 |
| 多池Token | 4 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 10 |
| Liquid层 | 7 |
| Mature层 | 2 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 1 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 主观察 | Score 84; Tier Liquid; LP $1.18M; Vol24H $114.2K; 24H -1.09%; V/LP 0.10x; 池数 1; 分项 L19/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 主观察 | Score 84; Tier Liquid; LP $1.28M; Vol24H $120.1K; 24H -0.09%; V/LP 0.09x; 池数 1; 分项 L19/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 81; Tier Early; LP $275.2K; Vol24H $1.46M; 24H +10.95%; V/LP 5.31x; 池数 1; 分项 L13/V15/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 主观察 | Score 78; Tier Early; LP $688.0K; Vol24H $4.65M; 24H +12.64%; V/LP 6.76x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 71; Tier Early; LP $276.9K; Vol24H $185.5K; 24H -19.40%; V/LP 0.67x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 次观察 | Score 67; Tier Early; LP $596.4K; Vol24H $2.36M; 24H +28.55%; V/LP 3.96x; 池数 1; 分项 L16/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULLCAT](https://dexscreener.com/solana/huqmpubbdq8w56y6wgd8limbf4zgyxs2aczlzs8mylna) | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | PVP风险池 | Score 44; Tier Micro; LP $84.0K; Vol24H $2.94M; 24H -2.56%; V/LP 34.96x; 池数 2; 分项 L8/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 34; Tier Micro; LP $83.7K; Vol24H $211.36M; 24H +7.49%; V/LP 2523.85x; 池数 1; 分项 L8/V17/B22/Buy8/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 32; Tier Early; LP $137.2K; Vol24H $3.74M; 24H -41.67%; V/LP 27.29x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Flea](https://dexscreener.com/solana/6aau4je3caa3gogza1tonkcuutfrzestwfg5wa3hu8km) | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | PVP风险池 | Score 30; Tier Micro; LP $35.7K; Vol24H $2.36M; 24H +1.00%; V/LP 66.05x; 池数 1; 分项 L5/V16/B22/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 86; Tier Early; LP $267.6K; Vol24H $1.45M; 24H -0.77%; V/LP 5.41x; 池数 1; 分项 L13/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 主观察 | Score 85; Tier Liquid; LP $1.18M; Vol24H $129.2K; 24H -1.45%; V/LP 0.11x; 池数 1; 分项 L19/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 主观察 | Score 84; Tier Liquid; LP $1.27M; Vol24H $120.1K; 24H -0.24%; V/LP 0.09x; 池数 1; 分项 L19/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 主观察 | Score 78; Tier Early; LP $686.3K; Vol24H $4.71M; 24H +12.96%; V/LP 6.86x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 74; Tier Liquid; LP $1.83M; Vol24H $53.2K; 24H +0.25%; V/LP 0.03x; 池数 1; 分项 L20/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 次观察 | Score 67; Tier Early; LP $587.2K; Vol24H $2.34M; 24H +25.47%; V/LP 3.98x; 池数 1; 分项 L16/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | PVP风险池 | Score 39; Tier Micro; LP $74.7K; Vol24H $2.65M; 24H -23.05%; V/LP 35.55x; 池数 2; 分项 L8/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 32; Tier Early; LP $129.9K; Vol24H $3.56M; 24H -51.48%; V/LP 27.40x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | PVP风险池 | Score 30; Tier Early; LP $176.5K; Vol24H $3.53M; 24H +770.00%; V/LP 20.02x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 29; Tier Micro; LP $83.2K; Vol24H $211.36M; 24H +6.47%; V/LP 2539.86x; 池数 1; 分项 L8/V17/B22/Buy3/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | PVP风险池 | Score 29; Tier Early; LP $111.4K; Vol24H $19.31M; 24H +2965.12%; V/LP 173.36x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | PVP风险池 | Score 20; Tier Micro; LP $84.4K; Vol24H $4.78M; 24H -88.86%; V/LP 56.58x; 池数 1; 分项 L9/V17/B0/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Flea](https://dexscreener.com/solana/6aau4je3caa3gogza1tonkcuutfrzestwfg5wa3hu8km) | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | PVP风险池 | Score 8; Tier Micro; LP $38.8K; Vol24H $2.35M; 24H +81.50%; V/LP 60.53x; 池数 1; 分项 L5/V16/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WIFARG](https://dexscreener.com/solana/7owxxha2bnrthhimpk7qcxvzyvsd6rjbqm6jmlctmzmk) | SOL | [CV9dcP...d5pump](https://solscan.io/token/CV9dcP2D9hYtcnNtoHoY4NQEN9fYxfBbQN72wkd5pump) | PVP风险池 | Score 4; Tier Early; LP $121.2K; Vol24H $4.05M; 24H +5043.00%; V/LP 33.41x; 池数 3; 分项 L10/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $52.41M; Vol24H $3.10M; 24H +0.14%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Micro; LP $74.7K; Vol24H $2.65M; 24H -23.05%; V/LP 35.55x; 池数 2; 分项 L8/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 32; Tier Early; LP $129.9K; Vol24H $3.56M; 24H -51.48%; V/LP 27.40x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $176.5K; Vol24H $3.53M; 24H +770.00%; V/LP 20.02x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 29; Tier Micro; LP $83.2K; Vol24H $211.36M; 24H +6.47%; V/LP 2539.86x; 池数 1; 分项 L8/V17/B22/Buy3/Risk-45 | 只记录热度，不进入主榜 |
| SOLdiers | SOL | [B4ptaV...tjU8vn](https://solscan.io/token/B4ptaVsUe6YbtBwAS38WFeweSrVNfQLCcj9JRrtjU8vn) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $111.4K; Vol24H $19.31M; 24H +2965.12%; V/LP 173.36x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高 | Score 20; Tier Micro; LP $84.4K; Vol24H $4.78M; 24H -88.86%; V/LP 56.58x; 池数 1; 分项 L9/V17/B0/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| [Flea](https://dexscreener.com/solana/6aau4je3caa3gogza1tonkcuutfrzestwfg5wa3hu8km) | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $38.8K; Vol24H $2.35M; 24H +81.50%; V/LP 60.53x; 池数 1; 分项 L5/V16/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [WIFARG](https://dexscreener.com/solana/7owxxha2bnrthhimpk7qcxvzyvsd6rjbqm6jmlctmzmk) | SOL | [CV9dcP...d5pump](https://solscan.io/token/CV9dcP2D9hYtcnNtoHoY4NQEN9fYxfBbQN72wkd5pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 4; Tier Early; LP $121.2K; Vol24H $4.05M; 24H +5043.00%; V/LP 33.41x; 池数 3; 分项 L10/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $52.41M; Vol24H $3.10M; 24H +0.14%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.36M; Vol24H $14.47M; 24H -17.53%; V/LP 6.13x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| XPIN | BSC | [0xd955...3d31a6](https://bscscan.com/token/0xd955c9ba56fb1ab30e34766e252a97ccce3d31a6) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 72; Tier Liquid; LP $981.5K; Vol24H $2.59M; 24H +5.89%; V/LP 2.64x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BSB | BSC | [0x595d...4679cc](https://bscscan.com/token/0x595deaad1eb5476ff1e649fdb7efc36f1e4679cc) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $9.78M; Vol24H $14.86M; 24H -8.57%; V/LP 1.52x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $1.60M; Vol24H $3.33M; 24H -17.38%; V/LP 2.08x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BULLCAT | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [ANT](https://dexscreener.com/solana/3rdfvazrxzdeeejfcms4h2j1a2i6dj8pwev1ho1p1rg9) | SOL | [H5imUB...yHrise](https://solscan.io/token/H5imUBBArRQhKxvBLJhb73ghXscbEgGpriRxCxyHrise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| RAVE | BSC | [0x9769...6a911c](https://bscscan.com/token/0x97693439ea2f0ecdeb9135881e49f354656a911c) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 10 / Liquid 7 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
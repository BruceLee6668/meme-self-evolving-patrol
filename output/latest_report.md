# 自我进化轮巡

**本轮时间 UTC：** 2026-07-15T01:54:57Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 103 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 201 |
| 合并后Token | 103 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 6 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 6 |
| Mature层 | 4 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 575，刷新时间 2026-07-13T01:59:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 3 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.28M; Vol24H $5.45M; 24H -6.72%; V/LP 4.25x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 主观察 | Score 81; Tier Early; LP $517.5K; Vol24H $1.82M; 24H -5.55%; V/LP 3.52x; 池数 1; 分项 L16/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 次观察 | Score 75; Tier Early; LP $678.5K; Vol24H $2.58M; 24H -9.16%; V/LP 3.80x; 池数 1; 分项 L17/V17/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 68; Tier Early; LP $311.0K; Vol24H $54.7K; 24H +6.12%; V/LP 0.18x; 池数 1; 分项 L14/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PALU | BSC | [0x02e7...ee4444](https://bscscan.com/token/0x02e75d28a8aa2a0033b8cf866fcf0bb0e1ee4444) | 次观察 | Score 65; Tier Early; LP $354.3K; Vol24H $2.40M; 24H -33.47%; V/LP 6.77x; 池数 1; 分项 L14/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [REX](https://dexscreener.com/solana/8xzxttcfq49n5awdmtlaok7mkmz65aaatpqryd9m1jl7) | SOL | [CmQJNJ...f7pump](https://solscan.io/token/CmQJNJ185pjzQoebPbcqZu1kTykHxJbn4gER1Af7pump) | 次观察 | Score 64; Tier Micro; LP $50.3K; Vol24H $55.8K; 24H -24.92%; V/LP 1.11x; 池数 1; 分项 L6/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 64; Tier Micro; LP $75.7K; Vol24H $114.1K; 24H -21.22%; V/LP 1.51x; 池数 2; 分项 L8/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 44; Tier Liquid; LP $1.78M; Vol24H $60.72M; 24H +4.27%; V/LP 34.15x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 43; Tier Early; LP $179.8K; Vol24H $4.55M; 24H +23.52%; V/LP 25.30x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [brain](https://dexscreener.com/solana/7rrfzq32e5px9odknjzpdeg2e9ovfrwh9qlranyp3dq4) | SOL | [9oDndF...Skpump](https://solscan.io/token/9oDndFiC7RW42vZcmSzacTKMWE9kgeqnzwXDGLSkpump) | PVP风险池 | Score 35; Tier Micro; LP $72.5K; Vol24H $6.90M; 24H +40.82%; V/LP 95.14x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 主观察 | Score 80; Tier Early; LP $513.0K; Vol24H $1.76M; 24H -13.92%; V/LP 3.43x; 池数 1; 分项 L16/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $895.1K; Vol24H $95.5K; 24H -5.16%; V/LP 0.11x; 池数 1; 分项 L18/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TRIA | BSC | [0xb0b9...dab482](https://bscscan.com/token/0xb0b92de23baa85fb06208277e925ced53edab482) | 主观察 | Score 79; Tier Liquid; LP $910.0K; Vol24H $3.16M; 24H +13.62%; V/LP 3.47x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 次观察 | Score 74; Tier Early; LP $684.1K; Vol24H $2.34M; 24H -11.27%; V/LP 3.42x; 池数 1; 分项 L17/V16/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 68; Tier Early; LP $303.3K; Vol24H $62.5K; 24H +2.34%; V/LP 0.21x; 池数 1; 分项 L14/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 44; Tier Liquid; LP $1.77M; Vol24H $58.34M; 24H -2.92%; V/LP 32.90x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 43; Tier Early; LP $180.1K; Vol24H $4.47M; 24H +24.57%; V/LP 24.82x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| brain | SOL | [9oDndF...Skpump](https://solscan.io/token/9oDndFiC7RW42vZcmSzacTKMWE9kgeqnzwXDGLSkpump) | PVP风险池 | Score 30; Tier Micro; LP $75.3K; Vol24H $5.29M; 24H +37.83%; V/LP 70.25x; 池数 2; 分项 L8/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HBULL | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | PVP风险池 | Score 30; Tier Early; LP $168.4K; Vol24H $4.91M; 24H +623.25%; V/LP 29.13x; 池数 7; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | PVP风险池 | Score 27; Tier Micro; LP $81.8K; Vol24H $12.38M; 24H +630.00%; V/LP 151.32x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | PVP风险池 | Score 20; Tier Early; LP $100.9K; Vol24H $13.46M; 24H +98.94%; V/LP 133.36x; 池数 1; 分项 L9/V17/B0/Buy0/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| NYX | SOL | [3UXSLK...kbpump](https://solscan.io/token/3UXSLKVxF5L6AaugmUhkRBoKETtThQwj6bD6qYkbpump) | PVP风险池 | Score 13; Tier Micro; LP $5.6K; Vol24H $3.99M; 24H -98.13%; V/LP 708.02x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Flea | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | PVP风险池 | Score 12; Tier Micro; LP $24.0K; Vol24H $3.50M; 24H +139.30%; V/LP 145.71x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $52.39M; Vol24H $4.37M; 24H +2.66%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 74; Tier Liquid; LP $2.45M; Vol24H $11.41M; 24H -22.26%; V/LP 4.66x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 44; Tier Liquid; LP $1.77M; Vol24H $58.34M; 24H -2.92%; V/LP 32.90x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Early; LP $180.1K; Vol24H $4.47M; 24H +24.57%; V/LP 24.82x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| brain | SOL | [9oDndF...Skpump](https://solscan.io/token/9oDndFiC7RW42vZcmSzacTKMWE9kgeqnzwXDGLSkpump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 30; Tier Micro; LP $75.3K; Vol24H $5.29M; 24H +37.83%; V/LP 70.25x; 池数 2; 分项 L8/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| HBULL | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $168.4K; Vol24H $4.91M; 24H +623.25%; V/LP 29.13x; 池数 7; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TrumpCoin](https://dexscreener.com/solana/fpjfwz3ngfvywkpdxzqm8qaljzmy6u3ngaa8nc7sndag) | SOL | [F4GpAF...f6pump](https://solscan.io/token/F4GpAFr6vrxU3Y887F3XWkXRgybCVjZNk63m72f6pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $81.8K; Vol24H $12.38M; 24H +630.00%; V/LP 151.32x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HAAL9K](https://dexscreener.com/solana/gano23nxt3p4jjq49hsjaxuv4xwpximrytvncsamqi8v) | SOL | [wobYcx...mBpump](https://solscan.io/token/wobYcxYiABaM6qByXMuBdespq3DPLNuSYqUpMmBpump) | LP达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高 | Score 20; Tier Early; LP $100.9K; Vol24H $13.46M; 24H +98.94%; V/LP 133.36x; 池数 1; 分项 L9/V17/B0/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| NYX | SOL | [3UXSLK...kbpump](https://solscan.io/token/3UXSLKVxF5L6AaugmUhkRBoKETtThQwj6bD6qYkbpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $5.6K; Vol24H $3.99M; 24H -98.13%; V/LP 708.02x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| Flea | SOL | [5eiJm3...FKpump](https://solscan.io/token/5eiJm3oJRXcd3Aahg338P9DFULG8PPzmCUXGoFKpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $24.0K; Vol24H $3.50M; 24H +139.30%; V/LP 145.71x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $52.39M; Vol24H $4.37M; 24H +2.66%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.45M; Vol24H $11.41M; 24H -22.26%; V/LP 4.66x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.68M; Vol24H $57.65M; 24H +0.03%; V/LP 3.46x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 67; Tier Mature; LP $20.37M; Vol24H $56.0K; 24H +3.04%; V/LP 0.00x; 池数 1; 分项 L20/V5/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 60; Tier Liquid; LP $1.62M; Vol24H $7.94M; 24H -34.50%; V/LP 4.89x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BSB | BSC | [0x595d...4679cc](https://bscscan.com/token/0x595deaad1eb5476ff1e649fdb7efc36f1e4679cc) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 60; Tier Mature; LP $10.42M; Vol24H $15.16M; 24H +29.26%; V/LP 1.45x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TRIA | BSC | [0xb0b9...dab482](https://bscscan.com/token/0xb0b92de23baa85fb06208277e925ced53edab482) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CASHCAT](https://dexscreener.com/solana/dsa3zsbjt5wa5esiwotlceux1lfcicfocrkapysr5yau) | SOL | [22deNC...mgpump](https://solscan.io/token/22deNCri9bBae1GWZxdaDxipMWdwAUQ2ddvxdSmgpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| brain | SOL | [9oDndF...Skpump](https://solscan.io/token/9oDndFiC7RW42vZcmSzacTKMWE9kgeqnzwXDGLSkpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| HBULL | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TRIA | BSC | [0xb0b9...dab482](https://bscscan.com/token/0xb0b92de23baa85fb06208277e925ced53edab482) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 6 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
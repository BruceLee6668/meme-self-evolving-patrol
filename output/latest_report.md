# 自我进化轮巡

**本轮时间 UTC：** 2026-06-24T18:47:55Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 133 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 299 |
| 合并后Token | 133 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 9 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 1 |
| 多池Token | 6 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 6 |
| Liquid层 | 11 |
| Mature层 | 1 |
| 需要链上确认 | 19 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 0 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 87; Tier Early; LP $346.9K; Vol24H $1.42M; 24H +1.47%; V/LP 4.10x; 池数 6; 分项 L14/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SLX | BSC | [0x02bc...4bc54d](https://bscscan.com/token/0x02bcc4c181b83a8c0a342bc003389cbecb4bc54d) | 次观察 | Score 71; Tier Liquid; LP $1.12M; Vol24H $4.16M; 24H +35.88%; V/LP 3.71x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 71; Tier Early; LP $281.0K; Vol24H $1.03M; 24H -29.36%; V/LP 3.65x; 池数 1; 分项 L13/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 69; Tier Early; LP $107.7K; Vol24H $410.6K; 24H -2.75%; V/LP 3.81x; 池数 3; 分项 L9/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 68; Tier Liquid; LP $1.59M; Vol24H $28.0K; 24H +8.09%; V/LP 0.02x; 池数 1; 分项 L20/V3/B17/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 次观察 | Score 68; Tier Liquid; LP $1.64M; Vol24H $25.37M; 24H -2.42%; V/LP 15.49x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 66; Tier Liquid; LP $2.01M; Vol24H $9.8K; 24H -0.49%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 65; Tier Liquid; LP $924.7K; Vol24H $804.42; 24H -1.46%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 次观察 | Score 64; Tier Early; LP $106.5K; Vol24H $436.1K; 24H -8.43%; V/LP 4.10x; 池数 1; 分项 L9/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 64; Tier Early; LP $393.7K; Vol24H $1.25M; 24H +25.70%; V/LP 3.19x; 池数 1; 分项 L15/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 87; Tier Early; LP $327.0K; Vol24H $1.35M; 24H -2.89%; V/LP 4.13x; 池数 1; 分项 L14/V15/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 79; Tier Early; LP $282.9K; Vol24H $907.8K; 24H -21.01%; V/LP 3.21x; 池数 1; 分项 L13/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 73; Tier Liquid; LP $1.59M; Vol24H $26.0K; 24H +6.40%; V/LP 0.02x; 池数 1; 分项 L20/V3/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 72; Tier Early; LP $371.5K; Vol24H $1.25M; 24H +14.69%; V/LP 3.36x; 池数 1; 分项 L14/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GTAVI](https://dexscreener.com/solana/3jtcvdjp9cszn9mjgxwlw37m48aubsry5es6wfcznqlm) | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | 次观察 | Score 71; Tier Early; LP $100.8K; Vol24H $735.0K; 24H +19.46%; V/LP 7.30x; 池数 1; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| SLX | BSC | [0x02bc...4bc54d](https://bscscan.com/token/0x02bcc4c181b83a8c0a342bc003389cbecb4bc54d) | 次观察 | Score 71; Tier Liquid; LP $1.13M; Vol24H $4.49M; 24H +27.66%; V/LP 3.98x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 69; Tier Liquid; LP $1.19M; Vol24H $9.3K; 24H -4.82%; V/LP 0.01x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 次观察 | Score 68; Tier Liquid; LP $1.67M; Vol24H $23.25M; 24H +0.08%; V/LP 13.95x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | [BiywH8...sypump](https://solscan.io/token/BiywH8Eq2CbGhwMHKwCnfTiccWJwN7r1Q4Qn9hsypump) | 次观察 | Score 65; Tier Micro; LP $63.3K; Vol24H $192.8K; 24H -0.66%; V/LP 3.04x; 池数 1; 分项 L7/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 65; Tier Liquid; LP $900.9K; Vol24H $4.4K; 24H -3.23%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 次观察 | Score 64; Tier Micro; LP $99.4K; Vol24H $460.9K; 24H -15.29%; V/LP 4.64x; 池数 1; 分项 L9/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 36; Tier Liquid; LP $1.44M; Vol24H $44.38M; 24H -24.23%; V/LP 30.92x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | PVP风险池 | Score 36; Tier Early; LP $101.8K; Vol24H $2.60M; 24H +33.88%; V/LP 25.52x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [EAGLE250](https://dexscreener.com/solana/3qhv2z6n5aknnzx56a2n4qvquz4cvbckuh24kck9t9qy) | SOL | [AXLmMW...zLpump](https://solscan.io/token/AXLmMWkRmSPdPxkuMqAD4nzYBK7QRssNkYZ6RXzLpump) | PVP风险池 | Score 30; Tier Micro; LP $68.9K; Vol24H $1.84M; 24H +1308.00%; V/LP 26.76x; 池数 5; 分项 L8/V16/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| world | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | PVP风险池 | Score 29; Tier Early; LP $115.4K; Vol24H $4.70M; 24H +2700.67%; V/LP 40.78x; 池数 5; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | 24H波动可控；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 36; Tier Liquid; LP $1.44M; Vol24H $44.38M; 24H -24.23%; V/LP 30.92x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-42 | 只记录热度，不进入主榜 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Early; LP $101.8K; Vol24H $2.60M; 24H +33.88%; V/LP 25.52x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [EAGLE250](https://dexscreener.com/solana/3qhv2z6n5aknnzx56a2n4qvquz4cvbckuh24kck9t9qy) | SOL | [AXLmMW...zLpump](https://solscan.io/token/AXLmMWkRmSPdPxkuMqAD4nzYBK7QRssNkYZ6RXzLpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $68.9K; Vol24H $1.84M; 24H +1308.00%; V/LP 26.76x; 池数 5; 分项 L8/V16/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| world | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $115.4K; Vol24H $4.70M; 24H +2700.67%; V/LP 40.78x; 池数 5; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [FITNESS](https://dexscreener.com/solana/rtopezgr592hepw8wfc4zaak5ezhgryxroxzsvshu2y) | SOL | [9af7Pm...dMpump](https://solscan.io/token/9af7PmWRca2QYmknQehoLH19jG5ss9ajYFpgL8dMpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 21; Tier Micro; LP $64.6K; Vol24H $2.60M; 24H +1114.00%; V/LP 40.25x; 池数 1; 分项 L7/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [WEN](https://dexscreener.com/solana/aawfsorcywroe5k28ah3f5onzz5cbydwqm97baqdzsoh) | SOL | [Eav7v7...wmpump](https://solscan.io/token/Eav7v75ydZ5k3ToyRsbovn4c2J38fNRmZV6oW4wmpump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高 | Score 17; Tier Micro; LP $65.3K; Vol24H $2.45M; 24H +2364.00%; V/LP 37.55x; 池数 4; 分项 L7/V16/B0/Buy0/Risk-30 | 只记录热度，不进入主榜 |
| STARMIND | SOL | [45Kt1m...X9pump](https://solscan.io/token/45Kt1mykq7kQWq2kLs1mfEHJmDLiiTk2rFKvkYX9pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $38.0K; Vol24H $1.86M; 24H +720.97%; V/LP 48.95x; 池数 2; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| POKÉDOKU | SOL | [72iZDQ...pGpump](https://solscan.io/token/72iZDQ4JtkiCDkxH1eLC3kbYdFkufqutgcUUeSpGpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 4; Tier Micro; LP $5.1K; Vol24H $2.56M; 24H -98.01%; V/LP 500.13x; 池数 1; 分项 L0/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 80; Tier Mature; LP $137.60M; Vol24H $174.55M; 24H +7.26%; V/LP 1.27x; 池数 1; 分项 L20/V17/B22/Buy12/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 77; Tier Liquid; LP $1.03M; Vol24H $926.5K; 24H -5.09%; V/LP 0.90x; 池数 2; 分项 L18/V13/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CARDS | SOL | [CARDSc...dKxYjp](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.61M; Vol24H $9.91M; 24H -8.88%; V/LP 2.75x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Liquid; LP $1.31M; Vol24H $7.97M; 24H -20.12%; V/LP 6.07x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/5hbf9jp8k5zdrzp9pokpypfqobse5mgcmw6nqodurgcd) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $802.4K; Vol24H $670.9K; 24H -4.68%; V/LP 0.84x; 池数 1; 分项 L18/V13/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [GTAVI](https://dexscreener.com/solana/3jtcvdjp9cszn9mjgxwlw37m48aubsry5es6wfcznqlm) | SOL | [EpVHyK...zYpump](https://solscan.io/token/EpVHyKK8oxcLmp2C2NhAos1oDxgBNriw3wSLSozYpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SLX | BSC | [0x02bc...4bc54d](https://bscscan.com/token/0x02bcc4c181b83a8c0a342bc003389cbecb4bc54d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | [BiywH8...sypump](https://solscan.io/token/BiywH8Eq2CbGhwMHKwCnfTiccWJwN7r1Q4Qn9hsypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 6 / Liquid 11 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 331} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
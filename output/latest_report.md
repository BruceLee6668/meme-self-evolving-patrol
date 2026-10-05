# 自我进化轮巡

**本轮时间 UTC：** 2026-10-05T01:29:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 137 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 250 |
| 合并后Token | 137 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 5 |
| 多池Token | 6 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 3 |
| Early层 | 13 |
| Liquid层 | 8 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1651，刷新时间 2026-09-28T02:48:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 2 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 86; Tier Liquid; LP $2.08M; Vol24H $3.53M; 24H -2.29%; V/LP 1.70x; 池数 9; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 82; Tier Liquid; LP $1.33M; Vol24H $2.50M; 24H +6.72%; V/LP 1.88x; 池数 1; 分项 L20/V16/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 74; Tier Early; LP $262.2K; Vol24H $251.8K; 24H -6.21%; V/LP 0.96x; 池数 1; 分项 L13/V10/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 69; Tier Micro; LP $90.6K; Vol24H $74.8K; 24H +7.87%; V/LP 0.83x; 池数 1; 分项 L9/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 次观察 | Score 68; Tier Liquid; LP $2.24M; Vol24H $18.87M; 24H +0.59%; V/LP 8.42x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Agency](https://dexscreener.com/solana/cyjwknliiy4fmiwqmcswfshxo7t9ubshgs2uraujcrk5) | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | PVP风险池 | Score 47; Tier Early; LP $514.3K; Vol24H $16.47M; 24H -16.92%; V/LP 32.02x; 池数 2; 分项 L16/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | PVP风险池 | Score 40; Tier Early; LP $272.2K; Vol24H $12.45M; 24H +41.32%; V/LP 45.73x; 池数 1; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SI | BSC | [0x531f...147777](https://bscscan.com/token/0x531f1fd7356923e4d4da6145ce3742ddfe147777) | PVP风险池 | Score 35; Tier Early; LP $218.3K; Vol24H $7.59M; 24H +161808.95%; V/LP 34.77x; 池数 2; 分项 L12/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CRAWL | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | PVP风险池 | Score 31; Tier Early; LP $189.3K; Vol24H $16.73M; 24H +421.55%; V/LP 88.37x; 池数 3; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HIGGS | SOL | [DoVAVz...pJpump](https://solscan.io/token/DoVAVzViX8Bjy3r15nwikSaSbzE6dV4ovd28aWpJpump) | PVP风险池 | Score 31; Tier Early; LP $222.2K; Vol24H $15.87M; 24H +4711.17%; V/LP 71.41x; 池数 4; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 主观察 | Score 82; Tier Liquid; LP $1.34M; Vol24H $2.25M; 24H +6.52%; V/LP 1.68x; 池数 1; 分项 L20/V16/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.07M; Vol24H $2.95M; 24H -15.14%; V/LP 1.42x; 池数 11; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 次观察 | Score 73; Tier Early; LP $339.7K; Vol24H $271.4K; 24H +22.61%; V/LP 0.80x; 池数 1; 分项 L14/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 73; Tier Early; LP $238.7K; Vol24H $94.5K; 24H +21.34%; V/LP 0.40x; 池数 1; 分项 L13/V7/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 73; Tier Early; LP $260.4K; Vol24H $220.2K; 24H +1.60%; V/LP 0.85x; 池数 1; 分项 L13/V9/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 次观察 | Score 68; Tier Liquid; LP $2.31M; Vol24H $18.98M; 24H +7.77%; V/LP 8.23x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 64; Tier Micro; LP $91.5K; Vol24H $86.9K; 24H +8.42%; V/LP 0.95x; 池数 1; 分项 L9/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | PVP风险池 | Score 56; Tier Liquid; LP $1.40M; Vol24H $40.17M; 24H -0.08%; V/LP 28.61x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | PVP风险池 | Score 51; Tier Liquid; LP $1.41M; Vol24H $31.70M; 24H +23.65%; V/LP 22.51x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | PVP风险池 | Score 48; Tier Early; LP $222.1K; Vol24H $12.75M; 24H -8.95%; V/LP 57.40x; 池数 1; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Agency](https://dexscreener.com/solana/cyjwknliiy4fmiwqmcswfshxo7t9ubshgs2uraujcrk5) | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | PVP风险池 | Score 46; Tier Early; LP $471.1K; Vol24H $15.56M; 24H -17.53%; V/LP 33.02x; 池数 2; 分项 L15/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CRAWL](https://dexscreener.com/solana/2b8tftz5ww8tremr3pgkgerlnjjyjxeapwmenvigmsl4) | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | PVP风险池 | Score 42; Tier Early; LP $163.5K; Vol24H $10.71M; 24H -13.92%; V/LP 65.52x; 池数 3; 分项 L11/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SI | BSC | [0x531f...147777](https://bscscan.com/token/0x531f1fd7356923e4d4da6145ce3742ddfe147777) | PVP风险池 | Score 35; Tier Early; LP $199.7K; Vol24H $10.55M; 24H +123952.96%; V/LP 52.83x; 池数 2; 分项 L12/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HIGGS](https://dexscreener.com/solana/bfrszakeqnzvtm3efhroo4erhagmmwn8brntiqkfh6ru) | SOL | [DoVAVz...pJpump](https://solscan.io/token/DoVAVzViX8Bjy3r15nwikSaSbzE6dV4ovd28aWpJpump) | PVP风险池 | Score 29; Tier Early; LP $129.9K; Vol24H $16.81M; 24H +2292.00%; V/LP 129.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Human](https://dexscreener.com/solana/fb2dw7cbcc2d1hkyf21kxkexesqfvsbntvdjauogmrws) | SOL | [8nPoBH...t4DMBC](https://solscan.io/token/8nPoBHiBM6pybxMws9PA2JRb9BjkppBfqcZGmot4DMBC) | PVP风险池 | Score 7; Tier Early; LP $286.2K; Vol24H $15.33M; 24H +11414.00%; V/LP 53.58x; 池数 5; 分项 L13/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Liquid; LP $1.40M; Vol24H $40.17M; 24H -0.08%; V/LP 28.61x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.41M; Vol24H $31.70M; 24H +23.65%; V/LP 22.51x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 48; Tier Early; LP $222.1K; Vol24H $12.75M; 24H -8.95%; V/LP 57.40x; 池数 1; 分项 L12/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Agency](https://dexscreener.com/solana/cyjwknliiy4fmiwqmcswfshxo7t9ubshgs2uraujcrk5) | SOL | [7Vertk...XVpump](https://solscan.io/token/7VertkgF9KLhxxJXHX6uaWuoYZTP9LdGj2bWmVXVpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 46; Tier Early; LP $471.1K; Vol24H $15.56M; 24H -17.53%; V/LP 33.02x; 池数 2; 分项 L15/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [CRAWL](https://dexscreener.com/solana/2b8tftz5ww8tremr3pgkgerlnjjyjxeapwmenvigmsl4) | SOL | [BXoHJd...Dkpump](https://solscan.io/token/BXoHJddsWJLHtAopeiSbKUSELsu8hSFMs8baGMDkpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $163.5K; Vol24H $10.71M; 24H -13.92%; V/LP 65.52x; 池数 3; 分项 L11/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| SI | BSC | [0x531f...147777](https://bscscan.com/token/0x531f1fd7356923e4d4da6145ce3742ddfe147777) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 35; Tier Early; LP $199.7K; Vol24H $10.55M; 24H +123952.96%; V/LP 52.83x; 池数 2; 分项 L12/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [HIGGS](https://dexscreener.com/solana/bfrszakeqnzvtm3efhroo4erhagmmwn8brntiqkfh6ru) | SOL | [DoVAVz...pJpump](https://solscan.io/token/DoVAVzViX8Bjy3r15nwikSaSbzE6dV4ovd28aWpJpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $129.9K; Vol24H $16.81M; 24H +2292.00%; V/LP 129.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Human](https://dexscreener.com/solana/fb2dw7cbcc2d1hkyf21kxkexesqfvsbntvdjauogmrws) | SOL | [8nPoBH...t4DMBC](https://solscan.io/token/8nPoBHiBM6pybxMws9PA2JRb9BjkppBfqcZGmot4DMBC) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 7; Tier Early; LP $286.2K; Vol24H $15.33M; 24H +11414.00%; V/LP 53.58x; 池数 5; 分项 L13/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $4.35M; Vol24H $5.41M; 24H +0.68%; V/LP 1.24x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.83M; Vol24H $9.52M; 24H +5.36%; V/LP 3.36x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.06M; Vol24H $3.15M; 24H +0.64%; V/LP 0.05x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 72; Tier Liquid; LP $2.88M; Vol24H $1.47M; 24H -1.67%; V/LP 0.51x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 67; Tier Early; LP $432.0K; Vol24H $1.48M; 24H +0.12%; V/LP 3.43x; 池数 1; 分项 L15/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [GOIF](https://dexscreener.com/solana/4d56grhvrhh825hjbrkx4t6a5u9ujwcmgpsyv9bwhy3o) | SOL | [nZbPjC...6Dpump](https://solscan.io/token/nZbPjCn4GJcLxrdHWRnMhPt875EyHSNTzhFmD6Dpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ct | BSC | [0x0a09...867f46](https://bscscan.com/token/0x0a092e544da31150b439a1aaa1a3a2214a867f46) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [MISTAKE](https://dexscreener.com/solana/867dkvaccyrrudp66bqnxbujxfjaxsnb9wtpc4cmbdad) | SOL | [HKZDfZ...9wpump](https://solscan.io/token/HKZDfZnkHZxd9agRDNPyDv4iT6LmAurJnpRtj9wpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| AEON | BSC | [0x277a...ec9b80](https://bscscan.com/token/0x277add739c6e0477616948357af9e79fe1ec9b80) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 3 / Early 13 / Liquid 8 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
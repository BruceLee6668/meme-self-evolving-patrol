# 自我进化轮巡

**本轮时间 UTC：** 2026-07-09T08:23:18Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 116 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 289 |
| 合并后Token | 116 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 1 |
| 低优先观察 | 9 |
| 多池Token | 12 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 15 |
| Liquid层 | 4 |
| Mature层 | 0 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 2 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 80; Tier Liquid; LP $1.27M; Vol24H $8.08M; 24H +12.03%; V/LP 6.36x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RETIRE](https://dexscreener.com/solana/bqznpn9o3mtugn8tyawwsqdx2ga11xbu3xz8xjwgmnax) | SOL | [HQJdVy...yJpump](https://solscan.io/token/HQJdVyNpAFSwJzeJTuR8Go2YmvtkmhyZD6X3xeyJpump) | 次观察 | Score 66; Tier Liquid; LP $3.52M; Vol24H $8.04M; 24H -56.71%; V/LP 2.28x; 池数 8; 分项 L20/V17/B8/Buy0/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 66; Tier Liquid; LP $1.20M; Vol24H $5.0K; 24H +1.23%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 65; Tier Early; LP $129.5K; Vol24H $344.6K; 24H +9.71%; V/LP 2.66x; 池数 3; 分项 L10/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| HOOD | SOL | [h5NciP...yBhood](https://solscan.io/token/h5NciPdMZ5QCB5BYETJMYBMpVx9ZuitR6HcVjyBhood) | 次观察 | Score 64; Tier Early; LP $258.6K; Vol24H $1.33M; 24H +551.14%; V/LP 5.15x; 池数 1; 分项 L13/V15/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 49; Tier Early; LP $261.8K; Vol24H $7.41M; 24H -2.43%; V/LP 28.30x; 池数 2; 分项 L13/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | PVP风险池 | Score 46; Tier Early; LP $447.3K; Vol24H $9.81M; 24H +20.52%; V/LP 21.93x; 池数 1; 分项 L15/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 45; Tier Early; LP $348.3K; Vol24H $7.14M; 24H -9.12%; V/LP 20.51x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 43; Tier Early; LP $525.1K; Vol24H $11.74M; 24H -49.78%; V/LP 22.36x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | PVP风险池 | Score 38; Tier Early; LP $154.4K; Vol24H $6.11M; 24H -49.19%; V/LP 39.55x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 80; Tier Liquid; LP $1.31M; Vol24H $8.23M; 24H +13.88%; V/LP 6.28x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 主观察 | Score 77; Tier Liquid; LP $4.54M; Vol24H $13.96M; 24H +30.68%; V/LP 3.08x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 74; Tier Early; LP $129.3K; Vol24H $294.0K; 24H -5.94%; V/LP 2.27x; 池数 4; 分项 L10/V10/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Punch](https://dexscreener.com/solana/a6khmifzn9am7vkbtvp4fzny9bco2jp63r9dphaw1vrq) | SOL | [NV2RYH...FSpump](https://solscan.io/token/NV2RYH954cTJ3ckFUpvfqaQXU4ARqqDH3562nFSpump) | 次观察 | Score 72; Tier Early; LP $196.3K; Vol24H $67.0K; 24H -5.38%; V/LP 0.34x; 池数 5; 分项 L12/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [drooling](https://dexscreener.com/solana/cfewdgnzgjjn1pykxgfpazfq1eq1xmvzns1kswswhsxa) | SOL | [B6f27E...hmpump](https://solscan.io/token/B6f27ETGcjgGNB1fqULJbXVmw9FnL8HgBp7R83hmpump) | 次观察 | Score 71; Tier Early; LP $198.6K; Vol24H $269.0K; 24H -9.32%; V/LP 1.35x; 池数 5; 分项 L12/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 次观察 | Score 71; Tier Micro; LP $93.3K; Vol24H $678.0K; 24H -21.75%; V/LP 7.27x; 池数 2; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| HOOD | SOL | [h5NciP...yBhood](https://solscan.io/token/h5NciPdMZ5QCB5BYETJMYBMpVx9ZuitR6HcVjyBhood) | 次观察 | Score 64; Tier Early; LP $247.1K; Vol24H $1.54M; 24H +393.33%; V/LP 6.23x; 池数 1; 分项 L13/V15/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 50; Tier Early; LP $299.5K; Vol24H $6.52M; 24H -12.47%; V/LP 21.78x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 44; Tier Early; LP $266.7K; Vol24H $6.42M; 24H -15.04%; V/LP 24.08x; 池数 2; 分项 L13/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 43; Tier Early; LP $503.7K; Vol24H $11.31M; 24H -53.97%; V/LP 22.44x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | PVP风险池 | Score 38; Tier Early; LP $157.5K; Vol24H $5.24M; 24H -26.65%; V/LP 33.26x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | PVP风险池 | Score 37; Tier Early; LP $464.1K; Vol24H $10.72M; 24H +28.27%; V/LP 23.11x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | PVP风险池 | Score 35; Tier Early; LP $203.7K; Vol24H $4.18M; 24H +158.00%; V/LP 20.51x; 池数 4; 分项 L12/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 30; Tier Liquid; LP $3.06M; Vol24H $138.85M; 24H -65.04%; V/LP 45.36x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BULLSEY | SOL | [7aD86T...Vcpump](https://solscan.io/token/7aD86TAvoXPBAkt7HxGsz3MG8UBdDUvcVeBLouVcpump) | PVP风险池 | Score 13; Tier Micro; LP $6.7K; Vol24H $5.23M; 24H -99.78%; V/LP 785.09x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 50; Tier Early; LP $299.5K; Vol24H $6.52M; 24H -12.47%; V/LP 21.78x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $266.7K; Vol24H $6.42M; 24H -15.04%; V/LP 24.08x; 池数 2; 分项 L13/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Early; LP $503.7K; Vol24H $11.31M; 24H -53.97%; V/LP 22.44x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [tolywifhat](https://dexscreener.com/solana/gdc11vqjfq6isptw1avoqowxnd7eq3jetjwh1ltt4qt8) | SOL | [E2ueKQ...Rzpump](https://solscan.io/token/E2ueKQ3EDTTmCkUA17j3KeTb2u6VT91xiyECdKRzpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $157.5K; Vol24H $5.24M; 24H -26.65%; V/LP 33.26x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $464.1K; Vol24H $10.72M; 24H +28.27%; V/LP 23.11x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [DONALT](https://dexscreener.com/solana/8yvumppwyjzqhsr2b5muoulugj8grusqm7yddswthgju) | SOL | [4eKYoR...cNpump](https://solscan.io/token/4eKYoR1hBHnRaYyg2d57H36uUatRNyZr1NRP9ScNpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 35; Tier Early; LP $203.7K; Vol24H $4.18M; 24H +158.00%; V/LP 20.51x; 池数 4; 分项 L12/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $3.06M; Vol24H $138.85M; 24H -65.04%; V/LP 45.36x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| BULLSEY | SOL | [7aD86T...Vcpump](https://solscan.io/token/7aD86TAvoXPBAkt7HxGsz3MG8UBdDUvcVeBLouVcpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $6.7K; Vol24H $5.23M; 24H -99.78%; V/LP 785.09x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.80M; Vol24H $19.56M; 24H -2.11%; V/LP 6.99x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Punch](https://dexscreener.com/solana/a6khmifzn9am7vkbtvp4fzny9bco2jp63r9dphaw1vrq) | SOL | [NV2RYH...FSpump](https://solscan.io/token/NV2RYH954cTJ3ckFUpvfqaQXU4ARqqDH3562nFSpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [drooling](https://dexscreener.com/solana/cfewdgnzgjjn1pykxgfpazfq1eq1xmvzns1kswswhsxa) | SOL | [B6f27E...hmpump](https://solscan.io/token/B6f27ETGcjgGNB1fqULJbXVmw9FnL8HgBp7R83hmpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| HOOD | SOL | [h5NciP...yBhood](https://solscan.io/token/h5NciPdMZ5QCB5BYETJMYBMpVx9ZuitR6HcVjyBhood) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [NIGGABULL](https://dexscreener.com/solana/985nrfke9yhrwmpvpw7gcje1jr7wtddnyzb4qcnzeq15) | SOL | [77x1fC...Vfpump](https://solscan.io/token/77x1fCskDLaiZmm2uZKEhARSCD2B86VaahTkK2Vfpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 1 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 15 / Liquid 4 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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
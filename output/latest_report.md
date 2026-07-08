# 自我进化轮巡

**本轮时间 UTC：** 2026-07-08T19:16:35Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 111 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 260 |
| 合并后Token | 111 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 1 |
| 低优先观察 | 11 |
| 多池Token | 11 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 12 |
| Liquid层 | 5 |
| Mature层 | 0 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.23M; Vol24H $7.68M; 24H -6.18%; V/LP 6.26x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 70; Tier Early; LP $307.2K; Vol24H $122.8K; 24H -10.81%; V/LP 0.40x; 池数 1; 分项 L14/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 次观察 | Score 68; Tier Liquid; LP $1.58M; Vol24H $15.26M; 24H -4.97%; V/LP 9.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 50; Tier Early; LP $347.5K; Vol24H $8.80M; 24H -16.46%; V/LP 25.32x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 43; Tier Early; LP $490.1K; Vol24H $11.37M; 24H -65.17%; V/LP 23.20x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 39; Tier Liquid; LP $1.57M; Vol24H $59.38M; 24H +10.49%; V/LP 37.71x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | PVP风险池 | Score 34; Tier Early; LP $179.0K; Vol24H $7.41M; 24H -43.41%; V/LP 41.39x; 池数 1; 分项 L12/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 33; Tier Early; LP $312.3K; Vol24H $21.66M; 24H +105.00%; V/LP 69.36x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 33; Tier Early; LP $352.1K; Vol24H $15.14M; 24H +11.98%; V/LP 43.00x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BULLSEY](https://dexscreener.com/solana/6mc6txdrckl1mhr8s9kys55cchkdzx3ayianas6aa9ym) | SOL | [7aD86T...Vcpump](https://solscan.io/token/7aD86TAvoXPBAkt7HxGsz3MG8UBdDUvcVeBLouVcpump) | PVP风险池 | Score 30; Tier Micro; LP $55.5K; Vol24H $8.36M; 24H +679.00%; V/LP 150.59x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.26M; Vol24H $7.34M; 24H +4.79%; V/LP 5.81x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATCOIN](https://dexscreener.com/solana/6fnwjffn6kdkybwk5pflwqznptmobaswuwvxig3g5d2d) | SOL | [5gTPsp...atcoin](https://solscan.io/token/5gTPspC2ricuGWiYQ4Ghausg8fsq7uCrGgSVACatcoin) | 次观察 | Score 69; Tier Micro; LP $78.3K; Vol24H $103.0K; 24H -6.53%; V/LP 1.32x; 池数 1; 分项 L8/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HAALAND](https://dexscreener.com/solana/6g7tlasdmzdtak182uk6k6h8vd3ywfn3aq8zrutrn3dn) | SOL | [EYvkcW...dppump](https://solscan.io/token/EYvkcWB5S4DFv7gJqR8D2W76U9n7kD3jvYcbSXdppump) | 次观察 | Score 67; Tier Micro; LP $51.3K; Vol24H $400.6K; 24H -18.49%; V/LP 7.81x; 池数 5; 分项 L7/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 66; Tier Liquid; LP $1.18M; Vol24H $8.7K; 24H -0.37%; V/LP 0.01x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TBB](https://dexscreener.com/solana/6unng2hl8udpjdpu3tchvatptu3dq8as7tymrwdn2llc) | SOL | [42cXQv...gppump](https://solscan.io/token/42cXQvAAr7hcPBPWAS4ocVtDyeJ4Fa6gRR2uG4gppump) | 次观察 | Score 65; Tier Early; LP $190.3K; Vol24H $864.3K; 24H +29.10%; V/LP 4.54x; 池数 5; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 50; Tier Early; LP $351.0K; Vol24H $11.91M; 24H +0.28%; V/LP 33.94x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 50; Tier Early; LP $322.4K; Vol24H $8.39M; 24H -17.38%; V/LP 26.03x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 43; Tier Early; LP $595.3K; Vol24H $13.21M; 24H -48.12%; V/LP 22.19x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 40; Tier Early; LP $283.1K; Vol24H $20.59M; 24H +58.83%; V/LP 72.74x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | PVP风险池 | Score 33; Tier Early; LP $171.0K; Vol24H $4.63M; 24H -40.67%; V/LP 27.08x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ok](https://dexscreener.com/solana/7uc5bj9ay4qa5f93pe6nuqgeekusqpa32rxt9jwszup5) | SOL | [CizcDa...Mmpump](https://solscan.io/token/CizcDa22HJjXybKLriibqP167GcJjqiDHDPtuiMmpump) | PVP风险池 | Score 28; Tier Early; LP $103.5K; Vol24H $6.83M; 24H +2336.00%; V/LP 66.00x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BULLSEY | SOL | [7aD86T...Vcpump](https://solscan.io/token/7aD86TAvoXPBAkt7HxGsz3MG8UBdDUvcVeBLouVcpump) | PVP风险池 | Score 25; Tier Micro; LP $25.8K; Vol24H $8.54M; 24H +62.69%; V/LP 331.39x; 池数 2; 分项 L4/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MASON](https://dexscreener.com/solana/6adx5qhm4iwee39nik8cambb3sjdgslw7vgpomy2vqwz) | SOL | [4gqUH4...o2pump](https://solscan.io/token/4gqUH4qMtkZTjeenrtVmcQXKEYg9aBUC8j2kQao2pump) | PVP风险池 | Score 21; Tier Micro; LP $64.3K; Vol24H $5.32M; 24H +1040.00%; V/LP 82.70x; 池数 2; 分项 L7/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 成熟池观察 | Score 80; Tier Liquid; LP $1.17M; Vol24H $1.51M; 24H -6.75%; V/LP 1.28x; 池数 2; 分项 L19/V15/B22/Buy12/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 低优先观察 | Score 63; Tier Liquid; LP $1.57M; Vol24H $14.97M; 24H -8.32%; V/LP 9.53x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 50; Tier Early; LP $351.0K; Vol24H $11.91M; 24H +0.28%; V/LP 33.94x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 50; Tier Early; LP $322.4K; Vol24H $8.39M; 24H -17.38%; V/LP 26.03x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Early; LP $595.3K; Vol24H $13.21M; 24H -48.12%; V/LP 22.19x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Early; LP $283.1K; Vol24H $20.59M; 24H +58.83%; V/LP 72.74x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 33; Tier Early; LP $171.0K; Vol24H $4.63M; 24H -40.67%; V/LP 27.08x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [ok](https://dexscreener.com/solana/7uc5bj9ay4qa5f93pe6nuqgeekusqpa32rxt9jwszup5) | SOL | [CizcDa...Mmpump](https://solscan.io/token/CizcDa22HJjXybKLriibqP167GcJjqiDHDPtuiMmpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $103.5K; Vol24H $6.83M; 24H +2336.00%; V/LP 66.00x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BULLSEY | SOL | [7aD86T...Vcpump](https://solscan.io/token/7aD86TAvoXPBAkt7HxGsz3MG8UBdDUvcVeBLouVcpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 25; Tier Micro; LP $25.8K; Vol24H $8.54M; 24H +62.69%; V/LP 331.39x; 池数 2; 分项 L4/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [MASON](https://dexscreener.com/solana/6adx5qhm4iwee39nik8cambb3sjdgslw7vgpomy2vqwz) | SOL | [4gqUH4...o2pump](https://solscan.io/token/4gqUH4qMtkZTjeenrtVmcQXKEYg9aBUC8j2kQao2pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 21; Tier Micro; LP $64.3K; Vol24H $5.32M; 24H +1040.00%; V/LP 82.70x; 池数 2; 分项 L7/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 80; Tier Liquid; LP $1.17M; Vol24H $1.51M; 24H -6.75%; V/LP 1.28x; 池数 2; 分项 L19/V15/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATCOIN](https://dexscreener.com/solana/6fnwjffn6kdkybwk5pflwqznptmobaswuwvxig3g5d2d) | SOL | [5gTPsp...atcoin](https://solscan.io/token/5gTPspC2ricuGWiYQ4Ghausg8fsq7uCrGgSVACatcoin) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [HAALAND](https://dexscreener.com/solana/6g7tlasdmzdtak182uk6k6h8vd3ywfn3aq8zrutrn3dn) | SOL | [EYvkcW...dppump](https://solscan.io/token/EYvkcWB5S4DFv7gJqR8D2W76U9n7kD3jvYcbSXdppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TBB](https://dexscreener.com/solana/6unng2hl8udpjdpu3tchvatptu3dq8as7tymrwdn2llc) | SOL | [42cXQv...gppump](https://solscan.io/token/42cXQvAAr7hcPBPWAS4ocVtDyeJ4Fa6gRR2uG4gppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 1 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 12 / Liquid 5 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 335} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
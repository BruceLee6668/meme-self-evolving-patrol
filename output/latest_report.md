# 自我进化轮巡

**本轮时间 UTC：** 2026-07-12T17:55:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 106 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 222 |
| 合并后Token | 106 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 3 |
| 多池Token | 8 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 2 |
| Mature层 | 6 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 1 |

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
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 81; Tier Liquid; LP $1.88M; Vol24H $13.25M; 24H +10.74%; V/LP 7.04x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| MANIFEST | SOL | [BCdwQB...ERpump](https://solscan.io/token/BCdwQBAn8dYB5YjTsoB6TdHAWokxv28k2oZUodERpump) | 主观察 | Score 81; Tier Liquid; LP $800.5K; Vol24H $1.64M; 24H +4.73%; V/LP 2.05x; 池数 1; 分项 L17/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 次观察 | Score 75; Tier Micro; LP $73.8K; Vol24H $235.9K; 24H +4.59%; V/LP 3.20x; 池数 1; 分项 L8/V9/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 75; Tier Early; LP $193.4K; Vol24H $989.9K; 24H -22.60%; V/LP 5.12x; 池数 1; 分项 L12/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 69; Tier Early; LP $297.7K; Vol24H $67.6K; 24H -2.25%; V/LP 0.23x; 池数 1; 分项 L14/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 64; Tier Micro; LP $84.1K; Vol24H $114.1K; 24H -10.31%; V/LP 1.36x; 池数 3; 分项 L8/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| quq | BSC | [0x4fa7...6b03bf](https://bscscan.com/token/0x4fa7c69a7b69f8bc48233024d546bc299d6b03bf) | PVP风险池 | Score 56; Tier Liquid; LP $4.66M; Vol24H $374.53M; 24H -5.58%; V/LP 80.39x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 46; Tier Early; LP $121.9K; Vol24H $28.98M; 24H -0.53%; V/LP 237.66x; 池数 1; 分项 L10/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 43; Tier Early; LP $201.6K; Vol24H $15.28M; 24H -22.92%; V/LP 75.79x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | PVP风险池 | Score 37; Tier Early; LP $126.5K; Vol24H $5.74M; 24H -79.35%; V/LP 45.33x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 81; Tier Liquid; LP $1.88M; Vol24H $12.92M; 24H +8.62%; V/LP 6.89x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 75; Tier Early; LP $212.8K; Vol24H $1.01M; 24H -7.32%; V/LP 4.73x; 池数 1; 分项 L12/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 75; Tier Early; LP $367.5K; Vol24H $566.9K; 24H +1.56%; V/LP 1.54x; 池数 1; 分项 L14/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 次观察 | Score 70; Tier Micro; LP $70.1K; Vol24H $228.9K; 24H +11.18%; V/LP 3.27x; 池数 1; 分项 L8/V9/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 70; Tier Micro; LP $85.2K; Vol24H $111.5K; 24H -7.72%; V/LP 1.31x; 池数 3; 分项 L9/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 69; Tier Early; LP $298.1K; Vol24H $68.0K; 24H -0.47%; V/LP 0.23x; 池数 1; 分项 L14/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 68; Tier Early; LP $210.8K; Vol24H $542.8K; 24H +30.04%; V/LP 2.58x; 池数 1; 分项 L12/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 46; Tier Early; LP $113.3K; Vol24H $28.12M; 24H -0.22%; V/LP 248.17x; 池数 1; 分项 L10/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [febu](https://dexscreener.com/solana/68nvmrvpyxgjgbgh2p92e93syhjcbe6qocizrqoqdjcb) | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | PVP风险池 | Score 38; Tier Early; LP $141.5K; Vol24H $5.74M; 24H -70.89%; V/LP 40.59x; 池数 2; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 35; Tier Early; LP $617.5K; Vol24H $22.50M; 24H +105.16%; V/LP 36.44x; 池数 1; 分项 L16/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 34; Tier Early; LP $185.2K; Vol24H $15.68M; 24H -34.53%; V/LP 84.66x; 池数 1; 分项 L12/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [UNC](https://dexscreener.com/solana/ak3u4akfzqqfqthjsndbavicic8qwzxb9cfkcqeaux6) | SOL | [6MJEQQ...V1pump](https://solscan.io/token/6MJEQQB6wC6wpRrjni15Q7By9DrbdbRFeJU3xqV1pump) | PVP风险池 | Score 12; Tier Micro; LP $34.3K; Vol24H $1.60M; 24H +449.00%; V/LP 46.70x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PumpfunLife | SOL | [DpqGBm...kupump](https://solscan.io/token/DpqGBmkc6SrY2vA1Yb5KuH571WW1oQJjJdD3d2kupump) | PVP风险池 | Score 10; Tier Micro; LP $26.2K; Vol24H $1.11M; 24H +239.17%; V/LP 42.24x; 池数 4; 分项 L4/V14/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LCM](https://dexscreener.com/solana/8vqqurpphewfj3lrv7a2ggjszdsvzvwnxfmgpaml3ieb) | SOL | [6t4L25...CZpump](https://solscan.io/token/6t4L25gvgdLUMsSUkb4JS5sBpcYyt3eYHoxdusCZpump) | PVP风险池 | Score 5; Tier Micro; LP $27.3K; Vol24H $1.20M; 24H +247.00%; V/LP 43.87x; 池数 6; 分项 L4/V14/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Scatman](https://dexscreener.com/solana/bgnmzetqfn7sjccftnepogo222lagqeez3hqgp9kytsz) | SOL | [Cit4M3...mu4mgA](https://solscan.io/token/Cit4M38LLvYFX2EGFFyit83WEZ1GFN8PA3nF57mu4mgA) | PVP风险池 | Score 0; Tier Micro; LP $34.9K; Vol24H $1.69M; 24H +479.00%; V/LP 48.52x; 池数 4; 分项 L5/V15/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 46; Tier Early; LP $113.3K; Vol24H $28.12M; 24H -0.22%; V/LP 248.17x; 池数 1; 分项 L10/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [febu](https://dexscreener.com/solana/68nvmrvpyxgjgbgh2p92e93syhjcbe6qocizrqoqdjcb) | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $141.5K; Vol24H $5.74M; 24H -70.89%; V/LP 40.59x; 池数 2; 分项 L11/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 35; Tier Early; LP $617.5K; Vol24H $22.50M; 24H +105.16%; V/LP 36.44x; 池数 1; 分项 L16/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 34; Tier Early; LP $185.2K; Vol24H $15.68M; 24H -34.53%; V/LP 84.66x; 池数 1; 分项 L12/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [UNC](https://dexscreener.com/solana/ak3u4akfzqqfqthjsndbavicic8qwzxb9cfkcqeaux6) | SOL | [6MJEQQ...V1pump](https://solscan.io/token/6MJEQQB6wC6wpRrjni15Q7By9DrbdbRFeJU3xqV1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $34.3K; Vol24H $1.60M; 24H +449.00%; V/LP 46.70x; 池数 1; 分项 L5/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| PumpfunLife | SOL | [DpqGBm...kupump](https://solscan.io/token/DpqGBmkc6SrY2vA1Yb5KuH571WW1oQJjJdD3d2kupump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $26.2K; Vol24H $1.11M; 24H +239.17%; V/LP 42.24x; 池数 4; 分项 L4/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [LCM](https://dexscreener.com/solana/8vqqurpphewfj3lrv7a2ggjszdsvzvwnxfmgpaml3ieb) | SOL | [6t4L25...CZpump](https://solscan.io/token/6t4L25gvgdLUMsSUkb4JS5sBpcYyt3eYHoxdusCZpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 5; Tier Micro; LP $27.3K; Vol24H $1.20M; 24H +247.00%; V/LP 43.87x; 池数 6; 分项 L4/V14/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [Scatman](https://dexscreener.com/solana/bgnmzetqfn7sjccftnepogo222lagqeez3hqgp9kytsz) | SOL | [Cit4M3...mu4mgA](https://solscan.io/token/Cit4M38LLvYFX2EGFFyit83WEZ1GFN8PA3nF57mu4mgA) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $34.9K; Vol24H $1.69M; 24H +479.00%; V/LP 48.52x; 池数 4; 分项 L5/V15/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 80; Tier Mature; LP $220.02M; Vol24H $76.53M; 24H +2.53%; V/LP 0.35x; 池数 1; 分项 L20/V17/B22/Buy12/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.23M; Vol24H $4.13M; 24H -1.41%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.16M; Vol24H $6.20M; 24H -8.77%; V/LP 2.86x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BabyDoge | BSC | [0xc748...02e8de](https://bscscan.com/token/0xc748673057861a797275cd8a068abb95a902e8de) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 72; Tier Mature; LP $7.20M; Vol24H $1.34M; 24H -2.64%; V/LP 0.19x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ORCA](https://dexscreener.com/solana/bsymmryrrwe4ppludo2bsxcecunu77ytxnaaebgbznpj) | SOL | [orcaEK...kektZE](https://solscan.io/token/orcaEKTdK7LKz57vaAYr9QeNsVEPfiu6QeMU1kektZE) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $37.54M; Vol24H $81.17M; 24H +1.57%; V/LP 2.16x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.60M; Vol24H $55.76M; 24H +0.13%; V/LP 3.36x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $64.37M; Vol24H $27.83M; 24H +4.09%; V/LP 0.43x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SUNUSI](https://dexscreener.com/solana/5smcocy9fvw3g1apyzyhxd2ozyasewkozjmtgsphjsjg) | SOL | [2vvw3c...VWpump](https://solscan.io/token/2vvw3cSwibzGD6SgW9QzRaBdmjkYrvs218DUy6VWpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [febu](https://dexscreener.com/solana/68nvmrvpyxgjgbgh2p92e93syhjcbe6qocizrqoqdjcb) | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 10 / Liquid 2 / Mature 6 | 下一步可以按层级分别设置进攻规则 |
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
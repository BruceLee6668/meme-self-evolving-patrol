# 自我进化轮巡

**本轮时间 UTC：** 2026-08-24T20:22:40Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 113 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 176 |
| 合并后Token | 113 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 8 |
| 多池Token | 8 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 11 |
| Liquid层 | 5 |
| Mature层 | 3 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1089，刷新时间 2026-08-24T00:46:57Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 主观察 | Score 80; Tier Early; LP $195.8K; Vol24H $1.06M; 24H -6.74%; V/LP 5.43x; 池数 1; 分项 L12/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $1.34M; Vol24H $229.3K; 24H -9.25%; V/LP 0.17x; 池数 1; 分项 L20/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 次观察 | Score 74; Tier Early; LP $311.7K; Vol24H $2.43M; 24H +24.88%; V/LP 7.78x; 池数 1; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 68; Tier Liquid; LP $1.77M; Vol24H $17.78M; 24H +12.85%; V/LP 10.02x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | PVP风险池 | Score 48; Tier Early; LP $216.1K; Vol24H $5.46M; 24H -19.42%; V/LP 25.26x; 池数 1; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Morty | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 38; Tier Early; LP $139.3K; Vol24H $6.66M; 24H +53.13%; V/LP 47.82x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | PVP风险池 | Score 36; Tier Micro; LP $78.8K; Vol24H $5.35M; 24H -18.13%; V/LP 67.90x; 池数 2; 分项 L8/V17/B17/Buy3/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CVXV666 | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | PVP风险池 | Score 29; Tier Early; LP $133.8K; Vol24H $8.89M; 24H +768.88%; V/LP 66.47x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CATALORIAN | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | PVP风险池 | Score 29; Tier Micro; LP $50.1K; Vol24H $6.15M; 24H -97.95%; V/LP 122.57x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Polycat | SOL | [B4iCqV...QTpump](https://solscan.io/token/B4iCqVsAZv9dBiBVv58GJiBxWGmwkwbtPTn4sUQTpump) | PVP风险池 | Score 26; Tier Micro; LP $51.7K; Vol24H $5.74M; 24H +644.50%; V/LP 111.19x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $1.31M; Vol24H $248.2K; 24H -14.37%; V/LP 0.19x; 池数 1; 分项 L19/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 次观察 | Score 74; Tier Early; LP $317.8K; Vol24H $2.48M; 24H +17.74%; V/LP 7.81x; 池数 1; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 73; Tier Liquid; LP $1.74M; Vol24H $17.13M; 24H +3.66%; V/LP 9.83x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| UPS | BSC | [0xae5a...afba01](https://bscscan.com/token/0xae5a409773b9a7dd0ae94ff437ac213d8fafba01) | 次观察 | Score 68; Tier Early; LP $108.1K; Vol24H $54.1K; 24H -6.08%; V/LP 0.50x; 池数 1; 分项 L9/V5/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | PVP风险池 | Score 39; Tier Early; LP $203.3K; Vol24H $5.57M; 24H -35.40%; V/LP 27.43x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | PVP风险池 | Score 36; Tier Micro; LP $81.4K; Vol24H $5.15M; 24H -19.53%; V/LP 63.18x; 池数 4; 分项 L8/V17/B17/Buy3/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [GrokBot](https://dexscreener.com/solana/dsx8gy83k3bb7bsgcobrpvnpwyw7kkvrdmktx6tmnrqs) | SOL | [GeSfrQ...vSpump](https://solscan.io/token/GeSfrQiscfsEv4Hx2TKaB9Nfid12qND1YYRYS1vSpump) | PVP风险池 | Score 35; Tier Early; LP $192.7K; Vol24H $5.13M; 24H +11437.00%; V/LP 26.64x; 池数 1; 分项 L12/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Morty | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 30; Tier Early; LP $169.1K; Vol24H $6.88M; 24H +123.75%; V/LP 40.70x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CATALORIAN | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | PVP风险池 | Score 30; Tier Micro; LP $51.3K; Vol24H $6.01M; 24H -98.00%; V/LP 117.11x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | PVP风险池 | Score 29; Tier Early; LP $115.6K; Vol24H $9.20M; 24H +590.00%; V/LP 79.62x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Polycat | SOL | [B4iCqV...QTpump](https://solscan.io/token/B4iCqVsAZv9dBiBVv58GJiBxWGmwkwbtPTn4sUQTpump) | PVP风险池 | Score 27; Tier Micro; LP $65.6K; Vol24H $5.98M; 24H +1050.19%; V/LP 91.04x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MGNOPE](https://dexscreener.com/solana/75kdzn4frvnjvhcirw8tnbjzs7aai5tnyzwccychhmrh) | SOL | [6ABMQV...1ypump](https://solscan.io/token/6ABMQVGdHCzrmTdj31eZFctPtrsXT7LJZ8YGRc1ypump) | PVP风险池 | Score 26; Tier Micro; LP $61.3K; Vol24H $3.48M; 24H +945.00%; V/LP 56.76x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $18.27M; Vol24H $19.62M; 24H +1.77%; V/LP 1.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/eoftfbgdbxzkeqzc5dtygvnkicwevfezgtzqm9eftj6b) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 成熟池观察 | Score 71; Tier Mature; LP $71.45M; Vol24H $96.44M; 24H +0.70%; V/LP 1.35x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 成熟池观察 | Score 66; Tier Mature; LP $6.53M; Vol24H $4.49M; 24H -12.57%; V/LP 0.69x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Early; LP $203.3K; Vol24H $5.57M; 24H -35.40%; V/LP 27.43x; 池数 1; 分项 L12/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 36; Tier Micro; LP $81.4K; Vol24H $5.15M; 24H -19.53%; V/LP 63.18x; 池数 4; 分项 L8/V17/B17/Buy3/Risk-33 | 只记录热度，不进入主榜 |
| [GrokBot](https://dexscreener.com/solana/dsx8gy83k3bb7bsgcobrpvnpwyw7kkvrdmktx6tmnrqs) | SOL | [GeSfrQ...vSpump](https://solscan.io/token/GeSfrQiscfsEv4Hx2TKaB9Nfid12qND1YYRYS1vSpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 35; Tier Early; LP $192.7K; Vol24H $5.13M; 24H +11437.00%; V/LP 26.64x; 池数 1; 分项 L12/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| Morty | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $169.1K; Vol24H $6.88M; 24H +123.75%; V/LP 40.70x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CATALORIAN | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $51.3K; Vol24H $6.01M; 24H -98.00%; V/LP 117.11x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $115.6K; Vol24H $9.20M; 24H +590.00%; V/LP 79.62x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Polycat | SOL | [B4iCqV...QTpump](https://solscan.io/token/B4iCqVsAZv9dBiBVv58GJiBxWGmwkwbtPTn4sUQTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $65.6K; Vol24H $5.98M; 24H +1050.19%; V/LP 91.04x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MGNOPE](https://dexscreener.com/solana/75kdzn4frvnjvhcirw8tnbjzs7aai5tnyzwccychhmrh) | SOL | [6ABMQV...1ypump](https://solscan.io/token/6ABMQVGdHCzrmTdj31eZFctPtrsXT7LJZ8YGRc1ypump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $61.3K; Vol24H $3.48M; 24H +945.00%; V/LP 56.76x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.27M; Vol24H $19.62M; 24H +1.77%; V/LP 1.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/eoftfbgdbxzkeqzc5dtygvnkicwevfezgtzqm9eftj6b) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $71.45M; Vol24H $96.44M; 24H +0.70%; V/LP 1.35x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 66; Tier Mature; LP $6.53M; Vol24H $4.49M; 24H -12.57%; V/LP 0.69x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| DGAI | BSC | [0x10d4...8ebd5e](https://bscscan.com/token/0x10d4183389e99233db3cc981c43443ebd28ebd5e) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $2.78M; Vol24H $18.19M; 24H +671.49%; V/LP 6.54x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 58; Tier Early; LP $696.9K; Vol24H $7.80M; 24H -1.69%; V/LP 11.20x; 池数 1; 分项 L17/V17/B22/Buy8/Risk-30 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| UPS | BSC | [0xae5a...afba01](https://bscscan.com/token/0xae5a409773b9a7dd0ae94ff437ac213d8fafba01) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [GrokBot](https://dexscreener.com/solana/dsx8gy83k3bb7bsgcobrpvnpwyw7kkvrdmktx6tmnrqs) | SOL | [GeSfrQ...vSpump](https://solscan.io/token/GeSfrQiscfsEv4Hx2TKaB9Nfid12qND1YYRYS1vSpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Morty | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CATALORIAN | SOL | [4cvZwC...nFpump](https://solscan.io/token/4cvZwC17oMiUA7peKX5GhbaUWv4U5Lwrd8118xnFpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 11 / Liquid 5 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |

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
| dexscreener_boosts | {'ok': True, 'count': 0, 'expanded': 0} |
| dexscreener_search | {'ok': True, 'count': 306} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
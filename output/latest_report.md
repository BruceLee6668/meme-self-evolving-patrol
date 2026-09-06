# 自我进化轮巡

**本轮时间 UTC：** 2026-09-06T22:51:13Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 142 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 233 |
| 合并后Token | 142 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 4 |
| 多池Token | 5 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 2 |
| Early层 | 16 |
| Liquid层 | 6 |
| Mature层 | 1 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1174，刷新时间 2026-08-31T02:36:52Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 0 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 86; Tier Liquid; LP $3.34M; Vol24H $2.99M; 24H -13.44%; V/LP 0.90x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 79; Tier Early; LP $580.5K; Vol24H $1.11M; 24H -23.48%; V/LP 1.90x; 池数 1; 分项 L16/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 77; Tier Liquid; LP $1.90M; Vol24H $9.45M; 24H +27.92%; V/LP 4.97x; 池数 2; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAAR](https://dexscreener.com/solana/6hzduckrzgoj5ugz2vwwkd56odxzizwymen7ccf7hsky) | SOL | [8H5yfL...6ypump](https://solscan.io/token/8H5yfL1GoDETLDaLYZzrgQuZs37eiKJjdfP21b6ypump) | 次观察 | Score 73; Tier Micro; LP $80.5K; Vol24H $342.9K; 24H -4.91%; V/LP 4.26x; 池数 1; 分项 L8/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 71; Tier Early; LP $601.6K; Vol24H $1.72M; 24H -26.77%; V/LP 2.85x; 池数 1; 分项 L16/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 67; Tier Early; LP $423.1K; Vol24H $1.35M; 24H -36.71%; V/LP 3.20x; 池数 3; 分项 L15/V15/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPARK](https://dexscreener.com/bsc/0xbbd30e4c5877f76e188189ebfd968abc312022cf) | BSC | [0x6711...358888](https://bscscan.com/token/0x67118eC0BBc3F1E743009cECaF00A9Ca3D358888) | 次观察 | Score 65; Tier Early; LP $405.1K; Vol24H $7.5K; 24H +0.84%; V/LP 0.02x; 池数 1; 分项 L15/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SME](https://dexscreener.com/bsc/0xb293980374739cfe7b41bbe5f7be31ae86ff18a8) | BSC | [0x36dB...2a0C92](https://bscscan.com/token/0x36dBcBCA106353D49e1E0E8974492fFB862a0C92) | 次观察 | Score 65; Tier Early; LP $394.2K; Vol24H $0.00; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L15/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 次观察 | Score 65; Tier Early; LP $159.2K; Vol24H $1.04M; 24H -56.20%; V/LP 6.50x; 池数 1; 分项 L11/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | PVP风险池 | Score 50; Tier Early; LP $324.5K; Vol24H $9.71M; 24H -8.23%; V/LP 29.91x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 86; Tier Liquid; LP $1.91M; Vol24H $9.54M; 24H +24.47%; V/LP 4.99x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 86; Tier Liquid; LP $3.33M; Vol24H $2.86M; 24H -15.50%; V/LP 0.86x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 79; Tier Early; LP $577.1K; Vol24H $928.8K; 24H -12.40%; V/LP 1.61x; 池数 1; 分项 L16/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [MAGA](https://dexscreener.com/solana/hvimk99ygssdnwz9esqumdthrfz4dade7j6phmfms6at) | SOL | [Hon2rH...KCpump](https://solscan.io/token/Hon2rHAiqkcDtUzL5gA2vjXPr7T1MPCK2UT2AHKCpump) | 次观察 | Score 71; Tier Early; LP $126.9K; Vol24H $94.3K; 24H +4.64%; V/LP 0.74x; 池数 5; 分项 L10/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 次观察 | Score 71; Tier Early; LP $540.5K; Vol24H $1.65M; 24H -41.97%; V/LP 3.05x; 池数 1; 分项 L16/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 67; Tier Early; LP $412.3K; Vol24H $1.38M; 24H -33.38%; V/LP 3.34x; 池数 2; 分项 L15/V15/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPARK](https://dexscreener.com/bsc/0xbbd30e4c5877f76e188189ebfd968abc312022cf) | BSC | [0x6711...358888](https://bscscan.com/token/0x67118eC0BBc3F1E743009cECaF00A9Ca3D358888) | 次观察 | Score 65; Tier Early; LP $406.1K; Vol24H $7.6K; 24H +1.14%; V/LP 0.02x; 池数 1; 分项 L15/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SME](https://dexscreener.com/bsc/0xb293980374739cfe7b41bbe5f7be31ae86ff18a8) | BSC | [0x36dB...2a0C92](https://bscscan.com/token/0x36dBcBCA106353D49e1E0E8974492fFB862a0C92) | 次观察 | Score 65; Tier Early; LP $394.2K; Vol24H $0.00; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L15/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 次观察 | Score 65; Tier Early; LP $170.5K; Vol24H $1.03M; 24H -46.87%; V/LP 6.06x; 池数 1; 分项 L11/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | PVP风险池 | Score 51; Tier Early; LP $466.6K; Vol24H $12.27M; 24H -21.25%; V/LP 26.31x; 池数 1; 分项 L15/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | PVP风险池 | Score 49; Tier Early; LP $278.6K; Vol24H $10.09M; 24H -22.93%; V/LP 36.22x; 池数 1; 分项 L13/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | PVP风险池 | Score 37; Tier Liquid; LP $813.1K; Vol24H $42.09M; 24H +158986.77%; V/LP 51.76x; 池数 1; 分项 L18/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BEN | BSC | [0x7bc7...857777](https://bscscan.com/token/0x7bc70ae0f2a67d2fdc0180a697a611f21c857777) | PVP风险池 | Score 34; Tier Early; LP $485.7K; Vol24H $33.70M; 24H +19651.30%; V/LP 69.38x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PURR | SOL | [8RNUw4...E2NZHQ](https://solscan.io/token/8RNUw4N655VSrZKuhGdywhbSMDTrheguFPfxbpE2NZHQ) | PVP风险池 | Score 34; Tier Early; LP $435.8K; Vol24H $9.23M; 24H +463.98%; V/LP 21.19x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AGI | SOL | [CaWZeU...aM5o7h](https://solscan.io/token/CaWZeUM4FvX9dPkjGc2xHS6tSN3qJfTWyvaG77aM5o7h) | PVP风险池 | Score 33; Tier Early; LP $302.7K; Vol24H $9.76M; 24H +186.68%; V/LP 32.23x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Early; LP $466.6K; Vol24H $12.27M; 24H -21.25%; V/LP 26.31x; 池数 1; 分项 L15/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AST | BSC | [0x265b...4affff](https://bscscan.com/token/0x265b3982ea730748100947f52561a4eab54affff) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Early; LP $278.6K; Vol24H $10.09M; 24H -22.93%; V/LP 36.22x; 池数 1; 分项 L13/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 37; Tier Liquid; LP $813.1K; Vol24H $42.09M; 24H +158986.77%; V/LP 51.76x; 池数 1; 分项 L18/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BEN | BSC | [0x7bc7...857777](https://bscscan.com/token/0x7bc70ae0f2a67d2fdc0180a697a611f21c857777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $485.7K; Vol24H $33.70M; 24H +19651.30%; V/LP 69.38x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| PURR | SOL | [8RNUw4...E2NZHQ](https://solscan.io/token/8RNUw4N655VSrZKuhGdywhbSMDTrheguFPfxbpE2NZHQ) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $435.8K; Vol24H $9.23M; 24H +463.98%; V/LP 21.19x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AGI | SOL | [CaWZeU...aM5o7h](https://solscan.io/token/CaWZeUM4FvX9dPkjGc2xHS6tSN3qJfTWyvaG77aM5o7h) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $302.7K; Vol24H $9.76M; 24H +186.68%; V/LP 32.23x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 32; Tier Early; LP $704.7K; Vol24H $22.21M; 24H -25.66%; V/LP 31.51x; 池数 1; 分项 L17/V17/B8/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 29; Tier Early; LP $270.4K; Vol24H $333.09M; 24H +569.00%; V/LP 1231.70x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.81M; Vol24H $3.48M; 24H -10.79%; V/LP 1.24x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $26.40M; Vol24H $22.06M; 24H +0.29%; V/LP 0.84x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USELESS | SOL | [Dz9mQ9...8Mbonk](https://solscan.io/token/Dz9mQ9NzkBcCsuGPFJ3r1bS4wgqKMHBPiVuniW8Mbonk) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $4.65M; Vol24H $12.08M; 24H -18.37%; V/LP 2.60x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZCAT | SOL | [HcRLc9...qiDeJR](https://solscan.io/token/HcRLc9VDgjLeK154xDawfb1dmVJ98DoSqcwTHGqiDeJR) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $1.13M; Vol24H $7.99M; 24H +320.08%; V/LP 7.09x; 池数 1; 分项 L19/V17/B0/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [MAGA](https://dexscreener.com/solana/hvimk99ygssdnwz9esqumdthrfz4dade7j6phmfms6at) | SOL | [Hon2rH...KCpump](https://solscan.io/token/Hon2rHAiqkcDtUzL5gA2vjXPr7T1MPCK2UT2AHKCpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Max | BSC | [0xe9bc...f77777](https://bscscan.com/token/0xe9bc5c6a86caa44fd7b469bf3cc7c563e4f77777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPARK](https://dexscreener.com/bsc/0xbbd30e4c5877f76e188189ebfd968abc312022cf) | BSC | [0x6711...358888](https://bscscan.com/token/0x67118eC0BBc3F1E743009cECaF00A9Ca3D358888) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SME](https://dexscreener.com/bsc/0xb293980374739cfe7b41bbe5f7be31ae86ff18a8) | BSC | [0x36dB...2a0C92](https://bscscan.com/token/0x36dBcBCA106353D49e1E0E8974492fFB862a0C92) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 2 / Early 16 / Liquid 6 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_boosts | {'ok': True, 'count': 30, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 339} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
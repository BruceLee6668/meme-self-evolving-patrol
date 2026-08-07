# 自我进化轮巡

**本轮时间 UTC：** 2026-08-07T15:50:45Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 117 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 200 |
| 合并后Token | 117 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 7 |
| 多池Token | 7 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 2 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 主观察 | Score 83; Tier Early; LP $417.3K; Vol24H $1.08M; 24H +2.32%; V/LP 2.58x; 池数 2; 分项 L15/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 82; Tier Early; LP $528.2K; Vol24H $475.4K; 24H +4.07%; V/LP 0.90x; 池数 1; 分项 L16/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NEEGY | SOL | [6oGuFD...22pump](https://solscan.io/token/6oGuFDbEeaSzTcvrmmd2MqfNYwHKXFoN7regcR22pump) | 主观察 | Score 79; Tier Early; LP $149.3K; Vol24H $1.00M; 24H -5.32%; V/LP 6.72x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 78; Tier Early; LP $365.9K; Vol24H $1.45M; 24H +19.62%; V/LP 3.97x; 池数 1; 分项 L14/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 76; Tier Early; LP $266.2K; Vol24H $313.8K; 24H +20.16%; V/LP 1.18x; 池数 5; 分项 L13/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 76; Tier Liquid; LP $1.11M; Vol24H $162.0K; 24H +22.66%; V/LP 0.15x; 池数 1; 分项 L19/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 73; Tier Liquid; LP $1.98M; Vol24H $105.7K; 24H +4.41%; V/LP 0.05x; 池数 1; 分项 L20/V7/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 次观察 | Score 67; Tier Micro; LP $55.5K; Vol24H $174.4K; 24H -1.86%; V/LP 3.14x; 池数 3; 分项 L7/V9/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 次观察 | Score 66; Tier Early; LP $382.4K; Vol24H $2.24M; 24H +46.90%; V/LP 5.86x; 池数 1; 分项 L15/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KIO | SOL | [7rMnp9...7opump](https://solscan.io/token/7rMnp9EJd61SvNn8LGc7SAJeQxM36oeECKmP2a7opump) | PVP风险池 | Score 29; Tier Micro; LP $78.2K; Vol24H $2.07M; 24H -55.66%; V/LP 26.53x; 池数 2; 分项 L8/V16/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| NEEGY | SOL | [6oGuFD...22pump](https://solscan.io/token/6oGuFDbEeaSzTcvrmmd2MqfNYwHKXFoN7regcR22pump) | 主观察 | Score 79; Tier Early; LP $145.0K; Vol24H $963.8K; 24H -6.37%; V/LP 6.65x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 77; Tier Liquid; LP $1.06M; Vol24H $202.9K; 24H +12.66%; V/LP 0.19x; 池数 1; 分项 L19/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 73; Tier Liquid; LP $1.96M; Vol24H $107.4K; 24H +3.63%; V/LP 0.05x; 池数 1; 分项 L20/V7/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 次观察 | Score 72; Tier Early; LP $405.0K; Vol24H $842.2K; 24H +61.74%; V/LP 2.08x; 池数 1; 分项 L15/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 69; Tier Early; LP $372.0K; Vol24H $1.48M; 24H +33.55%; V/LP 3.98x; 池数 1; 分项 L14/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 次观察 | Score 68; Tier Liquid; LP $1.50M; Vol24H $25.62M; 24H +5.51%; V/LP 17.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 次观察 | Score 66; Tier Early; LP $404.3K; Vol24H $2.22M; 24H +44.00%; V/LP 5.50x; 池数 1; 分项 L15/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | PVP风险池 | Score 49; Tier Early; LP $249.2K; Vol24H $7.05M; 24H +7.68%; V/LP 28.29x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 34; Tier Micro; LP $80.6K; Vol24H $42.76M; 24H +0.79%; V/LP 530.44x; 池数 1; 分项 L8/V17/B22/Buy8/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bStocks | BSC | [0x244b...fd7777](https://bscscan.com/token/0x244b112cf746e62a5df723cbde9906a6defd7777) | PVP风险池 | Score 30; Tier Early; LP $149.4K; Vol24H $5.82M; 24H +3666.92%; V/LP 38.98x; 池数 4; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MRPOM](https://dexscreener.com/solana/f3suijht7xtzyggvmruz2vzuu3swz4jieozaum1dmqyj) | SOL | [6ZHyei...nUpump](https://solscan.io/token/6ZHyei7C4yZrJvsQeBHRDGD7HXpA28sWsTuY2rnUpump) | PVP风险池 | Score 30; Tier Micro; LP $65.5K; Vol24H $2.39M; 24H +2372.00%; V/LP 36.48x; 池数 1; 分项 L8/V16/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TINYTANK | SOL | [AA3VLt...Sbpump](https://solscan.io/token/AA3VLt3muGJiXedDaMnkcst3pfjrg1JBxgHVSdSbpump) | PVP风险池 | Score 27; Tier Micro; LP $68.6K; Vol24H $6.77M; 24H +104.40%; V/LP 98.68x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| goon | SOL | [3c32HT...ugpump](https://solscan.io/token/3c32HTEvDVQC71irgNwQ6HX69Kw387V1aWBn76ugpump) | PVP风险池 | Score 27; Tier Micro; LP $70.4K; Vol24H $3.15M; 24H +2467.79%; V/LP 44.71x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HTZ](https://dexscreener.com/solana/ckhpkgsmbvav5hmrfjnri9pjcsmubsgidffakmybisy3) | SOL | [EnA53N...Y3pump](https://solscan.io/token/EnA53NmMzfsAs7p44dATdvT55HHUACxpEbC9AKY3pump) | PVP风险池 | Score 26; Tier Micro; LP $54.4K; Vol24H $3.61M; 24H +1423.00%; V/LP 66.49x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Monkey | BSC | [0x684a...58c276](https://bscscan.com/token/0x684a1768c8d0098811017b7812c23978dd58c276) | PVP风险池 | Score 19; Tier Early; LP $199.8K; Vol24H $4.31M; 24H +84.88%; V/LP 21.58x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Early; LP $249.2K; Vol24H $7.05M; 24H +7.68%; V/LP 28.29x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 34; Tier Micro; LP $80.6K; Vol24H $42.76M; 24H +0.79%; V/LP 530.44x; 池数 1; 分项 L8/V17/B22/Buy8/Risk-45 | 只记录热度，不进入主榜 |
| bStocks | BSC | [0x244b...fd7777](https://bscscan.com/token/0x244b112cf746e62a5df723cbde9906a6defd7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $149.4K; Vol24H $5.82M; 24H +3666.92%; V/LP 38.98x; 池数 4; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MRPOM](https://dexscreener.com/solana/f3suijht7xtzyggvmruz2vzuu3swz4jieozaum1dmqyj) | SOL | [6ZHyei...nUpump](https://solscan.io/token/6ZHyei7C4yZrJvsQeBHRDGD7HXpA28sWsTuY2rnUpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $65.5K; Vol24H $2.39M; 24H +2372.00%; V/LP 36.48x; 池数 1; 分项 L8/V16/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| TINYTANK | SOL | [AA3VLt...Sbpump](https://solscan.io/token/AA3VLt3muGJiXedDaMnkcst3pfjrg1JBxgHVSdSbpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $68.6K; Vol24H $6.77M; 24H +104.40%; V/LP 98.68x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| goon | SOL | [3c32HT...ugpump](https://solscan.io/token/3c32HTEvDVQC71irgNwQ6HX69Kw387V1aWBn76ugpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $70.4K; Vol24H $3.15M; 24H +2467.79%; V/LP 44.71x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HTZ](https://dexscreener.com/solana/ckhpkgsmbvav5hmrfjnri9pjcsmubsgidffakmybisy3) | SOL | [EnA53N...Y3pump](https://solscan.io/token/EnA53NmMzfsAs7p44dATdvT55HHUACxpEbC9AKY3pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $54.4K; Vol24H $3.61M; 24H +1423.00%; V/LP 66.49x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Monkey | BSC | [0x684a...58c276](https://bscscan.com/token/0x684a1768c8d0098811017b7812c23978dd58c276) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 19; Tier Early; LP $199.8K; Vol24H $4.31M; 24H +84.88%; V/LP 21.58x; 池数 1; 分项 L12/V17/B0/Buy8/Risk-42 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 75; Tier Liquid; LP $1.94M; Vol24H $830.8K; 24H +5.82%; V/LP 0.43x; 池数 2; 分项 L20/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $17.82M; Vol24H $69.73M; 24H +0.05%; V/LP 3.91x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 60; Tier Mature; LP $8.06M; Vol24H $22.85M; 24H +35.90%; V/LP 2.84x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| NEEGY | SOL | [6oGuFD...22pump](https://solscan.io/token/6oGuFDbEeaSzTcvrmmd2MqfNYwHKXFoN7regcR22pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| bStocks | BSC | [0x244b...fd7777](https://bscscan.com/token/0x244b112cf746e62a5df723cbde9906a6defd7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| NEEGY | SOL | [6oGuFD...22pump](https://solscan.io/token/6oGuFDbEeaSzTcvrmmd2MqfNYwHKXFoN7regcR22pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 2 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 6 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
| emergency_precision_check_policy | 本轮出现满足LP、低波动、买盘占优、非多池冲突的高优先候选 | 下轮这类候选优先进入链上精查或AVE单币紧急刷新建议 |
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |
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
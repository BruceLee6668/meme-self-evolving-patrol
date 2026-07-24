# 自我进化轮巡

**本轮时间 UTC：** 2026-07-24T12:21:16Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 117 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 242 |
| 合并后Token | 117 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 4 |
| 多池Token | 4 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 4 |
| Liquid层 | 13 |
| Mature层 | 2 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 3 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 主观察 | Score 86; Tier Liquid; LP $760.3K; Vol24H $1.34M; 24H +2.31%; V/LP 1.76x; 池数 1; 分项 L17/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 85; Tier Liquid; LP $1.30M; Vol24H $6.28M; 24H -4.46%; V/LP 4.82x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 主观察 | Score 81; Tier Liquid; LP $1.42M; Vol24H $3.25M; 24H +16.30%; V/LP 2.29x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 主观察 | Score 79; Tier Liquid; LP $925.6K; Vol24H $6.76M; 24H +16.17%; V/LP 7.30x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 次观察 | Score 72; Tier Early; LP $119.2K; Vol24H $725.4K; 24H -13.67%; V/LP 6.09x; 池数 1; 分项 L10/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 71; Tier Micro; LP $74.8K; Vol24H $57.3K; 24H -4.14%; V/LP 0.77x; 池数 1; 分项 L8/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 53; Tier Early; LP $687.9K; Vol24H $18.42M; 24H -21.70%; V/LP 26.78x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | PVP风险池 | Score 39; Tier Micro; LP $76.8K; Vol24H $7.29M; 24H -13.22%; V/LP 94.94x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 28; Tier Liquid; LP $922.4K; Vol24H $111.45M; 24H +34.78%; V/LP 120.83x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | PVP风险池 | Score 28; Tier Early; LP $104.3K; Vol24H $7.35M; 24H +4002.17%; V/LP 70.47x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 主观察 | Score 86; Tier Liquid; LP $760.0K; Vol24H $1.35M; 24H +4.48%; V/LP 1.78x; 池数 1; 分项 L17/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 主观察 | Score 86; Tier Liquid; LP $1.42M; Vol24H $3.66M; 24H +6.78%; V/LP 2.58x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 85; Tier Liquid; LP $1.31M; Vol24H $5.89M; 24H -7.22%; V/LP 4.50x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 主观察 | Score 79; Tier Liquid; LP $941.5K; Vol24H $7.08M; 24H +19.37%; V/LP 7.52x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 主观察 | Score 77; Tier Early; LP $119.3K; Vol24H $713.2K; 24H -7.26%; V/LP 5.98x; 池数 1; 分项 L10/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 72; Tier Micro; LP $75.4K; Vol24H $64.0K; 24H -2.25%; V/LP 0.85x; 池数 1; 分项 L8/V6/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.48M; Vol24H $675.33; 24H -0.03%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 次观察 | Score 69; Tier Liquid; LP $1.15M; Vol24H $30.05; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 53; Tier Early; LP $695.4K; Vol24H $18.35M; 24H -16.97%; V/LP 26.39x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | PVP风险池 | Score 39; Tier Micro; LP $76.4K; Vol24H $7.25M; 24H -19.96%; V/LP 94.85x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 28; Tier Liquid; LP $933.5K; Vol24H $110.13M; 24H +39.23%; V/LP 117.98x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | PVP风险池 | Score 28; Tier Early; LP $100.4K; Vol24H $7.54M; 24H +3544.76%; V/LP 75.16x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [claude](https://dexscreener.com/solana/7mo21dzam5mfa7aeqwjxopbel1xxzmdiexcd6hbvgv7y) | SOL | [BNRA5V...WMpump](https://solscan.io/token/BNRA5VFv769VGtb3Yw71Dcfs5dv56kaomtwiXcWMpump) | PVP风险池 | Score 19; Tier Micro; LP $17.4K; Vol24H $6.52M; 24H +27.53%; V/LP 375.85x; 池数 4; 分项 L2/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| RDLN | SOL | [HzdLSN...hGpump](https://solscan.io/token/HzdLSN25vVoPJQkdEV8nipBeVmKwc4RrHKYzCxhGpump) | PVP风险池 | Score 17; Tier Micro; LP $7.0K; Vol24H $12.43M; 24H -79.41%; V/LP 1764.75x; 池数 1; 分项 L0/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PUNY](https://dexscreener.com/solana/cx2nd2dg87tahma6hzotwhldxar468huswjeqh679dub) | SOL | [EknkqZ...QL1oYK](https://solscan.io/token/EknkqZDCFmCcn7keKVqb26PBJXtxFLgz8qguyaQL1oYK) | PVP风险池 | Score 7; Tier Micro; LP $45.1K; Vol24H $5.42M; 24H +746.00%; V/LP 120.25x; 池数 1; 分项 L6/V17/B0/Buy0/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 53; Tier Early; LP $695.4K; Vol24H $18.35M; 24H -16.97%; V/LP 26.39x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Micro; LP $76.4K; Vol24H $7.25M; 24H -19.96%; V/LP 94.85x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 28; Tier Liquid; LP $933.5K; Vol24H $110.13M; 24H +39.23%; V/LP 117.98x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| looong | SOL | [AkchGA...6wpump](https://solscan.io/token/AkchGAUdXXRGHt3HXaHbTvw3JLGUwtJRmYnkG66wpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $100.4K; Vol24H $7.54M; 24H +3544.76%; V/LP 75.16x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [claude](https://dexscreener.com/solana/7mo21dzam5mfa7aeqwjxopbel1xxzmdiexcd6hbvgv7y) | SOL | [BNRA5V...WMpump](https://solscan.io/token/BNRA5VFv769VGtb3Yw71Dcfs5dv56kaomtwiXcWMpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $17.4K; Vol24H $6.52M; 24H +27.53%; V/LP 375.85x; 池数 4; 分项 L2/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| RDLN | SOL | [HzdLSN...hGpump](https://solscan.io/token/HzdLSN25vVoPJQkdEV8nipBeVmKwc4RrHKYzCxhGpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $7.0K; Vol24H $12.43M; 24H -79.41%; V/LP 1764.75x; 池数 1; 分项 L0/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [PUNY](https://dexscreener.com/solana/cx2nd2dg87tahma6hzotwhldxar468huswjeqh679dub) | SOL | [EknkqZ...QL1oYK](https://solscan.io/token/EknkqZDCFmCcn7keKVqb26PBJXtxFLgz8qguyaQL1oYK) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；LP偏薄；Volume/LP极端偏高 | Score 7; Tier Micro; LP $45.1K; Vol24H $5.42M; 24H +746.00%; V/LP 120.25x; 池数 1; 分项 L6/V17/B0/Buy0/Risk-40 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 4; Tier Micro; LP $77.8K; Vol24H $77.14M; 24H -99.98%; V/LP 991.18x; 池数 1; 分项 L8/V17/B0/Buy0/Risk-45 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 77; Tier Mature; LP $20.01M; Vol24H $345.8K; 24H +0.60%; V/LP 0.02x; 池数 1; 分项 L20/V11/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 77; Tier Liquid; LP $1.92M; Vol24H $1.78M; 24H -2.06%; V/LP 0.93x; 池数 2; 分项 L20/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.68M; Vol24H $78.81M; 24H -0.04%; V/LP 4.72x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.40M; Vol24H $4.75M; 24H -9.59%; V/LP 3.40x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| VELVET | BSC | [0x8b19...8c1488](https://bscscan.com/token/0x8b194370825e37b33373e74a41009161808c1488) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 64; Tier Liquid; LP $2.09M; Vol24H $603.9K; 24H -9.93%; V/LP 0.29x; 池数 1; 分项 L20/V12/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BILL | BSC | [0xdf24...fc1fa5](https://bscscan.com/token/0xdf24f8c21cb404b3031a450d8e049d6e39fc1fa5) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 4 / Liquid 13 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 337} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
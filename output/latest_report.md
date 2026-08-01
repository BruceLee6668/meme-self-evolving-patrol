# 自我进化轮巡

**本轮时间 UTC：** 2026-08-01T05:50:21Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 137 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 250 |
| 合并后Token | 137 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 8 |
| 多池Token | 4 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 10 |
| Early层 | 8 |
| Liquid层 | 6 |
| Mature层 | 1 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 782，刷新时间 2026-07-27T02:07:24Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 81; Tier Early; LP $496.6K; Vol24H $2.38M; 24H +17.75%; V/LP 4.79x; 池数 1; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 主观察 | Score 77; Tier Liquid; LP $2.40M; Vol24H $15.13M; 24H +44.28%; V/LP 6.31x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 71; Tier Early; LP $356.4K; Vol24H $2.77M; 24H +54.37%; V/LP 7.79x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 次观察 | Score 68; Tier Liquid; LP $4.20M; Vol24H $62.51M; 24H -0.78%; V/LP 14.87x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 次观察 | Score 66; Tier Liquid; LP $1.03M; Vol24H $12.55M; 24H +3.57%; V/LP 12.20x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 次观察 | Score 65; Tier Early; LP $676.8K; Vol24H $12.46M; 24H -2.55%; V/LP 18.41x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 次观察 | Score 65; Tier Early; LP $182.1K; Vol24H $724.4K; 24H -33.53%; V/LP 3.98x; 池数 1; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WMTX | BSC | [0xdbb5...5439d7](https://bscscan.com/token/0xdbb5cf12408a3ac17d668037ce289f9ea75439d7) | 次观察 | Score 65; Tier Early; LP $690.0K; Vol24H $2.42M; 24H +100.84%; V/LP 3.51x; 池数 1; 分项 L17/V16/B0/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 39; Tier Micro; LP $71.9K; Vol24H $2.68M; 24H -17.46%; V/LP 37.23x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CALLCAT | SOL | [DTiLUG...tKpump](https://solscan.io/token/DTiLUGhzmtP3wZC6tXRXtxYPUxztvnQMxAW54ZtKpump) | PVP风险池 | Score 31; Tier Micro; LP $34.1K; Vol24H $5.16M; 24H -18.31%; V/LP 151.36x; 池数 2; 分项 L5/V17/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 主观察 | Score 86; Tier Liquid; LP $2.47M; Vol24H $14.98M; 24H +21.43%; V/LP 6.06x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 81; Tier Early; LP $489.2K; Vol24H $2.53M; 24H +18.72%; V/LP 5.16x; 池数 1; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [KET](https://dexscreener.com/solana/fex8csknxfaxaprqqarkgchyamvfwdg28sfmbxxgkngx) | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 主观察 | Score 77; Tier Early; LP $248.5K; Vol24H $1.34M; 24H +2.28%; V/LP 5.38x; 池数 1; 分项 L13/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WMTX | BSC | [0xdbb5...5439d7](https://bscscan.com/token/0xdbb5cf12408a3ac17d668037ce289f9ea75439d7) | 次观察 | Score 74; Tier Early; LP $642.4K; Vol24H $2.57M; 24H +74.77%; V/LP 4.00x; 池数 1; 分项 L17/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 次观察 | Score 68; Tier Liquid; LP $4.21M; Vol24H $59.73M; 24H -0.45%; V/LP 14.17x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 次观察 | Score 67; Tier Liquid; LP $1.03M; Vol24H $12.42M; 24H +6.26%; V/LP 12.03x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PIPECATE](https://dexscreener.com/solana/43lwefnqkhg49dg8vikuwnop5yxm5k1xx7sxwxee66iw) | SOL | [42dZuV...eYpump](https://solscan.io/token/42dZuV3YwxJonjqLLTyhK4phKRJSQ3UFKjTzmDeYpump) | PVP风险池 | Score 46; Tier Micro; LP $63.9K; Vol24H $2.22M; 24H +18.84%; V/LP 34.77x; 池数 2; 分项 L7/V16/B17/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 39; Tier Micro; LP $73.4K; Vol24H $2.58M; 24H -10.02%; V/LP 35.07x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 35; Tier Micro; LP $87.2K; Vol24H $44.44M; 24H +2.94%; V/LP 509.43x; 池数 1; 分项 L9/V17/B22/Buy8/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | PVP风险池 | Score 33; Tier Early; LP $351.8K; Vol24H $16.89M; 24H +21663.26%; V/LP 48.00x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| XAUt | BSC | [0x21ca...96a3bf](https://bscscan.com/token/0x21caef8a43163eea865baee23b9c2e327696a3bf) | PVP风险池 | Score 33; Tier Micro; LP $89.2K; Vol24H $5.75M; 24H -0.72%; V/LP 64.47x; 池数 1; 分项 L9/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [OnlyMarms](https://dexscreener.com/solana/fxak2fgjjxy1e4rpqcjeaamurcnjyjoshyvgtyq9ucn9) | SOL | [HBrfYZ...espump](https://solscan.io/token/HBrfYZgeLKdSvBBGnGkvAK4563pq8oBGpgNFAaespump) | PVP风险池 | Score 27; Tier Micro; LP $74.9K; Vol24H $3.23M; 24H +302.00%; V/LP 43.08x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CALLCAT](https://dexscreener.com/solana/3rwcsxhk8qazbmpbbpni9bmuzcrvgak7pwazkxc3gtzk) | SOL | [DTiLUG...tKpump](https://solscan.io/token/DTiLUGhzmtP3wZC6tXRXtxYPUxztvnQMxAW54ZtKpump) | PVP风险池 | Score 16; Tier Micro; LP $33.8K; Vol24H $1.92M; 24H -70.52%; V/LP 56.88x; 池数 1; 分项 L5/V16/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MOONDOGECOIN | SOL | [AYJ1tY...pxpump](https://solscan.io/token/AYJ1tYQZZJ1gmZhURYuXLwG9bygUcgBnYPzriLpxpump) | PVP风险池 | Score 10; Tier Micro; LP $12.6K; Vol24H $2.67M; 24H -99.87%; V/LP 212.34x; 池数 1; 分项 L1/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 75; Tier Liquid; LP $1.93M; Vol24H $782.9K; 24H +0.82%; V/LP 0.41x; 池数 2; 分项 L20/V13/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PIPECATE](https://dexscreener.com/solana/43lwefnqkhg49dg8vikuwnop5yxm5k1xx7sxwxee66iw) | SOL | [42dZuV...eYpump](https://solscan.io/token/42dZuV3YwxJonjqLLTyhK4phKRJSQ3UFKjTzmDeYpump) | 24H波动可控；买入笔数占优；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 46; Tier Micro; LP $63.9K; Vol24H $2.22M; 24H +18.84%; V/LP 34.77x; 池数 2; 分项 L7/V16/B17/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Micro; LP $73.4K; Vol24H $2.58M; 24H -10.02%; V/LP 35.07x; 池数 1; 分项 L8/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 35; Tier Micro; LP $87.2K; Vol24H $44.44M; 24H +2.94%; V/LP 509.43x; 池数 1; 分项 L9/V17/B22/Buy8/Risk-45 | 只记录热度，不进入主榜 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $351.8K; Vol24H $16.89M; 24H +21663.26%; V/LP 48.00x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| XAUt | BSC | [0x21ca...96a3bf](https://bscscan.com/token/0x21caef8a43163eea865baee23b9c2e327696a3bf) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；市值超过早期Alpha主榜上限 | Score 33; Tier Micro; LP $89.2K; Vol24H $5.75M; 24H -0.72%; V/LP 64.47x; 池数 1; 分项 L9/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [OnlyMarms](https://dexscreener.com/solana/fxak2fgjjxy1e4rpqcjeaamurcnjyjoshyvgtyq9ucn9) | SOL | [HBrfYZ...espump](https://solscan.io/token/HBrfYZgeLKdSvBBGnGkvAK4563pq8oBGpgNFAaespump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $74.9K; Vol24H $3.23M; 24H +302.00%; V/LP 43.08x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CALLCAT](https://dexscreener.com/solana/3rwcsxhk8qazbmpbbpni9bmuzcrvgak7pwazkxc3gtzk) | SOL | [DTiLUG...tKpump](https://solscan.io/token/DTiLUGhzmtP3wZC6tXRXtxYPUxztvnQMxAW54ZtKpump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $33.8K; Vol24H $1.92M; 24H -70.52%; V/LP 56.88x; 池数 1; 分项 L5/V16/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| MOONDOGECOIN | SOL | [AYJ1tY...pxpump](https://solscan.io/token/AYJ1tYQZZJ1gmZhURYuXLwG9bygUcgBnYPzriLpxpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $12.6K; Vol24H $2.67M; 24H -99.87%; V/LP 212.34x; 池数 1; 分项 L1/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 75; Tier Liquid; LP $1.93M; Vol24H $782.9K; 24H +0.82%; V/LP 0.41x; 池数 2; 分项 L20/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 72; Tier Mature; LP $10.55M; Vol24H $1.64M; 24H +0.14%; V/LP 0.16x; 池数 5; 分项 L20/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 61; Tier Liquid; LP $1.91M; Vol24H $23.27M; 24H -4.84%; V/LP 12.21x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-30 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [KET](https://dexscreener.com/solana/fex8csknxfaxaprqqarkgchyamvfwdg28sfmbxxgkngx) | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WMTX | BSC | [0xdbb5...5439d7](https://bscscan.com/token/0xdbb5cf12408a3ac17d668037ce289f9ea75439d7) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PIPECATE](https://dexscreener.com/solana/43lwefnqkhg49dg8vikuwnop5yxm5k1xx7sxwxee66iw) | SOL | [42dZuV...eYpump](https://solscan.io/token/42dZuV3YwxJonjqLLTyhK4phKRJSQ3UFKjTzmDeYpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| ASTEROID | BSC | [0x3309...db7777](https://bscscan.com/token/0x330990dae53bca4c5811c5362b44c33a47db7777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [KET](https://dexscreener.com/solana/fex8csknxfaxaprqqarkgchyamvfwdg28sfmbxxgkngx) | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 10 / Early 8 / Liquid 6 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
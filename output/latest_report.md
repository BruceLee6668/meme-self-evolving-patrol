# 自我进化轮巡

**本轮时间 UTC：** 2026-08-06T02:02:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 117 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 214 |
| 合并后Token | 117 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 5 |
| 多池Token | 9 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 11 |
| Liquid层 | 4 |
| Mature层 | 2 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 主观察 | Score 86; Tier Early; LP $472.4K; Vol24H $3.10M; 24H -4.32%; V/LP 6.57x; 池数 2; 分项 L15/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 主观察 | Score 82; Tier Early; LP $591.3K; Vol24H $3.99M; 24H -12.44%; V/LP 6.76x; 池数 1; 分项 L16/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 次观察 | Score 73; Tier Early; LP $124.2K; Vol24H $59.4K; 24H -0.58%; V/LP 0.48x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 次观察 | Score 72; Tier Early; LP $103.7K; Vol24H $60.4K; 24H -3.28%; V/LP 0.58x; 池数 1; 分项 L9/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 68; Tier Early; LP $314.6K; Vol24H $1.03M; 24H -27.94%; V/LP 3.28x; 池数 1; 分项 L14/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 65; Tier Early; LP $727.7K; Vol24H $10.72M; 24H -9.79%; V/LP 14.74x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 65; Tier Early; LP $113.1K; Vol24H $64.5K; 24H -18.54%; V/LP 0.57x; 池数 5; 分项 L10/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 次观察 | Score 65; Tier Micro; LP $72.1K; Vol24H $79.5K; 24H +0.14%; V/LP 1.10x; 池数 2; 分项 L8/V6/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 37; Tier Early; LP $129.2K; Vol24H $3.74M; 24H -42.70%; V/LP 28.98x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SISYPUSS](https://dexscreener.com/solana/6179hmyugysew9vmwaczxbbzd4dtf1w6z9s9yk3a9lkg) | SOL | [8HykgZ...xmpump](https://solscan.io/token/8HykgZKXNpMhfxQtDPb7AayRKJonZaQ8Mw1Xo3xmpump) | PVP风险池 | Score 34; Tier Micro; LP $53.5K; Vol24H $3.36M; 24H +66.32%; V/LP 62.84x; 池数 1; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 主观察 | Score 86; Tier Early; LP $475.5K; Vol24H $3.05M; 24H -6.26%; V/LP 6.41x; 池数 2; 分项 L15/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 主观察 | Score 82; Tier Early; LP $570.8K; Vol24H $3.57M; 24H -11.36%; V/LP 6.25x; 池数 1; 分项 L16/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 76; Tier Early; LP $320.9K; Vol24H $870.2K; 24H -11.70%; V/LP 2.71x; 池数 1; 分项 L14/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 次观察 | Score 73; Tier Early; LP $125.2K; Vol24H $58.7K; 24H -0.16%; V/LP 0.47x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 次观察 | Score 65; Tier Early; LP $738.0K; Vol24H $8.65M; 24H -19.35%; V/LP 11.73x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 次观察 | Score 65; Tier Micro; LP $71.7K; Vol24H $80.7K; 24H -0.57%; V/LP 1.13x; 池数 4; 分项 L8/V6/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 次观察 | Score 65; Tier Early; LP $684.0K; Vol24H $8.28M; 24H +6.85%; V/LP 12.10x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 37; Tier Early; LP $111.0K; Vol24H $3.45M; 24H -60.28%; V/LP 31.13x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 30; Tier Liquid; LP $1.96M; Vol24H $58.83M; 24H +41.29%; V/LP 29.95x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [KIO](https://dexscreener.com/solana/ccye73oa7dqrcs16fht3twevnhtlzrqzwn4c8smdxfwq) | SOL | [7rMnp9...7opump](https://solscan.io/token/7rMnp9EJd61SvNn8LGc7SAJeQxM36oeECKmP2a7opump) | PVP风险池 | Score 29; Tier Early; LP $123.0K; Vol24H $5.27M; 24H +1280.00%; V/LP 42.85x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | PVP风险池 | Score 28; Tier Early; LP $353.9K; Vol24H $9.02M; 24H +130.05%; V/LP 25.47x; 池数 1; 分项 L14/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PEEKO](https://dexscreener.com/solana/ejnl5crs31triyusokli4nuq8ncy1vkybtaxfkxw8phx) | SOL | [Yv2taG...Rqpump](https://solscan.io/token/Yv2taGqRuL9YNrWEGW5Tz9EuYjNzVikEspKzaRqpump) | PVP风险池 | Score 17; Tier Micro; LP $32.2K; Vol24H $2.11M; 24H +406.00%; V/LP 65.53x; 池数 1; 分项 L5/V16/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TikTok | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | PVP风险池 | Score 16; Tier Micro; LP $43.3K; Vol24H $1.43M; 24H -70.35%; V/LP 33.11x; 池数 7; 分项 L6/V15/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SISYPUSS](https://dexscreener.com/solana/6179hmyugysew9vmwaczxbbzd4dtf1w6z9s9yk3a9lkg) | SOL | [8HykgZ...xmpump](https://solscan.io/token/8HykgZKXNpMhfxQtDPb7AayRKJonZaQ8Mw1Xo3xmpump) | PVP风险池 | Score 15; Tier Micro; LP $47.8K; Vol24H $3.32M; 24H +159.00%; V/LP 69.60x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LARP](https://dexscreener.com/solana/fzgkrs9xiy7sdodyglb7rhnwwbhdpx9ehgmhgdvpyixr) | SOL | [Aq2idw...F1pump](https://solscan.io/token/Aq2idw7BeJX2WfNek6jGnp1z2s79CpFYZXo2zCF1pump) | PVP风险池 | Score 12; Tier Micro; LP $30.0K; Vol24H $2.53M; 24H +327.00%; V/LP 84.49x; 池数 1; 分项 L4/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $111.0K; Vol24H $3.45M; 24H -60.28%; V/LP 31.13x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $1.96M; Vol24H $58.83M; 24H +41.29%; V/LP 29.95x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [KIO](https://dexscreener.com/solana/ccye73oa7dqrcs16fht3twevnhtlzrqzwn4c8smdxfwq) | SOL | [7rMnp9...7opump](https://solscan.io/token/7rMnp9EJd61SvNn8LGc7SAJeQxM36oeECKmP2a7opump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $123.0K; Vol24H $5.27M; 24H +1280.00%; V/LP 42.85x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $353.9K; Vol24H $9.02M; 24H +130.05%; V/LP 25.47x; 池数 1; 分项 L14/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [PEEKO](https://dexscreener.com/solana/ejnl5crs31triyusokli4nuq8ncy1vkybtaxfkxw8phx) | SOL | [Yv2taG...Rqpump](https://solscan.io/token/Yv2taGqRuL9YNrWEGW5Tz9EuYjNzVikEspKzaRqpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $32.2K; Vol24H $2.11M; 24H +406.00%; V/LP 65.53x; 池数 1; 分项 L5/V16/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| TikTok | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $43.3K; Vol24H $1.43M; 24H -70.35%; V/LP 33.11x; 池数 7; 分项 L6/V15/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [SISYPUSS](https://dexscreener.com/solana/6179hmyugysew9vmwaczxbbzd4dtf1w6z9s9yk3a9lkg) | SOL | [8HykgZ...xmpump](https://solscan.io/token/8HykgZKXNpMhfxQtDPb7AayRKJonZaQ8Mw1Xo3xmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $47.8K; Vol24H $3.32M; 24H +159.00%; V/LP 69.60x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [LARP](https://dexscreener.com/solana/fzgkrs9xiy7sdodyglb7rhnwwbhdpx9ehgmhgdvpyixr) | SOL | [Aq2idw...F1pump](https://solscan.io/token/Aq2idw7BeJX2WfNek6jGnp1z2s79CpFYZXo2zCF1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $30.0K; Vol24H $2.53M; 24H +327.00%; V/LP 84.49x; 池数 1; 分项 L4/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $1.88M; Vol24H $831.1K; 24H -0.12%; V/LP 0.44x; 池数 2; 分项 L20/V13/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 74; Tier Mature; LP $6.21M; Vol24H $13.81M; 24H +3.46%; V/LP 2.22x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $4.22M; Vol24H $24.05M; 24H -6.10%; V/LP 5.70x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $17.37M; Vol24H $88.32M; 24H -0.00%; V/LP 5.09x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.51M; Vol24H $4.46M; 24H +23.95%; V/LP 2.96x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 11 / Liquid 4 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 346} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
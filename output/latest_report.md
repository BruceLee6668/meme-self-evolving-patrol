# 自我进化轮巡

**本轮时间 UTC：** 2026-07-11T17:50:45Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 113 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 235 |
| 合并后Token | 113 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 3 |
| 多池Token | 6 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 6 |
| Mature层 | 4 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 86; Tier Liquid; LP $1.33M; Vol24H $7.40M; 24H -2.54%; V/LP 5.55x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 主观察 | Score 80; Tier Early; LP $651.8K; Vol24H $1.11M; 24H -17.48%; V/LP 1.71x; 池数 1; 分项 L17/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAYLOR](https://dexscreener.com/solana/5yoaqpw38jfhslj8cmd2zj7ksjajbzhtpv1kx9fjekzv) | SOL | [BGwYnD...Pdpump](https://solscan.io/token/BGwYnDVe18aj9cozWcKNhiTUwayELULg5rHLGPPdpump) | 次观察 | Score 71; Tier Early; LP $161.2K; Vol24H $404.3K; 24H -19.72%; V/LP 2.51x; 池数 1; 分项 L11/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [NIGGABULL](https://dexscreener.com/solana/985nrfke9yhrwmpvpw7gcje1jr7wtddnyzb4qcnzeq15) | SOL | [77x1fC...Vfpump](https://solscan.io/token/77x1fCskDLaiZmm2uZKEhARSCD2B86VaahTkK2Vfpump) | 次观察 | Score 67; Tier Micro; LP $75.2K; Vol24H $313.8K; 24H -11.13%; V/LP 4.17x; 池数 2; 分项 L8/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 次观察 | Score 67; Tier Early; LP $143.5K; Vol24H $638.8K; 24H -13.48%; V/LP 4.45x; 池数 1; 分项 L11/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 67; Tier Early; LP $223.0K; Vol24H $1.32M; 24H -34.34%; V/LP 5.92x; 池数 1; 分项 L12/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| world | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | 次观察 | Score 67; Tier Early; LP $180.5K; Vol24H $407.2K; 24H -15.85%; V/LP 2.26x; 池数 1; 分项 L12/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| NORMIE | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | 次观察 | Score 66; Tier Early; LP $251.6K; Vol24H $863.1K; 24H +34.17%; V/LP 3.43x; 池数 2; 分项 L13/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Loom](https://dexscreener.com/solana/cyocg3bh5mfxk8mhublycixpbfnnu2qxmwfd1tmfkq7k) | SOL | [CgnQ8a...kYpump](https://solscan.io/token/CgnQ8a1u99Gk7qoySMd2wrGPMPm9bdcSJNhqMEkYpump) | PVP风险池 | Score 49; Tier Micro; LP $82.3K; Vol24H $3.02M; 24H +2.03%; V/LP 36.74x; 池数 2; 分项 L8/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CASHCAT](https://dexscreener.com/solana/9asrux6bowivf5mjfbuus1bpszqvoajmftkhpdqvkojx) | SOL | [3grmUL...nFpump](https://solscan.io/token/3grmULXrnQyN2A5LFStKFeSQsWvZjzNDsDVVLknFpump) | PVP风险池 | Score 33; Tier Micro; LP $52.9K; Vol24H $2.13M; 24H -71.37%; V/LP 40.24x; 池数 2; 分项 L7/V16/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 86; Tier Liquid; LP $1.34M; Vol24H $7.38M; 24H -3.73%; V/LP 5.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [NORMIE](https://dexscreener.com/solana/8n544cg9j44dkzu4cjswhxpwekxhqptr4r17kw9y5fbk) | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | 主观察 | Score 80; Tier Early; LP $236.5K; Vol24H $873.9K; 24H +0.93%; V/LP 3.70x; 池数 1; 分项 L13/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 主观察 | Score 80; Tier Early; LP $670.2K; Vol24H $1.07M; 24H -18.11%; V/LP 1.60x; 池数 1; 分项 L17/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAYLOR](https://dexscreener.com/solana/5yoaqpw38jfhslj8cmd2zj7ksjajbzhtpv1kx9fjekzv) | SOL | [BGwYnD...Pdpump](https://solscan.io/token/BGwYnDVe18aj9cozWcKNhiTUwayELULg5rHLGPPdpump) | 次观察 | Score 71; Tier Early; LP $160.7K; Vol24H $375.0K; 24H -21.67%; V/LP 2.33x; 池数 1; 分项 L11/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 66; Tier Early; LP $221.0K; Vol24H $1.29M; 24H -31.28%; V/LP 5.84x; 池数 1; 分项 L12/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 66; Tier Early; LP $151.2K; Vol24H $67.4K; 24H -14.03%; V/LP 0.45x; 池数 1; 分项 L11/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| world | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | 次观察 | Score 66; Tier Early; LP $175.4K; Vol24H $414.3K; 24H -21.07%; V/LP 2.36x; 池数 1; 分项 L11/V11/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Loom | SOL | [CgnQ8a...kYpump](https://solscan.io/token/CgnQ8a1u99Gk7qoySMd2wrGPMPm9bdcSJNhqMEkYpump) | PVP风险池 | Score 43; Tier Micro; LP $72.4K; Vol24H $2.51M; 24H -16.83%; V/LP 34.65x; 池数 2; 分项 L8/V16/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | PVP风险池 | Score 27; Tier Early; LP $248.9K; Vol24H $7.24M; 24H +135.25%; V/LP 29.07x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CASHCAT](https://dexscreener.com/solana/9asrux6bowivf5mjfbuus1bpszqvoajmftkhpdqvkojx) | SOL | [3grmUL...nFpump](https://solscan.io/token/3grmULXrnQyN2A5LFStKFeSQsWvZjzNDsDVVLknFpump) | PVP风险池 | Score 22; Tier Micro; LP $48.1K; Vol24H $2.07M; 24H -71.50%; V/LP 43.02x; 池数 1; 分项 L6/V16/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| reptilecoin | SOL | [BtUiqG...U9pump](https://solscan.io/token/BtUiqGdsW3H47yvtyKSLhQfzVpwov3wyYY6qssU9pump) | PVP风险池 | Score 16; Tier Micro; LP $32.1K; Vol24H $2.17M; 24H -57.23%; V/LP 67.54x; 池数 2; 分项 L5/V16/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LIZARD](https://dexscreener.com/solana/5sgh3r8p76vchzzy1pxrwcelbehzxbrx1dbnzvlvdfsh) | SOL | [7NTs9F...dwpump](https://solscan.io/token/7NTs9FPw7tP2Bfjcn8eAJZUr4ApG8n9ZbXkT7Adwpump) | PVP风险池 | Score 14; Tier Micro; LP $25.1K; Vol24H $1.24M; 24H +193.00%; V/LP 49.32x; 池数 1; 分项 L4/V14/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [GHOSTI](https://dexscreener.com/solana/5xq1qzhbb3gu8bas7sdmtnnnxjuyffkoeyhx5zhhbvbu) | SOL | [6hKk9y...E4pump](https://solscan.io/token/6hKk9ymYMejWURC1GhKj66Rwcn6VNnHHe1E3JgE4pump) | PVP风险池 | Score 13; Tier Micro; LP $24.5K; Vol24H $3.14M; 24H +165.00%; V/LP 128.11x; 池数 2; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| mogdog | SOL | [BmSjM7...xFpump](https://solscan.io/token/BmSjM7C7VRhznMMVzXidgyuE5ehvTHbRr1uGe2xFpump) | PVP风险池 | Score 12; Tier Micro; LP $21.2K; Vol24H $2.54M; 24H -88.53%; V/LP 119.82x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [67febu](https://dexscreener.com/solana/8r9gp3gasvqpas34cl4wqay59remvahwjwhaqgrs3exp) | SOL | [AcBFpe...gepump](https://solscan.io/token/AcBFpes1zvKPmsPTSMXaZWiEFpWZ5KZ7SmnbZbgepump) | PVP风险池 | Score 0; Tier Micro; LP $46.0K; Vol24H $1.64M; 24H +861.00%; V/LP 35.54x; 池数 2; 分项 L6/V15/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Loom | SOL | [CgnQ8a...kYpump](https://solscan.io/token/CgnQ8a1u99Gk7qoySMd2wrGPMPm9bdcSJNhqMEkYpump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Micro; LP $72.4K; Vol24H $2.51M; 24H -16.83%; V/LP 34.65x; 池数 2; 分项 L8/V16/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $248.9K; Vol24H $7.24M; 24H +135.25%; V/LP 29.07x; 池数 2; 分项 L13/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [CASHCAT](https://dexscreener.com/solana/9asrux6bowivf5mjfbuus1bpszqvoajmftkhpdqvkojx) | SOL | [3grmUL...nFpump](https://solscan.io/token/3grmULXrnQyN2A5LFStKFeSQsWvZjzNDsDVVLknFpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $48.1K; Vol24H $2.07M; 24H -71.50%; V/LP 43.02x; 池数 1; 分项 L6/V16/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| reptilecoin | SOL | [BtUiqG...U9pump](https://solscan.io/token/BtUiqGdsW3H47yvtyKSLhQfzVpwov3wyYY6qssU9pump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $32.1K; Vol24H $2.17M; 24H -57.23%; V/LP 67.54x; 池数 2; 分项 L5/V16/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [LIZARD](https://dexscreener.com/solana/5sgh3r8p76vchzzy1pxrwcelbehzxbrx1dbnzvlvdfsh) | SOL | [7NTs9F...dwpump](https://solscan.io/token/7NTs9FPw7tP2Bfjcn8eAJZUr4ApG8n9ZbXkT7Adwpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $25.1K; Vol24H $1.24M; 24H +193.00%; V/LP 49.32x; 池数 1; 分项 L4/V14/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [GHOSTI](https://dexscreener.com/solana/5xq1qzhbb3gu8bas7sdmtnnnxjuyffkoeyhx5zhhbvbu) | SOL | [6hKk9y...E4pump](https://solscan.io/token/6hKk9ymYMejWURC1GhKj66Rwcn6VNnHHe1E3JgE4pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $24.5K; Vol24H $3.14M; 24H +165.00%; V/LP 128.11x; 池数 2; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| mogdog | SOL | [BmSjM7...xFpump](https://solscan.io/token/BmSjM7C7VRhznMMVzXidgyuE5ehvTHbRr1uGe2xFpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $21.2K; Vol24H $2.54M; 24H -88.53%; V/LP 119.82x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [67febu](https://dexscreener.com/solana/8r9gp3gasvqpas34cl4wqay59remvahwjwhaqgrs3exp) | SOL | [AcBFpe...gepump](https://solscan.io/token/AcBFpes1zvKPmsPTSMXaZWiEFpWZ5KZ7SmnbZbgepump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $46.0K; Vol24H $1.64M; 24H +861.00%; V/LP 35.54x; 池数 2; 分项 L6/V15/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 80; Tier Mature; LP $216.19M; Vol24H $66.49M; 24H +5.25%; V/LP 0.31x; 池数 1; 分项 L20/V17/B22/Buy12/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.24M; Vol24H $8.10M; 24H +17.66%; V/LP 3.62x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $51.28M; Vol24H $4.29M; 24H -5.96%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| XPIN | BSC | [0xd955...3d31a6](https://bscscan.com/token/0xd955c9ba56fb1ab30e34766e252a97ccce3d31a6) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.09M; Vol24H $8.15M; 24H +5.42%; V/LP 7.45x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.64M; Vol24H $37.93M; 24H +0.02%; V/LP 2.28x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.76M; Vol24H $21.07M; 24H -12.79%; V/LP 7.63x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ORCA](https://dexscreener.com/solana/bsymmryrrwe4ppludo2bsxcecunu77ytxnaaebgbznpj) | SOL | [orcaEK...kektZE](https://solscan.io/token/orcaEKTdK7LKz57vaAYr9QeNsVEPfiu6QeMU1kektZE) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $37.23M; Vol24H $36.00M; 24H +1.68%; V/LP 0.97x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [NORMIE](https://dexscreener.com/solana/8n544cg9j44dkzu4cjswhxpwekxhqptr4r17kw9y5fbk) | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SAYLOR](https://dexscreener.com/solana/5yoaqpw38jfhslj8cmd2zj7ksjajbzhtpv1kx9fjekzv) | SOL | [BGwYnD...Pdpump](https://solscan.io/token/BGwYnDVe18aj9cozWcKNhiTUwayELULg5rHLGPPdpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| world | SOL | [FMqh9m...aJpump](https://solscan.io/token/FMqh9mqR6drPZqqW6wPqLHxX4rqNDWGhYLaMfoaJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Loom | SOL | [CgnQ8a...kYpump](https://solscan.io/token/CgnQ8a1u99Gk7qoySMd2wrGPMPm9bdcSJNhqMEkYpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [CASHCAT](https://dexscreener.com/solana/9asrux6bowivf5mjfbuus1bpszqvoajmftkhpdqvkojx) | SOL | [3grmUL...nFpump](https://solscan.io/token/3grmULXrnQyN2A5LFStKFeSQsWvZjzNDsDVVLknFpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [NORMIE](https://dexscreener.com/solana/8n544cg9j44dkzu4cjswhxpwekxhqptr4r17kw9y5fbk) | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TripleT](https://dexscreener.com/solana/3kfcgj5r3zshw8htdbzjsrrksrymkvsmfhc4vo4iddxd) | SOL | [J8PSdN...KZpump](https://solscan.io/token/J8PSdNP3QewKq2Z1JJJFDMaqF7KcaiJhR7gbr5KZpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 6 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 334} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
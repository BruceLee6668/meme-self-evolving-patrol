# 自我进化轮巡

**本轮时间 UTC：** 2026-10-07T21:43:31Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 145 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 264 |
| 合并后Token | 145 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 3 |
| 多池Token | 8 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 3 |
| Early层 | 14 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1693，刷新时间 2026-10-05T03:16:23Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 3 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 86; Tier Liquid; LP $2.16M; Vol24H $3.89M; 24H -7.61%; V/LP 1.80x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.12M; Vol24H $3.05M; 24H -0.53%; V/LP 2.73x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.03M; Vol24H $14.22M; 24H -21.97%; V/LP 7.00x; 池数 11; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PAID | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 81; Tier Early; LP $527.0K; Vol24H $2.47M; 24H +22.83%; V/LP 4.69x; 池数 2; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TART](https://dexscreener.com/bsc/0x30000a407fabebe29439f8e437050512ff6661be) | BSC | [0x7AB8...750314](https://bscscan.com/token/0x7AB8d02CBb51Ff7223fDe700eAaa2a91Bf750314) | 主观察 | Score 78; Tier Early; LP $450.0K; Vol24H $187.4K; 24H +6.80%; V/LP 0.42x; 池数 3; 分项 L15/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 76; Tier Liquid; LP $828.2K; Vol24H $1.19M; 24H +10.85%; V/LP 1.44x; 池数 1; 分项 L18/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [DOTF](https://dexscreener.com/solana/5gacckldzuagnuckgwjsat1wgnucuwthcyy8cc47lftv) | SOL | [umfFX5...W9pump](https://solscan.io/token/umfFX5o3mTxAfkq5DkZ96Fqkyr7JezEo6fjCcW9pump) | 次观察 | Score 73; Tier Early; LP $380.7K; Vol24H $222.3K; 24H +24.55%; V/LP 0.58x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VSOF](https://dexscreener.com/solana/agzjpu5vwg3wvsixkfpxwktas4qdxkvmd5fiyn5whzsq) | SOL | [h8E5CB...mcpump](https://solscan.io/token/h8E5CB7GAC5qx865EYPbaCNZShft9NHdAB4MJmcpump) | 次观察 | Score 72; Tier Early; LP $235.3K; Vol24H $251.5K; 24H +21.59%; V/LP 1.07x; 池数 1; 分项 L13/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 次观察 | Score 72; Tier Early; LP $294.1K; Vol24H $161.8K; 24H -7.68%; V/LP 0.55x; 池数 1; 分项 L13/V8/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 71; Tier Early; LP $120.7K; Vol24H $632.7K; 24H +5.49%; V/LP 5.24x; 池数 2; 分项 L10/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 85; Tier Early; LP $498.1K; Vol24H $1.40M; 24H -7.76%; V/LP 2.81x; 池数 2; 分项 L16/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 83; Tier Liquid; LP $4.10M; Vol24H $3.75M; 24H -3.27%; V/LP 0.91x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 81; Tier Liquid; LP $2.16M; Vol24H $3.35M; 24H -10.33%; V/LP 1.55x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 主观察 | Score 79; Tier Early; LP $294.5K; Vol24H $452.7K; 24H -3.40%; V/LP 1.54x; 池数 5; 分项 L14/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 76; Tier Liquid; LP $814.0K; Vol24H $1.13M; 24H +17.30%; V/LP 1.39x; 池数 1; 分项 L18/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 74; Tier Early; LP $500.7K; Vol24H $195.7K; 24H +23.93%; V/LP 0.39x; 池数 1; 分项 L16/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 次观察 | Score 72; Tier Liquid; LP $1.97M; Vol24H $12.22M; 24H -42.37%; V/LP 6.21x; 池数 9; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [THEROS](https://dexscreener.com/solana/behtrqrfgfamdp82vbj161ybd8xyedb422hwaf1gfm3u) | SOL | [2UfBjN...72cPa2](https://solscan.io/token/2UfBjNeDwzZsoUnr3hNKF4vkzAgiGmBNYCAxLq72cPa2) | 次观察 | Score 70; Tier Liquid; LP $2.75M; Vol24H $2.3K; 24H -2.41%; V/LP 0.00x; 池数 5; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 70; Tier Early; LP $360.7K; Vol24H $299.7K; 24H -0.18%; V/LP 0.83x; 池数 1; 分项 L14/V10/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/epuglbw1vko8qkq3mvqokowjc3u7ctbt7rumapw5kxeb) | SOL | [T6QteE...74pump](https://solscan.io/token/T6QteEAgXUpNnCYREjeKANrRkTtGCpxgjkSXz74pump) | 次观察 | Score 68; Tier Early; LP $384.4K; Vol24H $226.5K; 24H +35.27%; V/LP 0.59x; 池数 3; 分项 L15/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AUTON | SOL | [39ahtL...qQS8fz](https://solscan.io/token/39ahtL8ynzE4amH26J29C93PA5172V3ft9UuUcqQS8fz) | PVP风险池 | Score 50; Tier Early; LP $330.0K; Vol24H $12.08M; 24H -19.35%; V/LP 36.61x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [EVERYTHING](https://dexscreener.com/solana/fcfej9ujfnfcsiazgduesecmj2np6myxdm5h2jpfzbdc) | SOL | [E6vtwC...m7pump](https://solscan.io/token/E6vtwCUtcNJdQEPGY8vWKahtu2sfwxQ4j68pUKm7pump) | PVP风险池 | Score 36; Tier Early; LP $253.4K; Vol24H $6.08M; 24H +7824.00%; V/LP 23.98x; 池数 1; 分项 L13/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATCRAFT](https://dexscreener.com/solana/7mqdgteiad4tkupg9hstypqnestntrauehh1zj1awp8x) | SOL | [ADPN2a...7Cpump](https://solscan.io/token/ADPN2aqzY5RhkBC7bNQWFhTFFEYKY4drHUQG887Cpump) | PVP风险池 | Score 34; Tier Micro; LP $26.6K; Vol24H $4.22M; 24H -14.03%; V/LP 158.75x; 池数 1; 分项 L4/V17/B17/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RARINU](https://dexscreener.com/solana/a2asuorcetj9kwkmzhf3pvsslgzrnmnghiqku8uegqmj) | SOL | [45VHsi...9Hpump](https://solscan.io/token/45VHsie7CwFfPKWCw28PCdZdJWMA5Y6k56wDam9Hpump) | PVP风险池 | Score 34; Tier Early; LP $148.7K; Vol24H $3.74M; 24H +1160.00%; V/LP 25.18x; 池数 1; 分项 L11/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [A1](https://dexscreener.com/solana/f2p22sfcg4gkja2upyqzef9bpw3rsec5q2wmvewuibl7) | SOL | [FAopSo...K2pump](https://solscan.io/token/FAopSovS2WFJK5qEAmcuwAVH98CvmBwT6Lpq4EK2pump) | PVP风险池 | Score 33; Tier Early; LP $130.4K; Vol24H $5.64M; 24H +145.00%; V/LP 43.23x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AUTON | SOL | [39ahtL...qQS8fz](https://solscan.io/token/39ahtL8ynzE4amH26J29C93PA5172V3ft9UuUcqQS8fz) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 50; Tier Early; LP $330.0K; Vol24H $12.08M; 24H -19.35%; V/LP 36.61x; 池数 1; 分项 L14/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [EVERYTHING](https://dexscreener.com/solana/fcfej9ujfnfcsiazgduesecmj2np6myxdm5h2jpfzbdc) | SOL | [E6vtwC...m7pump](https://solscan.io/token/E6vtwCUtcNJdQEPGY8vWKahtu2sfwxQ4j68pUKm7pump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 36; Tier Early; LP $253.4K; Vol24H $6.08M; 24H +7824.00%; V/LP 23.98x; 池数 1; 分项 L13/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [CATCRAFT](https://dexscreener.com/solana/7mqdgteiad4tkupg9hstypqnestntrauehh1zj1awp8x) | SOL | [ADPN2a...7Cpump](https://solscan.io/token/ADPN2aqzY5RhkBC7bNQWFhTFFEYKY4drHUQG887Cpump) | 24H波动可控；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 34; Tier Micro; LP $26.6K; Vol24H $4.22M; 24H -14.03%; V/LP 158.75x; 池数 1; 分项 L4/V17/B17/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [RARINU](https://dexscreener.com/solana/a2asuorcetj9kwkmzhf3pvsslgzrnmnghiqku8uegqmj) | SOL | [45VHsi...9Hpump](https://solscan.io/token/45VHsie7CwFfPKWCw28PCdZdJWMA5Y6k56wDam9Hpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $148.7K; Vol24H $3.74M; 24H +1160.00%; V/LP 25.18x; 池数 1; 分项 L11/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [A1](https://dexscreener.com/solana/f2p22sfcg4gkja2upyqzef9bpw3rsec5q2wmvewuibl7) | SOL | [FAopSo...K2pump](https://solscan.io/token/FAopSovS2WFJK5qEAmcuwAVH98CvmBwT6Lpq4EK2pump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $130.4K; Vol24H $5.64M; 24H +145.00%; V/LP 43.23x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [TWEETCRAFT](https://dexscreener.com/solana/3nbq9zynlpdqqdvyf8ximbwywqfkzd7m7fypry524efq) | SOL | [HzYCHq...d5MZQy](https://solscan.io/token/HzYCHqAN2uoHGRnL9v2ChCfFQX3bvJuJd5zu2Hd5MZQy) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $118.9K; Vol24H $11.37M; 24H +80.28%; V/LP 95.64x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CLAUDIA | SOL | [2j5SaS...hnW2ZM](https://solscan.io/token/2j5SaS7xy776qCBpyPQbZjyQSAtKiFgrwjfErthnW2ZM) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Micro; LP $50.7K; Vol24H $6.49M; 24H +351.44%; V/LP 128.01x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TMNP](https://dexscreener.com/solana/hwvs3tmrhgebmxea69dnw4ksqono3ethuwnzb1s6shdc) | SOL | [BR1HcT...iLpump](https://solscan.io/token/BR1HcT9RP6ewqLhhYnhpDaa9Uh3Tj8TSKyS9yTiLpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 4; Tier Micro; LP $3.8K; Vol24H $5.02M; 24H -93.75%; V/LP 1308.44x; 池数 5; 分项 L0/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H波动可控；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $2.27M; Vol24H $5.85M; 24H -23.86%; V/LP 2.58x; 池数 1; 分项 L20/V17/B17/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $57.99M; Vol24H $3.79M; 24H -0.23%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 71; Tier Early; LP $372.1K; Vol24H $1.53M; 24H -7.46%; V/LP 4.11x; 池数 1; 分项 L14/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $4.47M; Vol24H $30.68M; 24H +10.91%; V/LP 6.86x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [THEROS](https://dexscreener.com/solana/behtrqrfgfamdp82vbj161ybd8xyedb422hwaf1gfm3u) | SOL | [2UfBjN...72cPa2](https://solscan.io/token/2UfBjNeDwzZsoUnr3hNKF4vkzAgiGmBNYCAxLq72cPa2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/epuglbw1vko8qkq3mvqokowjc3u7ctbt7rumapw5kxeb) | SOL | [T6QteE...74pump](https://solscan.io/token/T6QteEAgXUpNnCYREjeKANrRkTtGCpxgjkSXz74pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 3 / Early 14 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
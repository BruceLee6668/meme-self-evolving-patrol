# 自我进化轮巡

**本轮时间 UTC：** 2026-10-09T01:39:36Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 160 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 281 |
| 合并后Token | 160 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 8 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 0 |
| 多池Token | 6 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 11 |
| Liquid层 | 7 |
| Mature层 | 1 |
| 需要链上确认 | 21 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1693，刷新时间 2026-10-05T03:16:23Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 4 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 86; Tier Liquid; LP $2.12M; Vol24H $3.75M; 24H -0.09%; V/LP 1.77x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 82; Tier Early; LP $506.5K; Vol24H $678.0K; 24H +9.32%; V/LP 1.34x; 池数 1; 分项 L16/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.02M; Vol24H $5.64M; 24H +8.34%; V/LP 2.79x; 池数 4; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 80; Tier Liquid; LP $2.64M; Vol24H $1.83M; 24H -38.22%; V/LP 0.69x; 池数 1; 分项 L20/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [baton](https://dexscreener.com/solana/cb7zrgplhji3th7htxykeqbxvnjppetvckxuwakbuhxu) | SOL | [Hg5Ja5...hgpump](https://solscan.io/token/Hg5Ja55T5wESq4vyFoiVCMeHXtGyVA69X2UHq8hgpump) | 次观察 | Score 73; Tier Early; LP $737.9K; Vol24H $1.64M; 24H +51.36%; V/LP 2.22x; 池数 1; 分项 L17/V15/B8/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 73; Tier Early; LP $348.0K; Vol24H $841.5K; 24H +0.12%; V/LP 2.42x; 池数 1; 分项 L14/V13/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| VELL | BSC | [0x40f4...f753f2](https://bscscan.com/token/0x40f4100b47189c4b41b5ae3d3156d304b3f753f2) | 次观察 | Score 73; Tier Early; LP $343.8K; Vol24H $80.6K; 24H -21.41%; V/LP 0.23x; 池数 1; 分项 L14/V6/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/epuglbw1vko8qkq3mvqokowjc3u7ctbt7rumapw5kxeb) | SOL | [T6QteE...74pump](https://solscan.io/token/T6QteEAgXUpNnCYREjeKANrRkTtGCpxgjkSXz74pump) | 次观察 | Score 68; Tier Early; LP $428.6K; Vol24H $221.0K; 24H +30.01%; V/LP 0.52x; 池数 3; 分项 L15/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DOTF](https://dexscreener.com/solana/5gacckldzuagnuckgwjsat1wgnucuwthcyy8cc47lftv) | SOL | [umfFX5...W9pump](https://solscan.io/token/umfFX5o3mTxAfkq5DkZ96Fqkyr7JezEo6fjCcW9pump) | 次观察 | Score 68; Tier Early; LP $430.4K; Vol24H $214.8K; 24H +26.21%; V/LP 0.50x; 池数 1; 分项 L15/V9/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| RDNT | BSC | [0xf7de...1384df](https://bscscan.com/token/0xf7de7e8a6bd59ed41a4b5fe50278b3b7f31384df) | 次观察 | Score 66; Tier Early; LP $118.8K; Vol24H $584.0K; 24H -15.08%; V/LP 4.92x; 池数 1; 分项 L10/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 87; Tier Early; LP $512.7K; Vol24H $783.3K; 24H +4.97%; V/LP 1.53x; 池数 1; 分项 L16/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 86; Tier Liquid; LP $2.14M; Vol24H $3.91M; 24H +1.72%; V/LP 1.83x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.22M; Vol24H $6.65M; 24H +14.46%; V/LP 2.99x; 池数 10; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| HOOKED | SOL | [C1mBfB...ZtPngE](https://solscan.io/token/C1mBfBoDkwWfd6uTFZp62ARHLjeVp3bDpCDMfMZtPngE) | 主观察 | Score 78; Tier Early; LP $635.7K; Vol24H $3.05M; 24H +23.61%; V/LP 4.80x; 池数 1; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CREPE | BSC | [0xeb2b...8d931d](https://bscscan.com/token/0xeb2b7d5691878627eff20492ca7c9a71228d931d) | 主观察 | Score 77; Tier Early; LP $636.5K; Vol24H $78.6K; 24H -3.07%; V/LP 0.12x; 池数 1; 分项 L17/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Pumpoween](https://dexscreener.com/solana/8nvfb1unnk9adtl5hoof8hahf2rt4glpwx9cteadikhg) | SOL | [5Gefef...vFpump](https://solscan.io/token/5GefefPX1mDs6ZJB1apYmz6fCTCiNJpHturZ9bvFpump) | 次观察 | Score 75; Tier Micro; LP $96.6K; Vol24H $127.9K; 24H -6.12%; V/LP 1.32x; 池数 6; 分项 L9/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [baton](https://dexscreener.com/solana/cb7zrgplhji3th7htxykeqbxvnjppetvckxuwakbuhxu) | SOL | [Hg5Ja5...hgpump](https://solscan.io/token/Hg5Ja55T5wESq4vyFoiVCMeHXtGyVA69X2UHq8hgpump) | 次观察 | Score 74; Tier Liquid; LP $766.1K; Vol24H $2.04M; 24H +34.95%; V/LP 2.66x; 池数 1; 分项 L17/V16/B8/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 71; Tier Early; LP $241.0K; Vol24H $231.3K; 24H -16.65%; V/LP 0.96x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 次观察 | Score 70; Tier Early; LP $123.4K; Vol24H $402.2K; 24H +2.32%; V/LP 3.26x; 池数 2; 分项 L10/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 68; Tier Early; LP $348.0K; Vol24H $791.4K; 24H -8.14%; V/LP 2.27x; 池数 1; 分项 L14/V13/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GOMO](https://dexscreener.com/solana/5a7qurjlart146jajjype5nh6vlyfpn2qrhuslqbsczy) | SOL | [9XKzy4...hEpump](https://solscan.io/token/9XKzy4KahcZaGJPJtz1PtqGPB3CiseoBrx7TcQhEpump) | 次观察 | Score 67; Tier Micro; LP $85.1K; Vol24H $477.9K; 24H -19.21%; V/LP 5.62x; 池数 1; 分项 L9/V12/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| VELL | BSC | [0x40f4...f753f2](https://bscscan.com/token/0x40f4100b47189c4b41b5ae3d3156d304b3f753f2) | 次观察 | Score 67; Tier Early; LP $344.8K; Vol24H $27.3K; 24H +0.46%; V/LP 0.08x; 池数 1; 分项 L14/V3/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 64; Tier Early; LP $378.8K; Vol24H $1.09M; 24H +25.12%; V/LP 2.88x; 池数 2; 分项 L15/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| quq | BSC | [0x4fa7...6b03bf](https://bscscan.com/token/0x4fa7c69a7b69f8bc48233024d546bc299d6b03bf) | PVP风险池 | Score 56; Tier Liquid; LP $1.66M; Vol24H $110.96M; 24H -0.06%; V/LP 66.89x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Gary](https://dexscreener.com/solana/2uzutqejcxcr1eswmdgtpqewm5pcekewrsnvrpc1ehs1) | SOL | [8ZCmwp...AFpump](https://solscan.io/token/8ZCmwpW3MtC5UpNcZf7U4HMvRNTo71syU11BDiAFpump) | PVP风险池 | Score 33; Tier Early; LP $134.6K; Vol24H $5.31M; 24H +1603.00%; V/LP 39.42x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| quq | BSC | [0x4fa7...6b03bf](https://bscscan.com/token/0x4fa7c69a7b69f8bc48233024d546bc299d6b03bf) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Liquid; LP $1.66M; Vol24H $110.96M; 24H -0.06%; V/LP 66.89x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Gary](https://dexscreener.com/solana/2uzutqejcxcr1eswmdgtpqewm5pcekewrsnvrpc1ehs1) | SOL | [8ZCmwp...AFpump](https://solscan.io/token/8ZCmwpW3MtC5UpNcZf7U4HMvRNTo71syU11BDiAFpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $134.6K; Vol24H $5.31M; 24H +1603.00%; V/LP 39.42x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| BORDR | SOL | [6Mix12...Fbordr](https://solscan.io/token/6Mix12LiHrQFojaQEnfPUC65Qkwd6X4Y5Qg93oFbordr) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $122.0K; Vol24H $5.09M; 24H +297.34%; V/LP 41.74x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TikTok](https://dexscreener.com/solana/bjhum36bzoybhergspkzlzsttbpbdbjcdoeka7o9n2o) | SOL | [64oAuE...TLYgCp](https://solscan.io/token/64oAuE88tNP7KsSyaiJTKGP4sWmLMFGWLUs9eBTLYgCp) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $95.1K; Vol24H $5.83M; 24H +1826.00%; V/LP 61.26x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TWEETCRAFT | SOL | [HzYCHq...d5MZQy](https://solscan.io/token/HzYCHqAN2uoHGRnL9v2ChCfFQX3bvJuJd5zu2Hd5MZQy) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Early; LP $151.6K; Vol24H $6.74M; 24H +83.32%; V/LP 44.46x; 池数 2; 分项 L11/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [CAPYBARA](https://dexscreener.com/solana/8abjfad9xwx9iadnpkweadpfmj2aztrdnwqs37fcboob) | SOL | [3xrw3J...1mpZVf](https://solscan.io/token/3xrw3JKyaSYjzksYc8nrZE1kReQAxoHT3epi3P1mpZVf) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 12; Tier Micro; LP $49.9K; Vol24H $4.48M; 24H +396.00%; V/LP 89.86x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| [ECSTACRAFT](https://dexscreener.com/solana/j6mdru9cyxqaxasthhpf8ym1gyrfwrmqfwptwlvhgs7n) | SOL | [5MS2zt...WJpump](https://solscan.io/token/5MS2zt6GU3KU4r8qn2gZc8W2yKdtPkLVxFDRe8WJpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $4.7K; Vol24H $7.75M; 24H -92.78%; V/LP 1636.73x; 池数 8; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| swordinu | SOL | [2BVfJ4...6bpump](https://solscan.io/token/2BVfJ4AHMvHdKtEZNHaBr48dQzTfZvYkjaaxbM6bpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $9.5K; Vol24H $5.01M; 24H -99.94%; V/LP 529.43x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.26M; Vol24H $9.10M; 24H -6.15%; V/LP 4.03x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $4.23M; Vol24H $13.94M; 24H -2.00%; V/LP 3.30x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $58.10M; Vol24H $5.14M; 24H +0.20%; V/LP 0.09x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/assyvunbfazjprrnh3kuuvztehkomvweohz86f4q5d9x) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Liquid; LP $1.95M; Vol24H $5.95M; 24H -6.65%; V/LP 3.05x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| CREPE | BSC | [0xeb2b...8d931d](https://bscscan.com/token/0xeb2b7d5691878627eff20492ca7c9a71228d931d) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| HOOKED | SOL | [C1mBfB...ZtPngE](https://solscan.io/token/C1mBfBoDkwWfd6uTFZp62ARHLjeVp3bDpCDMfMZtPngE) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Pumpoween](https://dexscreener.com/solana/8nvfb1unnk9adtl5hoof8hahf2rt4glpwx9cteadikhg) | SOL | [5Gefef...vFpump](https://solscan.io/token/5GefefPX1mDs6ZJB1apYmz6fCTCiNJpHturZ9bvFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [baton](https://dexscreener.com/solana/cb7zrgplhji3th7htxykeqbxvnjppetvckxuwakbuhxu) | SOL | [Hg5Ja5...hgpump](https://solscan.io/token/Hg5Ja55T5wESq4vyFoiVCMeHXtGyVA69X2UHq8hgpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/aqp9ekhgp1u35usbdayglpgnvzuyezlshfxfzkw3cye9) | SOL | [7MuvW6...Ropump](https://solscan.io/token/7MuvW6G2pDTGSjzpjqeDYigUsXqqd6TmEzLgvRRopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CREPE | BSC | [0xeb2b...8d931d](https://bscscan.com/token/0xeb2b7d5691878627eff20492ca7c9a71228d931d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| HOOKED | SOL | [C1mBfB...ZtPngE](https://solscan.io/token/C1mBfBoDkwWfd6uTFZp62ARHLjeVp3bDpCDMfMZtPngE) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 6 / Early 11 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
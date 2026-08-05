# 自我进化轮巡

**本轮时间 UTC：** 2026-08-05T06:23:14Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 136 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 241 |
| 合并后Token | 136 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 3 |
| 多池Token | 7 |
| 多池冲突 | 0 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 6 |
| Mature层 | 4 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 2 |

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
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 83; Tier Liquid; LP $1.86M; Vol24H $57.4K; 24H +2.72%; V/LP 0.03x; 池数 1; 分项 L20/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 80; Tier Liquid; LP $1.00M; Vol24H $132.3K; 24H +5.19%; V/LP 0.13x; 池数 1; 分项 L18/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 次观察 | Score 73; Tier Early; LP $125.0K; Vol24H $57.1K; 24H +2.79%; V/LP 0.46x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 次观察 | Score 72; Tier Early; LP $107.0K; Vol24H $58.2K; 24H +0.91%; V/LP 0.54x; 池数 1; 分项 L9/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 72; Tier Early; LP $462.3K; Vol24H $3.32M; 24H +67.20%; V/LP 7.19x; 池数 2; 分项 L15/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 70; Tier Early; LP $347.1K; Vol24H $2.00M; 24H -35.30%; V/LP 5.75x; 池数 1; 分项 L14/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RINO](https://dexscreener.com/solana/8vy2nshplulrhfnvx2m2hebzgqx9nooxjqe4pfkkdebk) | SOL | [8bVP1R...twrise](https://solscan.io/token/8bVP1RqzpFa9zuVs5y84GV5zKAqYXworCfjoY1twrise) | 次观察 | Score 69; Tier Liquid; LP $1.13M; Vol24H $28.55; 24H -0.14%; V/LP 0.00x; 池数 1; 分项 L19/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 47; Tier Early; LP $157.8K; Vol24H $11.60M; 24H -23.62%; V/LP 73.55x; 池数 2; 分项 L11/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 44; Tier Early; LP $692.4K; Vol24H $24.94M; 24H -49.05%; V/LP 36.01x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 30; Tier Liquid; LP $1.69M; Vol24H $43.04M; 24H +73.79%; V/LP 25.50x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 主观察 | Score 83; Tier Liquid; LP $1.87M; Vol24H $51.5K; 24H +2.74%; V/LP 0.03x; 池数 1; 分项 L20/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $992.3K; Vol24H $117.1K; 24H +4.71%; V/LP 0.12x; 池数 1; 分项 L18/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 78; Tier Liquid; LP $2.05M; Vol24H $186.3K; 24H +0.00%; V/LP 0.09x; 池数 1; 分项 L20/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 次观察 | Score 73; Tier Early; LP $125.4K; Vol24H $57.0K; 24H +4.19%; V/LP 0.45x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 次观察 | Score 72; Tier Early; LP $107.7K; Vol24H $58.1K; 24H +1.71%; V/LP 0.54x; 池数 1; 分项 L9/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 70; Tier Early; LP $353.7K; Vol24H $1.97M; 24H -31.52%; V/LP 5.58x; 池数 1; 分项 L14/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 65; Tier Early; LP $514.8K; Vol24H $3.49M; 24H +106.00%; V/LP 6.77x; 池数 2; 分项 L16/V17/B0/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Fapcoin](https://dexscreener.com/solana/aypfy111g9nt1jvunymtjd9is2m8c3pbveosmx9echeu) | SOL | [8vGr1e...Mrpump](https://solscan.io/token/8vGr1eX9vfpootWiUPYa5kYoGx9bTuRy2Xc4dNMrpump) | 次观察 | Score 64; Tier Micro; LP $95.7K; Vol24H $88.3K; 24H -20.84%; V/LP 0.92x; 池数 1; 分项 L9/V6/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 44; Tier Early; LP $731.7K; Vol24H $23.71M; 24H -37.02%; V/LP 32.41x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 39; Tier Early; LP $182.1K; Vol24H $11.11M; 24H +46.49%; V/LP 61.01x; 池数 2; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | PVP风险池 | Score 30; Tier Micro; LP $68.0K; Vol24H $2.88M; 24H -36.68%; V/LP 42.32x; 池数 1; 分项 L8/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 29; Tier Micro; LP $66.0K; Vol24H $1.82M; 24H +27.76%; V/LP 27.51x; 池数 1; 分项 L8/V16/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| JLY | SOL | [6fEaYu...RPpump](https://solscan.io/token/6fEaYuzirTMXFnFo7dGKHJs8wWVFPdh1bfZL9oRPpump) | PVP风险池 | Score 28; Tier Micro; LP $95.9K; Vol24H $4.16M; 24H +283.81%; V/LP 43.43x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TikTok](https://dexscreener.com/solana/d5kwljmshdma1qbyzcuagtf2zc6wtncix4lmbxpdih9n) | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | PVP风险池 | Score 27; Tier Micro; LP $68.7K; Vol24H $11.50M; 24H -80.40%; V/LP 167.28x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 22; Tier Liquid; LP $1.73M; Vol24H $49.65M; 24H +84.36%; V/LP 28.75x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Early; LP $731.7K; Vol24H $23.71M; 24H -37.02%; V/LP 32.41x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Early; LP $182.1K; Vol24H $11.11M; 24H +46.49%; V/LP 61.01x; 池数 2; 分项 L12/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 30; Tier Micro; LP $68.0K; Vol24H $2.88M; 24H -36.68%; V/LP 42.32x; 池数 1; 分项 L8/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 29; Tier Micro; LP $66.0K; Vol24H $1.82M; 24H +27.76%; V/LP 27.51x; 池数 1; 分项 L8/V16/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| JLY | SOL | [6fEaYu...RPpump](https://solscan.io/token/6fEaYuzirTMXFnFo7dGKHJs8wWVFPdh1bfZL9oRPpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $95.9K; Vol24H $4.16M; 24H +283.81%; V/LP 43.43x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TikTok](https://dexscreener.com/solana/d5kwljmshdma1qbyzcuagtf2zc6wtncix4lmbxpdih9n) | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $68.7K; Vol24H $11.50M; 24H -80.40%; V/LP 167.28x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 22; Tier Liquid; LP $1.73M; Vol24H $49.65M; 24H +84.36%; V/LP 28.75x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [Instagram ](https://dexscreener.com/solana/5w21dwfcsb4aieaizl5s1r1utdwgdtuhuengczbyf15p) | SOL | [Ef4E8v...Nrpump](https://solscan.io/token/Ef4E8vBoosFWhxXWqRHQAsXiuuAbocrN9PnpgHNrpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $35.2K; Vol24H $3.14M; 24H +544.00%; V/LP 89.23x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 75; Tier Liquid; LP $1.89M; Vol24H $1.15M; 24H -8.40%; V/LP 0.61x; 池数 2; 分项 L20/V14/B17/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| JACKET | BSC | [0x57ae...5affff](https://bscscan.com/token/0x57aedac0ccaafdec0ec62fc4fbfd8252735affff) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $3705.83M; Vol24H $7.10M; 24H -19.55%; V/LP 0.00x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [SOL](https://dexscreener.com/bsc/0xbffec96e8f3b5058b1817c14e4380758fada01ef) | BSC | [0x570A...fD43dF](https://bscscan.com/token/0x570A5D26f7765Ecb712C0924E4De545B89fD43dF) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 71; Tier Liquid; LP $969.9K; Vol24H $2.28M; 24H +0.39%; V/LP 2.35x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $17.46M; Vol24H $106.90M; 24H +0.04%; V/LP 6.12x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $5.63M; Vol24H $14.59M; 24H +15.29%; V/LP 2.59x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；成熟大池 | Score 59; Tier Mature; LP $19.88M; Vol24H $50.8K; 24H +2.30%; V/LP 0.00x; 池数 1; 分项 L20/V5/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SAOF](https://dexscreener.com/solana/9m8zrwlehhvywc3t8jwyamrsy5usufr8ajxjun2hfagr) | SOL | [uVP7aA...6qpump](https://solscan.io/token/uVP7aAZGpgLEZcMasnxd9MUd948jprAA54P6h6qpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Fapcoin](https://dexscreener.com/solana/aypfy111g9nt1jvunymtjd9is2m8c3pbveosmx9echeu) | SOL | [8vGr1e...Mrpump](https://solscan.io/token/8vGr1eX9vfpootWiUPYa5kYoGx9bTuRy2Xc4dNMrpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Doom](https://dexscreener.com/solana/31cucgseqquhuakwjrvs9ytkscaddbsywbqtg9emdukh) | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
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
| dexscreener_search | {'ok': True, 'count': 344} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
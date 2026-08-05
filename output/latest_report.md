# 自我进化轮巡

**本轮时间 UTC：** 2026-08-05T00:02:41Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 139 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 236 |
| 合并后Token | 139 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 6 |
| 多池Token | 8 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 5 |
| Mature层 | 3 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 1 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 80; Tier Liquid; LP $988.5K; Vol24H $134.5K; 24H +1.80%; V/LP 0.14x; 池数 1; 分项 L18/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SAOF | SOL | [8oSMq4...dqQbhX](https://solscan.io/token/8oSMq4sSyheFNVHrd5dEANGF29CMQwcnZZe8DrdqQbhX) | 主观察 | Score 76; Tier Early; LP $138.9K; Vol24H $100.3K; 24H +3.43%; V/LP 0.72x; 池数 1; 分项 L11/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 75; Tier Early; LP $315.6K; Vol24H $653.9K; 24H +10.20%; V/LP 2.07x; 池数 1; 分项 L14/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Cupsey | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 73; Tier Early; LP $494.5K; Vol24H $3.05M; 24H +73.01%; V/LP 6.16x; 池数 2; 分项 L16/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 次观察 | Score 72; Tier Early; LP $105.2K; Vol24H $58.4K; 24H -1.64%; V/LP 0.56x; 池数 1; 分项 L9/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Chonketha | SOL | [HcfnJx...zdpump](https://solscan.io/token/HcfnJxLov6tY8i1dq9uYRRZKCvxADPpovcfkyXzdpump) | 次观察 | Score 71; Tier Early; LP $239.8K; Vol24H $1.02M; 24H -9.47%; V/LP 4.24x; 池数 1; 分项 L13/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 44; Tier Early; LP $730.7K; Vol24H $28.29M; 24H -55.80%; V/LP 38.72x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | PVP风险池 | Score 31; Tier Micro; LP $85.4K; Vol24H $8.45M; 24H -72.54%; V/LP 98.92x; 池数 1; 分项 L9/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 30; Tier Early; LP $170.5K; Vol24H $15.90M; 24H +521.35%; V/LP 93.29x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | PVP风险池 | Score 30; Tier Micro; LP $70.8K; Vol24H $6.58M; 24H -47.31%; V/LP 92.91x; 池数 1; 分项 L8/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 80; Tier Early; LP $307.0K; Vol24H $659.6K; 24H +3.37%; V/LP 2.15x; 池数 1; 分项 L14/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 80; Tier Liquid; LP $991.5K; Vol24H $129.2K; 24H +3.83%; V/LP 0.13x; 池数 1; 分项 L18/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 77; Tier Liquid; LP $2.05M; Vol24H $158.3K; 24H +0.00%; V/LP 0.08x; 池数 2; 分项 L20/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SAOF | SOL | [8oSMq4...dqQbhX](https://solscan.io/token/8oSMq4sSyheFNVHrd5dEANGF29CMQwcnZZe8DrdqQbhX) | 主观察 | Score 76; Tier Early; LP $138.9K; Vol24H $100.0K; 24H +3.34%; V/LP 0.72x; 池数 1; 分项 L11/V7/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 次观察 | Score 72; Tier Early; LP $104.7K; Vol24H $58.0K; 24H -2.83%; V/LP 0.55x; 池数 1; 分项 L9/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 72; Tier Early; LP $464.3K; Vol24H $3.12M; 24H +58.16%; V/LP 6.71x; 池数 2; 分项 L15/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 70; Tier Early; LP $365.3K; Vol24H $1.91M; 24H -33.56%; V/LP 5.22x; 池数 1; 分项 L14/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 44; Tier Liquid; LP $792.6K; Vol24H $27.16M; 24H -52.17%; V/LP 34.27x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | PVP风险池 | Score 30; Tier Early; LP $163.8K; Vol24H $15.95M; 24H +490.07%; V/LP 97.38x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | PVP风险池 | Score 30; Tier Micro; LP $70.5K; Vol24H $5.92M; 24H -46.99%; V/LP 83.98x; 池数 1; 分项 L8/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| OnlyMarms | SOL | [HBrfYZ...espump](https://solscan.io/token/HBrfYZgeLKdSvBBGnGkvAK4563pq8oBGpgNFAaespump) | PVP风险池 | Score 29; Tier Early; LP $119.0K; Vol24H $3.50M; 24H +114.08%; V/LP 29.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TikTok](https://dexscreener.com/solana/d5kwljmshdma1qbyzcuagtf2zc6wtncix4lmbxpdih9n) | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | PVP风险池 | Score 28; Tier Micro; LP $93.1K; Vol24H $16.59M; 24H +2704.00%; V/LP 178.24x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 27; Tier Liquid; LP $1.74M; Vol24H $37.12M; 24H +91.92%; V/LP 21.33x; 池数 1; 分项 L20/V17/B0/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [JLY](https://dexscreener.com/solana/gtuhxczfn7y9yujg58ppysesrx6kykbnnvbmnkczem6z) | SOL | [6fEaYu...RPpump](https://solscan.io/token/6fEaYuzirTMXFnFo7dGKHJs8wWVFPdh1bfZL9oRPpump) | PVP风险池 | Score 26; Tier Micro; LP $55.3K; Vol24H $4.30M; 24H +1379.00%; V/LP 77.66x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Instagram ](https://dexscreener.com/solana/5w21dwfcsb4aieaizl5s1r1utdwgdtuhuengczbyf15p) | SOL | [Ef4E8v...Nrpump](https://solscan.io/token/Ef4E8vBoosFWhxXWqRHQAsXiuuAbocrN9PnpgHNrpump) | PVP风险池 | Score 26; Tier Micro; LP $65.7K; Vol24H $2.39M; 24H +2213.00%; V/LP 36.31x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 44; Tier Liquid; LP $792.6K; Vol24H $27.16M; 24H -52.17%; V/LP 34.27x; 池数 2; 分项 L17/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $163.8K; Vol24H $15.95M; 24H +490.07%; V/LP 97.38x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 30; Tier Micro; LP $70.5K; Vol24H $5.92M; 24H -46.99%; V/LP 83.98x; 池数 1; 分项 L8/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| OnlyMarms | SOL | [HBrfYZ...espump](https://solscan.io/token/HBrfYZgeLKdSvBBGnGkvAK4563pq8oBGpgNFAaespump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $119.0K; Vol24H $3.50M; 24H +114.08%; V/LP 29.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TikTok](https://dexscreener.com/solana/d5kwljmshdma1qbyzcuagtf2zc6wtncix4lmbxpdih9n) | SOL | [89RAit...kvpump](https://solscan.io/token/89RAitwPJBEfLK4Gcg5iv7AjFABHWNvoD5rkvRkvpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $93.1K; Vol24H $16.59M; 24H +2704.00%; V/LP 178.24x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 27; Tier Liquid; LP $1.74M; Vol24H $37.12M; 24H +91.92%; V/LP 21.33x; 池数 1; 分项 L20/V17/B0/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| [JLY](https://dexscreener.com/solana/gtuhxczfn7y9yujg58ppysesrx6kykbnnvbmnkczem6z) | SOL | [6fEaYu...RPpump](https://solscan.io/token/6fEaYuzirTMXFnFo7dGKHJs8wWVFPdh1bfZL9oRPpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $55.3K; Vol24H $4.30M; 24H +1379.00%; V/LP 77.66x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Instagram ](https://dexscreener.com/solana/5w21dwfcsb4aieaizl5s1r1utdwgdtuhuengczbyf15p) | SOL | [Ef4E8v...Nrpump](https://solscan.io/token/Ef4E8vBoosFWhxXWqRHQAsXiuuAbocrN9PnpgHNrpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $65.7K; Vol24H $2.39M; 24H +2213.00%; V/LP 36.31x; 池数 1; 分项 L8/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $1.86M; Vol24H $4.07M; 24H -7.31%; V/LP 2.19x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| JACKET | BSC | [0x57ae...5affff](https://bscscan.com/token/0x57aedac0ccaafdec0ec62fc4fbfd8252735affff) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $3743.15M; Vol24H $7.54M; 24H +15.23%; V/LP 0.00x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $17.74M; Vol24H $91.29M; 24H +0.04%; V/LP 5.15x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 60; Tier Mature; LP $5.48M; Vol24H $13.27M; 24H +30.34%; V/LP 2.42x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SAOF | SOL | [8oSMq4...dqQbhX](https://solscan.io/token/8oSMq4sSyheFNVHrd5dEANGF29CMQwcnZZe8DrdqQbhX) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [TTF](https://dexscreener.com/solana/4gtt5e27yomsawwgtkmy8xvrngak9mvb2xwnqfa5qoxp) | SOL | [Q4FCUJ...rfpump](https://solscan.io/token/Q4FCUJgAEPxTbRZq1GVKw6mEaSRVjtxbP6pt7rfpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Doom | SOL | [Gymbmn...Y9pump](https://solscan.io/token/Gymbmn9wwMKe4NnmVceyyfpncp9arbwPfSdBsyY9pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| 1 | BSC | [0xff5d...0e4444](https://bscscan.com/token/0xff5d99a5c16cf2ffb4e7da1d7c42a791e70e4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SAOF | SOL | [8oSMq4...dqQbhX](https://solscan.io/token/8oSMq4sSyheFNVHrd5dEANGF29CMQwcnZZe8DrdqQbhX) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 10 / Liquid 5 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 345} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
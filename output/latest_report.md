# 自我进化轮巡

**本轮时间 UTC：** 2026-08-12T21:39:35Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 126 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 248 |
| 合并后Token | 126 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 4 |
| 多池Token | 9 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 5 |
| Liquid层 | 10 |
| Mature层 | 3 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 983，刷新时间 2026-08-10T01:06:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 1 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 82; Tier Liquid; LP $764.6K; Vol24H $2.42M; 24H -19.07%; V/LP 3.16x; 池数 2; 分项 L17/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 77; Tier Liquid; LP $1.17M; Vol24H $216.2K; 24H +20.46%; V/LP 0.18x; 池数 1; 分项 L19/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 73; Tier Early; LP $627.4K; Vol24H $2.21M; 24H -29.90%; V/LP 3.52x; 池数 2; 分项 L17/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 68; Tier Early; LP $589.0K; Vol24H $2.88M; 24H +34.25%; V/LP 4.88x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | PVP风险池 | Score 44; Tier Liquid; LP $2.17M; Vol24H $59.44M; 24H +5.59%; V/LP 27.35x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MEFLIX](https://dexscreener.com/solana/4xcmgdqn7xn4uaekbvmhyqmtemjaokfajetxnm6gsec1) | SOL | [9khsvW...hnpump](https://solscan.io/token/9khsvWZMUNi73ot9UbkgnuNgqtq2LWRJG2acVrhnpump) | PVP风险池 | Score 43; Tier Early; LP $211.7K; Vol24H $10.02M; 24H +15.78%; V/LP 47.32x; 池数 3; 分项 L12/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MARIO64 | SOL | [CX2v7J...WJpump](https://solscan.io/token/CX2v7JSHJQDcNooubzzvZG8TPaDwbaPgfzcXRSWJpump) | PVP风险池 | Score 35; Tier Micro; LP $75.6K; Vol24H $5.04M; 24H -67.17%; V/LP 66.62x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ElonCoin | BSC | [0x499c...317777](https://bscscan.com/token/0x499c573997a1382f4051ece45b3d6b2f0e317777) | PVP风险池 | Score 35; Tier Micro; LP $82.2K; Vol24H $3.18M; 24H +32.35%; V/LP 38.71x; 池数 1; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOT](https://dexscreener.com/solana/2cdmgj24mytdzpgfvveytgfldah6387yeabxwcjy1mlg) | SOL | [HukaK2...myT8WJ](https://solscan.io/token/HukaK2eHhbTyiuUwuKMntjPJP4aGdD4VwiExsNmyT8WJ) | PVP风险池 | Score 34; Tier Micro; LP $59.1K; Vol24H $4.03M; 24H -73.99%; V/LP 68.10x; 池数 2; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Plumber](https://dexscreener.com/solana/j3hkh2ne88wrie1shpe53jd7ke12e2lmg7cnlb4bjftn) | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | PVP风险池 | Score 29; Tier Early; LP $138.4K; Vol24H $17.16M; 24H +741.00%; V/LP 124.00x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 85; Tier Liquid; LP $2.36M; Vol24H $445.9K; 24H +2.62%; V/LP 0.19x; 池数 1; 分项 L20/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 82; Tier Liquid; LP $759.3K; Vol24H $2.43M; 24H -22.72%; V/LP 3.20x; 池数 2; 分项 L17/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 77; Tier Early; LP $583.8K; Vol24H $2.69M; 24H +14.27%; V/LP 4.61x; 池数 1; 分项 L16/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 77; Tier Liquid; LP $1.16M; Vol24H $215.4K; 24H +14.81%; V/LP 0.19x; 池数 1; 分项 L19/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 73; Tier Liquid; LP $2.05M; Vol24H $89.0K; 24H -2.23%; V/LP 0.04x; 池数 1; 分项 L20/V7/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 73; Tier Early; LP $642.1K; Vol24H $2.02M; 24H -30.94%; V/LP 3.14x; 池数 2; 分项 L17/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WW](https://dexscreener.com/solana/cb2x8djgpmjhudrr6gzmvpp9mxxqensnmxvm388nncge) | SOL | [14doqP...Xqpump](https://solscan.io/token/14doqPq3fLzx6kB4JRRnCMDPPLeGmGXd6QY5ZGXqpump) | 次观察 | Score 64; Tier Micro; LP $68.6K; Vol24H $503.2K; 24H +14.29%; V/LP 7.33x; 池数 3; 分项 L8/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | PVP风险池 | Score 39; Tier Liquid; LP $2.20M; Vol24H $56.63M; 24H +11.70%; V/LP 25.69x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ElonCoin | BSC | [0x499c...317777](https://bscscan.com/token/0x499c573997a1382f4051ece45b3d6b2f0e317777) | PVP风险池 | Score 36; Tier Micro; LP $84.5K; Vol24H $3.16M; 24H +67.07%; V/LP 37.45x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MARIO64 | SOL | [CX2v7J...WJpump](https://solscan.io/token/CX2v7JSHJQDcNooubzzvZG8TPaDwbaPgfzcXRSWJpump) | PVP风险池 | Score 35; Tier Micro; LP $71.5K; Vol24H $4.76M; 24H -73.54%; V/LP 66.61x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BOT | SOL | [HukaK2...myT8WJ](https://solscan.io/token/HukaK2eHhbTyiuUwuKMntjPJP4aGdD4VwiExsNmyT8WJ) | PVP风险池 | Score 35; Tier Micro; LP $66.3K; Vol24H $3.67M; 24H -60.32%; V/LP 55.39x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Plumber](https://dexscreener.com/solana/j3hkh2ne88wrie1shpe53jd7ke12e2lmg7cnlb4bjftn) | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | PVP风险池 | Score 29; Tier Early; LP $130.6K; Vol24H $17.06M; 24H +421.00%; V/LP 130.63x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [GTA](https://dexscreener.com/solana/42clgy3eds7x8k3qqgjwnginpnooqjtlreqcwrwq46gf) | SOL | [BVEaDT...xTpump](https://solscan.io/token/BVEaDToN2Ufn8m1Jnqy8rtwwCiiMC7JcFtvmKPxTpump) | PVP风险池 | Score 27; Tier Micro; LP $66.4K; Vol24H $6.68M; 24H +1758.00%; V/LP 100.56x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | PVP风险池 | Score 20; Tier Liquid; LP $817.5K; Vol24H $33.43M; 24H +134.34%; V/LP 40.89x; 池数 1; 分项 L18/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PITCOIN](https://dexscreener.com/solana/atnqriwpy8kgjp9us3rm4ffayva3yde63hppew4tdeaf) | SOL | [G1iBvj...m1pump](https://solscan.io/token/G1iBvjhZ9wpGUZdQcvhRSqjow3x6xetsnmEBBMm1pump) | PVP风险池 | Score 0; Tier Micro; LP $27.6K; Vol24H $6.08M; 24H +217.00%; V/LP 220.31x; 池数 1; 分项 L4/V17/B0/Buy3/Risk-65 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $2.20M; Vol24H $56.63M; 24H +11.70%; V/LP 25.69x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| ElonCoin | BSC | [0x499c...317777](https://bscscan.com/token/0x499c573997a1382f4051ece45b3d6b2f0e317777) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $84.5K; Vol24H $3.16M; 24H +67.07%; V/LP 37.45x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MARIO64 | SOL | [CX2v7J...WJpump](https://solscan.io/token/CX2v7JSHJQDcNooubzzvZG8TPaDwbaPgfzcXRSWJpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $71.5K; Vol24H $4.76M; 24H -73.54%; V/LP 66.61x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BOT | SOL | [HukaK2...myT8WJ](https://solscan.io/token/HukaK2eHhbTyiuUwuKMntjPJP4aGdD4VwiExsNmyT8WJ) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $66.3K; Vol24H $3.67M; 24H -60.32%; V/LP 55.39x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Plumber](https://dexscreener.com/solana/j3hkh2ne88wrie1shpe53jd7ke12e2lmg7cnlb4bjftn) | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $130.6K; Vol24H $17.06M; 24H +421.00%; V/LP 130.63x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [GTA](https://dexscreener.com/solana/42clgy3eds7x8k3qqgjwnginpnooqjtlreqcwrwq46gf) | SOL | [BVEaDT...xTpump](https://solscan.io/token/BVEaDToN2Ufn8m1Jnqy8rtwwCiiMC7JcFtvmKPxTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $66.4K; Vol24H $6.68M; 24H +1758.00%; V/LP 100.56x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 20; Tier Liquid; LP $817.5K; Vol24H $33.43M; 24H +134.34%; V/LP 40.89x; 池数 1; 分项 L18/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [PITCOIN](https://dexscreener.com/solana/atnqriwpy8kgjp9us3rm4ffayva3yde63hppew4tdeaf) | SOL | [G1iBvj...m1pump](https://solscan.io/token/G1iBvjhZ9wpGUZdQcvhRSqjow3x6xetsnmEBBMm1pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $27.6K; Vol24H $6.08M; 24H +217.00%; V/LP 220.31x; 池数 1; 分项 L4/V17/B0/Buy3/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $13.97M; Vol24H $7.63M; 24H -0.31%; V/LP 0.55x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.48M; Vol24H $4.19M; 24H +0.02%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $12.34M; Vol24H $2.36M; 24H -0.26%; V/LP 0.19x; 池数 5; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $2.08M; Vol24H $791.7K; 24H -1.71%; V/LP 0.38x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BLUAI | BSC | [0xed9a...cf9aad](https://bscscan.com/token/0xed9ae3def8d6f052971bb8b6d1975ff267cf9aad) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 63; Tier Liquid; LP $751.4K; Vol24H $233.8K; 24H -1.55%; V/LP 0.31x; 池数 1; 分项 L17/V9/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BR | BSC | [0xff7d...f56b41](https://bscscan.com/token/0xff7d6a96ae471bbcd7713af9cb1feeb16cf56b41) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $1.15M; Vol24H $1.05M; 24H +70.35%; V/LP 0.91x; 池数 1; 分项 L19/V14/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [WW](https://dexscreener.com/solana/cb2x8djgpmjhudrr6gzmvpp9mxxqensnmxvm388nncge) | SOL | [14doqP...Xqpump](https://solscan.io/token/14doqPq3fLzx6kB4JRRnCMDPPLeGmGXd6QY5ZGXqpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| ElonCoin | BSC | [0x499c...317777](https://bscscan.com/token/0x499c573997a1382f4051ece45b3d6b2f0e317777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| MARIO64 | SOL | [CX2v7J...WJpump](https://solscan.io/token/CX2v7JSHJQDcNooubzzvZG8TPaDwbaPgfzcXRSWJpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 5 / Liquid 10 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 338} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
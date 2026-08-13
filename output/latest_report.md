# 自我进化轮巡

**本轮时间 UTC：** 2026-08-13T01:24:56Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 126 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 215 |
| 合并后Token | 126 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 4 |
| 多池Token | 7 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 7 |
| Liquid层 | 8 |
| Mature层 | 2 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 983，刷新时间 2026-08-10T01:06:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 85; Tier Liquid; LP $2.36M; Vol24H $459.3K; 24H +1.19%; V/LP 0.19x; 池数 1; 分项 L20/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 82; Tier Liquid; LP $791.9K; Vol24H $2.51M; 24H -16.26%; V/LP 3.18x; 池数 2; 分项 L17/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 82; Tier Liquid; LP $1.15M; Vol24H $202.5K; 24H +4.91%; V/LP 0.18x; 池数 1; 分项 L19/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 79; Tier Liquid; LP $2.05M; Vol24H $328.7K; 24H +0.00%; V/LP 0.16x; 池数 1; 分项 L20/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 76; Tier Early; LP $583.1K; Vol24H $2.45M; 24H +11.69%; V/LP 4.19x; 池数 1; 分项 L16/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 71; Tier Early; LP $600.3K; Vol24H $1.70M; 24H -37.04%; V/LP 2.83x; 池数 2; 分项 L16/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VORF](https://dexscreener.com/solana/dohsu6suphskcycqhahecbo3aj6trc7dsvepezznea3f) | SOL | [3VshVu...DXpump](https://solscan.io/token/3VshVuxnWQLevRL6YEWDLs8Zqicnj11tzPP5BgDXpump) | 次观察 | Score 64; Tier Early; LP $134.0K; Vol24H $257.9K; 24H +79.70%; V/LP 1.92x; 池数 1; 分项 L10/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Plumber | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | PVP风险池 | Score 51; Tier Early; LP $118.7K; Vol24H $15.06M; 24H +0.91%; V/LP 126.91x; 池数 2; 分项 L10/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | PVP风险池 | Score 39; Tier Liquid; LP $2.17M; Vol24H $57.20M; 24H +8.29%; V/LP 26.31x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOT](https://dexscreener.com/solana/2cdmgj24mytdzpgfvveytgfldah6387yeabxwcjy1mlg) | SOL | [HukaK2...myT8WJ](https://solscan.io/token/HukaK2eHhbTyiuUwuKMntjPJP4aGdD4VwiExsNmyT8WJ) | PVP风险池 | Score 35; Tier Micro; LP $67.7K; Vol24H $3.19M; 24H -62.18%; V/LP 47.06x; 池数 2; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 82; Tier Liquid; LP $761.5K; Vol24H $2.52M; 24H -19.63%; V/LP 3.31x; 池数 2; 分项 L17/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 82; Tier Liquid; LP $1.14M; Vol24H $192.5K; 24H +6.12%; V/LP 0.17x; 池数 1; 分项 L19/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 76; Tier Early; LP $572.7K; Vol24H $2.27M; 24H +18.93%; V/LP 3.97x; 池数 1; 分项 L16/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 次观察 | Score 75; Tier Early; LP $241.0K; Vol24H $131.0K; 24H -2.59%; V/LP 0.54x; 池数 5; 分项 L13/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 75; Tier Early; LP $600.3K; Vol24H $1.53M; 24H -19.09%; V/LP 2.55x; 池数 2; 分项 L16/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VORF](https://dexscreener.com/solana/dohsu6suphskcycqhahecbo3aj6trc7dsvepezznea3f) | SOL | [3VshVu...DXpump](https://solscan.io/token/3VshVuxnWQLevRL6YEWDLs8Zqicnj11tzPP5BgDXpump) | 次观察 | Score 65; Tier Early; LP $139.6K; Vol24H $266.0K; 24H +78.02%; V/LP 1.91x; 池数 1; 分项 L11/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | PVP风险池 | Score 39; Tier Liquid; LP $1.97M; Vol24H $57.87M; 24H -16.07%; V/LP 29.42x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Plumber | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | PVP风险池 | Score 37; Tier Early; LP $123.9K; Vol24H $8.05M; 24H -62.73%; V/LP 64.94x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | PVP风险池 | Score 35; Tier Micro; LP $78.7K; Vol24H $3.29M; 24H +45.07%; V/LP 41.84x; 池数 1; 分项 L8/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GTA | SOL | [BVEaDT...xTpump](https://solscan.io/token/BVEaDToN2Ufn8m1Jnqy8rtwwCiiMC7JcFtvmKPxTpump) | PVP风险池 | Score 27; Tier Micro; LP $80.0K; Vol24H $7.89M; 24H +2400.38%; V/LP 98.60x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | PVP风险池 | Score 20; Tier Liquid; LP $828.4K; Vol24H $42.99M; 24H +137.29%; V/LP 51.89x; 池数 1; 分项 L18/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PITCOIN](https://dexscreener.com/solana/atnqriwpy8kgjp9us3rm4ffayva3yde63hppew4tdeaf) | SOL | [G1iBvj...m1pump](https://solscan.io/token/G1iBvjhZ9wpGUZdQcvhRSqjow3x6xetsnmEBBMm1pump) | PVP风险池 | Score 14; Tier Micro; LP $34.1K; Vol24H $6.56M; 24H +355.00%; V/LP 192.36x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [apes](https://dexscreener.com/solana/5qwem5zppekb1vmkjrkpvc3kelrleyonhvhj85czffse) | SOL | [7ZgRjH...Kfpump](https://solscan.io/token/7ZgRjHSnjDqc73mYitJZ4NAAVtdWrTyQEnoXB6Kfpump) | PVP风险池 | Score 14; Tier Micro; LP $36.1K; Vol24H $5.45M; 24H +435.00%; V/LP 150.91x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [COGE](https://dexscreener.com/solana/5q1araopbu8omqbmjcwhfsdun2ucdxhwdfs8t9tgruck) | SOL | [AvecKF...XQpump](https://solscan.io/token/AvecKFxn8ihToR7gwgAVjfqV56N1rWhN7hv8joXQpump) | PVP风险池 | Score 13; Tier Micro; LP $27.1K; Vol24H $3.71M; 24H +248.00%; V/LP 136.85x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $13.98M; Vol24H $6.61M; 24H -0.34%; V/LP 0.47x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $1.97M; Vol24H $57.87M; 24H -16.07%; V/LP 29.42x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Plumber | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $123.9K; Vol24H $8.05M; 24H -62.73%; V/LP 64.94x; 池数 2; 分项 L10/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Micro; LP $78.7K; Vol24H $3.29M; 24H +45.07%; V/LP 41.84x; 池数 1; 分项 L8/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| GTA | SOL | [BVEaDT...xTpump](https://solscan.io/token/BVEaDToN2Ufn8m1Jnqy8rtwwCiiMC7JcFtvmKPxTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $80.0K; Vol24H $7.89M; 24H +2400.38%; V/LP 98.60x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 20; Tier Liquid; LP $828.4K; Vol24H $42.99M; 24H +137.29%; V/LP 51.89x; 池数 1; 分项 L18/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [PITCOIN](https://dexscreener.com/solana/atnqriwpy8kgjp9us3rm4ffayva3yde63hppew4tdeaf) | SOL | [G1iBvj...m1pump](https://solscan.io/token/G1iBvjhZ9wpGUZdQcvhRSqjow3x6xetsnmEBBMm1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $34.1K; Vol24H $6.56M; 24H +355.00%; V/LP 192.36x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [apes](https://dexscreener.com/solana/5qwem5zppekb1vmkjrkpvc3kelrleyonhvhj85czffse) | SOL | [7ZgRjH...Kfpump](https://solscan.io/token/7ZgRjHSnjDqc73mYitJZ4NAAVtdWrTyQEnoXB6Kfpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.1K; Vol24H $5.45M; 24H +435.00%; V/LP 150.91x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [COGE](https://dexscreener.com/solana/5q1araopbu8omqbmjcwhfsdun2ucdxhwdfs8t9tgruck) | SOL | [AvecKF...XQpump](https://solscan.io/token/AvecKFxn8ihToR7gwgAVjfqV56N1rWhN7hv8joXQpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $27.1K; Vol24H $3.71M; 24H +248.00%; V/LP 136.85x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $13.98M; Vol24H $6.61M; 24H -0.34%; V/LP 0.47x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $1.53M; Vol24H $2.48M; 24H +0.05%; V/LP 1.62x; 池数 1; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $12.60M; Vol24H $2.31M; 24H +0.02%; V/LP 0.18x; 池数 5; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 73; Tier Liquid; LP $1.12M; Vol24H $8.74M; 24H +0.31%; V/LP 7.78x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BLUAI | BSC | [0xed9a...cf9aad](https://bscscan.com/token/0xed9ae3def8d6f052971bb8b6d1975ff267cf9aad) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 63; Tier Liquid; LP $758.1K; Vol24H $226.0K; 24H -0.47%; V/LP 0.30x; 池数 1; 分项 L17/V9/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BR | BSC | [0xff7d...f56b41](https://bscscan.com/token/0xff7d6a96ae471bbcd7713af9cb1feeb16cf56b41) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 61; Tier Liquid; LP $1.17M; Vol24H $1.23M; 24H +75.98%; V/LP 1.05x; 池数 1; 分项 L19/V14/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [VORF](https://dexscreener.com/solana/dohsu6suphskcycqhahecbo3aj6trc7dsvepezznea3f) | SOL | [3VshVu...DXpump](https://solscan.io/token/3VshVuxnWQLevRL6YEWDLs8Zqicnj11tzPP5BgDXpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Plumber | SOL | [GCa9TZ...jFpump](https://solscan.io/token/GCa9TZMK9Q3VUSkhZgX76YAQBjqQd1dPxkBnZojFpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| GTA | SOL | [BVEaDT...xTpump](https://solscan.io/token/BVEaDToN2Ufn8m1Jnqy8rtwwCiiMC7JcFtvmKPxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 7 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_boosts | {'ok': True, 'count': 29, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 339} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
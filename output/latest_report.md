# 自我进化轮巡

**本轮时间 UTC：** 2026-08-10T07:20:15Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 135 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 260 |
| 合并后Token | 135 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 5 |
| 多池Token | 10 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 7 |
| Mature层 | 3 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 3 |

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
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 85; Tier Liquid; LP $1.81M; Vol24H $2.27M; 24H +8.14%; V/LP 1.25x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $948.1K; Vol24H $4.87M; 24H +8.32%; V/LP 5.14x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 81; Tier Early; LP $541.4K; Vol24H $2.25M; 24H -16.88%; V/LP 4.16x; 池数 2; 分项 L16/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 76; Tier Liquid; LP $1.06M; Vol24H $129.7K; 24H -9.27%; V/LP 0.12x; 池数 1; 分项 L19/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 73; Tier Early; LP $127.3K; Vol24H $57.3K; 24H +6.88%; V/LP 0.45x; 池数 3; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 50; Tier Early; LP $376.1K; Vol24H $16.82M; 24H -15.63%; V/LP 44.71x; 池数 2; 分项 L14/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | PVP风险池 | Score 32; Tier Early; LP $120.3K; Vol24H $4.65M; 24H +47.62%; V/LP 38.63x; 池数 2; 分项 L10/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Remus](https://dexscreener.com/solana/flbsnxkr6sddkepbb254yosgjqufbuyz8qvykybwpv47) | SOL | [23e4CN...XYPgme](https://solscan.io/token/23e4CNuJxvBQ7RjNLc8Bh3yN3pQq6jeiTbyzJGXYPgme) | PVP风险池 | Score 26; Tier Micro; LP $64.4K; Vol24H $10.91M; 24H +1291.00%; V/LP 169.26x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RISK](https://dexscreener.com/solana/5vhfpld8galvmqe7hbd3jycsqmnn2c61stwbgeymssbi) | SOL | [BCFffe...B1pump](https://solscan.io/token/BCFffeVdfad5gCpuVXrnq5WAAuGLpxakM3z3zfB1pump) | PVP风险池 | Score 24; Tier Early; LP $111.4K; Vol24H $6.60M; 24H +2762.00%; V/LP 59.20x; 池数 5; 分项 L10/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bark](https://dexscreener.com/solana/6pidtwpgoxfmhtkjaa6wrn7r45avhwgybm6l5vprbmop) | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | PVP风险池 | Score 15; Tier Micro; LP $47.6K; Vol24H $11.51M; 24H +657.00%; V/LP 241.90x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 89; Tier Liquid; LP $932.0K; Vol24H $4.89M; 24H -3.61%; V/LP 5.25x; 池数 2; 分项 L18/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 85; Tier Liquid; LP $1.81M; Vol24H $2.17M; 24H +9.09%; V/LP 1.20x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 80; Tier Early; LP $295.5K; Vol24H $559.1K; 24H +4.86%; V/LP 1.89x; 池数 5; 分项 L14/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 73; Tier Early; LP $128.5K; Vol24H $57.6K; 24H +7.88%; V/LP 0.45x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 次观察 | Score 68; Tier Liquid; LP $1.68M; Vol24H $20.74M; 24H +16.02%; V/LP 12.34x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 67; Tier Liquid; LP $1.13M; Vol24H $1.85M; 24H +183.00%; V/LP 1.63x; 池数 2; 分项 L19/V16/B0/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 51; Tier Early; LP $403.2K; Vol24H $16.58M; 24H -20.92%; V/LP 41.11x; 池数 2; 分项 L15/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | PVP风险池 | Score 45; Tier Early; LP $107.8K; Vol24H $4.37M; 24H -6.16%; V/LP 40.55x; 池数 1; 分项 L9/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Bark | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | PVP风险池 | Score 26; Tier Micro; LP $52.1K; Vol24H $11.64M; 24H +784.63%; V/LP 223.30x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Remus | SOL | [23e4CN...XYPgme](https://solscan.io/token/23e4CNuJxvBQ7RjNLc8Bh3yN3pQq6jeiTbyzJGXYPgme) | PVP风险池 | Score 26; Tier Micro; LP $62.3K; Vol24H $10.95M; 24H +1182.88%; V/LP 175.69x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Sheep](https://dexscreener.com/solana/hwxhw242texcczevruxsyj5eybj2ezjmvvwty4h8n69a) | SOL | [Dz2iVS...V5pump](https://solscan.io/token/Dz2iVSLXFp7dXowD1nybWyCXuUcpV7cBZu68YPV5pump) | PVP风险池 | Score 26; Tier Micro; LP $55.8K; Vol24H $2.92M; 24H +156.00%; V/LP 52.27x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PUMPGUY](https://dexscreener.com/solana/3kcqzdnlgsuk4oy2s8jytry2zs11tqkgyg3s1fusflek) | SOL | [tpg7sW...Tppump](https://solscan.io/token/tpg7sWJPSKijHqPqtpHY2BWBEUq1RwGxmJpD8Tppump) | PVP风险池 | Score 26; Tier Micro; LP $62.8K; Vol24H $2.67M; 24H +232.00%; V/LP 42.57x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOT](https://dexscreener.com/solana/fucql6yzqdk6ggfffuvotpvuswyglel5wdmvdbvaecem) | SOL | [3zbV8n...xEEd5D](https://solscan.io/token/3zbV8nS9Wx2WxJ16uXYjTZZvoHbTnrvTQYyZE5xEEd5D) | PVP风险池 | Score 15; Tier Micro; LP $39.8K; Vol24H $4.89M; 24H +556.00%; V/LP 123.00x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HORACE](https://dexscreener.com/solana/fzd7vmvsucvta7xd6fngc58wc1refh3memcvcnyhnf1b) | SOL | [Hv814f...Qppump](https://solscan.io/token/Hv814fa7MB1B2ZBrvjyz9iHimBJ1YAx1Gir8FMQppump) | PVP风险池 | Score 14; Tier Micro; LP $38.4K; Vol24H $6.72M; 24H +462.00%; V/LP 175.11x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 成熟池观察 | Score 74; Tier Mature; LP $12.48M; Vol24H $8.35M; 24H +23.21%; V/LP 0.67x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Early; LP $403.2K; Vol24H $16.58M; 24H -20.92%; V/LP 41.11x; 池数 2; 分项 L15/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Early; LP $107.8K; Vol24H $4.37M; 24H -6.16%; V/LP 40.55x; 池数 1; 分项 L9/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Bark | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $52.1K; Vol24H $11.64M; 24H +784.63%; V/LP 223.30x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Remus | SOL | [23e4CN...XYPgme](https://solscan.io/token/23e4CNuJxvBQ7RjNLc8Bh3yN3pQq6jeiTbyzJGXYPgme) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.3K; Vol24H $10.95M; 24H +1182.88%; V/LP 175.69x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Sheep](https://dexscreener.com/solana/hwxhw242texcczevruxsyj5eybj2ezjmvvwty4h8n69a) | SOL | [Dz2iVS...V5pump](https://solscan.io/token/Dz2iVSLXFp7dXowD1nybWyCXuUcpV7cBZu68YPV5pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $55.8K; Vol24H $2.92M; 24H +156.00%; V/LP 52.27x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [PUMPGUY](https://dexscreener.com/solana/3kcqzdnlgsuk4oy2s8jytry2zs11tqkgyg3s1fusflek) | SOL | [tpg7sW...Tppump](https://solscan.io/token/tpg7sWJPSKijHqPqtpHY2BWBEUq1RwGxmJpD8Tppump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.8K; Vol24H $2.67M; 24H +232.00%; V/LP 42.57x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BOT](https://dexscreener.com/solana/fucql6yzqdk6ggfffuvotpvuswyglel5wdmvdbvaecem) | SOL | [3zbV8n...xEEd5D](https://solscan.io/token/3zbV8nS9Wx2WxJ16uXYjTZZvoHbTnrvTQYyZE5xEEd5D) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $39.8K; Vol24H $4.89M; 24H +556.00%; V/LP 123.00x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [HORACE](https://dexscreener.com/solana/fzd7vmvsucvta7xd6fngc58wc1refh3memcvcnyhnf1b) | SOL | [Hv814f...Qppump](https://solscan.io/token/Hv814fa7MB1B2ZBrvjyz9iHimBJ1YAx1Gir8FMQppump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $38.4K; Vol24H $6.72M; 24H +462.00%; V/LP 175.11x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $12.48M; Vol24H $8.35M; 24H +23.21%; V/LP 0.67x; 池数 3; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.10M; Vol24H $692.6K; 24H -0.64%; V/LP 0.63x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Mature; LP $6.39M; Vol24H $16.67M; 24H +11.08%; V/LP 2.61x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $3.90M; Vol24H $15.50M; 24H +9.27%; V/LP 3.97x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Mature; LP $8.10M; Vol24H $18.70M; 24H -16.64%; V/LP 2.31x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BLUAI | BSC | [0xed9a...cf9aad](https://bscscan.com/token/0xed9ae3def8d6f052971bb8b6d1975ff267cf9aad) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 67; Tier Liquid; LP $837.6K; Vol24H $3.34M; 24H -21.89%; V/LP 3.98x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Bark | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Remus | SOL | [23e4CN...XYPgme](https://solscan.io/token/23e4CNuJxvBQ7RjNLc8Bh3yN3pQq6jeiTbyzJGXYPgme) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 8 / Early 7 / Liquid 7 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
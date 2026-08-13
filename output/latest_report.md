# 自我进化轮巡

**本轮时间 UTC：** 2026-08-13T21:38:54Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 129 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 251 |
| 合并后Token | 129 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 2 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 9 |
| Mature层 | 1 |
| 需要链上确认 | 15 |
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
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 主观察 | Score 86; Tier Early; LP $441.1K; Vol24H $3.26M; 24H +1.94%; V/LP 7.39x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $846.0K; Vol24H $3.85M; 24H +19.17%; V/LP 4.55x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 80; Tier Liquid; LP $1.13M; Vol24H $120.0K; 24H -7.08%; V/LP 0.11x; 池数 1; 分项 L19/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 74; Tier Early; LP $604.8K; Vol24H $930.9K; 24H -9.80%; V/LP 1.54x; 池数 2; 分项 L16/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 67; Tier Liquid; LP $1.58M; Vol24H $18.82; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 次观察 | Score 65; Tier Liquid; LP $757.9K; Vol24H $8.20M; 24H +0.41%; V/LP 10.81x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VORF](https://dexscreener.com/solana/dohsu6suphskcycqhahecbo3aj6trc7dsvepezznea3f) | SOL | [3VshVu...DXpump](https://solscan.io/token/3VshVuxnWQLevRL6YEWDLs8Zqicnj11tzPP5BgDXpump) | 次观察 | Score 64; Tier Micro; LP $74.6K; Vol24H $495.4K; 24H -73.86%; V/LP 6.64x; 池数 1; 分项 L8/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | PVP风险池 | Score 49; Tier Liquid; LP $919.9K; Vol24H $19.46M; 24H -16.01%; V/LP 21.15x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | PVP风险池 | Score 37; Tier Liquid; LP $839.6K; Vol24H $28.74M; 24H +15.26%; V/LP 34.24x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| utility | BSC | [0xede0...847777](https://bscscan.com/token/0xede00776439f9c49c592e43eee34777a51847777) | PVP风险池 | Score 33; Tier Early; LP $312.6K; Vol24H $15.99M; 24H +1268.07%; V/LP 51.16x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 主观察 | Score 86; Tier Early; LP $468.0K; Vol24H $3.09M; 24H +2.82%; V/LP 6.60x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $852.9K; Vol24H $3.90M; 24H +22.91%; V/LP 4.57x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 80; Tier Liquid; LP $1.13M; Vol24H $108.1K; 24H -5.21%; V/LP 0.10x; 池数 1; 分项 L19/V7/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 次观察 | Score 73; Tier Early; LP $607.9K; Vol24H $891.9K; 24H -11.39%; V/LP 1.47x; 池数 1; 分项 L16/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 次观察 | Score 67; Tier Liquid; LP $1.58M; Vol24H $18.82; 24H +0.00%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 次观察 | Score 65; Tier Early; LP $713.3K; Vol24H $8.11M; 24H +1.02%; V/LP 11.38x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | PVP风险池 | Score 49; Tier Liquid; LP $926.6K; Vol24H $19.42M; 24H -12.21%; V/LP 20.96x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | PVP风险池 | Score 42; Tier Liquid; LP $839.7K; Vol24H $26.82M; 24H +6.22%; V/LP 31.94x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| utility | BSC | [0xede0...847777](https://bscscan.com/token/0xede00776439f9c49c592e43eee34777a51847777) | PVP风险池 | Score 33; Tier Early; LP $333.0K; Vol24H $16.03M; 24H +1538.11%; V/LP 48.15x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PLANSEM](https://dexscreener.com/solana/4pwnxh6ce2y5cydrkyvfewey9rbew1tbc8jvf9fft317) | SOL | [j8RdRQ...obpump](https://solscan.io/token/j8RdRQ8tQRbx62cr46e5LM8ekRDZr1opqmbgsobpump) | PVP风险池 | Score 27; Tier Micro; LP $66.2K; Vol24H $7.96M; 24H +1521.00%; V/LP 120.22x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| K-HOME | SOL | [EUB1eZ...yjpump](https://solscan.io/token/EUB1eZBt4m3X4FbperWnKGJdvLsuLMu2YmJix5yjpump) | PVP风险池 | Score 27; Tier Micro; LP $78.2K; Vol24H $7.49M; 24H +8056.65%; V/LP 95.77x; 池数 7; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CHAM | SOL | [GJaxyL...zaCHAM](https://solscan.io/token/GJaxyLPuZh5U2U4LgAVdGGC6KYRVXZp8t91P2vzaCHAM) | PVP风险池 | Score 26; Tier Micro; LP $58.3K; Vol24H $7.00M; 24H +1088.45%; V/LP 120.14x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | PVP风险池 | Score 26; Tier Micro; LP $56.5K; Vol24H $4.90M; 24H +310.00%; V/LP 86.84x; 池数 6; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOIÚNA](https://dexscreener.com/solana/63jzrkafyryrizeet1y7hzbmv2kfx48twsxzeoigk6ar) | SOL | [GRehQK...kGpump](https://solscan.io/token/GRehQKv9E3fVuNJGQTwAAjYpcixRCYKkzAXAb5kGpump) | PVP风险池 | Score 14; Tier Micro; LP $36.2K; Vol24H $15.90M; 24H +276.00%; V/LP 439.67x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 成熟池观察 | Score 74; Tier Mature; LP $12.06M; Vol24H $2.88M; 24H -5.24%; V/LP 0.24x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $926.6K; Vol24H $19.42M; 24H -12.21%; V/LP 20.96x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 42; Tier Liquid; LP $839.7K; Vol24H $26.82M; 24H +6.22%; V/LP 31.94x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| utility | BSC | [0xede0...847777](https://bscscan.com/token/0xede00776439f9c49c592e43eee34777a51847777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $333.0K; Vol24H $16.03M; 24H +1538.11%; V/LP 48.15x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [PLANSEM](https://dexscreener.com/solana/4pwnxh6ce2y5cydrkyvfewey9rbew1tbc8jvf9fft317) | SOL | [j8RdRQ...obpump](https://solscan.io/token/j8RdRQ8tQRbx62cr46e5LM8ekRDZr1opqmbgsobpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $66.2K; Vol24H $7.96M; 24H +1521.00%; V/LP 120.22x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| K-HOME | SOL | [EUB1eZ...yjpump](https://solscan.io/token/EUB1eZBt4m3X4FbperWnKGJdvLsuLMu2YmJix5yjpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $78.2K; Vol24H $7.49M; 24H +8056.65%; V/LP 95.77x; 池数 7; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CHAM | SOL | [GJaxyL...zaCHAM](https://solscan.io/token/GJaxyLPuZh5U2U4LgAVdGGC6KYRVXZp8t91P2vzaCHAM) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $58.3K; Vol24H $7.00M; 24H +1088.45%; V/LP 120.14x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $56.5K; Vol24H $4.90M; 24H +310.00%; V/LP 86.84x; 池数 6; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BOIÚNA](https://dexscreener.com/solana/63jzrkafyryrizeet1y7hzbmv2kfx48twsxzeoigk6ar) | SOL | [GRehQK...kGpump](https://solscan.io/token/GRehQKv9E3fVuNJGQTwAAjYpcixRCYKkzAXAb5kGpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.2K; Vol24H $15.90M; 24H +276.00%; V/LP 439.67x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $12.06M; Vol24H $2.88M; 24H -5.24%; V/LP 0.24x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.09M; Vol24H $826.4K; 24H -1.48%; V/LP 0.76x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.71M; Vol24H $7.38M; 24H +5.51%; V/LP 4.31x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BLUAI | BSC | [0xed9a...cf9aad](https://bscscan.com/token/0xed9ae3def8d6f052971bb8b6d1975ff267cf9aad) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $774.1K; Vol24H $424.3K; 24H +6.76%; V/LP 0.55x; 池数 1; 分项 L17/V11/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ALON | SOL | [8XtRWb...z9s5WS](https://solscan.io/token/8XtRWb4uAAJFMP4QQhoYYCWR6XXb7ybcCdiqPwz9s5WS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | [0x85E4...06a988](https://bscscan.com/token/0x85E43bF8faAF04ceDdcD03d6C07438b72606a988) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| DOS | BSC | [0xb0f0...a30e37](https://bscscan.com/token/0xb0f09ea9ae0515c3551080d4a745c8115aa30e37) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| APR | BSC | [0x299a...611099](https://bscscan.com/token/0x299ad4299da5b2b93fba4c96967b040c7f611099) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| utility | BSC | [0xede0...847777](https://bscscan.com/token/0xede00776439f9c49c592e43eee34777a51847777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 3 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 9 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
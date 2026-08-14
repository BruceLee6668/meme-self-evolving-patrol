# 自我进化轮巡

**本轮时间 UTC：** 2026-08-14T16:48:31Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 133 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 260 |
| 合并后Token | 133 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 4 |
| 多池Token | 10 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 8 |
| Liquid层 | 6 |
| Mature层 | 5 |
| 需要链上确认 | 15 |
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
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 88; Tier Liquid; LP $789.0K; Vol24H $4.78M; 24H -6.56%; V/LP 6.06x; 池数 2; 分项 L17/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 主观察 | Score 85; Tier Early; LP $473.7K; Vol24H $2.41M; 24H +0.84%; V/LP 5.09x; 池数 2; 分项 L15/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ACU | BSC | [0x6ef2...8cfeaf](https://bscscan.com/token/0x6ef2ffb38d64afe18ce782da280b300e358cfeaf) | 主观察 | Score 79; Tier Liquid; LP $918.5K; Vol24H $4.13M; 24H -12.18%; V/LP 4.50x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 次观察 | Score 67; Tier Liquid; LP $1.22M; Vol24H $10.37M; 24H -0.16%; V/LP 8.50x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | PVP风险池 | Score 45; Tier Micro; LP $85.1K; Vol24H $5.53M; 24H -15.61%; V/LP 64.98x; 池数 1; 分项 L9/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Momota](https://dexscreener.com/solana/bngrt9clk62z6iym7yqizvufeognfhjvhmw3r595pwzb) | SOL | [CrJPSv...espump](https://solscan.io/token/CrJPSvj625TnPdWS42aG5ybMcHeFvnNqq5AExVespump) | PVP风险池 | Score 39; Tier Early; LP $184.2K; Vol24H $4.94M; 24H +63.42%; V/LP 26.83x; 池数 2; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bBroker | BSC | [0xf196...cd7777](https://bscscan.com/token/0xf1969f437fe3c485468fb17b0d9861c24dcd7777) | PVP风险池 | Score 29; Tier Early; LP $126.6K; Vol24H $5.58M; 24H +386.09%; V/LP 44.04x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| cc | SOL | [E3i7sT...m2pump](https://solscan.io/token/E3i7sTY5QYEBh3itepnomZQt7Eh5kzmHFk1vkm2pump) | PVP风险池 | Score 22; Tier Micro; LP $77.9K; Vol24H $2.82M; 24H +118.96%; V/LP 36.27x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [K-HOME](https://dexscreener.com/solana/abgs2ze2ix81ntsxd7ccys8vvqn64jrnjuprs3jrlghv) | SOL | [EUB1eZ...yjpump](https://solscan.io/token/EUB1eZBt4m3X4FbperWnKGJdvLsuLMu2YmJix5yjpump) | PVP风险池 | Score 17; Tier Micro; LP $45.8K; Vol24H $2.38M; 24H -60.57%; V/LP 51.81x; 池数 1; 分项 L6/V16/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BOB | SOL | [4CmYEy...krpump](https://solscan.io/token/4CmYEygEusR76TpjxUbTjSLjyDbCMjxKhRKNozkrpump) | PVP风险池 | Score 14; Tier Micro; LP $38.5K; Vol24H $5.18M; 24H +531.92%; V/LP 134.52x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ACU | BSC | [0x6ef2...8cfeaf](https://bscscan.com/token/0x6ef2ffb38d64afe18ce782da280b300e358cfeaf) | 主观察 | Score 84; Tier Liquid; LP $936.2K; Vol24H $3.75M; 24H -6.13%; V/LP 4.00x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 83; Tier Liquid; LP $785.0K; Vol24H $4.34M; 24H -15.17%; V/LP 5.53x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 主观察 | Score 80; Tier Early; LP $454.1K; Vol24H $2.34M; 24H -10.37%; V/LP 5.16x; 池数 2; 分项 L15/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 73; Tier Early; LP $283.3K; Vol24H $85.9K; 24H -6.41%; V/LP 0.30x; 池数 5; 分项 L13/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 次观察 | Score 72; Tier Liquid; LP $1.31M; Vol24H $11.13M; 24H +0.27%; V/LP 8.52x; 池数 1; 分项 L19/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOS](https://dexscreener.com/solana/9htnhhvtwrpirdcsybzoahtlrz4nkxxne8qdkdczx57f) | SOL | [HmjCoa...P8pump](https://solscan.io/token/HmjCoarLh5duURfJ333DwfFiPyTCgFT35pRSAoP8pump) | 次观察 | Score 67; Tier Early; LP $348.8K; Vol24H $31.3K; 24H -7.72%; V/LP 0.09x; 池数 5; 分项 L14/V3/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | PVP风险池 | Score 55; Tier Liquid; LP $1.31M; Vol24H $27.56M; 24H -3.35%; V/LP 21.12x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Momota | SOL | [CrJPSv...espump](https://solscan.io/token/CrJPSvj625TnPdWS42aG5ybMcHeFvnNqq5AExVespump) | PVP风险池 | Score 39; Tier Early; LP $180.9K; Vol24H $4.95M; 24H +66.09%; V/LP 27.35x; 池数 2; 分项 L12/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | PVP风险池 | Score 36; Tier Micro; LP $99.1K; Vol24H $6.53M; 24H -45.24%; V/LP 65.89x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bBroker | BSC | [0xf196...cd7777](https://bscscan.com/token/0xf1969f437fe3c485468fb17b0d9861c24dcd7777) | PVP风险池 | Score 29; Tier Early; LP $116.3K; Vol24H $5.52M; 24H +362.02%; V/LP 47.44x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOB](https://dexscreener.com/solana/dhn4tufpkdroxdxyvthfx3y4yp6ahr8fukcrcgsp4mi3) | SOL | [4CmYEy...krpump](https://solscan.io/token/4CmYEygEusR76TpjxUbTjSLjyDbCMjxKhRKNozkrpump) | PVP风险池 | Score 22; Tier Micro; LP $35.5K; Vol24H $3.26M; 24H -59.46%; V/LP 91.63x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| cc | SOL | [E3i7sT...m2pump](https://solscan.io/token/E3i7sTY5QYEBh3itepnomZQt7Eh5kzmHFk1vkm2pump) | PVP风险池 | Score 22; Tier Micro; LP $66.9K; Vol24H $2.85M; 24H +86.20%; V/LP 42.65x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [K-HOME](https://dexscreener.com/solana/abgs2ze2ix81ntsxd7ccys8vvqn64jrnjuprs3jrlghv) | SOL | [EUB1eZ...yjpump](https://solscan.io/token/EUB1eZBt4m3X4FbperWnKGJdvLsuLMu2YmJix5yjpump) | PVP风险池 | Score 16; Tier Micro; LP $38.4K; Vol24H $2.18M; 24H -58.90%; V/LP 56.70x; 池数 1; 分项 L5/V16/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/cj2ohyuhe2ktjexd4erbbbxckfqab4teebivlhnpj6gs) | SOL | [Dmkj4d...xDpump](https://solscan.io/token/Dmkj4dB3Ngva9gWKkDgj8UMF39EC7ArpGf2rxLxDpump) | PVP风险池 | Score 2; Tier Micro; LP $68.4K; Vol24H $3.43M; 24H +2016.00%; V/LP 50.07x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $51.79M; Vol24H $3.21M; 24H -0.32%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 55; Tier Liquid; LP $1.31M; Vol24H $27.56M; 24H -3.35%; V/LP 21.12x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Momota | SOL | [CrJPSv...espump](https://solscan.io/token/CrJPSvj625TnPdWS42aG5ybMcHeFvnNqq5AExVespump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Early; LP $180.9K; Vol24H $4.95M; 24H +66.09%; V/LP 27.35x; 池数 2; 分项 L12/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $99.1K; Vol24H $6.53M; 24H -45.24%; V/LP 65.89x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| bBroker | BSC | [0xf196...cd7777](https://bscscan.com/token/0xf1969f437fe3c485468fb17b0d9861c24dcd7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $116.3K; Vol24H $5.52M; 24H +362.02%; V/LP 47.44x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BOB](https://dexscreener.com/solana/dhn4tufpkdroxdxyvthfx3y4yp6ahr8fukcrcgsp4mi3) | SOL | [4CmYEy...krpump](https://solscan.io/token/4CmYEygEusR76TpjxUbTjSLjyDbCMjxKhRKNozkrpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 22; Tier Micro; LP $35.5K; Vol24H $3.26M; 24H -59.46%; V/LP 91.63x; 池数 1; 分项 L5/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| cc | SOL | [E3i7sT...m2pump](https://solscan.io/token/E3i7sTY5QYEBh3itepnomZQt7Eh5kzmHFk1vkm2pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 22; Tier Micro; LP $66.9K; Vol24H $2.85M; 24H +86.20%; V/LP 42.65x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [K-HOME](https://dexscreener.com/solana/abgs2ze2ix81ntsxd7ccys8vvqn64jrnjuprs3jrlghv) | SOL | [EUB1eZ...yjpump](https://solscan.io/token/EUB1eZBt4m3X4FbperWnKGJdvLsuLMu2YmJix5yjpump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 16; Tier Micro; LP $38.4K; Vol24H $2.18M; 24H -58.90%; V/LP 56.70x; 池数 1; 分项 L5/V16/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [FTR](https://dexscreener.com/solana/cj2ohyuhe2ktjexd4erbbbxckfqab4teebivlhnpj6gs) | SOL | [Dmkj4d...xDpump](https://solscan.io/token/Dmkj4dB3Ngva9gWKkDgj8UMF39EC7ArpGf2rxLxDpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 2; Tier Micro; LP $68.4K; Vol24H $3.43M; 24H +2016.00%; V/LP 50.07x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.79M; Vol24H $3.21M; 24H -0.32%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 75; Tier Liquid; LP $2.10M; Vol24H $761.0K; 24H +6.76%; V/LP 0.36x; 池数 1; 分项 L20/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.09M; Vol24H $760.2K; 24H +0.07%; V/LP 0.70x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 72; Tier Mature; LP $12.32M; Vol24H $1.48M; 24H +4.34%; V/LP 0.12x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $79.19M; Vol24H $30.41M; 24H +2.61%; V/LP 0.38x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $152.46M; Vol24H $38.18M; 24H +4.44%; V/LP 0.25x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/eoftfbgdbxzkeqzc5dtygvnkicwevfezgtzqm9eftj6b) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $55.94M; Vol24H $18.57M; 24H +6.94%; V/LP 0.33x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ACU | BSC | [0x6ef2...8cfeaf](https://bscscan.com/token/0x6ef2ffb38d64afe18ce782da280b300e358cfeaf) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| GMEB | BSC | [0x46ce...5bb15c](https://bscscan.com/token/0x46ceefda28dd7207059ed19b0acdc026955bb15c) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [TOS](https://dexscreener.com/solana/9htnhhvtwrpirdcsybzoahtlrz4nkxxne8qdkdczx57f) | SOL | [HmjCoa...P8pump](https://solscan.io/token/HmjCoarLh5duURfJ333DwfFiPyTCgFT35pRSAoP8pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Momota | SOL | [CrJPSv...espump](https://solscan.io/token/CrJPSvj625TnPdWS42aG5ybMcHeFvnNqq5AExVespump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| XST | SOL | [XSTuo1...WTYZqP](https://solscan.io/token/XSTuo1fV7HHMhs4BYiwtrWSLsMCJNrooH2AssWTYZqP) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ACU | BSC | [0x6ef2...8cfeaf](https://bscscan.com/token/0x6ef2ffb38d64afe18ce782da280b300e358cfeaf) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 6 / Early 8 / Liquid 6 / Mature 5 | 下一步可以按层级分别设置进攻规则 |
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
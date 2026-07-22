# 自我进化轮巡

**本轮时间 UTC：** 2026-07-22T17:11:01Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 113 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 199 |
| 合并后Token | 113 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 1 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 6 |
| 多池Token | 7 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 9 |
| Early层 | 5 |
| Liquid层 | 6 |
| Mature层 | 5 |
| 需要链上确认 | 11 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 11 个，验证通过 11 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 2 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| QAIT | BSC | [0x4d41...249493](https://bscscan.com/token/0x4d41a5d412f4ef44a35b9f53b06db65ede249493) | 主观察 | Score 80; Tier Liquid; LP $1.14M; Vol24H $2.61M; 24H -22.87%; V/LP 2.30x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $921.4K; Vol24H $74.6K; 24H -1.27%; V/LP 0.08x; 池数 1; 分项 L18/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 65; Tier Early; LP $631.7K; Vol24H $10.41M; 24H +21.21%; V/LP 16.48x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 29; Tier Early; LP $117.3K; Vol24H $6.57M; 24H +11.74%; V/LP 55.98x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | PVP风险池 | Score 28; Tier Early; LP $102.1K; Vol24H $5.42M; 24H +4377.00%; V/LP 53.08x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DOYR | BSC | [0x925c...864444](https://bscscan.com/token/0x925c8ab7a9a8a148e87cd7f1ec7ecc3625864444) | PVP风险池 | Score 25; Tier Early; LP $172.2K; Vol24H $4.04M; 24H +201.23%; V/LP 23.46x; 池数 1; 分项 L11/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| she | SOL | [9sWbnw...6Hpump](https://solscan.io/token/9sWbnwdcR4vjmdKz9q56QmfAd3332kQ6qFxZka6Hpump) | PVP风险池 | Score 18; Tier Micro; LP $18.8K; Vol24H $1.39M; 24H -77.73%; V/LP 74.17x; 池数 1; 分项 L3/V15/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| psyopcat | SOL | [8JjeSH...NXpump](https://solscan.io/token/8JjeSHi4LsbAHbCvk5mDDoMbkaB9eiZHsVu67fNXpump) | PVP风险池 | Score 11; Tier Micro; LP $21.5K; Vol24H $2.02M; 24H +119.12%; V/LP 93.70x; 池数 1; 分项 L3/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Elonius](https://dexscreener.com/solana/ch5yezgs8nkvvr8vac1vbtpuwix2bboaewnmjuywvmch) | SOL | [H2QT2d...AUpump](https://solscan.io/token/H2QT2dBoyhverFCukWX4VKcHJUv2WjcrzgLGCnAUpump) | PVP风险池 | Score 10; Tier Micro; LP $23.7K; Vol24H $1.49M; 24H +182.00%; V/LP 63.04x; 池数 1; 分项 L3/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy911](https://dexscreener.com/solana/blqyupg1rwxxzrrhesvzffr2henqysxpaje1brvflqwv) | SOL | [8nZxdp...Q7pump](https://solscan.io/token/8nZxdpMFB4k73ynQ8Z1fAK1apoJsWYcShLkGfPQ7pump) | PVP风险池 | Score 1; Tier Micro; LP $58.8K; Vol24H $2.88M; 24H +1175.00%; V/LP 49.07x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| QAIT | BSC | [0x4d41...249493](https://bscscan.com/token/0x4d41a5d412f4ef44a35b9f53b06db65ede249493) | 主观察 | Score 79; Tier Liquid; LP $1.13M; Vol24H $2.21M; 24H -16.70%; V/LP 1.96x; 池数 1; 分项 L19/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $922.2K; Vol24H $71.2K; 24H -2.78%; V/LP 0.08x; 池数 1; 分项 L18/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 64; Tier Early; LP $613.0K; Vol24H $10.68M; 24H +23.19%; V/LP 17.42x; 池数 2; 分项 L16/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 38; Tier Liquid; LP $1.07M; Vol24H $22.28M; 24H +10.37%; V/LP 20.75x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 29; Tier Early; LP $121.3K; Vol24H $6.39M; 24H +13.17%; V/LP 52.73x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | PVP风险池 | Score 28; Tier Micro; LP $92.1K; Vol24H $6.19M; 24H +3430.00%; V/LP 67.21x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DOYR | BSC | [0x925c...864444](https://bscscan.com/token/0x925c8ab7a9a8a148e87cd7f1ec7ecc3625864444) | PVP风险池 | Score 25; Tier Early; LP $167.4K; Vol24H $4.07M; 24H +127.87%; V/LP 24.29x; 池数 1; 分项 L11/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| psyopcat | SOL | [8JjeSH...NXpump](https://solscan.io/token/8JjeSHi4LsbAHbCvk5mDDoMbkaB9eiZHsVu67fNXpump) | PVP风险池 | Score 11; Tier Micro; LP $22.5K; Vol24H $2.04M; 24H +140.28%; V/LP 90.61x; 池数 1; 分项 L3/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SWOLEDOGE | SOL | [Cnm8Pa...TKpump](https://solscan.io/token/Cnm8PaGvGFPT1dDqvRLYRZLwqdTN8dUTtQZT1BTKpump) | PVP风险池 | Score 11; Tier Micro; LP $30.2K; Vol24H $1.71M; 24H +376.89%; V/LP 56.65x; 池数 2; 分项 L4/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Elonius](https://dexscreener.com/solana/ch5yezgs8nkvvr8vac1vbtpuwix2bboaewnmjuywvmch) | SOL | [H2QT2d...AUpump](https://solscan.io/token/H2QT2dBoyhverFCukWX4VKcHJUv2WjcrzgLGCnAUpump) | PVP风险池 | Score 11; Tier Micro; LP $25.3K; Vol24H $1.53M; 24H +216.00%; V/LP 60.45x; 池数 1; 分项 L4/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy911](https://dexscreener.com/solana/blqyupg1rwxxzrrhesvzffr2henqysxpaje1brvflqwv) | SOL | [8nZxdp...Q7pump](https://solscan.io/token/8nZxdpMFB4k73ynQ8Z1fAK1apoJsWYcShLkGfPQ7pump) | PVP风险池 | Score 3; Tier Micro; LP $85.4K; Vol24H $5.16M; 24H +2230.00%; V/LP 60.41x; 池数 5; 分项 L9/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $12.51M; Vol24H $5.18M; 24H -0.52%; V/LP 0.41x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 78; Tier Liquid; LP $2.09M; Vol24H $6.51M; 24H -13.45%; V/LP 3.11x; 池数 2; 分项 L20/V17/B17/Buy12/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 74; Tier Mature; LP $51.38M; Vol24H $4.04M; 24H +0.14%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 71; Tier Mature; LP $16.78M; Vol24H $58.68M; 24H -0.00%; V/LP 3.50x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 38; Tier Liquid; LP $1.07M; Vol24H $22.28M; 24H +10.37%; V/LP 20.75x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 29; Tier Early; LP $121.3K; Vol24H $6.39M; 24H +13.17%; V/LP 52.73x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $92.1K; Vol24H $6.19M; 24H +3430.00%; V/LP 67.21x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| DOYR | BSC | [0x925c...864444](https://bscscan.com/token/0x925c8ab7a9a8a148e87cd7f1ec7ecc3625864444) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 25; Tier Early; LP $167.4K; Vol24H $4.07M; 24H +127.87%; V/LP 24.29x; 池数 1; 分项 L11/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| psyopcat | SOL | [8JjeSH...NXpump](https://solscan.io/token/8JjeSHi4LsbAHbCvk5mDDoMbkaB9eiZHsVu67fNXpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $22.5K; Vol24H $2.04M; 24H +140.28%; V/LP 90.61x; 池数 1; 分项 L3/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| SWOLEDOGE | SOL | [Cnm8Pa...TKpump](https://solscan.io/token/Cnm8PaGvGFPT1dDqvRLYRZLwqdTN8dUTtQZT1BTKpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $30.2K; Vol24H $1.71M; 24H +376.89%; V/LP 56.65x; 池数 2; 分项 L4/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Elonius](https://dexscreener.com/solana/ch5yezgs8nkvvr8vac1vbtpuwix2bboaewnmjuywvmch) | SOL | [H2QT2d...AUpump](https://solscan.io/token/H2QT2dBoyhverFCukWX4VKcHJUv2WjcrzgLGCnAUpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $25.3K; Vol24H $1.53M; 24H +216.00%; V/LP 60.45x; 池数 1; 分项 L4/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Jimothy911](https://dexscreener.com/solana/blqyupg1rwxxzrrhesvzffr2henqysxpaje1brvflqwv) | SOL | [8nZxdp...Q7pump](https://solscan.io/token/8nZxdpMFB4k73ynQ8Z1fAK1apoJsWYcShLkGfPQ7pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $85.4K; Vol24H $5.16M; 24H +2230.00%; V/LP 60.41x; 池数 5; 分项 L9/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $12.51M; Vol24H $5.18M; 24H -0.52%; V/LP 0.41x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $2.09M; Vol24H $6.51M; 24H -13.45%; V/LP 3.11x; 池数 2; 分项 L20/V17/B17/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $51.38M; Vol24H $4.04M; 24H +0.14%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.78M; Vol24H $58.68M; 24H -0.00%; V/LP 3.50x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| QAIT | BSC | [0x4d41...249493](https://bscscan.com/token/0x4d41a5d412f4ef44a35b9f53b06db65ede249493) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| DOYR | BSC | [0x925c...864444](https://bscscan.com/token/0x925c8ab7a9a8a148e87cd7f1ec7ecc3625864444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| psyopcat | SOL | [8JjeSH...NXpump](https://solscan.io/token/8JjeSHi4LsbAHbCvk5mDDoMbkaB9eiZHsVu67fNXpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| SWOLEDOGE | SOL | [Cnm8Pa...TKpump](https://solscan.io/token/Cnm8PaGvGFPT1dDqvRLYRZLwqdTN8dUTtQZT1BTKpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Elonius](https://dexscreener.com/solana/ch5yezgs8nkvvr8vac1vbtpuwix2bboaewnmjuywvmch) | SOL | [H2QT2d...AUpump](https://solscan.io/token/H2QT2dBoyhverFCukWX4VKcHJUv2WjcrzgLGCnAUpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| QAIT | BSC | [0x4d41...249493](https://bscscan.com/token/0x4d41a5d412f4ef44a35b9f53b06db65ede249493) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 2 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 9 / Early 5 / Liquid 6 / Mature 5 | 下一步可以按层级分别设置进攻规则 |
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
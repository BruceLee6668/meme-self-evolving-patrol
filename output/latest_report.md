# 自我进化轮巡

**本轮时间 UTC：** 2026-07-23T19:06:21Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 215 |
| 合并后Token | 106 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 9 |
| 多池Token | 6 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 9 |
| Liquid层 | 9 |
| Mature层 | 2 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 68; Tier Liquid; LP $1.92M; Vol24H $88.9K; 24H -9.18%; V/LP 0.05x; 池数 1; 分项 L20/V7/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 56; Tier Liquid; LP $1.36M; Vol24H $43.25M; 24H -2.81%; V/LP 31.83x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 53; Tier Early; LP $718.4K; Vol24H $21.72M; 24H +23.72%; V/LP 30.23x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| B2 | BSC | [0x783c...6ee2a2](https://bscscan.com/token/0x783c3f003f172c6ac5ac700218a357d2d66ee2a2) | PVP风险池 | Score 39; Tier Early; LP $636.6K; Vol24H $14.98M; 24H -27.15%; V/LP 23.53x; 池数 1; 分项 L17/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BOP | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | PVP风险池 | Score 30; Tier Early; LP $157.7K; Vol24H $8.08M; 24H +132.73%; V/LP 51.23x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 28; Tier Liquid; LP $906.9K; Vol24H $33.49M; 24H +34.88%; V/LP 36.92x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | PVP风险池 | Score 23; Tier Micro; LP $95.7K; Vol24H $7.50M; 24H +183.00%; V/LP 78.39x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 7; Tier Micro; LP $79.6K; Vol24H $136.24M; 24H -99.98%; V/LP 1711.83x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | PVP风险池 | Score 0; Tier Micro; LP $17.8K; Vol24H $82.13M; 24H -99.98%; V/LP 4618.73x; 池数 1; 分项 L2/V17/B0/Buy3/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 成熟池观察 | Score 74; Tier Liquid; LP $2.72M; Vol24H $7.27M; 24H -3.16%; V/LP 2.67x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [NORMIE](https://dexscreener.com/solana/8n544cg9j44dkzu4cjswhxpwekxhqptr4r17kw9y5fbk) | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | 次观察 | Score 73; Tier Early; LP $302.1K; Vol24H $1.36M; 24H +41.76%; V/LP 4.52x; 池数 1; 分项 L14/V15/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 68; Tier Liquid; LP $1.87M; Vol24H $93.3K; 24H -10.73%; V/LP 0.05x; 池数 1; 分项 L20/V7/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | PVP风险池 | Score 56; Tier Liquid; LP $1.36M; Vol24H $43.47M; 24H -2.11%; V/LP 31.91x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 53; Tier Early; LP $673.4K; Vol24H $23.29M; 24H -20.00%; V/LP 34.59x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | PVP风险池 | Score 46; Tier Early; LP $117.5K; Vol24H $8.15M; 24H -22.58%; V/LP 69.39x; 池数 2; 分项 L10/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | PVP风险池 | Score 35; Tier Early; LP $288.2K; Vol24H $6.28M; 24H +49.75%; V/LP 21.78x; 池数 2; 分项 L13/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 28; Tier Liquid; LP $898.5K; Vol24H $47.97M; 24H +34.09%; V/LP 53.39x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | PVP风险池 | Score 23; Tier Micro; LP $98.1K; Vol24H $7.51M; 24H +183.00%; V/LP 76.59x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 7; Tier Micro; LP $77.6K; Vol24H $119.57M; 24H -99.98%; V/LP 1540.35x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | PVP风险池 | Score 0; Tier Micro; LP $17.7K; Vol24H $68.71M; 24H -99.98%; V/LP 3878.85x; 池数 1; 分项 L2/V17/B0/Buy3/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 成熟池观察 | Score 74; Tier Liquid; LP $2.72M; Vol24H $7.85M; 24H -2.80%; V/LP 2.88x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 74; Tier Liquid; LP $1.44M; Vol24H $6.73M; 24H -1.72%; V/LP 4.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 成熟池观察 | Score 73; Tier Mature; LP $19.92M; Vol24H $112.5K; 24H -1.75%; V/LP 0.01x; 池数 1; 分项 L20/V7/B22/Buy12/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 73; Tier Liquid; LP $1.86M; Vol24H $2.13M; 24H -8.08%; V/LP 1.14x; 池数 2; 分项 L20/V16/B17/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 成熟池观察 | Score 71; Tier Mature; LP $16.64M; Vol24H $58.69M; 24H -0.01%; V/LP 3.53x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Liquid; LP $1.36M; Vol24H $43.47M; 24H -2.11%; V/LP 31.91x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 53; Tier Early; LP $673.4K; Vol24H $23.29M; 24H -20.00%; V/LP 34.59x; 池数 2; 分项 L17/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 46; Tier Early; LP $117.5K; Vol24H $8.15M; 24H -22.58%; V/LP 69.39x; 池数 2; 分项 L10/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Early; LP $288.2K; Vol24H $6.28M; 24H +49.75%; V/LP 21.78x; 池数 2; 分项 L13/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 28; Tier Liquid; LP $898.5K; Vol24H $47.97M; 24H +34.09%; V/LP 53.39x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 23; Tier Micro; LP $98.1K; Vol24H $7.51M; 24H +183.00%; V/LP 76.59x; 池数 1; 分项 L9/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 7; Tier Micro; LP $77.6K; Vol24H $119.57M; 24H -99.98%; V/LP 1540.35x; 池数 1; 分项 L8/V17/B0/Buy3/Risk-45 | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 0; Tier Micro; LP $17.7K; Vol24H $68.71M; 24H -99.98%; V/LP 3878.85x; 池数 1; 分项 L2/V17/B0/Buy3/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $2.72M; Vol24H $7.85M; 24H -2.80%; V/LP 2.88x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.44M; Vol24H $6.73M; 24H -1.72%; V/LP 4.68x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $19.92M; Vol24H $112.5K; 24H -1.75%; V/LP 0.01x; 池数 1; 分项 L20/V7/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.86M; Vol24H $2.13M; 24H -8.08%; V/LP 1.14x; 池数 2; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.64M; Vol24H $58.69M; 24H -0.01%; V/LP 3.53x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [NORMIE](https://dexscreener.com/solana/8n544cg9j44dkzu4cjswhxpwekxhqptr4r17kw9y5fbk) | SOL | [4MrsXQ...j9pump](https://solscan.io/token/4MrsXQzaosYNyFd4wKDvgnC5xRtRqgXRrijFTGj9pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/3wsaser1eupbegmp6vptcmwg38xsvmjuwa2oqhbt3vyb) | SOL | [99kDGD...nhCSAZ](https://solscan.io/token/99kDGDi5Q655ctCAsxfyGSnws8qUwx3KPHF3t5nhCSAZ) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| QQQB | BSC | [0x2058...11efc7](https://bscscan.com/token/0x205812cdbed920aff76c6580abd681a46d11efc7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [BlackBear](https://dexscreener.com/solana/bwitoefdarynw3cx8w8fmz5g26hbikhjfueifgrxybws) | SOL | [8X1N2H...GYpump](https://solscan.io/token/8X1N2HmiP11UXidmyRNHLoBGjAhXU4rk5GnrVYGYpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [BOP](https://dexscreener.com/solana/5h23rfazdacpmodbu35ozq3qyxrcvvxscjfb9hsnckfy) | SOL | [B62soc...w6pump](https://solscan.io/token/B62socheoeJVqiKnihcR96g61tzALYwcMsE91Sw6pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| KET | SOL | [9Pfync...Lxpump](https://solscan.io/token/9Pfync3ejPC9eHqVzq3nYQJAhyhjqpnB9UsaSfLxpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [CAGE](https://dexscreener.com/solana/4fgumkjhc8s7zyeslrppi8xbsstmbyj9kjbelz1wvoup) | SOL | [gF2fSf...V7pump](https://solscan.io/token/gF2fSfar4x1BiZ9n2MLMAVYVWQYzxpsrXC6hGV7pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| - | - | - | 本轮无钱包行为样本 | - | 0 | - |

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
| 主观察候选 | 0 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 9 / Liquid 9 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
| dexscreener_search | {'ok': True, 'count': 337} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
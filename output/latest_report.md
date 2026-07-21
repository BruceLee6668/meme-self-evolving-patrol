# 自我进化轮巡

**本轮时间 UTC：** 2026-07-21T21:01:38Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 110 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 195 |
| 合并后Token | 110 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 7 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 7 |
| Liquid层 | 7 |
| Mature层 | 4 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 732，刷新时间 2026-07-20T02:12:03Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $939.2K; Vol24H $124.1K; 24H +8.72%; V/LP 0.13x; 池数 1; 分项 L18/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BULLCAT](https://dexscreener.com/solana/huqmpubbdq8w56y6wgd8limbf4zgyxs2aczlzs8mylna) | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 次观察 | Score 70; Tier Micro; LP $96.5K; Vol24H $640.6K; 24H -12.23%; V/LP 6.64x; 池数 1; 分项 L9/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 次观察 | Score 66; Tier Liquid; LP $890.1K; Vol24H $12.48M; 24H -7.67%; V/LP 14.03x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 52; Tier Early; LP $496.3K; Vol24H $10.67M; 24H +11.70%; V/LP 21.50x; 池数 2; 分项 L16/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HEMI | BSC | [0x5ffd...5afc5b](https://bscscan.com/token/0x5ffd0eadc186af9512542d0d5e5eafc65d5afc5b) | PVP风险池 | Score 50; Tier Early; LP $296.3K; Vol24H $6.26M; 24H -7.33%; V/LP 21.13x; 池数 1; 分项 L14/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 29; Tier Micro; LP $78.7K; Vol24H $95.17M; 24H -2.51%; V/LP 1208.49x; 池数 1; 分项 L8/V17/B22/Buy3/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GMEBULL | SOL | [4tnZ57...TYpump](https://solscan.io/token/4tnZ57E3oWjaZKSQY1iwgqiD8ivAGk5TambivhTYpump) | PVP风险池 | Score 29; Tier Early; LP $113.0K; Vol24H $3.63M; 24H +3182.65%; V/LP 32.12x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $114.3K; Vol24H $6.97M; 24H -39.53%; V/LP 60.95x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Jimhood | SOL | [6wCpTa...wkpump](https://solscan.io/token/6wCpTaxLmCeBdsazRebYNHtFNC1mPJDWKscHHVwkpump) | PVP风险池 | Score 17; Tier Micro; LP $11.0K; Vol24H $13.31M; 24H -71.09%; V/LP 1204.39x; 池数 1; 分项 L0/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEXE | BSC | [0x6e88...15ce3e](https://bscscan.com/token/0x6e88056e8376ae7709496ba64d37fa2f8015ce3e) | PVP风险池 | Score 17; Tier Micro; LP $57.2K; Vol24H $7.32M; 24H -63.62%; V/LP 127.98x; 池数 1; 分项 L7/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 79; Tier Liquid; LP $934.4K; Vol24H $125.6K; 24H +9.96%; V/LP 0.13x; 池数 1; 分项 L18/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [BULLCAT](https://dexscreener.com/solana/huqmpubbdq8w56y6wgd8limbf4zgyxs2aczlzs8mylna) | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 次观察 | Score 75; Tier Micro; LP $94.1K; Vol24H $556.2K; 24H -1.54%; V/LP 5.91x; 池数 1; 分项 L9/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 74; Tier Early; LP $157.2K; Vol24H $1.07M; 24H +5.61%; V/LP 6.84x; 池数 2; 分项 L11/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 69; Tier Early; LP $523.7K; Vol24H $9.24M; 24H +1.81%; V/LP 17.65x; 池数 2; 分项 L16/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USOH](https://dexscreener.com/solana/8vjnscdcyeeskbbg4tunf3y4lhbg5cmeub8nzm3a6gzm) | SOL | [SrxbiY...Ctpump](https://solscan.io/token/SrxbiYw29qnTH9dwg3LyNVg9UMHwsfjC9U9dkCtpump) | PVP风险池 | Score 43; Tier Early; LP $543.7K; Vol24H $2.14M; 24H +164971.00%; V/LP 3.93x; 池数 2; 分项 L16/V16/B0/Buy12/Risk-25 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GMEBULL | SOL | [4tnZ57...TYpump](https://solscan.io/token/4tnZ57E3oWjaZKSQY1iwgqiD8ivAGk5TambivhTYpump) | PVP风险池 | Score 28; Tier Early; LP $101.9K; Vol24H $3.86M; 24H +2626.91%; V/LP 37.82x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $114.9K; Vol24H $7.00M; 24H -38.11%; V/LP 60.87x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | PVP风险池 | Score 19; Tier Mature; LP $90.72M; Vol24H $5440.33M; 24H +485336.00%; V/LP 59.97x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DEXE | BSC | [0x6e88...15ce3e](https://bscscan.com/token/0x6e88056e8376ae7709496ba64d37fa2f8015ce3e) | PVP风险池 | Score 17; Tier Micro; LP $56.9K; Vol24H $7.28M; 24H -64.24%; V/LP 127.88x; 池数 1; 分项 L7/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [she ](https://dexscreener.com/solana/aksihdkvtg4jbyyv8v7gewypiau6c7ms9krndcfjbs76) | SOL | [9sWbnw...6Hpump](https://solscan.io/token/9sWbnwdcR4vjmdKz9q56QmfAd3332kQ6qFxZka6Hpump) | PVP风险池 | Score 13; Tier Micro; LP $32.8K; Vol24H $2.31M; 24H +386.00%; V/LP 70.50x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MELON](https://dexscreener.com/solana/g6gfzvpespq6w3vqj3cnjqguntmhxwvaztqpg9v5jjya) | SOL | [9AwZKi...Tnpump](https://solscan.io/token/9AwZKiUicugQ7hNdoKJEmV1psybm7yQMMsBb4hTnpump) | PVP风险池 | Score 13; Tier Micro; LP $35.9K; Vol24H $2.26M; 24H +420.00%; V/LP 62.97x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Jimhood | SOL | [6wCpTa...wkpump](https://solscan.io/token/6wCpTaxLmCeBdsazRebYNHtFNC1mPJDWKscHHVwkpump) | PVP风险池 | Score 9; Tier Micro; LP $10.7K; Vol24H $13.02M; 24H -97.41%; V/LP 1213.45x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $51.10M; Vol24H $3.75M; 24H -1.61%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 77; Tier Liquid; LP $2.15M; Vol24H $1.69M; 24H -0.48%; V/LP 0.78x; 池数 2; 分项 L20/V15/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 成熟池观察 | Score 74; Tier Liquid; LP $1.21M; Vol24H $872.9K; 24H +1.08%; V/LP 0.72x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [USOH](https://dexscreener.com/solana/8vjnscdcyeeskbbg4tunf3y4lhbg5cmeub8nzm3a6gzm) | SOL | [SrxbiY...Ctpump](https://solscan.io/token/SrxbiYw29qnTH9dwg3LyNVg9UMHwsfjC9U9dkCtpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；24H涨跌幅过热；年轻币短期暴拉 | Score 43; Tier Early; LP $543.7K; Vol24H $2.14M; 24H +164971.00%; V/LP 3.93x; 池数 2; 分项 L16/V16/B0/Buy12/Risk-25 | 只记录热度，不进入主榜 |
| GMEBULL | SOL | [4tnZ57...TYpump](https://solscan.io/token/4tnZ57E3oWjaZKSQY1iwgqiD8ivAGk5TambivhTYpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Early; LP $101.9K; Vol24H $3.86M; 24H +2626.91%; V/LP 37.82x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 20; Tier Early; LP $114.9K; Vol24H $7.00M; 24H -38.11%; V/LP 60.87x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 19; Tier Mature; LP $90.72M; Vol24H $5440.33M; 24H +485336.00%; V/LP 59.97x; 池数 1; 分项 L20/V17/B0/Buy3/Risk-45 | 只记录热度，不进入主榜 |
| DEXE | BSC | [0x6e88...15ce3e](https://bscscan.com/token/0x6e88056e8376ae7709496ba64d37fa2f8015ce3e) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 17; Tier Micro; LP $56.9K; Vol24H $7.28M; 24H -64.24%; V/LP 127.88x; 池数 1; 分项 L7/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [she ](https://dexscreener.com/solana/aksihdkvtg4jbyyv8v7gewypiau6c7ms9krndcfjbs76) | SOL | [9sWbnw...6Hpump](https://solscan.io/token/9sWbnwdcR4vjmdKz9q56QmfAd3332kQ6qFxZka6Hpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $32.8K; Vol24H $2.31M; 24H +386.00%; V/LP 70.50x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [MELON](https://dexscreener.com/solana/g6gfzvpespq6w3vqj3cnjqguntmhxwvaztqpg9v5jjya) | SOL | [9AwZKi...Tnpump](https://solscan.io/token/9AwZKiUicugQ7hNdoKJEmV1psybm7yQMMsBb4hTnpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $35.9K; Vol24H $2.26M; 24H +420.00%; V/LP 62.97x; 池数 1; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Jimhood | SOL | [6wCpTa...wkpump](https://solscan.io/token/6wCpTaxLmCeBdsazRebYNHtFNC1mPJDWKscHHVwkpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $10.7K; Vol24H $13.02M; 24H -97.41%; V/LP 1213.45x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.10M; Vol24H $3.75M; 24H -1.61%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 77; Tier Liquid; LP $2.15M; Vol24H $1.69M; 24H -0.48%; V/LP 0.78x; 池数 2; 分项 L20/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.21M; Vol24H $872.9K; 24H +1.08%; V/LP 0.72x; 池数 2; 分项 L19/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.37M; Vol24H $9.30M; 24H -4.52%; V/LP 6.78x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $17.07M; Vol24H $52.98M; 24H +0.07%; V/LP 3.10x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；成熟大池 | Score 58; Tier Mature; LP $20.49M; Vol24H $9.8K; 24H +0.04%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [BULLCAT](https://dexscreener.com/solana/huqmpubbdq8w56y6wgd8limbf4zgyxs2aczlzs8mylna) | SOL | [G9j8WW...1Lpump](https://solscan.io/token/G9j8WWDeJXZdvwQgP82ooDuHmpc3Gy8NCSins71Lpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 人生逆袭 | BSC | [0x7b8b...997777](https://bscscan.com/token/0x7b8b0a2f11de504273d22e4433647c686c997777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [USOH](https://dexscreener.com/solana/8vjnscdcyeeskbbg4tunf3y4lhbg5cmeub8nzm3a6gzm) | SOL | [SrxbiY...Ctpump](https://solscan.io/token/SrxbiYw29qnTH9dwg3LyNVg9UMHwsfjC9U9dkCtpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| GMEBULL | SOL | [4tnZ57...TYpump](https://solscan.io/token/4tnZ57E3oWjaZKSQY1iwgqiD8ivAGk5TambivhTYpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Bonk](https://dexscreener.com/solana/2hxctgnfeqfnsxv8d7ztybebeaowmwwvedqq8v3obyas) | SOL | [DezXAZ...pPB263](https://solscan.io/token/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| DEXE | BSC | [0x6e88...15ce3e](https://bscscan.com/token/0x6e88056e8376ae7709496ba64d37fa2f8015ce3e) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
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
| 主观察候选 | 1 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 7 / Liquid 7 / Mature 4 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 335} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
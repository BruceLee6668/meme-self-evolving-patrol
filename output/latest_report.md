# 自我进化轮巡

**本轮时间 UTC：** 2026-08-02T19:08:31Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 139 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 248 |
| 合并后Token | 139 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 3 |
| 低优先观察 | 9 |
| 多池Token | 8 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 8 |
| Liquid层 | 6 |
| Mature层 | 3 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 782，刷新时间 2026-07-27T02:07:24Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 83; Tier Early; LP $446.7K; Vol24H $1.23M; 24H -6.94%; V/LP 2.75x; 池数 1; 分项 L15/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 次观察 | Score 72; Tier Liquid; LP $2.27M; Vol24H $8.14M; 24H +43.56%; V/LP 3.58x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.46M; Vol24H $1.4K; 24H -0.39%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 65; Tier Liquid; LP $1.79M; Vol24H $43.2K; 24H -0.33%; V/LP 0.02x; 池数 1; 分项 L20/V4/B22/Buy3/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PIZZA | BSC | [0x8554...b07777](https://bscscan.com/token/0x8554d38b95e4f7ca11d391008627df30b2b07777) | PVP风险池 | Score 29; Tier Early; LP $126.3K; Vol24H $8.40M; 24H +3807.31%; V/LP 66.52x; 池数 1; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [memes](https://dexscreener.com/bsc/0xd3c8668bff07b02d78019afe7f9a6e581499def2) | BSC | [0xF745...EE4444](https://bscscan.com/token/0xF74548802f4c700315F019FdE17178b392EE4444) | PVP风险池 | Score 28; Tier Micro; LP $90.0K; Vol24H $7.58M; 24H +51.26%; V/LP 84.29x; 池数 11; 分项 L9/V17/B8/Buy3/Risk-33 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Slop | SOL | [EVY4xJ...dApump](https://solscan.io/token/EVY4xJ3ytMHa77sjgs2uVj7fgXj1ha98QSQxPadApump) | PVP风险池 | Score 25; Tier Micro; LP $62.5K; Vol24H $2.50M; 24H +20315.09%; V/LP 40.05x; 池数 1; 分项 L7/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| JORDAN | SOL | [8TLxeY...jppump](https://solscan.io/token/8TLxeYnnWpMFiC9npbh7XzyHpLtTYmw6DCuHBJjppump) | PVP风险池 | Score 23; Tier Micro; LP $92.2K; Vol24H $5.56M; 24H +3847.18%; V/LP 60.27x; 池数 2; 分项 L9/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [STOCKERS](https://dexscreener.com/solana/4zcviz4pe9hy6vlg3fdq2gpug59gkpejkpe69nuc7b3f) | SOL | [CeyZtF...Qppump](https://solscan.io/token/CeyZtFUiYP5oxCZ99urwHMvdCW67cY2yALknfrQppump) | PVP风险池 | Score 16; Tier Micro; LP $41.1K; Vol24H $1.37M; 24H -78.23%; V/LP 33.22x; 池数 1; 分项 L6/V15/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [catcall ](https://dexscreener.com/solana/4fvntrl5rbyvw4ku4p6mg73uwpfmalu6gq2nppfqvitv) | SOL | [FEJdyN...Vdpump](https://solscan.io/token/FEJdyNUQeroXwQNqTZGQbjfjdXcVgeeXDCKpAtVdpump) | PVP风险池 | Score 11; Tier Micro; LP $24.8K; Vol24H $1.72M; 24H +243.00%; V/LP 69.38x; 池数 2; 分项 L4/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 主观察 | Score 83; Tier Early; LP $444.3K; Vol24H $1.10M; 24H -6.60%; V/LP 2.48x; 池数 1; 分项 L15/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 主观察 | Score 81; Tier Liquid; LP $2.03M; Vol24H $9.20M; 24H +17.64%; V/LP 4.54x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.46M; Vol24H $1.4K; 24H -0.39%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 65; Tier Liquid; LP $1.80M; Vol24H $43.4K; 24H +0.41%; V/LP 0.02x; 池数 1; 分项 L20/V4/B22/Buy3/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 次观察 | Score 65; Tier Early; LP $672.3K; Vol24H $6.95M; 24H -5.90%; V/LP 10.34x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| memes | BSC | [0xf745...ee4444](https://bscscan.com/token/0xf74548802f4c700315f019fde17178b392ee4444) | PVP风险池 | Score 40; Tier Micro; LP $87.4K; Vol24H $7.06M; 24H +8.64%; V/LP 80.78x; 池数 9; 分项 L9/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PIZZA | BSC | [0x8554...b07777](https://bscscan.com/token/0x8554d38b95e4f7ca11d391008627df30b2b07777) | PVP风险池 | Score 30; Tier Early; LP $141.2K; Vol24H $8.51M; 24H +4518.57%; V/LP 60.29x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [JORDAN](https://dexscreener.com/solana/5xstd6cxw2bwgu3wfvcmgzrhrssbbtqhxgn7iq5gwugs) | SOL | [8TLxeY...jppump](https://solscan.io/token/8TLxeYnnWpMFiC9npbh7XzyHpLtTYmw6DCuHBJjppump) | PVP风险池 | Score 28; Tier Micro; LP $88.1K; Vol24H $5.79M; 24H +3409.00%; V/LP 65.67x; 池数 3; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Kimchi](https://dexscreener.com/solana/6f1hd3hodh3a8zhsl4dda5yb6tjgypidwizvhjjrbn5m) | SOL | [Am8iBf...Qfpump](https://solscan.io/token/Am8iBffqgaedfdK5XhtorbcRrKzwH9nyL3ySikQfpump) | PVP风险池 | Score 27; Tier Early; LP $106.1K; Vol24H $2.26M; 24H +421.00%; V/LP 21.33x; 池数 1; 分项 L9/V16/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Slop](https://dexscreener.com/solana/9cudqjhdk5tpatkrdyyuarnlfwttwapt3exszmeqxsjd) | SOL | [EVY4xJ...dApump](https://solscan.io/token/EVY4xJ3ytMHa77sjgs2uVj7fgXj1ha98QSQxPadApump) | PVP风险池 | Score 26; Tier Micro; LP $62.3K; Vol24H $2.87M; 24H +19463.00%; V/LP 45.98x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [3place](https://dexscreener.com/solana/fyuo73hxjif3w8qeagbkxump1rcarhh3j81cjcrqmpv3) | SOL | [7K4jGR...2Upump](https://solscan.io/token/7K4jGRV7PY1EymiY3jx75JSfi1jjzG7Gh5XHqF2Upump) | PVP风险池 | Score 12; Tier Micro; LP $40.0K; Vol24H $1.27M; 24H +331.00%; V/LP 31.83x; 池数 7; 分项 L6/V14/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [catcall ](https://dexscreener.com/solana/4fvntrl5rbyvw4ku4p6mg73uwpfmalu6gq2nppfqvitv) | SOL | [FEJdyN...Vdpump](https://solscan.io/token/FEJdyNUQeroXwQNqTZGQbjfjdXcVgeeXDCKpAtVdpump) | PVP风险池 | Score 10; Tier Micro; LP $23.0K; Vol24H $1.74M; 24H +194.00%; V/LP 75.72x; 池数 1; 分项 L3/V15/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TURTLEBOSS](https://dexscreener.com/solana/7ei3dnzgmrywhzgmeyj42dj3i2pw87rz5zh3uk4rctjs) | SOL | [FkLqaR...BJpump](https://solscan.io/token/FkLqaRrAn7VkMaMHSM5hQMRCezu1jeDapQ9nFtBJpump) | PVP风险池 | Score 0; Tier Micro; LP $29.1K; Vol24H $1.19M; 24H +330.00%; V/LP 41.00x; 池数 6; 分项 L4/V14/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 78; Tier Liquid; LP $2.12M; Vol24H $1.84M; 24H +4.42%; V/LP 0.87x; 池数 3; 分项 L20/V16/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $13.20M; Vol24H $19.34M; 24H +1.08%; V/LP 1.46x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| memes | BSC | [0xf745...ee4444](https://bscscan.com/token/0xf74548802f4c700315f019fde17178b392ee4444) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Micro; LP $87.4K; Vol24H $7.06M; 24H +8.64%; V/LP 80.78x; 池数 9; 分项 L9/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| PIZZA | BSC | [0x8554...b07777](https://bscscan.com/token/0x8554d38b95e4f7ca11d391008627df30b2b07777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $141.2K; Vol24H $8.51M; 24H +4518.57%; V/LP 60.29x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [JORDAN](https://dexscreener.com/solana/5xstd6cxw2bwgu3wfvcmgzrhrssbbtqhxgn7iq5gwugs) | SOL | [8TLxeY...jppump](https://solscan.io/token/8TLxeYnnWpMFiC9npbh7XzyHpLtTYmw6DCuHBJjppump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $88.1K; Vol24H $5.79M; 24H +3409.00%; V/LP 65.67x; 池数 3; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Kimchi](https://dexscreener.com/solana/6f1hd3hodh3a8zhsl4dda5yb6tjgypidwizvhjjrbn5m) | SOL | [Am8iBf...Qfpump](https://solscan.io/token/Am8iBffqgaedfdK5XhtorbcRrKzwH9nyL3ySikQfpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $106.1K; Vol24H $2.26M; 24H +421.00%; V/LP 21.33x; 池数 1; 分项 L9/V16/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Slop](https://dexscreener.com/solana/9cudqjhdk5tpatkrdyyuarnlfwttwapt3exszmeqxsjd) | SOL | [EVY4xJ...dApump](https://solscan.io/token/EVY4xJ3ytMHa77sjgs2uVj7fgXj1ha98QSQxPadApump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $62.3K; Vol24H $2.87M; 24H +19463.00%; V/LP 45.98x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [3place](https://dexscreener.com/solana/fyuo73hxjif3w8qeagbkxump1rcarhh3j81cjcrqmpv3) | SOL | [7K4jGR...2Upump](https://solscan.io/token/7K4jGRV7PY1EymiY3jx75JSfi1jjzG7Gh5XHqF2Upump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $40.0K; Vol24H $1.27M; 24H +331.00%; V/LP 31.83x; 池数 7; 分项 L6/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [catcall ](https://dexscreener.com/solana/4fvntrl5rbyvw4ku4p6mg73uwpfmalu6gq2nppfqvitv) | SOL | [FEJdyN...Vdpump](https://solscan.io/token/FEJdyNUQeroXwQNqTZGQbjfjdXcVgeeXDCKpAtVdpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $23.0K; Vol24H $1.74M; 24H +194.00%; V/LP 75.72x; 池数 1; 分项 L3/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [TURTLEBOSS](https://dexscreener.com/solana/7ei3dnzgmrywhzgmeyj42dj3i2pw87rz5zh3uk4rctjs) | SOL | [FkLqaR...BJpump](https://solscan.io/token/FkLqaRrAn7VkMaMHSM5hQMRCezu1jeDapQ9nFtBJpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $29.1K; Vol24H $1.19M; 24H +330.00%; V/LP 41.00x; 池数 6; 分项 L4/V14/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $2.12M; Vol24H $1.84M; 24H +4.42%; V/LP 0.87x; 池数 3; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $13.20M; Vol24H $19.34M; 24H +1.08%; V/LP 1.46x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 67; Tier Mature; LP $10.84M; Vol24H $1.81M; 24H +10.29%; V/LP 0.17x; 池数 5; 分项 L20/V15/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| GRVT | BSC | [0x46f2...f91be7](https://bscscan.com/token/0x46f2564e0fa8248d15125e7e54173cfbdef91be7) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| memes | BSC | [0xf745...ee4444](https://bscscan.com/token/0xf74548802f4c700315f019fde17178b392ee4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| PIZZA | BSC | [0x8554...b07777](https://bscscan.com/token/0x8554d38b95e4f7ca11d391008627df30b2b07777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [JORDAN](https://dexscreener.com/solana/5xstd6cxw2bwgu3wfvcmgzrhrssbbtqhxgn7iq5gwugs) | SOL | [8TLxeY...jppump](https://solscan.io/token/8TLxeYnnWpMFiC9npbh7XzyHpLtTYmw6DCuHBJjppump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [Kimchi](https://dexscreener.com/solana/6f1hd3hodh3a8zhsl4dda5yb6tjgypidwizvhjjrbn5m) | SOL | [Am8iBf...Qfpump](https://solscan.io/token/Am8iBffqgaedfdK5XhtorbcRrKzwH9nyL3ySikQfpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Slop](https://dexscreener.com/solana/9cudqjhdk5tpatkrdyyuarnlfwttwapt3exszmeqxsjd) | SOL | [EVY4xJ...dApump](https://solscan.io/token/EVY4xJ3ytMHa77sjgs2uVj7fgXj1ha98QSQxPadApump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| KOMA | BSC | [0xd5ea...7f3c19](https://bscscan.com/token/0xd5eaaac47bd1993d661bc087e15dfb079a7f3c19) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 3 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 8 / Liquid 6 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
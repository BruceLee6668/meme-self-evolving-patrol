# 自我进化轮巡

**本轮时间 UTC：** 2026-08-25T12:36:18Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 133 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 239 |
| 合并后Token | 133 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 6 |
| 多池Token | 8 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 9 |
| Liquid层 | 6 |
| Mature层 | 3 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1089，刷新时间 2026-08-24T00:46:57Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $1.27M; Vol24H $304.4K; 24H -13.27%; V/LP 0.24x; 池数 1; 分项 L19/V10/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 75; Tier Early; LP $376.8K; Vol24H $601.3K; 24H +15.19%; V/LP 1.60x; 池数 5; 分项 L14/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 次观察 | Score 74; Tier Early; LP $351.8K; Vol24H $2.27M; 24H -8.34%; V/LP 6.45x; 池数 1; 分项 L14/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GrokBot](https://dexscreener.com/solana/dsx8gy83k3bb7bsgcobrpvnpwyw7kkvrdmktx6tmnrqs) | SOL | [GeSfrQ...vSpump](https://solscan.io/token/GeSfrQiscfsEv4Hx2TKaB9Nfid12qND1YYRYS1vSpump) | 次观察 | Score 68; Tier Early; LP $187.5K; Vol24H $2.43M; 24H -7.81%; V/LP 12.94x; 池数 1; 分项 L12/V16/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| UPS | BSC | [0xae5a...afba01](https://bscscan.com/token/0xae5a409773b9a7dd0ae94ff437ac213d8fafba01) | 次观察 | Score 68; Tier Early; LP $109.9K; Vol24H $58.6K; 24H -16.41%; V/LP 0.53x; 池数 1; 分项 L10/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 56; Tier Early; LP $472.7K; Vol24H $10.41M; 24H -5.28%; V/LP 22.02x; 池数 6; 分项 L15/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 42; Tier Early; LP $153.7K; Vol24H $5.07M; 24H -10.64%; V/LP 32.97x; 池数 2; 分项 L11/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CVXV666](https://dexscreener.com/solana/hcqesmkzs1d1kgh1ymkwsekd7yp22g1wmgkxgtmkzq2q) | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | PVP风险池 | Score 31; Tier Early; LP $105.0K; Vol24H $4.03M; 24H -36.74%; V/LP 38.33x; 池数 2; 分项 L9/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BATON | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | PVP风险池 | Score 28; Tier Micro; LP $87.3K; Vol24H $12.16M; 24H +1903.95%; V/LP 139.32x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [csvoss](https://dexscreener.com/solana/btyhuwj6vyz5qvrznz4qgvkvbacauhnvyxjedml3jqyp) | SOL | [HBDkJT...1gpump](https://solscan.io/token/HBDkJT9kMc12usUrcZDpWyfr7kvTTEfvbeyofL1gpump) | PVP风险池 | Score 19; Tier Micro; LP $39.8K; Vol24H $3.46M; 24H +195.00%; V/LP 87.05x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 主观察 | Score 79; Tier Early; LP $351.2K; Vol24H $2.18M; 24H -4.37%; V/LP 6.20x; 池数 1; 分项 L14/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 75; Tier Liquid; LP $952.8K; Vol24H $4.84M; 24H +70.74%; V/LP 5.08x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WUKONG](https://dexscreener.com/bsc/0x424e1dc83e7364c4574150dab6ac122f57cf18f5) | BSC | [0xc5Fe...1c7777](https://bscscan.com/token/0xc5Feb05e1FF77a934c2B67828BC234dAf81c7777) | 次观察 | Score 74; Tier Liquid; LP $3.39M; Vol24H $7.77M; 24H +75.30%; V/LP 2.29x; 池数 3; 分项 L20/V17/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/hxfrsd7uc3lgdbcbgpyptqlbsk2syubfqicxvumcj5uw) | SOL | [ZrZy8Q...VFpump](https://solscan.io/token/ZrZy8Q1uXG2PSPn7X4NaMQMRa11paZ2xReKNsVFpump) | 次观察 | Score 70; Tier Early; LP $199.2K; Vol24H $175.5K; 24H +23.23%; V/LP 0.88x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| UPS | BSC | [0xae5a...afba01](https://bscscan.com/token/0xae5a409773b9a7dd0ae94ff437ac213d8fafba01) | 次观察 | Score 68; Tier Early; LP $110.1K; Vol24H $56.1K; 24H -19.97%; V/LP 0.51x; 池数 1; 分项 L10/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 56; Tier Early; LP $479.1K; Vol24H $10.24M; 24H -6.04%; V/LP 21.37x; 池数 5; 分项 L15/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 42; Tier Early; LP $157.1K; Vol24H $4.86M; 24H +11.92%; V/LP 30.95x; 池数 2; 分项 L11/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CVXV666 | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | PVP风险池 | Score 41; Tier Early; LP $114.3K; Vol24H $3.84M; 24H -20.52%; V/LP 33.62x; 池数 2; 分项 L10/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BATON | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | PVP风险池 | Score 28; Tier Micro; LP $96.2K; Vol24H $12.68M; 24H +2275.16%; V/LP 131.71x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | PVP风险池 | Score 27; Tier Micro; LP $81.4K; Vol24H $2.56M; 24H +604.00%; V/LP 31.45x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [kylie](https://dexscreener.com/solana/3kbndtpzhw76zogfj4x3mpyu9wp1fqbynyx743dxjtno) | SOL | [6b7KQs...2rpump](https://solscan.io/token/6b7KQsXqb6JR5Nmeer5zGRmo51dwDfttM5b5Nu2rpump) | PVP风险池 | Score 15; Tier Micro; LP $43.0K; Vol24H $6.52M; 24H +349.00%; V/LP 151.60x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 100CATS | SOL | [GUt3eb...P1pump](https://solscan.io/token/GUt3ebbJm6SJCvpa8SfFzZe132a78qZDyc2yXAP1pump) | PVP风险池 | Score 13; Tier Micro; LP $3.0K; Vol24H $2.84M; 24H -99.00%; V/LP 945.13x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MARTIN](https://dexscreener.com/solana/anyskudzswmsw3n4knbm9rtqpcxbubzmbyzxkzuphxww) | SOL | [GHU8yQ...XSpump](https://solscan.io/token/GHU8yQL74VCmVXMpPrx9mY8UWzdbD6RPf6BHeyXSpump) | PVP风险池 | Score 10; Tier Micro; LP $40.5K; Vol24H $8.70M; 24H +230.00%; V/LP 214.88x; 池数 1; 分项 L6/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 79; Tier Liquid; LP $2.77M; Vol24H $2.88M; 24H -4.62%; V/LP 1.04x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $18.65M; Vol24H $21.52M; 24H +0.42%; V/LP 1.15x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Early; LP $479.1K; Vol24H $10.24M; 24H -6.04%; V/LP 21.37x; 池数 5; 分项 L15/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $157.1K; Vol24H $4.86M; 24H +11.92%; V/LP 30.95x; 池数 2; 分项 L11/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| CVXV666 | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 41; Tier Early; LP $114.3K; Vol24H $3.84M; 24H -20.52%; V/LP 33.62x; 池数 2; 分项 L10/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| BATON | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $96.2K; Vol24H $12.68M; 24H +2275.16%; V/LP 131.71x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $81.4K; Vol24H $2.56M; 24H +604.00%; V/LP 31.45x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [kylie](https://dexscreener.com/solana/3kbndtpzhw76zogfj4x3mpyu9wp1fqbynyx743dxjtno) | SOL | [6b7KQs...2rpump](https://solscan.io/token/6b7KQsXqb6JR5Nmeer5zGRmo51dwDfttM5b5Nu2rpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $43.0K; Vol24H $6.52M; 24H +349.00%; V/LP 151.60x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| 100CATS | SOL | [GUt3eb...P1pump](https://solscan.io/token/GUt3ebbJm6SJCvpa8SfFzZe132a78qZDyc2yXAP1pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $3.0K; Vol24H $2.84M; 24H -99.00%; V/LP 945.13x; 池数 1; 分项 L0/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [MARTIN](https://dexscreener.com/solana/anyskudzswmsw3n4knbm9rtqpcxbubzmbyzxkzuphxww) | SOL | [GHU8yQ...XSpump](https://solscan.io/token/GHU8yQL74VCmVXMpPrx9mY8UWzdbD6RPf6BHeyXSpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $40.5K; Vol24H $8.70M; 24H +230.00%; V/LP 214.88x; 池数 1; 分项 L6/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.77M; Vol24H $2.88M; 24H -4.62%; V/LP 1.04x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.65M; Vol24H $21.52M; 24H +0.42%; V/LP 1.15x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/eoftfbgdbxzkeqzc5dtygvnkicwevfezgtzqm9eftj6b) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $72.07M; Vol24H $76.85M; 24H +12.46%; V/LP 1.07x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Early; LP $693.1K; Vol24H $4.81M; 24H -2.79%; V/LP 6.93x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| DGAI | BSC | [0x10d4...8ebd5e](https://bscscan.com/token/0x10d4183389e99233db3cc981c43443ebd28ebd5e) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.65M; Vol24H $15.84M; 24H +66.48%; V/LP 5.98x; 池数 1; 分项 L20/V17/B8/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 66; Tier Mature; LP $6.01M; Vol24H $3.82M; 24H -22.80%; V/LP 0.64x; 池数 1; 分项 L20/V17/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WUKONG](https://dexscreener.com/bsc/0x424e1dc83e7364c4574150dab6ac122f57cf18f5) | BSC | [0xc5Fe...1c7777](https://bscscan.com/token/0xc5Feb05e1FF77a934c2B67828BC234dAf81c7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [SAOF](https://dexscreener.com/solana/hxfrsd7uc3lgdbcbgpyptqlbsk2syubfqicxvumcj5uw) | SOL | [ZrZy8Q...VFpump](https://solscan.io/token/ZrZy8Q1uXG2PSPn7X4NaMQMRa11paZ2xReKNsVFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| UPS | BSC | [0xae5a...afba01](https://bscscan.com/token/0xae5a409773b9a7dd0ae94ff437ac213d8fafba01) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| CVXV666 | SOL | [C3bajJ...iBpump](https://solscan.io/token/C3bajJW843KN9Uu441JkXN7zVMs4VM2HvdAGyGiBpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BATON | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 9 / Liquid 6 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
# 自我进化轮巡

**本轮时间 UTC：** 2026-08-25T17:25:49Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 132 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 231 |
| 合并后Token | 132 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 2 |
| 多池Token | 7 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 9 |
| Liquid层 | 8 |
| Mature层 | 2 |
| 需要链上确认 | 16 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1089，刷新时间 2026-08-24T00:46:57Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 1 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 89; Tier Liquid; LP $3.19M; Vol24H $1.51M; 24H -3.12%; V/LP 0.47x; 池数 1; 分项 L20/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 82; Tier Liquid; LP $1.30M; Vol24H $315.2K; 24H -9.37%; V/LP 0.24x; 池数 1; 分项 L19/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 75; Tier Liquid; LP $988.5K; Vol24H $6.43M; 24H +74.91%; V/LP 6.51x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 70; Tier Early; LP $371.9K; Vol24H $96.1K; 24H +11.12%; V/LP 0.26x; 池数 1; 分项 L14/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 次观察 | Score 68; Tier Liquid; LP $1.67M; Vol24H $13.53M; 24H -12.36%; V/LP 8.11x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 56; Tier Early; LP $467.1K; Vol24H $9.66M; 24H +1.21%; V/LP 20.68x; 池数 12; 分项 L15/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 41; Tier Early; LP $138.1K; Vol24H $4.42M; 24H +9.20%; V/LP 31.97x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BATON](https://dexscreener.com/solana/6vkqkcnqljqnlkaboykka6l5gpvsjy2bbwrmevsppjoj) | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | PVP风险池 | Score 28; Tier Micro; LP $91.0K; Vol24H $13.42M; 24H +1684.00%; V/LP 147.42x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | PVP风险池 | Score 27; Tier Micro; LP $75.3K; Vol24H $3.38M; 24H +481.00%; V/LP 44.88x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PENGU | SOL | [2zMMhc...Bouauv](https://solscan.io/token/2zMMhcVQEXDtdE6vsFS7S7D5oUodfJHE8vd1gnBouauv) | PVP风险池 | Score 18; Tier Micro; LP $32.7K; Vol24H $1.91M; 24H +0.12%; V/LP 58.48x; 池数 1; 分项 L5/V16/B22/Buy3/Risk-52 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 主观察 | Score 91; Tier Liquid; LP $1.72M; Vol24H $13.31M; 24H +0.18%; V/LP 7.72x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 89; Tier Liquid; LP $3.18M; Vol24H $1.46M; 24H -3.36%; V/LP 0.46x; 池数 1; 分项 L20/V15/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 82; Tier Liquid; LP $1.30M; Vol24H $319.0K; 24H -9.30%; V/LP 0.25x; 池数 1; 分项 L19/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 75; Tier Liquid; LP $976.1K; Vol24H $6.38M; 24H +65.80%; V/LP 6.54x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 次观察 | Score 71; Tier Early; LP $384.0K; Vol24H $104.6K; 24H +22.58%; V/LP 0.27x; 池数 1; 分项 L15/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 70; Tier Early; LP $311.9K; Vol24H $516.2K; 24H +28.61%; V/LP 1.65x; 池数 5; 分项 L14/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WOFI](https://dexscreener.com/solana/6eeyaup2jzuqtrp7huufectkfkrnhmpk3uaslfbglqb4) | SOL | [xmUzLu...Ezpump](https://solscan.io/token/xmUzLunAjxipLfGeXQZAurCdvuqkKdpxnNVwNEzpump) | 次观察 | Score 70; Tier Early; LP $221.3K; Vol24H $181.4K; 24H +23.50%; V/LP 0.82x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/hxfrsd7uc3lgdbcbgpyptqlbsk2syubfqicxvumcj5uw) | SOL | [ZrZy8Q...VFpump](https://solscan.io/token/ZrZy8Q1uXG2PSPn7X4NaMQMRa11paZ2xReKNsVFpump) | 次观察 | Score 70; Tier Early; LP $201.5K; Vol24H $175.8K; 24H +23.72%; V/LP 0.87x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 56; Tier Early; LP $458.0K; Vol24H $9.59M; 24H +4.90%; V/LP 20.94x; 池数 6; 分项 L15/V17/B22/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | PVP风险池 | Score 33; Tier Early; LP $157.3K; Vol24H $4.43M; 24H +28.60%; V/LP 28.13x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BATON](https://dexscreener.com/solana/6vkqkcnqljqnlkaboykka6l5gpvsjy2bbwrmevsppjoj) | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | PVP风险池 | Score 27; Tier Micro; LP $71.0K; Vol24H $13.57M; 24H +992.00%; V/LP 191.16x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | PVP风险池 | Score 26; Tier Micro; LP $60.4K; Vol24H $3.58M; 24H +276.00%; V/LP 59.18x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [KERMIT](https://dexscreener.com/solana/hxqcf5m1e3wydrb9zna4du9e5lpwygdycpk7wg5qcsuc) | SOL | [31TBAG...AJpump](https://solscan.io/token/31TBAGQ4cydajbZYCqvuyA9SqmKV7zvtdmohkLAJpump) | PVP风险池 | Score 23; Tier Micro; LP $30.2K; Vol24H $1.59M; 24H +76.89%; V/LP 52.76x; 池数 1; 分项 L4/V15/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PENGU | SOL | [2zMMhc...Bouauv](https://solscan.io/token/2zMMhcVQEXDtdE6vsFS7S7D5oUodfJHE8vd1gnBouauv) | PVP风险池 | Score 17; Tier Micro; LP $33.0K; Vol24H $1.78M; 24H +3.79%; V/LP 53.99x; 池数 1; 分项 L5/V15/B22/Buy3/Risk-52 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [kylie](https://dexscreener.com/solana/3kbndtpzhw76zogfj4x3mpyu9wp1fqbynyx743dxjtno) | SOL | [6b7KQs...2rpump](https://solscan.io/token/6b7KQsXqb6JR5Nmeer5zGRmo51dwDfttM5b5Nu2rpump) | PVP风险池 | Score 14; Tier Micro; LP $32.1K; Vol24H $6.63M; 24H +156.00%; V/LP 206.21x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Early; LP $458.0K; Vol24H $9.59M; 24H +4.90%; V/LP 20.94x; 池数 6; 分项 L15/V17/B22/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 33; Tier Early; LP $157.3K; Vol24H $4.43M; 24H +28.60%; V/LP 28.13x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [BATON](https://dexscreener.com/solana/6vkqkcnqljqnlkaboykka6l5gpvsjy2bbwrmevsppjoj) | SOL | [6Hebn6...Gppump](https://solscan.io/token/6Hebn672FvMSq61mo4HYq86QgLHgBUm6y8A9bXGppump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $71.0K; Vol24H $13.57M; 24H +992.00%; V/LP 191.16x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MrCate](https://dexscreener.com/solana/fizqsex6xcycbzvrxj5vbzo8jeqjhhn61yplaydataci) | SOL | [52ZzDV...BWpump](https://solscan.io/token/52ZzDVDPk8S4T1rfKNWSvtDnzhLN8omMK1xLCBBWpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $60.4K; Vol24H $3.58M; 24H +276.00%; V/LP 59.18x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [KERMIT](https://dexscreener.com/solana/hxqcf5m1e3wydrb9zna4du9e5lpwygdycpk7wg5qcsuc) | SOL | [31TBAG...AJpump](https://solscan.io/token/31TBAGQ4cydajbZYCqvuyA9SqmKV7zvtdmohkLAJpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 23; Tier Micro; LP $30.2K; Vol24H $1.59M; 24H +76.89%; V/LP 52.76x; 池数 1; 分项 L4/V15/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| PENGU | SOL | [2zMMhc...Bouauv](https://solscan.io/token/2zMMhcVQEXDtdE6vsFS7S7D5oUodfJHE8vd1gnBouauv) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 17; Tier Micro; LP $33.0K; Vol24H $1.78M; 24H +3.79%; V/LP 53.99x; 池数 1; 分项 L5/V15/B22/Buy3/Risk-52 | 只记录热度，不进入主榜 |
| [kylie](https://dexscreener.com/solana/3kbndtpzhw76zogfj4x3mpyu9wp1fqbynyx743dxjtno) | SOL | [6b7KQs...2rpump](https://solscan.io/token/6b7KQsXqb6JR5Nmeer5zGRmo51dwDfttM5b5Nu2rpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $32.1K; Vol24H $6.63M; 24H +156.00%; V/LP 206.21x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [QUEEZING](https://dexscreener.com/solana/h4hjevfwamwfnejkemcfcfwcxfxdxnuwii8hgzrqhflj) | SOL | [6ybRJG...CUpump](https://solscan.io/token/6ybRJGfWpArsP5bWDmUcrqakiSeUR8P581C8H9CUpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $32.0K; Vol24H $2.51M; 24H +213.00%; V/LP 78.28x; 池数 5; 分项 L5/V16/B0/Buy3/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $2.73M; Vol24H $2.52M; 24H -0.61%; V/LP 0.92x; 池数 2; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.35M; Vol24H $4.36M; 24H +4.50%; V/LP 3.22x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.70M; Vol24H $17.26M; 24H +0.42%; V/LP 0.92x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $173.45M; Vol24H $152.07M; 24H +9.40%; V/LP 0.88x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 71; Tier Early; LP $692.8K; Vol24H $3.90M; 24H +4.21%; V/LP 5.62x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| DGAI | BSC | [0x10d4...8ebd5e](https://bscscan.com/token/0x10d4183389e99233db3cc981c43443ebd28ebd5e) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $2.69M; Vol24H $15.29M; 24H +67.63%; V/LP 5.68x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| VELVET | BSC | [0x8b19...8c1488](https://bscscan.com/token/0x8b194370825e37b33373e74a41009161808c1488) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $785.9K; Vol24H $456.1K; 24H -23.84%; V/LP 0.58x; 池数 1; 分项 L17/V11/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [three](https://dexscreener.com/solana/5byl7mzolabynwmpzkpkjf4mgkz7febzranos19pre2z) | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WOFI](https://dexscreener.com/solana/6eeyaup2jzuqtrp7huufectkfkrnhmpk3uaslfbglqb4) | SOL | [xmUzLu...Ezpump](https://solscan.io/token/xmUzLunAjxipLfGeXQZAurCdvuqkKdpxnNVwNEzpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SAOF](https://dexscreener.com/solana/hxfrsd7uc3lgdbcbgpyptqlbsk2syubfqicxvumcj5uw) | SOL | [ZrZy8Q...VFpump](https://solscan.io/token/ZrZy8Q1uXG2PSPn7X4NaMQMRa11paZ2xReKNsVFpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| [Morty](https://dexscreener.com/solana/8wa7x9ewdfvkikqrecmr3omwljmaqks2csjxw1pws7dh) | SOL | [GUmbtf...jzpump](https://solscan.io/token/GUmbtfjSZkybSFgPibBcvwExEBdXwewJHR5PkTjzpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 9 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
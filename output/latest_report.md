# 自我进化轮巡

**本轮时间 UTC：** 2026-07-06T21:25:17Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 132 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 306 |
| 合并后Token | 132 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 7 |
| 多池Token | 9 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 12 |
| Liquid层 | 6 |
| Mature层 | 2 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Joby](https://dexscreener.com/solana/brbvi3yr1rrkorbk5xcag1e5urldyjgrmjixvzd6gffc) | SOL | [4SnKwn...2Jpump](https://solscan.io/token/4SnKwnz6DyagftnFqdxsvWvehrcbEDhxmmXNQk2Jpump) | 主观察 | Score 79; Tier Early; LP $162.0K; Vol24H $1.03M; 24H +5.27%; V/LP 6.37x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BABYCZ | BSC | [0xc7ae...9e4444](https://bscscan.com/token/0xc7aeb1a936fcf98cfe4dd552f6cbf48ac19e4444) | 次观察 | Score 75; Tier Micro; LP $53.3K; Vol24H $328.5K; 24H -6.95%; V/LP 6.17x; 池数 1; 分项 L7/V10/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 74; Tier Early; LP $185.7K; Vol24H $758.3K; 24H -5.25%; V/LP 4.08x; 池数 3; 分项 L12/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 次观察 | Score 70; Tier Early; LP $187.6K; Vol24H $176.4K; 24H +1.35%; V/LP 0.94x; 池数 1; 分项 L12/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 69; Tier Early; LP $215.9K; Vol24H $125.5K; 24H -21.16%; V/LP 0.58x; 池数 3; 分项 L12/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RETARD](https://dexscreener.com/solana/4fsjvbrpus55exor2mldbakhceusqxsyk5ndu62ntqme) | SOL | [2q68mq...inpump](https://solscan.io/token/2q68mqEbjwmnMjs1o3KZDNZVyMv6RZKkHcm64iinpump) | 次观察 | Score 68; Tier Early; LP $102.5K; Vol24H $278.7K; 24H +5.95%; V/LP 2.72x; 池数 5; 分项 L9/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 45; Tier Liquid; LP $994.7K; Vol24H $34.36M; 24H +47.13%; V/LP 34.54x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 43; Tier Early; LP $527.9K; Vol24H $28.38M; 24H -67.05%; V/LP 53.76x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | PVP风险池 | Score 36; Tier Micro; LP $96.1K; Vol24H $5.32M; 24H -76.48%; V/LP 55.35x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 33; Tier Early; LP $303.8K; Vol24H $11.86M; 24H +34976.47%; V/LP 39.05x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BAS | BSC | [0x0f0d...db4e37](https://bscscan.com/token/0x0f0df6cb17ee5e883eddfef9153fc6036bdb4e37) | 主观察 | Score 83; Tier Liquid; LP $2.05M; Vol24H $12.71M; 24H -6.15%; V/LP 6.21x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Joby](https://dexscreener.com/solana/brbvi3yr1rrkorbk5xcag1e5urldyjgrmjixvzd6gffc) | SOL | [4SnKwn...2Jpump](https://solscan.io/token/4SnKwnz6DyagftnFqdxsvWvehrcbEDhxmmXNQk2Jpump) | 主观察 | Score 79; Tier Early; LP $163.3K; Vol24H $969.3K; 24H -6.05%; V/LP 5.94x; 池数 1; 分项 L11/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 次观察 | Score 75; Tier Early; LP $178.7K; Vol24H $1.12M; 24H -13.70%; V/LP 6.27x; 池数 1; 分项 L12/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 74; Tier Early; LP $189.8K; Vol24H $759.1K; 24H +2.21%; V/LP 4.00x; 池数 3; 分项 L12/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PATTYICE](https://dexscreener.com/solana/9ekxwq8pxysiqddwawuw6knybyapib7ga3iyloxatcbz) | SOL | [2jz9E5...9rpump](https://solscan.io/token/2jz9E5JrEbxLg1RhU68aaSikDvpQurCEZz9BBF9rpump) | 次观察 | Score 71; Tier Micro; LP $93.8K; Vol24H $706.6K; 24H +19.25%; V/LP 7.53x; 池数 5; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 次观察 | Score 64; Tier Early; LP $187.0K; Vol24H $146.8K; 24H +8.22%; V/LP 0.79x; 池数 2; 分项 L12/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 45; Tier Liquid; LP $992.2K; Vol24H $32.29M; 24H +74.45%; V/LP 32.54x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 43; Tier Early; LP $510.1K; Vol24H $24.71M; 24H -68.04%; V/LP 48.44x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | PVP风险池 | Score 36; Tier Early; LP $101.9K; Vol24H $4.75M; 24H -77.81%; V/LP 46.63x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 33; Tier Early; LP $304.0K; Vol24H $12.36M; 24H +118438.00%; V/LP 40.68x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 31; Tier Early; LP $199.1K; Vol24H $4.44M; 24H -10.06%; V/LP 22.28x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BIF](https://dexscreener.com/solana/6wjspkymm4uq7qekcnfsu9jq7pf3zzjbmhw6efabmexc) | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | PVP风险池 | Score 30; Tier Early; LP $149.9K; Vol24H $5.57M; 24H +9258.00%; V/LP 37.15x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAYLOR](https://dexscreener.com/solana/6pnitpjjxs8axepzt3wjhvswnhwkvrhcxayn6smfbbyy) | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | PVP风险池 | Score 30; Tier Micro; LP $52.8K; Vol24H $4.30M; 24H +785.00%; V/LP 81.34x; 池数 1; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Vaaland](https://dexscreener.com/solana/31a3uvuvzhjj8sopj8g3qzuha6ebk8andgmokpx3kfdf) | SOL | [6uYAQy...YCpump](https://solscan.io/token/6uYAQyXYMQ5sTNPRZmYSVMGTAzgkTrK5mGtHpPYCpump) | PVP风险池 | Score 30; Tier Micro; LP $56.5K; Vol24H $3.08M; 24H +668.00%; V/LP 54.54x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $18.38M; Vol24H $13.47M; 24H +2.36%; V/LP 0.73x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Liquid; LP $992.2K; Vol24H $32.29M; 24H +74.45%; V/LP 32.54x; 池数 1; 分项 L18/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Early; LP $510.1K; Vol24H $24.71M; 24H -68.04%; V/LP 48.44x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Early; LP $101.9K; Vol24H $4.75M; 24H -77.81%; V/LP 46.63x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $304.0K; Vol24H $12.36M; 24H +118438.00%; V/LP 40.68x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 31; Tier Early; LP $199.1K; Vol24H $4.44M; 24H -10.06%; V/LP 22.28x; 池数 1; 分项 L12/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [BIF](https://dexscreener.com/solana/6wjspkymm4uq7qekcnfsu9jq7pf3zzjbmhw6efabmexc) | SOL | [62YE1d...i2pump](https://solscan.io/token/62YE1d4sRArBQzR5bdbxsx2k9LV3MdPV4xMC4Di2pump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $149.9K; Vol24H $5.57M; 24H +9258.00%; V/LP 37.15x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SAYLOR](https://dexscreener.com/solana/6pnitpjjxs8axepzt3wjhvswnhwkvrhcxayn6smfbbyy) | SOL | [AVVLwZ...Wapump](https://solscan.io/token/AVVLwZcNnts8JffDiEZxLNXGk9nLAzRr6hf9KDWapump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $52.8K; Vol24H $4.30M; 24H +785.00%; V/LP 81.34x; 池数 1; 分项 L7/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [Vaaland](https://dexscreener.com/solana/31a3uvuvzhjj8sopj8g3qzuha6ebk8andgmokpx3kfdf) | SOL | [6uYAQy...YCpump](https://solscan.io/token/6uYAQyXYMQ5sTNPRZmYSVMGTAzgkTrK5mGtHpPYCpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $56.5K; Vol24H $3.08M; 24H +668.00%; V/LP 54.54x; 池数 2; 分项 L7/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $18.38M; Vol24H $13.47M; 24H +2.36%; V/LP 0.73x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| USDT | BSC | [0x55d3...197955](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $16.88M; Vol24H $117.63M; 24H +0.06%; V/LP 6.97x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $1.62M; Vol24H $2.28M; 24H +8.77%; V/LP 1.41x; 池数 1; 分项 L20/V16/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $3.53M; Vol24H $25.95M; 24H +39.66%; V/LP 7.35x; 池数 7; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [Joby](https://dexscreener.com/solana/brbvi3yr1rrkorbk5xcag1e5urldyjgrmjixvzd6gffc) | SOL | [4SnKwn...2Jpump](https://solscan.io/token/4SnKwnz6DyagftnFqdxsvWvehrcbEDhxmmXNQk2Jpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BAS | BSC | [0x0f0d...db4e37](https://bscscan.com/token/0x0f0df6cb17ee5e883eddfef9153fc6036bdb4e37) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PATTYICE](https://dexscreener.com/solana/9ekxwq8pxysiqddwawuw6knybyapib7ga3iyloxatcbz) | SOL | [2jz9E5...9rpump](https://solscan.io/token/2jz9E5JrEbxLg1RhU68aaSikDvpQurCEZz9BBF9rpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [BULL](https://dexscreener.com/solana/hngjllzkwx2mnwhwdkfycmowz8fth2bxxdpj1vbvkjnb) | SOL | [3TYgKw...Hspump](https://solscan.io/token/3TYgKwkE2Y3rxdw9osLRSpxpXmSC1C1oo19W9KHspump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [LEVI](https://dexscreener.com/solana/eqmxjt3vqvfuwamr5duyajmalrkhogf4n3yxaa7rgzak) | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [Joby](https://dexscreener.com/solana/brbvi3yr1rrkorbk5xcag1e5urldyjgrmjixvzd6gffc) | SOL | [4SnKwn...2Jpump](https://solscan.io/token/4SnKwnz6DyagftnFqdxsvWvehrcbEDhxmmXNQk2Jpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BAS | BSC | [0x0f0d...db4e37](https://bscscan.com/token/0x0f0df6cb17ee5e883eddfef9153fc6036bdb4e37) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 5 / Early 12 / Liquid 6 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
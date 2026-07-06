# 自我进化轮巡

**本轮时间 UTC：** 2026-07-06T05:06:49Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 121 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 367 |
| 合并后Token | 121 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 10 |
| 多池Token | 14 |
| 多池冲突 | 6 |
| Symbol桥接合并 | 4 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 12 |
| Liquid层 | 4 |
| Mature层 | 1 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 0 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 主观察 | Score 80; Tier Early; LP $471.8K; Vol24H $2.44M; 24H -22.14%; V/LP 5.16x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CATWIF](https://dexscreener.com/solana/4dytblybdqyqjavjlrht4xtqkvm7qayzuttjfsicromp) | SOL | [5pYB12...9spump](https://solscan.io/token/5pYB12kEhfhSFXJjZ7JtyqDpt6uUqhsF6iu6Ee9spump) | 主观察 | Score 76; Tier Early; LP $192.0K; Vol24H $1.49M; 24H +22.51%; V/LP 7.74x; 池数 1; 分项 L12/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 次观察 | Score 73; Tier Early; LP $183.7K; Vol24H $597.4K; 24H -22.40%; V/LP 3.25x; 池数 5; 分项 L12/V12/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 64; Tier Micro; LP $64.9K; Vol24H $149.6K; 24H -20.31%; V/LP 2.30x; 池数 2; 分项 L7/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 54; Tier Liquid; LP $882.1K; Vol24H $18.69M; 24H -0.60%; V/LP 21.18x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [manlet](https://dexscreener.com/solana/8qdidakuynykar4dh2zfzzvg5gbtufyjcwqpgwt9fs1y) | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | PVP风险池 | Score 41; Tier Early; LP $328.4K; Vol24H $7.46M; 24H -31.22%; V/LP 22.73x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0x7a84...504444](https://bscscan.com/token/0x7a848a5a8169aa6a2f603d056a749f924f504444) | PVP风险池 | Score 37; Tier Liquid; LP $851.4K; Vol24H $58.98M; 24H +135.99%; V/LP 69.27x; 池数 2; 分项 L18/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 36; Tier Early; LP $739.8K; Vol24H $51.64M; 24H +48710.23%; V/LP 69.80x; 池数 1; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HEYI | BSC | [0x4ce6...a24444](https://bscscan.com/token/0x4ce634563bb2f72961483357dc31b4c146a24444) | PVP风险池 | Score 30; Tier Early; LP $163.9K; Vol24H $9.05M; 24H +311.82%; V/LP 55.19x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ACM](https://dexscreener.com/solana/hksdmj6kthsczxmvvus24wvk3wgzfuepqhwdkcjhkepz) | SOL | [4PRz3E...vhpump](https://solscan.io/token/4PRz3EwhbjrrX6YksMDuUzrXT51pr7CQtXNCravhpump) | PVP风险池 | Score 28; Tier Micro; LP $84.5K; Vol24H $4.12M; 24H +3038.00%; V/LP 48.68x; 池数 6; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 主观察 | Score 78; Tier Early; LP $192.2K; Vol24H $612.9K; 24H -6.65%; V/LP 3.19x; 池数 5; 分项 L12/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 70; Tier Micro; LP $66.3K; Vol24H $146.3K; 24H +4.79%; V/LP 2.21x; 池数 2; 分项 L8/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 次观察 | Score 67; Tier Early; LP $364.7K; Vol24H $7.16M; 24H +2.33%; V/LP 19.62x; 池数 7; 分项 L14/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ZERO | SOL | [EmcxFT...dwpump](https://solscan.io/token/EmcxFTNVDqyLHp11NvwvLZ4D7LKGbG9i7B8RF7dwpump) | 次观察 | Score 65; Tier Early; LP $318.5K; Vol24H $2.24M; 24H +47.89%; V/LP 7.03x; 池数 1; 分项 L14/V16/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 次观察 | Score 64; Tier Early; LP $113.8K; Vol24H $278.2K; 24H -21.01%; V/LP 2.45x; 池数 1; 分项 L10/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 54; Tier Liquid; LP $857.6K; Vol24H $18.24M; 24H +3.53%; V/LP 21.27x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CZ | BSC | [0xac97...af7277](https://bscscan.com/token/0xac97d8c1ed5f21c08781d1220740be3925af7277) | PVP风险池 | Score 40; Tier Liquid; LP $879.4K; Vol24H $188.37M; 24H -75.14%; V/LP 214.21x; 池数 2; 分项 L18/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HEYI | BSC | [0x4ce6...a24444](https://bscscan.com/token/0x4ce634563bb2f72961483357dc31b4c146a24444) | PVP风险池 | Score 38; Tier Early; LP $165.5K; Vol24H $8.06M; 24H +70.75%; V/LP 48.70x; 池数 3; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | PVP风险池 | Score 36; Tier Early; LP $749.2K; Vol24H $54.97M; 24H +49418.04%; V/LP 73.38x; 池数 1; 分项 L17/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TOLY | SOL | [CvqxZz...dKpump](https://solscan.io/token/CvqxZzFZqDKSpD1bNSkwQ6j9stSCBVgQ9GT4tLdKpump) | PVP风险池 | Score 36; Tier Micro; LP $96.7K; Vol24H $3.83M; 24H +47.88%; V/LP 39.58x; 池数 6; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | PVP风险池 | Score 30; Tier Early; LP $172.5K; Vol24H $4.62M; 24H +4864.77%; V/LP 26.80x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ACM | SOL | [4PRz3E...vhpump](https://solscan.io/token/4PRz3EwhbjrrX6YksMDuUzrXT51pr7CQtXNCravhpump) | PVP风险池 | Score 28; Tier Micro; LP $94.7K; Vol24H $4.42M; 24H +2120.59%; V/LP 46.71x; 池数 7; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [0x](https://dexscreener.com/solana/3fganhkt84zlgg449h1bguqtddp1nmbxcb1oohap32ui) | SOL | [CMx1EU...DVpump](https://solscan.io/token/CMx1EUTXhnUKYF5xYMCSkDmJfvRSD7a4iwayW1DVpump) | PVP风险池 | Score 9; Tier Micro; LP $35.6K; Vol24H $3.78M; 24H +369.00%; V/LP 106.15x; 池数 2; 分项 L5/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 成熟池观察 | Score 71; Tier Mature; LP $5.28M; Vol24H $5.18M; 24H -6.92%; V/LP 0.98x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 69; Tier Liquid; LP $3.41M; Vol24H $23.25M; 24H +24.89%; V/LP 6.82x; 池数 3; 分项 L20/V17/B17/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 54; Tier Liquid; LP $857.6K; Vol24H $18.24M; 24H +3.53%; V/LP 21.27x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| CZ | BSC | [0xac97...af7277](https://bscscan.com/token/0xac97d8c1ed5f21c08781d1220740be3925af7277) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Liquid; LP $879.4K; Vol24H $188.37M; 24H -75.14%; V/LP 214.21x; 池数 2; 分项 L18/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| HEYI | BSC | [0x4ce6...a24444](https://bscscan.com/token/0x4ce634563bb2f72961483357dc31b4c146a24444) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $165.5K; Vol24H $8.06M; 24H +70.75%; V/LP 48.70x; 池数 3; 分项 L11/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TCC | BSC | [0xa439...954444](https://bscscan.com/token/0xa4390b901a63641c92327e5793b45fcb46954444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 36; Tier Early; LP $749.2K; Vol24H $54.97M; 24H +49418.04%; V/LP 73.38x; 池数 1; 分项 L17/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TOLY | SOL | [CvqxZz...dKpump](https://solscan.io/token/CvqxZzFZqDKSpD1bNSkwQ6j9stSCBVgQ9GT4tLdKpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $96.7K; Vol24H $3.83M; 24H +47.88%; V/LP 39.58x; 池数 6; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AB | BSC | [0x747b...2b4444](https://bscscan.com/token/0x747b87ddb438b73044b38832027acb06412b4444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $172.5K; Vol24H $4.62M; 24H +4864.77%; V/LP 26.80x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| ACM | SOL | [4PRz3E...vhpump](https://solscan.io/token/4PRz3EwhbjrrX6YksMDuUzrXT51pr7CQtXNCravhpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $94.7K; Vol24H $4.42M; 24H +2120.59%; V/LP 46.71x; 池数 7; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [0x](https://dexscreener.com/solana/3fganhkt84zlgg449h1bguqtddp1nmbxcb1oohap32ui) | SOL | [CMx1EU...DVpump](https://solscan.io/token/CMx1EUTXhnUKYF5xYMCSkDmJfvRSD7a4iwayW1DVpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $35.6K; Vol24H $3.78M; 24H +369.00%; V/LP 106.15x; 池数 2; 分项 L5/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限 | Score 71; Tier Mature; LP $5.28M; Vol24H $5.18M; 24H -6.92%; V/LP 0.98x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.41M; Vol24H $23.25M; 24H +24.89%; V/LP 6.82x; 池数 3; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| manlet | SOL | [DdPrHY...3Zpump](https://solscan.io/token/DdPrHYqM8Ueovnk9kAnAgoGhswkuaTqmxcoZzU3Zpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ZERO | SOL | [EmcxFT...dwpump](https://solscan.io/token/EmcxFTNVDqyLHp11NvwvLZ4D7LKGbG9i7B8RF7dwpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SON](https://dexscreener.com/solana/ec9rk1gqmn4d7tjp2efx6m1on1rmxxr5gh4pkswjqskx) | SOL | [ACpzkG...Nppump](https://solscan.io/token/ACpzkGJV3DDU8HXy8yjab7RL9qNmDGym2GwLkzNppump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [公牛](https://dexscreener.com/solana/bw2skkml1wydd7tfnlzemuwdry5rdk1zk36pzg3ndfac) | SOL | [H1ohgr...btpump](https://solscan.io/token/H1ohgrouxAGCMwWya1j7Ewur5M2pGkQtZ791icbtpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [BABYANSEM](https://dexscreener.com/solana/ckb2oh5rweruvnzhgxbggs5mpmsofrxhgcz7mtafyxqx) | SOL | [iB1umQ...jipump](https://solscan.io/token/iB1umQs5Jzq6ysaRk5yRKaJ4XJcWgqHDxsdVtjipump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [bullbank](https://dexscreener.com/solana/39iqrdn8cbuouns3nwutjzzvxdnd97gglkrrmqszbqfk) | SOL | [BKTxYx...hnpump](https://solscan.io/token/BKTxYxj3ugjzsP5WTFh1suKHEfUn31nPb6gkpGhnpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [SATOSHI](https://dexscreener.com/solana/88ucacaxrjqlogps7jqxqntbfmnsj1uhena2ygshaxns) | SOL | [2R8GSy...p7pump](https://solscan.io/token/2R8GSyFMz1xbJznogKyM11GfxD3de61bPbYoiip7pump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 12 / Liquid 4 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 341} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
# 自我进化轮巡

**本轮时间 UTC：** 2026-08-09T04:58:44Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 139 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 241 |
| 合并后Token | 139 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 3 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 9 |
| Liquid层 | 7 |
| Mature层 | 3 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 3 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $915.5K; Vol24H $6.98M; 24H -20.25%; V/LP 7.63x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 84; Tier Early; LP $542.2K; Vol24H $1.25M; 24H -4.93%; V/LP 2.31x; 池数 1; 分项 L16/V14/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 77; Tier Liquid; LP $1.11M; Vol24H $202.0K; 24H -2.31%; V/LP 0.18x; 池数 1; 分项 L19/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dealer](https://dexscreener.com/solana/fjhugiw2hz9uozus6haaednftirkjk22hn3ykae2eg5x) | SOL | [6f8ZQh...Zopump](https://solscan.io/token/6f8ZQhxqfigdv7UszZ1rirbV7Sgv83s3rxv1N2Zopump) | 次观察 | Score 73; Tier Micro; LP $64.3K; Vol24H $511.1K; 24H +2.73%; V/LP 7.95x; 池数 1; 分项 L7/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 次观察 | Score 73; Tier Early; LP $466.3K; Vol24H $2.76M; 24H +9.07%; V/LP 5.92x; 池数 1; 分项 L15/V17/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 72; Tier Early; LP $245.9K; Vol24H $55.6K; 24H -3.49%; V/LP 0.23x; 池数 1; 分项 L13/V5/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 次观察 | Score 71; Tier Early; LP $223.4K; Vol24H $72.9K; 24H +23.21%; V/LP 0.33x; 池数 1; 分项 L12/V6/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VenusCoin](https://dexscreener.com/bsc/0x12cd92372983c4d60fd40ae6c7545bbc5ebc8ca7) | BSC | [0x5460...8d7777](https://bscscan.com/token/0x5460b5E88799D27bbdf8A210926C17Dec18d7777) | 次观察 | Score 70; Tier Early; LP $185.3K; Vol24H $560.0K; 24H -14.42%; V/LP 3.02x; 池数 3; 分项 L12/V12/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 次观察 | Score 70; Tier Early; LP $274.1K; Vol24H $141.3K; 24H +10.15%; V/LP 0.52x; 池数 1; 分项 L13/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 次观察 | Score 69; Tier Early; LP $617.8K; Vol24H $11.54M; 24H -5.77%; V/LP 18.67x; 池数 2; 分项 L16/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $886.7K; Vol24H $6.47M; 24H -21.39%; V/LP 7.30x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 79; Tier Early; LP $539.1K; Vol24H $1.16M; 24H -15.11%; V/LP 2.14x; 池数 1; 分项 L16/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 主观察 | Score 78; Tier Early; LP $463.1K; Vol24H $2.84M; 24H +7.10%; V/LP 6.13x; 池数 1; 分项 L15/V17/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 77; Tier Liquid; LP $1.11M; Vol24H $188.5K; 24H -2.61%; V/LP 0.17x; 池数 1; 分项 L19/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 73; Tier Early; LP $122.6K; Vol24H $58.4K; 24H -3.40%; V/LP 0.48x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 次观察 | Score 71; Tier Early; LP $225.0K; Vol24H $71.1K; 24H +22.54%; V/LP 0.32x; 池数 1; 分项 L12/V6/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VenusCoin](https://dexscreener.com/bsc/0x12cd92372983c4d60fd40ae6c7545bbc5ebc8ca7) | BSC | [0x5460...8d7777](https://bscscan.com/token/0x5460b5E88799D27bbdf8A210926C17Dec18d7777) | 次观察 | Score 70; Tier Early; LP $185.4K; Vol24H $546.6K; 24H -24.56%; V/LP 2.95x; 池数 6; 分项 L12/V12/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 次观察 | Score 70; Tier Early; LP $273.0K; Vol24H $141.0K; 24H +8.34%; V/LP 0.52x; 池数 1; 分项 L13/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 67; Tier Early; LP $250.5K; Vol24H $55.7K; 24H -1.15%; V/LP 0.22x; 池数 1; 分项 L13/V5/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 39; Tier Liquid; LP $2.02M; Vol24H $55.20M; 24H -14.88%; V/LP 27.32x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 34; Tier Early; LP $465.2K; Vol24H $36.39M; 24H +42792.69%; V/LP 78.22x; 池数 3; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | PVP风险池 | Score 27; Tier Micro; LP $76.3K; Vol24H $3.90M; 24H +2493.00%; V/LP 51.17x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| claudius | SOL | [46amR3...VSpump](https://solscan.io/token/46amR3aeQE7MJ9QDrgNRqBP3FcsJ9QNYV71L2vVSpump) | PVP风险池 | Score 26; Tier Micro; LP $52.9K; Vol24H $5.30M; 24H +1064.30%; V/LP 100.20x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAVECAT](https://dexscreener.com/solana/fju39s2tyzkmixcqnn45zgctquocnyjpmlmoxrwdtuq5) | SOL | [mNzssX...S3pump](https://solscan.io/token/mNzssXQ9hU1ASJ1CVuu4JjrFBrfeVdR2JzirKS3pump) | PVP风险池 | Score 24; Tier Early; LP $125.2K; Vol24H $5.03M; 24H +184.00%; V/LP 40.14x; 池数 1; 分项 L10/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Frohorse](https://dexscreener.com/solana/5elnx7mtk6ttrmvfgxj3utk8wxtbq81kzruhflehrhvq) | SOL | [9p84TE...uMpump](https://solscan.io/token/9p84TE2ZwH8PXU7QMvj8ieK3TWodZPdCjpE8Q2uMpump) | PVP风险池 | Score 17; Tier Micro; LP $34.4K; Vol24H $3.22M; 24H -69.92%; V/LP 93.61x; 池数 1; 分项 L5/V17/B8/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $2.02M; Vol24H $55.20M; 24H -14.88%; V/LP 27.32x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $465.2K; Vol24H $36.39M; 24H +42792.69%; V/LP 78.22x; 池数 3; 分项 L15/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $76.3K; Vol24H $3.90M; 24H +2493.00%; V/LP 51.17x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| claudius | SOL | [46amR3...VSpump](https://solscan.io/token/46amR3aeQE7MJ9QDrgNRqBP3FcsJ9QNYV71L2vVSpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $52.9K; Vol24H $5.30M; 24H +1064.30%; V/LP 100.20x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [RAVECAT](https://dexscreener.com/solana/fju39s2tyzkmixcqnn45zgctquocnyjpmlmoxrwdtuq5) | SOL | [mNzssX...S3pump](https://solscan.io/token/mNzssXQ9hU1ASJ1CVuu4JjrFBrfeVdR2JzirKS3pump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Early; LP $125.2K; Vol24H $5.03M; 24H +184.00%; V/LP 40.14x; 池数 1; 分项 L10/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Frohorse](https://dexscreener.com/solana/5elnx7mtk6ttrmvfgxj3utk8wxtbq81kzruhflehrhvq) | SOL | [9p84TE...uMpump](https://solscan.io/token/9p84TE2ZwH8PXU7QMvj8ieK3TWodZPdCjpE8Q2uMpump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $34.4K; Vol24H $3.22M; 24H -69.92%; V/LP 93.61x; 池数 1; 分项 L5/V17/B8/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [Apu](https://dexscreener.com/solana/dwptsuia3aaeiot1mrdtkn3upjr6ckrwdztpiyrrbfzr) | SOL | [FKAgTQ...K1pump](https://solscan.io/token/FKAgTQJYgaLDRH3Fa78DeA69B9CdfFQ67oepzaK1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $24.9K; Vol24H $5.16M; 24H +191.00%; V/LP 207.33x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| RUBY | SOL | [JBKWfC...8cpump](https://solscan.io/token/JBKWfCwhW91RvkZb1S9HL8x59YuBbnVFxgwpkx8cpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $11.4K; Vol24H $3.50M; 24H +463.85%; V/LP 306.81x; 池数 1; 分项 L1/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 79; Tier Liquid; LP $3.81M; Vol24H $5.90M; 24H +3.58%; V/LP 1.55x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Mature; LP $8.40M; Vol24H $16.14M; 24H +1.54%; V/LP 1.92x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 71; Tier Mature; LP $11.06M; Vol24H $1.29M; 24H +1.41%; V/LP 0.12x; 池数 3; 分项 L20/V14/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $1.98M; Vol24H $857.5K; 24H -4.05%; V/LP 0.43x; 池数 2; 分项 L20/V13/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；成熟大池 | Score 58; Tier Mature; LP $20.00M; Vol24H $7.2K; 24H +1.85%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VenusCoin](https://dexscreener.com/bsc/0x12cd92372983c4d60fd40ae6c7545bbc5ebc8ca7) | BSC | [0x5460...8d7777](https://bscscan.com/token/0x5460b5E88799D27bbdf8A210926C17Dec18d7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 4 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 9 / Liquid 7 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
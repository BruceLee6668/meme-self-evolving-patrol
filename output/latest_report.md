# 自我进化轮巡

**本轮时间 UTC：** 2026-06-27T10:00:40Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 136 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 319 |
| 合并后Token | 136 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 0 |
| 多池Token | 10 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 6 |
| Liquid层 | 9 |
| Mature层 | 3 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 6 个，BSC Transfer样本 4 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 86; Tier Liquid; LP $1.74M; Vol24H $13.18M; 24H +1.04%; V/LP 7.57x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 主观察 | Score 86; Tier Liquid; LP $2.05M; Vol24H $13.47M; 24H -6.93%; V/LP 6.56x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.09M; Vol24H $4.72M; 24H -2.43%; V/LP 4.33x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 83; Tier Early; LP $292.3K; Vol24H $588.1K; 24H +1.91%; V/LP 2.01x; 池数 1; 分项 L13/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 76; Tier Liquid; LP $981.8K; Vol24H $215.5K; 24H +7.35%; V/LP 0.22x; 池数 1; 分项 L18/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Jotchua](https://dexscreener.com/solana/akqyqgeifbbhqmanukzrrurgokskkbv8nvdccc87frr8) | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 69; Tier Early; LP $477.4K; Vol24H $982.6K; 24H +45.33%; V/LP 2.06x; 池数 2; 分项 L15/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 68; Tier Early; LP $173.1K; Vol24H $2.66M; 24H -5.29%; V/LP 15.39x; 池数 1; 分项 L11/V17/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 67; Tier Micro; LP $63.7K; Vol24H $419.0K; 24H +11.36%; V/LP 6.58x; 池数 1; 分项 L7/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 66; Tier Early; LP $103.1K; Vol24H $163.2K; 24H -2.38%; V/LP 1.58x; 池数 2; 分项 L9/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 64; Tier Early; LP $436.4K; Vol24H $1.00M; 24H +27.10%; V/LP 2.29x; 池数 2; 分项 L15/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 主观察 | Score 86; Tier Early; LP $334.0K; Vol24H $1.04M; 24H -2.68%; V/LP 3.10x; 池数 5; 分项 L14/V14/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 主观察 | Score 86; Tier Liquid; LP $2.05M; Vol24H $12.17M; 24H -6.60%; V/LP 5.93x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.09M; Vol24H $4.45M; 24H -0.45%; V/LP 4.10x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 83; Tier Early; LP $287.6K; Vol24H $601.0K; 24H -0.45%; V/LP 2.09x; 池数 1; 分项 L13/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 81; Tier Liquid; LP $1.75M; Vol24H $12.82M; 24H +11.37%; V/LP 7.31x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 次观察 | Score 76; Tier Micro; LP $61.1K; Vol24H $396.4K; 24H +2.29%; V/LP 6.49x; 池数 5; 分项 L7/V11/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 76; Tier Liquid; LP $958.1K; Vol24H $200.9K; 24H -4.67%; V/LP 0.21x; 池数 1; 分项 L18/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 66; Tier Early; LP $542.5K; Vol24H $1.78M; 24H +41.95%; V/LP 3.29x; 池数 2; 分项 L16/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 次观察 | Score 64; Tier Early; LP $181.3K; Vol24H $2.74M; 24H +8.26%; V/LP 15.11x; 池数 1; 分项 L12/V17/B17/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 64; Tier Early; LP $448.4K; Vol24H $1.02M; 24H +43.47%; V/LP 2.28x; 池数 2; 分项 L15/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 49; Tier Liquid; LP $930.5K; Vol24H $64.21M; 24H -22.48%; V/LP 69.01x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [79AU](https://dexscreener.com/bsc/0xad8b5dae02a6541130fcfb9002506b80dec2622f) | BSC | [0x23cc...f67C05](https://bscscan.com/token/0x23cc6ec45F08B96ff4354e723368bfA705f67C05) | PVP风险池 | Score 27; Tier Early; LP $708.5K; Vol24H $13.85M; 24H +588.00%; V/LP 19.55x; 池数 1; 分项 L17/V17/B0/Buy12/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 𝕏GIFT | SOL | [FGnzUz...eFpump](https://solscan.io/token/FGnzUzwqULDuZk3WX4CGdKeeZiSwp9kHQKL5HGeFpump) | PVP风险池 | Score 26; Tier Micro; LP $36.2K; Vol24H $3.99M; 24H -63.20%; V/LP 110.04x; 池数 2; 分项 L5/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pondeer](https://dexscreener.com/solana/4btvosm4paw3w5yxdcfqrvhhgkkyni1orgtfn1cpjbxh) | SOL | [5B8qah...hjpump](https://solscan.io/token/5B8qahEJezLtTHPU1Du1AsfAMf4kUVAdaMky7vhjpump) | PVP风险池 | Score 19; Tier Micro; LP $41.6K; Vol24H $3.01M; 24H +266.00%; V/LP 72.50x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FRONT | SOL | [26Rre7...WApump](https://solscan.io/token/26Rre7jT3jUaU29s6oS6QbLSwpbV2ZSZmouZAFWApump) | PVP风险池 | Score 13; Tier Micro; LP $25.0K; Vol24H $2.90M; 24H -41.45%; V/LP 115.88x; 池数 2; 分项 L4/V17/B8/Buy0/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $930.5K; Vol24H $64.21M; 24H -22.48%; V/LP 69.01x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [79AU](https://dexscreener.com/bsc/0xad8b5dae02a6541130fcfb9002506b80dec2622f) | BSC | [0x23cc...f67C05](https://bscscan.com/token/0x23cc6ec45F08B96ff4354e723368bfA705f67C05) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP偏高；年轻币短期暴拉 | Score 27; Tier Early; LP $708.5K; Vol24H $13.85M; 24H +588.00%; V/LP 19.55x; 池数 1; 分项 L17/V17/B0/Buy12/Risk-43 | 只记录热度，不进入主榜 |
| 𝕏GIFT | SOL | [FGnzUz...eFpump](https://solscan.io/token/FGnzUzwqULDuZk3WX4CGdKeeZiSwp9kHQKL5HGeFpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 26; Tier Micro; LP $36.2K; Vol24H $3.99M; 24H -63.20%; V/LP 110.04x; 池数 2; 分项 L5/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [Pondeer](https://dexscreener.com/solana/4btvosm4paw3w5yxdcfqrvhhgkkyni1orgtfn1cpjbxh) | SOL | [5B8qah...hjpump](https://solscan.io/token/5B8qahEJezLtTHPU1Du1AsfAMf4kUVAdaMky7vhjpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 19; Tier Micro; LP $41.6K; Vol24H $3.01M; 24H +266.00%; V/LP 72.50x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| FRONT | SOL | [26Rre7...WApump](https://solscan.io/token/26Rre7jT3jUaU29s6oS6QbLSwpbV2ZSZmouZAFWApump) | 24H未过热但已明显波动；LP未达主观察门槛；24H成交合格；卖出笔数占优；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $25.0K; Vol24H $2.90M; 24H -41.45%; V/LP 115.88x; 池数 2; 分项 L4/V17/B8/Buy0/Risk-40 | 只记录热度，不进入主榜 |
| [SOL](https://dexscreener.com/solana/83s1ifx6usw6ggu2har8pxi9yz9mowh5xemmy6x9kxkk) | SOL | [BUphiK...2kpump](https://solscan.io/token/BUphiKNBKbPgKEfbxpRjWeq4qtsUiTi6GiveTX2kpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $26.3K; Vol24H $4.55M; 24H +207.00%; V/LP 172.77x; 池数 2; 分项 L4/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [WENDU](https://dexscreener.com/solana/difsa6xdswceyxddexgmv9wiplradmvdjggsdhevr834) | SOL | [H7uiPQ...yXpump](https://solscan.io/token/H7uiPQTTq7d8Rhuqw4V6ntroZhakbLCw9PWzuLyXpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 6; Tier Micro; LP $5.6K; Vol24H $1.27M; 24H -98.61%; V/LP 227.90x; 池数 3; 分项 L0/V14/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [TRADER](https://dexscreener.com/solana/5lstgouga7ghhdbgwg1ego2eq839x5yzudqoxxspztwz) | SOL | [BbydPt...2rpump](https://solscan.io/token/BbydPty2qDLNjoeHtWiFjBfibBvBkXK84agHuU2rpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $88.2K; Vol24H $5.71M; 24H +2597.00%; V/LP 64.67x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 76; Tier Liquid; LP $1.11M; Vol24H $1.65M; 24H +2.55%; V/LP 1.49x; 池数 2; 分项 L19/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.16M; Vol24H $16.10M; 24H -5.88%; V/LP 5.10x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $13.42M; Vol24H $6.51M; 24H +11.60%; V/LP 0.49x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CARDS | SOL | [CARDSc...dKxYjp](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.41M; Vol24H $3.67M; 24H -9.12%; V/LP 1.07x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 68; Tier Mature; LP $8.64M; Vol24H $434.8K; 24H +4.25%; V/LP 0.05x; 池数 3; 分项 L20/V11/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 68; Tier Mature; LP $146.27M; Vol24H $194.69M; 24H -2.15%; V/LP 1.33x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/5hbf9jp8k5zdrzp9pokpypfqobse5mgcmw6nqodurgcd) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H波动可控；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 62; Tier Liquid; LP $944.5K; Vol24H $1.44M; 24H +11.27%; V/LP 1.53x; 池数 1; 分项 L18/V15/B17/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CS](https://dexscreener.com/solana/c3hajo5hfxwcgsoxzeqsqzbtfhcdxujb4qna4aqpq6xg) | SOL | [9qwxah...topump](https://solscan.io/token/9qwxahBxcgKyn5X7kZvkN7qxKZg6pkVD8Lo4URtopump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [KINS](https://dexscreener.com/solana/f42tznkpavq1vucrl6ymhc6yqvpt84fwwgzbntv2wb3w) | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TOESCOIN](https://dexscreener.com/solana/ee3zk9fxp9guair2xerefxf4tsexezffuwetrna2pkcv) | SOL | [6ehEcT...HDpump](https://solscan.io/token/6ehEcTMCc85aNF4x9CWx8HuvWGhxQtvKdhKVf2HDpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 6 / Liquid 9 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
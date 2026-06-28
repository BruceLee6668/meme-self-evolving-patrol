# 自我进化轮巡

**本轮时间 UTC：** 2026-06-28T23:07:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 130 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 346 |
| 合并后Token | 130 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 9 |
| 低优先观察 | 2 |
| 多池Token | 10 |
| 多池冲突 | 6 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 6 |
| Liquid层 | 9 |
| Mature层 | 3 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ACT | SOL | [GJAFwW...Unpump](https://solscan.io/token/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | 次观察 | Score 71; Tier Liquid; LP $1.19M; Vol24H $4.69M; 24H +42.81%; V/LP 3.93x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 70; Tier Early; LP $232.5K; Vol24H $746.1K; 24H -28.46%; V/LP 3.21x; 池数 1; 分项 L13/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 68; Tier Liquid; LP $1.28M; Vol24H $31.1K; 24H +0.40%; V/LP 0.02x; 池数 1; 分项 L19/V3/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | PVP风险池 | Score 27; Tier Micro; LP $69.9K; Vol24H $7.33M; 24H +2016.00%; V/LP 104.85x; 池数 6; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| WYNN | SOL | [G9ds9r...32pump](https://solscan.io/token/G9ds9rppyJVZs4ZiRv6jVEq4Tq7kRcXxFgbhz232pump) | PVP风险池 | Score 27; Tier Micro; LP $72.0K; Vol24H $4.16M; 24H +2605.71%; V/LP 57.85x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | PVP风险池 | Score 26; Tier Liquid; LP $1.12M; Vol24H $52.28M; 24H +1273.00%; V/LP 46.63x; 池数 6; 分项 L19/V17/B0/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Hobbes](https://dexscreener.com/solana/55hjyfdtgkp2dmj7azykxop3fgrnw9dyqewwq3sg7qdo) | SOL | [Bqs76K...5npump](https://solscan.io/token/Bqs76KADGDkiwskqdqTu1jaNrpJyzV5ZxpvJrL5npump) | PVP风险池 | Score 26; Tier Micro; LP $56.2K; Vol24H $2.83M; 24H +101.00%; V/LP 50.45x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | PVP风险池 | Score 25; Tier Early; LP $146.1K; Vol24H $5.49M; 24H +125.00%; V/LP 37.58x; 池数 17; 分项 L11/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CLIVE](https://dexscreener.com/solana/b1gflecdjbygddskkqmdp8xz5tticgdw7addvqqsuufe) | SOL | [HEU5mP...u2DoiA](https://solscan.io/token/HEU5mPDm5jCyn4AjQKjvWuvttACKvitgpAdwfmu2DoiA) | PVP风险池 | Score 14; Tier Micro; LP $35.4K; Vol24H $3.18M; 24H +549.00%; V/LP 90.05x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SKULLY](https://dexscreener.com/solana/j9d2q27ofsfebbeorotxjiqvsulkdesfnnvoecrw6zhl) | SOL | [FE9v2Q...mipump](https://solscan.io/token/FE9v2QJfNPmgNf5yGFu4MJvafVrPCtPCDRxeS5mipump) | PVP风险池 | Score 3; Tier Early; LP $107.7K; Vol24H $9.47M; 24H +3987.00%; V/LP 87.87x; 池数 15; 分项 L9/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 81; Tier Liquid; LP $1.71M; Vol24H $13.58M; 24H -13.19%; V/LP 7.92x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 主观察 | Score 80; Tier Early; LP $191.7K; Vol24H $1.42M; 24H +11.41%; V/LP 7.42x; 池数 5; 分项 L12/V15/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ACT | SOL | [GJAFwW...Unpump](https://solscan.io/token/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | 次观察 | Score 71; Tier Liquid; LP $1.18M; Vol24H $4.78M; 24H +39.95%; V/LP 4.04x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 次观察 | Score 70; Tier Early; LP $229.5K; Vol24H $741.1K; 24H -32.63%; V/LP 3.23x; 池数 1; 分项 L13/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 次观察 | Score 68; Tier Liquid; LP $1.28M; Vol24H $31.1K; 24H +0.40%; V/LP 0.02x; 池数 1; 分项 L19/V3/B22/Buy8/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 68; Tier Early; LP $470.8K; Vol24H $4.01M; 24H -6.18%; V/LP 8.53x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Hobbes](https://dexscreener.com/solana/55hjyfdtgkp2dmj7azykxop3fgrnw9dyqewwq3sg7qdo) | SOL | [Bqs76K...5npump](https://solscan.io/token/Bqs76KADGDkiwskqdqTu1jaNrpJyzV5ZxpvJrL5npump) | PVP风险池 | Score 34; Tier Micro; LP $55.7K; Vol24H $2.83M; 24H +51.44%; V/LP 50.79x; 池数 1; 分项 L7/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| WYNN | SOL | [G9ds9r...32pump](https://solscan.io/token/G9ds9rppyJVZs4ZiRv6jVEq4Tq7kRcXxFgbhz232pump) | PVP风险池 | Score 28; Tier Micro; LP $87.7K; Vol24H $4.38M; 24H +3812.62%; V/LP 49.92x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | PVP风险池 | Score 27; Tier Micro; LP $72.9K; Vol24H $7.41M; 24H +2182.00%; V/LP 101.75x; 池数 6; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | PVP风险池 | Score 26; Tier Liquid; LP $1.08M; Vol24H $52.11M; 24H +665.00%; V/LP 48.17x; 池数 5; 分项 L19/V17/B0/Buy8/Risk-42 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | PVP风险池 | Score 24; Tier Early; LP $138.0K; Vol24H $5.37M; 24H +135.00%; V/LP 38.94x; 池数 17; 分项 L10/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SKULLY](https://dexscreener.com/solana/j9d2q27ofsfebbeorotxjiqvsulkdesfnnvoecrw6zhl) | SOL | [FE9v2Q...mipump](https://solscan.io/token/FE9v2QJfNPmgNf5yGFu4MJvafVrPCtPCDRxeS5mipump) | PVP风险池 | Score 17; Tier Micro; LP $8.3K; Vol24H $12.51M; 24H -78.89%; V/LP 1506.60x; 池数 15; 分项 L0/V17/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CUPSEY](https://dexscreener.com/solana/5xkxyzu4udrkq7q1lfyivcdgrwdghzc5urdza8weddkx) | SOL | [BwAU6g...WYpump](https://solscan.io/token/BwAU6gsimrFhJrRcZqKxQJayfnkyyan63WNCJRWYpump) | PVP风险池 | Score 14; Tier Micro; LP $36.9K; Vol24H $5.56M; 24H +591.00%; V/LP 150.51x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CLIVE](https://dexscreener.com/solana/b1gflecdjbygddskkqmdp8xz5tticgdw7addvqqsuufe) | SOL | [HEU5mP...u2DoiA](https://solscan.io/token/HEU5mPDm5jCyn4AjQKjvWuvttACKvitgpAdwfmu2DoiA) | PVP风险池 | Score 13; Tier Micro; LP $30.0K; Vol24H $3.22M; 24H +363.00%; V/LP 107.47x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 成熟池观察 | Score 78; Tier Liquid; LP $1.06M; Vol24H $698.4K; 24H -1.67%; V/LP 0.66x; 池数 2; 分项 L19/V13/B22/Buy12/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [Hobbes](https://dexscreener.com/solana/55hjyfdtgkp2dmj7azykxop3fgrnw9dyqewwq3sg7qdo) | SOL | [Bqs76K...5npump](https://solscan.io/token/Bqs76KADGDkiwskqdqTu1jaNrpJyzV5ZxpvJrL5npump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 34; Tier Micro; LP $55.7K; Vol24H $2.83M; 24H +51.44%; V/LP 50.79x; 池数 1; 分项 L7/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| WYNN | SOL | [G9ds9r...32pump](https://solscan.io/token/G9ds9rppyJVZs4ZiRv6jVEq4Tq7kRcXxFgbhz232pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $87.7K; Vol24H $4.38M; 24H +3812.62%; V/LP 49.92x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $72.9K; Vol24H $7.41M; 24H +2182.00%; V/LP 101.75x; 池数 6; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 26; Tier Liquid; LP $1.08M; Vol24H $52.11M; 24H +665.00%; V/LP 48.17x; 池数 5; 分项 L19/V17/B0/Buy8/Risk-42 | 只记录热度，不进入主榜 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 24; Tier Early; LP $138.0K; Vol24H $5.37M; 24H +135.00%; V/LP 38.94x; 池数 17; 分项 L10/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [SKULLY](https://dexscreener.com/solana/j9d2q27ofsfebbeorotxjiqvsulkdesfnnvoecrw6zhl) | SOL | [FE9v2Q...mipump](https://solscan.io/token/FE9v2QJfNPmgNf5yGFu4MJvafVrPCtPCDRxeS5mipump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 17; Tier Micro; LP $8.3K; Vol24H $12.51M; 24H -78.89%; V/LP 1506.60x; 池数 15; 分项 L0/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [CUPSEY](https://dexscreener.com/solana/5xkxyzu4udrkq7q1lfyivcdgrwdghzc5urdza8weddkx) | SOL | [BwAU6g...WYpump](https://solscan.io/token/BwAU6gsimrFhJrRcZqKxQJayfnkyyan63WNCJRWYpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $36.9K; Vol24H $5.56M; 24H +591.00%; V/LP 150.51x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [CLIVE](https://dexscreener.com/solana/b1gflecdjbygddskkqmdp8xz5tticgdw7addvqqsuufe) | SOL | [HEU5mP...u2DoiA](https://solscan.io/token/HEU5mPDm5jCyn4AjQKjvWuvttACKvitgpAdwfmu2DoiA) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $30.0K; Vol24H $3.22M; 24H +363.00%; V/LP 107.47x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $1.06M; Vol24H $698.4K; 24H -1.67%; V/LP 0.66x; 池数 2; 分项 L19/V13/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BAS | BSC | [0x0f0d...db4e37](https://bscscan.com/token/0x0f0df6cb17ee5e883eddfef9153fc6036bdb4e37) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $2.52M; Vol24H $19.85M; 24H +3.85%; V/LP 7.87x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SLX | BSC | [0x02bc...4bc54d](https://bscscan.com/token/0x02bcc4c181b83a8c0a342bc003389cbecb4bc54d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.24M; Vol24H $5.13M; 24H +6.86%; V/LP 4.12x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $156.03M; Vol24H $82.49M; 24H +1.00%; V/LP 0.53x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $2.47M; Vol24H $5.80M; 24H +16.24%; V/LP 2.35x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Early; LP $183.3K; Vol24H $1.32M; 24H -2.31%; V/LP 7.20x; 池数 1; 分项 L12/V15/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTW | BSC | [0x4440...35acaa](https://bscscan.com/token/0x444045b0ee1ee319a660a5e3d604ca0ffa35acaa) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 68; Tier Liquid; LP $1.25M; Vol24H $3.40M; 24H -15.26%; V/LP 2.73x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 66; Tier Mature; LP $67.47M; Vol24H $149.32M; 24H +12.47%; V/LP 2.21x; 池数 4; 分项 L20/V17/B17/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| ACT | SOL | [GJAFwW...Unpump](https://solscan.io/token/GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | [3XJb1B...Mirise](https://solscan.io/token/3XJb1BtqeXNNAeAAfCzqF5ReWjok11cnStJdM1Mirise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PUMP](https://dexscreener.com/solana/4c8kctyztmtzwv83y5actpvt2axyyu2t9zhhdotfgnno) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [Hobbes](https://dexscreener.com/solana/55hjyfdtgkp2dmj7azykxop3fgrnw9dyqewwq3sg7qdo) | SOL | [Bqs76K...5npump](https://solscan.io/token/Bqs76KADGDkiwskqdqTu1jaNrpJyzV5ZxpvJrL5npump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| WYNN | SOL | [G9ds9r...32pump](https://solscan.io/token/G9ds9rppyJVZs4ZiRv6jVEq4Tq7kRcXxFgbhz232pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [🐂🀄️](https://dexscreener.com/solana/c2x7vgnyeja4tshs9drbvjsek7z3h2kprowm7yqfrspq) | SOL | [EPD8jj...yhUnBh](https://solscan.io/token/EPD8jj7bVhNh3o7Wx1XZ39aaacSki8p2ABaN61yhUnBh) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | [SPCXwB...a53N69](https://solscan.io/token/SPCXwBHVrKpRqMRawL3NNvt1sXP2Yf3edwRbta53N69) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 9 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 6 / Liquid 9 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 331} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
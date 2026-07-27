# 自我进化轮巡

**本轮时间 UTC：** 2026-07-27T06:23:37Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 110 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 253 |
| 合并后Token | 110 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 7 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 10 |
| Early层 | 5 |
| Liquid层 | 8 |
| Mature层 | 2 |
| 需要链上确认 | 12 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 782，刷新时间 2026-07-27T02:07:24Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 0 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 73; Tier Early; LP $345.2K; Vol24H $1.70M; 24H +12.11%; V/LP 4.93x; 池数 2; 分项 L14/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 70; Tier Liquid; LP $1.03M; Vol24H $4.76M; 24H -43.23%; V/LP 4.64x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 次观察 | Score 68; Tier Liquid; LP $2.70M; Vol24H $2.23M; 24H +26.19%; V/LP 0.82x; 池数 2; 分项 L20/V16/B8/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 33; Tier Early; LP $297.9K; Vol24H $30.03M; 24H +22699.00%; V/LP 100.79x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Kittens | SOL | [C1rBBX...KGpump](https://solscan.io/token/C1rBBXwHPRHeBDhbwSrdGy9EMR9E1AntVg6dabKGpump) | PVP风险池 | Score 26; Tier Micro; LP $51.2K; Vol24H $4.26M; 24H +993.29%; V/LP 83.28x; 池数 2; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TRUMP2028](https://dexscreener.com/solana/gdn39onzalyngfbsyn6df4sautkpfwgynijinyodqv6w) | SOL | [2d2GZd...TQpump](https://solscan.io/token/2d2GZdehy2YGrj1MJ3y3yhXjficMa2J3GtncxkTQpump) | PVP风险池 | Score 21; Tier Micro; LP $66.6K; Vol24H $2.48M; 24H +122.00%; V/LP 37.25x; 池数 1; 分项 L8/V16/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [POTUS](https://dexscreener.com/solana/c87z1bfme742nd5pblg5vt6py4suadap2jrijbk2cxse) | SOL | [HbfRgc...LMVNJb](https://solscan.io/token/HbfRgcHXskbsXwucVAsF41bA2cvAPTzAyWSSv8LMVNJb) | PVP风险池 | Score 18; Tier Micro; LP $17.1K; Vol24H $2.20M; 24H +54.48%; V/LP 128.66x; 池数 5; 分项 L2/V16/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 16; Tier Micro; LP $81.9K; Vol24H $266.37M; 24H -99.98%; V/LP 3251.48x; 池数 1; 分项 L8/V17/B0/Buy12/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | PVP风险池 | Score 12; Tier Micro; LP $10.5K; Vol24H $2.26M; 24H -97.61%; V/LP 215.85x; 池数 1; 分项 L0/V16/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SalaryCat](https://dexscreener.com/solana/a9j6qb8vue8rxxcql9t58j2k63cdpaf7knvcffc7bx9b) | SOL | [GiRrLz...n1pump](https://solscan.io/token/GiRrLzdan5Gz31ngH4zgxk6ybYaryNVCSLdAJyn1pump) | PVP风险池 | Score 9; Tier Micro; LP $35.1K; Vol24H $4.51M; 24H +453.00%; V/LP 128.59x; 池数 2; 分项 L5/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 80; Tier Liquid; LP $2.70M; Vol24H $2.38M; 24H +13.62%; V/LP 0.88x; 池数 1; 分项 L20/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 次观察 | Score 73; Tier Early; LP $345.1K; Vol24H $1.60M; 24H +17.88%; V/LP 4.65x; 池数 1; 分项 L14/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 次观察 | Score 70; Tier Liquid; LP $989.7K; Vol24H $4.14M; 24H -33.01%; V/LP 4.18x; 池数 1; 分项 L18/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Miu](https://dexscreener.com/solana/hqvzp7hxhcovjysnp6fofy5adcfigj1cdwt8gppapnbv) | SOL | [7LNFZc...wvpump](https://solscan.io/token/7LNFZcNigZay5U9e2sq6n2Z4iM8BC2Dd53L14pwvpump) | 次观察 | Score 64; Tier Micro; LP $71.9K; Vol24H $527.7K; 24H -29.59%; V/LP 7.34x; 池数 1; 分项 L8/V12/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 32; Tier Early; LP $289.9K; Vol24H $34.09M; 24H +20007.68%; V/LP 117.59x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Kittens](https://dexscreener.com/solana/aphyqrgq68ycb2fz5s9dafqvthfkhtcvpwb6nvwmx1p5) | SOL | [C1rBBX...KGpump](https://solscan.io/token/C1rBBXwHPRHeBDhbwSrdGy9EMR9E1AntVg6dabKGpump) | PVP风险池 | Score 15; Tier Micro; LP $40.6K; Vol24H $4.57M; 24H +575.00%; V/LP 112.57x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 富贵 | BSC | [0x198d...3b4444](https://bscscan.com/token/0x198dba421a7db566a90da5de7901abe3443b4444) | PVP风险池 | Score 13; Tier Micro; LP $31.0K; Vol24H $2.15M; 24H +585.87%; V/LP 69.43x; 池数 30; 分项 L5/V16/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | PVP风险池 | Score 11; Tier Micro; LP $10.3K; Vol24H $1.64M; 24H -96.61%; V/LP 159.12x; 池数 1; 分项 L0/V15/B0/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| HAPPYCAT | SOL | [9AX92x...m2pump](https://solscan.io/token/9AX92xMkM5Z26nQzmJfb5wRZsLSs4n4fTJxMNom2pump) | PVP风险池 | Score 9; Tier Micro; LP $4.0K; Vol24H $4.05M; 24H -97.56%; V/LP 1011.10x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| SalaryCat | SOL | [GiRrLz...n1pump](https://solscan.io/token/GiRrLzdan5Gz31ngH4zgxk6ybYaryNVCSLdAJyn1pump) | PVP风险池 | Score 8; Tier Micro; LP $29.5K; Vol24H $4.58M; 24H +279.46%; V/LP 155.60x; 池数 2; 分项 L4/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Nongwan](https://dexscreener.com/solana/j5zuquvwjhtrtgixefel3bpnvzcw5rfb12sr55tc715l) | SOL | [Fvvj98...twpump](https://solscan.io/token/Fvvj98QtaA3RjVgeQn79NokiMaLgBRje1Q9bXetwpump) | PVP风险池 | Score 3; Tier Micro; LP $90.7K; Vol24H $6.45M; 24H +3366.00%; V/LP 71.16x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MAGAVERSE](https://dexscreener.com/solana/9daltnvu5scn1f21fjlkm5kmnrtdyr7rzmqctjuekewx) | SOL | [AdMJoQ...ZKyK5R](https://solscan.io/token/AdMJoQiounJbXVZDqtVdjCRcp2NVtovw7426ENZKyK5R) | PVP风险池 | Score 0; Tier Micro; LP $24.1K; Vol24H $1.58M; 24H +199.00%; V/LP 65.51x; 池数 11; 分项 L4/V15/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 成熟池观察 | Score 79; Tier Mature; LP $51.34M; Vol24H $3.41M; 24H -0.49%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 成熟池观察 | Score 74; Tier Mature; LP $10.26M; Vol24H $3.93M; 24H +5.03%; V/LP 0.38x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 成熟池观察 | Score 74; Tier Liquid; LP $1.41M; Vol24H $5.12M; 24H +2.19%; V/LP 3.64x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $289.9K; Vol24H $34.09M; 24H +20007.68%; V/LP 117.59x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Kittens](https://dexscreener.com/solana/aphyqrgq68ycb2fz5s9dafqvthfkhtcvpwb6nvwmx1p5) | SOL | [C1rBBX...KGpump](https://solscan.io/token/C1rBBXwHPRHeBDhbwSrdGy9EMR9E1AntVg6dabKGpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $40.6K; Vol24H $4.57M; 24H +575.00%; V/LP 112.57x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| 富贵 | BSC | [0x198d...3b4444](https://bscscan.com/token/0x198dba421a7db566a90da5de7901abe3443b4444) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $31.0K; Vol24H $2.15M; 24H +585.87%; V/LP 69.43x; 池数 30; 分项 L5/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $10.3K; Vol24H $1.64M; 24H -96.61%; V/LP 159.12x; 池数 1; 分项 L0/V15/B0/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| HAPPYCAT | SOL | [9AX92x...m2pump](https://solscan.io/token/9AX92xMkM5Z26nQzmJfb5wRZsLSs4n4fTJxMNom2pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $4.0K; Vol24H $4.05M; 24H -97.56%; V/LP 1011.10x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| SalaryCat | SOL | [GiRrLz...n1pump](https://solscan.io/token/GiRrLzdan5Gz31ngH4zgxk6ybYaryNVCSLdAJyn1pump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $29.5K; Vol24H $4.58M; 24H +279.46%; V/LP 155.60x; 池数 2; 分项 L4/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [Nongwan](https://dexscreener.com/solana/j5zuquvwjhtrtgixefel3bpnvzcw5rfb12sr55tc715l) | SOL | [Fvvj98...twpump](https://solscan.io/token/Fvvj98QtaA3RjVgeQn79NokiMaLgBRje1Q9bXetwpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $90.7K; Vol24H $6.45M; 24H +3366.00%; V/LP 71.16x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [MAGAVERSE](https://dexscreener.com/solana/9daltnvu5scn1f21fjlkm5kmnrtdyr7rzmqctjuekewx) | SOL | [AdMJoQ...ZKyK5R](https://solscan.io/token/AdMJoQiounJbXVZDqtVdjCRcp2NVtovw7426ENZKyK5R) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $24.1K; Vol24H $1.58M; 24H +199.00%; V/LP 65.51x; 池数 11; 分项 L4/V15/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.34M; Vol24H $3.41M; 24H -0.49%; V/LP 0.07x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $10.26M; Vol24H $3.93M; 24H +5.03%; V/LP 0.38x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $1.41M; Vol24H $5.12M; 24H +2.19%; V/LP 3.64x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $4.01M; Vol24H $10.83M; 24H +13.80%; V/LP 2.70x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 67; Tier Liquid; LP $994.1K; Vol24H $4.90M; 24H +12.72%; V/LP 4.93x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 66; Tier Liquid; LP $1.97M; Vol24H $1.24M; 24H -8.24%; V/LP 0.63x; 池数 2; 分项 L20/V14/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| ESPORTS | BSC | [0xf39e...508e48](https://bscscan.com/token/0xf39e4b21c84e737df08e2c3b32541d856f508e48) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Miu](https://dexscreener.com/solana/hqvzp7hxhcovjysnp6fofy5adcfigj1cdwt8gppapnbv) | SOL | [7LNFZc...wvpump](https://solscan.io/token/7LNFZcNigZay5U9e2sq6n2Z4iM8BC2Dd53L14pwvpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Kittens](https://dexscreener.com/solana/aphyqrgq68ycb2fz5s9dafqvthfkhtcvpwb6nvwmx1p5) | SOL | [C1rBBX...KGpump](https://solscan.io/token/C1rBBXwHPRHeBDhbwSrdGy9EMR9E1AntVg6dabKGpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| 富贵 | BSC | [0x198d...3b4444](https://bscscan.com/token/0x198dba421a7db566a90da5de7901abe3443b4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| Cupsey2028 | SOL | [7LRpii...YWpump](https://solscan.io/token/7LRpiiDzNVRdxfatA5T1iGvQmPUP46pMkpfGnqYWpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| HAPPYCAT | SOL | [9AX92x...m2pump](https://solscan.io/token/9AX92xMkM5Z26nQzmJfb5wRZsLSs4n4fTJxMNom2pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| SalaryCat | SOL | [GiRrLz...n1pump](https://solscan.io/token/GiRrLzdan5Gz31ngH4zgxk6ybYaryNVCSLdAJyn1pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [TROLL](https://dexscreener.com/solana/4w2cysotx6czaugmmwg13hdpy4qemg2czekyeqyk9ama) | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 10 / Early 5 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
# 自我进化轮巡

**本轮时间 UTC：** 2026-07-29T21:55:03Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 219 |
| 合并后Token | 119 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 7 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 9 |
| Early层 | 6 |
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
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 74; Tier Early; LP $143.2K; Vol24H $231.5K; 24H +4.07%; V/LP 1.62x; 池数 1; 分项 L11/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.44M; Vol24H $1.5K; 24H +0.16%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 66; Tier Micro; LP $76.7K; Vol24H $239.0K; 24H -0.02%; V/LP 3.12x; 池数 1; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | PVP风险池 | Score 51; Tier Liquid; LP $1.36M; Vol24H $43.50M; 24H -11.46%; V/LP 31.98x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Fauci | SOL | [3VFnDo...Zepump](https://solscan.io/token/3VFnDoACa991DYe987w354sbvmhqjjzC4Z31SoZepump) | PVP风险池 | Score 29; Tier Early; LP $132.5K; Vol24H $9.28M; 24H +6472.98%; V/LP 70.05x; 池数 4; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $111.8K; Vol24H $5.23M; 24H -36.27%; V/LP 46.76x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Gnomes](https://dexscreener.com/solana/apyk52fhc7wkapkucgvl2qxchaespuhtsog8vsngyrpr) | SOL | [6Quog2...CZpump](https://solscan.io/token/6Quog29HQ5tA5BdnCv3FWpW8WEpdxCsxEpt2TGCZpump) | PVP风险池 | Score 20; Tier Micro; LP $51.6K; Vol24H $2.33M; 24H +91.32%; V/LP 45.07x; 池数 1; 分项 L7/V16/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FRANK](https://dexscreener.com/solana/bm7uqqeanv8xnlbci1xkqipzxugztc4vqfsqvc3zoomk) | SOL | [3aqXuw...phpump](https://solscan.io/token/3aqXuwp6HuVXs9vdD9Gpg4dzJaUx443RjK7GXzphpump) | PVP风险池 | Score 15; Tier Micro; LP $42.6K; Vol24H $5.54M; 24H -93.58%; V/LP 130.05x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DOGCAT | SOL | [Cbj8wD...L6pump](https://solscan.io/token/Cbj8wDvAvbRw8McNPd7ZhUrcw8NSvsyfR4db6pL6pump) | PVP风险池 | Score 15; Tier Micro; LP $42.5K; Vol24H $5.50M; 24H +229.85%; V/LP 129.34x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DEER](https://dexscreener.com/solana/acbgxfs98ovvd5cmqqfgueropfp1bjexajtmn9rz65vf) | SOL | [5exGpv...Hxpump](https://solscan.io/token/5exGpveFdn2Dcr9o7Pyj35DoYj588rEfkNLcZqHxpump) | PVP风险池 | Score 13; Tier Micro; LP $24.9K; Vol24H $3.15M; 24H +229.00%; V/LP 126.36x; 池数 1; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 次观察 | Score 70; Tier Liquid; LP $1.44M; Vol24H $1.5K; 24H +0.52%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 次观察 | Score 68; Tier Early; LP $137.8K; Vol24H $209.2K; 24H -18.35%; V/LP 1.52x; 池数 1; 分项 L10/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 次观察 | Score 66; Tier Micro; LP $76.8K; Vol24H $235.1K; 24H -0.08%; V/LP 3.06x; 池数 1; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | PVP风险池 | Score 51; Tier Liquid; LP $1.39M; Vol24H $42.68M; 24H -9.84%; V/LP 30.74x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Fauci](https://dexscreener.com/solana/2jf324deswftkbfvtzwby8tgedhhncjepai82smx5pfr) | SOL | [3VFnDo...Zepump](https://solscan.io/token/3VFnDoACa991DYe987w354sbvmhqjjzC4Z31SoZepump) | PVP风险池 | Score 28; Tier Micro; LP $96.3K; Vol24H $11.13M; 24H +3377.00%; V/LP 115.62x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 20; Tier Early; LP $114.6K; Vol24H $5.00M; 24H -25.24%; V/LP 43.63x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [FRANK](https://dexscreener.com/solana/bm7uqqeanv8xnlbci1xkqipzxugztc4vqfsqvc3zoomk) | SOL | [3aqXuw...phpump](https://solscan.io/token/3aqXuwp6HuVXs9vdD9Gpg4dzJaUx443RjK7GXzphpump) | PVP风险池 | Score 15; Tier Micro; LP $45.5K; Vol24H $4.56M; 24H -87.59%; V/LP 100.43x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MarketCat | SOL | [G8Modk...LBpump](https://solscan.io/token/G8ModkdDYTuUWLTVR4FAV8orFyZKXccZPhtUvvLBpump) | PVP风险池 | Score 12; Tier Micro; LP $19.3K; Vol24H $3.36M; 24H +86.91%; V/LP 174.30x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [DEER](https://dexscreener.com/solana/acbgxfs98ovvd5cmqqfgueropfp1bjexajtmn9rz65vf) | SOL | [5exGpv...Hxpump](https://solscan.io/token/5exGpveFdn2Dcr9o7Pyj35DoYj588rEfkNLcZqHxpump) | PVP风险池 | Score 12; Tier Micro; LP $23.4K; Vol24H $3.22M; 24H +189.00%; V/LP 137.30x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| DOGCAT | SOL | [Cbj8wD...L6pump](https://solscan.io/token/Cbj8wDvAvbRw8McNPd7ZhUrcw8NSvsyfR4db6pL6pump) | PVP风险池 | Score 9; Tier Micro; LP $7.6K; Vol24H $5.62M; 24H -83.06%; V/LP 742.20x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Fraudci](https://dexscreener.com/solana/67fxdnxif9xczfunzc2uvarne2h1q2ir8nztrfuhxkvv) | SOL | [3DrBHM...RPpump](https://solscan.io/token/3DrBHMJ1rnWp7mMRNmNbWbp4zNiHkM483GqXSzRPpump) | PVP风险池 | Score 0; Tier Micro; LP $45.5K; Vol24H $4.33M; 24H +831.00%; V/LP 95.21x; 池数 12; 分项 L6/V17/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 78; Tier Liquid; LP $1.90M; Vol24H $1.85M; 24H +2.74%; V/LP 0.98x; 池数 2; 分项 L20/V16/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 成熟池观察 | Score 73; Tier Mature; LP $10.00M; Vol24H $1.89M; 24H -1.15%; V/LP 0.19x; 池数 5; 分项 L20/V16/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 成熟池观察 | Score 72; Tier Liquid; LP $1.00M; Vol24H $7.53M; 24H -5.83%; V/LP 7.50x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 成熟池观察 | Score 69; Tier Mature; LP $19.49M; Vol24H $94.6K; 24H -4.91%; V/LP 0.00x; 池数 1; 分项 L20/V7/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.39M; Vol24H $42.68M; 24H -9.84%; V/LP 30.74x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [Fauci](https://dexscreener.com/solana/2jf324deswftkbfvtzwby8tgedhhncjepai82smx5pfr) | SOL | [3VFnDo...Zepump](https://solscan.io/token/3VFnDoACa991DYe987w354sbvmhqjjzC4Z31SoZepump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $96.3K; Vol24H $11.13M; 24H +3377.00%; V/LP 115.62x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 20; Tier Early; LP $114.6K; Vol24H $5.00M; 24H -25.24%; V/LP 43.63x; 池数 1; 分项 L10/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [FRANK](https://dexscreener.com/solana/bm7uqqeanv8xnlbci1xkqipzxugztc4vqfsqvc3zoomk) | SOL | [3aqXuw...phpump](https://solscan.io/token/3aqXuwp6HuVXs9vdD9Gpg4dzJaUx443RjK7GXzphpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $45.5K; Vol24H $4.56M; 24H -87.59%; V/LP 100.43x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| MarketCat | SOL | [G8Modk...LBpump](https://solscan.io/token/G8ModkdDYTuUWLTVR4FAV8orFyZKXccZPhtUvvLBpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $19.3K; Vol24H $3.36M; 24H +86.91%; V/LP 174.30x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [DEER](https://dexscreener.com/solana/acbgxfs98ovvd5cmqqfgueropfp1bjexajtmn9rz65vf) | SOL | [5exGpv...Hxpump](https://solscan.io/token/5exGpveFdn2Dcr9o7Pyj35DoYj588rEfkNLcZqHxpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 12; Tier Micro; LP $23.4K; Vol24H $3.22M; 24H +189.00%; V/LP 137.30x; 池数 1; 分项 L3/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| DOGCAT | SOL | [Cbj8wD...L6pump](https://solscan.io/token/Cbj8wDvAvbRw8McNPd7ZhUrcw8NSvsyfR4db6pL6pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $7.6K; Vol24H $5.62M; 24H -83.06%; V/LP 742.20x; 池数 1; 分项 L0/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [Fraudci](https://dexscreener.com/solana/67fxdnxif9xczfunzc2uvarne2h1q2ir8nztrfuhxkvv) | SOL | [3DrBHM...RPpump](https://solscan.io/token/3DrBHMJ1rnWp7mMRNmNbWbp4zNiHkM483GqXSzRPpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $45.5K; Vol24H $4.33M; 24H +831.00%; V/LP 95.21x; 池数 12; 分项 L6/V17/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 78; Tier Liquid; LP $1.90M; Vol24H $1.85M; 24H +2.74%; V/LP 0.98x; 池数 2; 分项 L20/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限 | Score 73; Tier Mature; LP $10.00M; Vol24H $1.89M; 24H -1.15%; V/LP 0.19x; 池数 5; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 72; Tier Liquid; LP $1.00M; Vol24H $7.53M; 24H -5.83%; V/LP 7.50x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 69; Tier Mature; LP $19.49M; Vol24H $94.6K; 24H -4.91%; V/LP 0.00x; 池数 1; 分项 L20/V7/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| Beat | BSC | [0xcf32...8a3e36](https://bscscan.com/token/0xcf3232b85b43bca90e51d38cc06cc8bb8c8a3e36) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.39M; Vol24H $22.54M; 24H +15.04%; V/LP 6.65x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $1.45M; Vol24H $3.65M; 24H +9.54%; V/LP 2.52x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| COSM | BSC | [0x0d6a...40f6dc](https://bscscan.com/token/0x0d6ae45c96ec4df860300087462266e19140f6dc) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 59; Tier Early; LP $407.1K; Vol24H $648.5K; 24H -14.47%; V/LP 1.59x; 池数 1; 分项 L15/V12/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | [58smR4...3vrise](https://solscan.io/token/58smR4GCZBxXfUUiX6KZ4JXkK6jmX42vjatWgA3vrise) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| febu | SOL | [4ko5tS...L6pump](https://solscan.io/token/4ko5tSr5o3H4v1sFtjTSd9MPUW7yx5AFCpkNPoL6pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Staccana](https://dexscreener.com/solana/2higkrf25q9wmcyfgyk96aaufvv5zucfdafhhduvetcq) | SOL | [73edX6...i1pump](https://solscan.io/token/73edX6xoGY4v5y2hzuKdrUbJXLntqgmo74au1Ki1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| ON | BSC | [0x0e4f...051d48](https://bscscan.com/token/0x0e4f6209ed984b21edea43ace6e09559ed051d48) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Fauci](https://dexscreener.com/solana/2jf324deswftkbfvtzwby8tgedhhncjepai82smx5pfr) | SOL | [3VFnDo...Zepump](https://solscan.io/token/3VFnDoACa991DYe987w354sbvmhqjjzC4Z31SoZepump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [FRANK](https://dexscreener.com/solana/bm7uqqeanv8xnlbci1xkqipzxugztc4vqfsqvc3zoomk) | SOL | [3aqXuw...phpump](https://solscan.io/token/3aqXuwp6HuVXs9vdD9Gpg4dzJaUx443RjK7GXzphpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| MarketCat | SOL | [G8Modk...LBpump](https://solscan.io/token/G8ModkdDYTuUWLTVR4FAV8orFyZKXccZPhtUvvLBpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [DEER](https://dexscreener.com/solana/acbgxfs98ovvd5cmqqfgueropfp1bjexajtmn9rz65vf) | SOL | [5exGpv...Hxpump](https://solscan.io/token/5exGpveFdn2Dcr9o7Pyj35DoYj588rEfkNLcZqHxpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| - | - | - | 本轮无钱包行为样本 | - | 0 | - |

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
| 主观察候选 | 0 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 9 / Early 6 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
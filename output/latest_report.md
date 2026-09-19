# 自我进化轮巡

**本轮时间 UTC：** 2026-09-19T00:53:14Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 133 个合并Token中筛出 1 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 209 |
| 合并后Token | 133 |
| 输出候选 | 25 |
| 主观察 | 1 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 7 |
| 多池Token | 6 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 10 |
| Liquid层 | 8 |
| Mature层 | 2 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 1 个，BSC Transfer样本 1 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| GSTOCK | BSC | [0xcafd...3f9e20](https://bscscan.com/token/0xcafdbce93477261db8250e42bdae6e66733f9e20) | 主观察 | Score 86; Tier Early; LP $563.2K; Vol24H $3.67M; 24H -21.86%; V/LP 6.52x; 池数 1; 分项 L16/V17/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.25M; Vol24H $1.42M; 24H +4.79%; V/LP 0.33x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 73; Tier Early; LP $395.7K; Vol24H $586.8K; 24H +5.74%; V/LP 1.48x; 池数 1; 分项 L15/V12/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 71; Tier Liquid; LP $1.25M; Vol24H $147.5K; 24H +19.19%; V/LP 0.12x; 池数 1; 分项 L19/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | PVP风险池 | Score 56; Tier Liquid; LP $1.77M; Vol24H $61.77M; 24H +2.00%; V/LP 34.99x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 53; Tier Early; LP $529.6K; Vol24H $157.05M; 24H -15.24%; V/LP 296.52x; 池数 1; 分项 L16/V17/B17/Buy12/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| B13B | BSC | [0x4902...eeec3f](https://bscscan.com/token/0x4902c5ebc598265ed2212b559b042de8a5eeec3f) | PVP风险池 | Score 51; Tier Liquid; LP $1.63M; Vol24H $47.22M; 24H +11.89%; V/LP 28.94x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MCAT | SOL | [241aTY...tnmoon](https://solscan.io/token/241aTYhVXZ4WBVSFpfY37RqoCGBQ73KiRFAKvTtnmoon) | PVP风险池 | Score 37; Tier Early; LP $125.6K; Vol24H $7.30M; 24H -78.08%; V/LP 58.14x; 池数 1; 分项 L10/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Tilcayo | SOL | [AyYNfP...s2thto](https://solscan.io/token/AyYNfPtftg2zDP4ZbgcoQMggQtwLh4zpfVVmUJs2thto) | PVP风险池 | Score 36; Tier Micro; LP $88.8K; Vol24H $7.17M; 24H -69.13%; V/LP 80.79x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MYX | BSC | [0xd825...c63e16](https://bscscan.com/token/0xd82544bf0dfe8385ef8fa34d67e6e4940cc63e16) | PVP风险池 | Score 35; Tier Early; LP $269.1K; Vol24H $7.12M; 24H +27.65%; V/LP 26.44x; 池数 1; 分项 L13/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.25M; Vol24H $1.43M; 24H +3.94%; V/LP 0.34x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| GSTOCK | BSC | [0xcafd...3f9e20](https://bscscan.com/token/0xcafdbce93477261db8250e42bdae6e66733f9e20) | 次观察 | Score 73; Tier Early; LP $520.5K; Vol24H $3.09M; 24H -50.58%; V/LP 5.94x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 72; Tier Early; LP $376.9K; Vol24H $542.4K; 24H -3.17%; V/LP 1.44x; 池数 1; 分项 L14/V12/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 71; Tier Liquid; LP $1.22M; Vol24H $159.8K; 24H +15.37%; V/LP 0.13x; 池数 1; 分项 L19/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 70; Tier Micro; LP $88.2K; Vol24H $128.6K; 24H +17.22%; V/LP 1.46x; 池数 1; 分项 L9/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 58; Tier Early; LP $503.2K; Vol24H $157.04M; 24H -7.82%; V/LP 312.08x; 池数 1; 分项 L16/V17/B22/Buy12/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | PVP风险池 | Score 56; Tier Liquid; LP $1.76M; Vol24H $64.16M; 24H +5.28%; V/LP 36.42x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| B13B | BSC | [0x4902...eeec3f](https://bscscan.com/token/0x4902c5ebc598265ed2212b559b042de8a5eeec3f) | PVP风险池 | Score 51; Tier Liquid; LP $1.67M; Vol24H $46.61M; 24H +14.52%; V/LP 27.99x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | PVP风险池 | Score 45; Tier Liquid; LP $895.7K; Vol24H $18.71M; 24H +45.97%; V/LP 20.89x; 池数 2; 分项 L18/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Tilcayo | SOL | [AyYNfP...s2thto](https://solscan.io/token/AyYNfPtftg2zDP4ZbgcoQMggQtwLh4zpfVVmUJs2thto) | PVP风险池 | Score 36; Tier Micro; LP $98.0K; Vol24H $6.50M; 24H -69.33%; V/LP 66.37x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| MYX | BSC | [0xd825...c63e16](https://bscscan.com/token/0xd82544bf0dfe8385ef8fa34d67e6e4940cc63e16) | PVP风险池 | Score 35; Tier Early; LP $270.8K; Vol24H $7.25M; 24H +26.56%; V/LP 26.78x; 池数 1; 分项 L13/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TIGRINO | SOL | [91ryaC...Lgpump](https://solscan.io/token/91ryaCo5yGpYZM3bs6GUPs97VWJQj7RozBmqPULgpump) | PVP风险池 | Score 31; Tier Early; LP $223.1K; Vol24H $12.82M; 24H +9131.25%; V/LP 57.47x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 23; Tier Early; LP $128.2K; Vol24H $139.78M; 24H +14.53%; V/LP 1090.75x; 池数 1; 分项 L10/V17/B17/Buy0/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PUMP](https://dexscreener.com/solana/2uf4xh61rdwxng9woyxsvqp7zua6klfpb3nvnrqeoisd) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 成熟池观察 | Score 79; Tier Mature; LP $22.32M; Vol24H $7.78M; 24H +4.80%; V/LP 0.35x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 成熟池观察 | Score 79; Tier Mature; LP $6.80M; Vol24H $7.54M; 24H +2.40%; V/LP 1.11x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 58; Tier Early; LP $503.2K; Vol24H $157.04M; 24H -7.82%; V/LP 312.08x; 池数 1; 分项 L16/V17/B22/Buy12/Risk-33 | 只记录热度，不进入主榜 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 56; Tier Liquid; LP $1.76M; Vol24H $64.16M; 24H +5.28%; V/LP 36.42x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| B13B | BSC | [0x4902...eeec3f](https://bscscan.com/token/0x4902c5ebc598265ed2212b559b042de8a5eeec3f) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Liquid; LP $1.67M; Vol24H $46.61M; 24H +14.52%; V/LP 27.99x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Liquid; LP $895.7K; Vol24H $18.71M; 24H +45.97%; V/LP 20.89x; 池数 2; 分项 L18/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Tilcayo | SOL | [AyYNfP...s2thto](https://solscan.io/token/AyYNfPtftg2zDP4ZbgcoQMggQtwLh4zpfVVmUJs2thto) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $98.0K; Vol24H $6.50M; 24H -69.33%; V/LP 66.37x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| MYX | BSC | [0xd825...c63e16](https://bscscan.com/token/0xd82544bf0dfe8385ef8fa34d67e6e4940cc63e16) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 35; Tier Early; LP $270.8K; Vol24H $7.25M; 24H +26.56%; V/LP 26.78x; 池数 1; 分项 L13/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| TIGRINO | SOL | [91ryaC...Lgpump](https://solscan.io/token/91ryaCo5yGpYZM3bs6GUPs97VWJQj7RozBmqPULgpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $223.1K; Vol24H $12.82M; 24H +9131.25%; V/LP 57.47x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H波动可控；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 23; Tier Early; LP $128.2K; Vol24H $139.78M; 24H +14.53%; V/LP 1090.75x; 池数 1; 分项 L10/V17/B17/Buy0/Risk-45 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PUMP](https://dexscreener.com/solana/2uf4xh61rdwxng9woyxsvqp7zua6klfpb3nvnrqeoisd) | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $22.32M; Vol24H $7.78M; 24H +4.80%; V/LP 0.35x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Mature; LP $6.80M; Vol24H $7.54M; 24H +2.40%; V/LP 1.11x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.52M; Vol24H $3.25M; 24H +14.54%; V/LP 1.29x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.56M; Vol24H $21.37M; 24H +16.56%; V/LP 5.99x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 60; Tier Liquid; LP $3.53M; Vol24H $11.72M; 24H +47.91%; V/LP 3.32x; 池数 2; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| GSTOCK | BSC | [0xcafd...3f9e20](https://bscscan.com/token/0xcafdbce93477261db8250e42bdae6e66733f9e20) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CNPY | BSC | [0xc69b...90ddd2](https://bscscan.com/token/0xc69b16cf18cea1e5d0bb6a1a9db802097790ddd2) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [METH](https://dexscreener.com/solana/5fa9x4whjvktyyqrzarrda8oj1out2m5lvnqtxiawkxq) | SOL | [6CsmCt...efqLym](https://solscan.io/token/6CsmCtDAhRcbp3G4KiinKC2JjLJ9BpR7isqcgZefqLym) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| B13B | BSC | [0x4902...eeec3f](https://bscscan.com/token/0x4902c5ebc598265ed2212b559b042de8a5eeec3f) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 5 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 5 / Early 10 / Liquid 8 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
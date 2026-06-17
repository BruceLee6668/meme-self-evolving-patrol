# 自我进化轮巡

**本轮时间 UTC：** 2026-06-17T16:58:46Z
**版本：** 0.2.0-alpha-range-dedupe-pvp
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 129 个合并Token中筛出 5 个主观察候选。v0.2已加入早期Alpha区间过滤和PVP可见分层，但仍未接入钱包级确认，不能直接定义为真实聪明钱吸筹。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 274 |
| 合并后Token | 129 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 10 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 0 |
| 多池Token | 8 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 5 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|
| - | - | 上次记录不可用 | 第一次或无有效 previous_snapshot | - | - | - |

### B. 本轮扫描结果表
| Token | 链 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|
| TOESCOIN | SOL | 主观察 | Score 88; LP $363.4K; Vol24H $2.26M; 24H +7.23%; V/LP 6.22x; 池数 2; 分项 L14/V16/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SIREN | BSC | 主观察 | Score 87; LP $2.40M; Vol24H $814.3K; 24H +2.24%; V/LP 0.34x; 池数 1; 分项 L20/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [FISTFLOOR](https://dexscreener.com/solana/3fgmjpi5wgr9jhqf37lz8uh3dzsydjzslkrff4gagw5s) | SOL | 主观察 | Score 86; LP $2.32M; Vol24H $137.3K; 24H +5.05%; V/LP 0.06x; 池数 1; 分项 L20/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| SPACE | BSC | 主观察 | Score 86; LP $2.54M; Vol24H $15.10M; 24H +0.25%; V/LP 5.94x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | 主观察 | Score 85; LP $1.17M; Vol24H $5.08M; 24H +1.58%; V/LP 4.33x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PLASTIC](https://dexscreener.com/solana/83dtgbjqp1xgknjqdxvqzf9shqduhjgaid5yrvgkz4oh) | SOL | 次观察 | Score 84; LP $1.94M; Vol24H $79.4K; 24H -3.30%; V/LP 0.04x; 池数 1; 分项 L20/V6/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，不直接进攻 |
| three | SOL | 次观察 | Score 83; LP $255.9K; Vol24H $548.1K; 24H +1.43%; V/LP 2.14x; 池数 1; 分项 L13/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，不直接进攻 |
| [WORLDCUP](https://dexscreener.com/solana/etmhxtenfkmk85tacveebzdbv9htziwzdsddmshrp2wb) | SOL | 次观察 | Score 78; LP $146.8K; Vol24H $829.8K; 24H -1.35%; V/LP 5.65x; 池数 4; 分项 L11/V13/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度 | proxy_metrics_only | 次观察，不直接进攻 |
| [Staccana](https://dexscreener.com/solana/g8uquje1rssqbddegmpgqmsukfjuf9zw7wssbrzxc7wr) | SOL | 次观察 | Score 77; LP $119.5K; Vol24H $211.1K; 24H +0.07%; V/LP 1.77x; 池数 3; 分项 L10/V9/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，不直接进攻 |
| [SPCX69](https://dexscreener.com/solana/5qphhqpaw3cz5anbnhqgzjxjm7ennrka6hwtzhmxj2dr) | SOL | 次观察 | Score 77; LP $167.6K; Vol24H $927.0K; 24H -15.13%; V/LP 5.53x; 池数 1; 分项 L11/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，不直接进攻 |
| KINS | SOL | 次观察 | Score 73; LP $393.6K; Vol24H $1.23M; 24H +17.93%; V/LP 3.13x; 池数 2; 分项 L15/V14/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，等成交/LP结构继续改善 |
| [USBC](https://dexscreener.com/solana/e98eyybmtmbkxwycnrdbcdkj6hfas3hzxg2lkdq1htd) | SOL | 次观察 | Score 72; LP $55.4K; Vol24H $364.7K; 24H -7.81%; V/LP 6.58x; 池数 1; 分项 L7/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，等成交/LP结构继续改善 |
| [VIRL](https://dexscreener.com/solana/8px97np5wy871smszwhqyl9z97k3vzhgjvkfvat7carz) | SOL | 次观察 | Score 66; LP $71.3K; Vol24H $180.5K; 24H -5.19%; V/LP 2.53x; 池数 1; 分项 L8/V9/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，等成交/LP结构继续改善 |
| [VIN](https://dexscreener.com/bsc/0xde52cff316d8a70256bee647073312c1aa7ee2cf) | BSC | 次观察 | Score 65; LP $995.9K; Vol24H $3.3K; 24H +0.71%; V/LP 0.00x; 池数 1; 分项 L18/V0/B22/Buy12/Risk-11 | 钱包级数据不可用；当前仅代理指标 | proxy_metrics_only | 次观察，等成交/LP结构继续改善 |
| [LOA](https://dexscreener.com/solana/enymbpwxnvj7ebav3d9stticmidtm658lorfqvlwvscf) | SOL | 次观察 | Score 64; LP $118.0K; Vol24H $320.9K; 24H +9.45%; V/LP 2.72x; 池数 4; 分项 L10/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度 | proxy_metrics_only | 次观察，等成交/LP结构继续改善 |

## 第二部分：逻辑复盘表格

### A. 上次逻辑总结表
| 逻辑项 | 上次规则 | 本轮验证 |
|---|---|---|
| 主观察门槛 | LP >= $100K，且非PVP | v0.2继续保留，并增加早期Alpha上限过滤 |
| PVP过滤 | Volume/LP > 8x 降级，>20x 排除主榜 | 继续保留，避免刷量币进主榜 |
| 多池处理 | v0.1仍可能出现Gecko-only重复 | v0.2增加symbol bridge合并，以最大LP池为代表 |
| Smart Money | AVE周缓存/本地钱包评分/代理指标分层 | 仍未接AVE，当前只用代理指标，置信度低 |

### B. 本轮逻辑总结表
| 逻辑项 | 本轮结果 | 判断 |
|---|---|---|
| 主观察候选 | 5 个 | 主榜已压缩，并排除过成熟大池，但仍需钱包留存确认 |
| PVP风险池 | 8 个 | v0.2保留可见PVP池，避免风险币被静默忽略 |
| 多池合并 | 8 个多池Token，Symbol桥接 5 个 | 避免单小池和Gecko-only重复误判 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| Smart Money | 仅代理指标 | 不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| early_alpha_range_filter | 检测到成熟池候选，不能让大池成熟资产占用早期Alpha主榜 | 成熟大池进入成熟池观察，不作为底部MEME扫货主观察 |
| multi_pool_conflict_policy | 本轮存在多池数据冲突，不能用单池数据给高置信判断 | 多池价格/LP冲突的币降置信度，不直接升级主观察 |
| symbol_bridge_merge_policy | 本轮存在symbol桥接合并，说明重复输出问题正在被修正 | 减少同一Token在主观察/次观察中重复出现 |

### D. 挖掘策略调优表
| 项目 | 本轮判断 |
|---|---|
| 当前挖掘策略是否有效 | 部分有效：免费源可发现候选，v0.2能压缩主榜、合并多池、分离成熟池和PVP池 |
| 主要问题 | 缺少钱包级数据、AVE周缓存、链上Swap留存和S0精确回放 |
| 假阳性风险 | 已降低，但代理指标仍可能误判买盘质量 |
| 漏筛风险 | 存在，DEXScreener/GeckoTerminal无法覆盖所有新池细节 |
| 候选来源调整 | 暂不新增外部源，先观察v0.2早期Alpha过滤效果；下一步接BSC/SOL链上精查 |
| 阈值调整 | 已加入max_lp/max_fdv/max_mcap主榜上限；继续观察是否过严 |
| 下轮挖掘方向 | 重点看主观察是否更接近早期Alpha；同时检查PVP风险池是否不再为0、成熟资产是否不再占主榜 |

## 第三部分：策略回写确认

| 项目 | 状态 |
|---|---|
| 是否已将本轮优化策略写回主定时策略 | 是 |
| 写回内容摘要 | 本轮确认结构性规则：早期Alpha区间过滤、PVP可见分层、多池冲突降置信、重复合并增强 |
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
- This v0.2 scan uses free public sources only.
- AVE Smart Money weekly cache is not connected yet.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet.
- v0.2 adds early-alpha range filters; mature/liquid assets are separated from main early-alpha watchlist.
- Symbol bridge merging reduces Gecko-only duplicates but may still be approximate for ambiguous tickers.
# 自我进化轮巡

**本轮时间 UTC：** 2026-08-08T19:24:34Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 140 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 240 |
| 合并后Token | 140 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 4 |
| 多池Token | 8 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 2 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 8 |
| Liquid层 | 8 |
| Mature层 | 3 |
| 需要链上确认 | 15 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 2 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 86; Tier Early; LP $546.7K; Vol24H $2.43M; 24H -2.78%; V/LP 4.45x; 池数 1; 分项 L16/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 84; Tier Liquid; LP $2.52M; Vol24H $1.49M; 24H +14.63%; V/LP 0.59x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $1.12M; Vol24H $311.6K; 24H +4.36%; V/LP 0.28x; 池数 1; 分项 L19/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 次观察 | Score 73; Tier Liquid; LP $4.24M; Vol24H $2.66M; 24H +117.10%; V/LP 0.63x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 次观察 | Score 71; Tier Early; LP $101.7K; Vol24H $719.7K; 24H +8.40%; V/LP 7.08x; 池数 1; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SOLCEX](https://dexscreener.com/solana/4ro3pg1xzgsjenfgcccngqqrhyvqhhjwcl27ohmxmmtg) | SOL | [AMjzRn...dFPk6K](https://solscan.io/token/AMjzRn1TBQwQfNAjHFeBb7uGbbqbJB7FzXAnGgdFPk6K) | 次观察 | Score 65; Tier Early; LP $282.8K; Vol24H $137.9K; 24H +18.15%; V/LP 0.49x; 池数 5; 分项 L13/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 44; Tier Liquid; LP $2.09M; Vol24H $49.50M; 24H +1.68%; V/LP 23.71x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | PVP风险池 | Score 44; Tier Early; LP $268.2K; Vol24H $7.97M; 24H -14.40%; V/LP 29.70x; 池数 1; 分项 L13/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Jimothy](https://dexscreener.com/solana/5pghkctym6odbhgo2tkmst2ajmjsb2uzbqrkkn4zuft5) | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 43; Tier Early; LP $603.6K; Vol24H $12.98M; 24H +55.71%; V/LP 21.50x; 池数 2; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TOAD | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 33; Tier Early; LP $358.9K; Vol24H $22.73M; 24H +44580.70%; V/LP 63.34x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 主观察 | Score 86; Tier Early; LP $548.0K; Vol24H $2.37M; 24H -2.19%; V/LP 4.33x; 池数 1; 分项 L16/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 主观察 | Score 84; Tier Liquid; LP $2.53M; Vol24H $1.54M; 24H +14.53%; V/LP 0.61x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 78; Tier Liquid; LP $1.12M; Vol24H $312.0K; 24H +3.37%; V/LP 0.28x; 池数 1; 分项 L19/V10/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 次观察 | Score 73; Tier Liquid; LP $4.29M; Vol24H $2.76M; 24H +113.70%; V/LP 0.64x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 次观察 | Score 71; Tier Early; LP $101.9K; Vol24H $696.5K; 24H +12.51%; V/LP 6.83x; 池数 1; 分项 L9/V13/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 次观察 | Score 67; Tier Micro; LP $55.6K; Vol24H $186.2K; 24H +3.53%; V/LP 3.35x; 池数 3; 分项 L7/V9/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SOLCEX](https://dexscreener.com/solana/4ro3pg1xzgsjenfgcccngqqrhyvqhhjwcl27ohmxmmtg) | SOL | [AMjzRn...dFPk6K](https://solscan.io/token/AMjzRn1TBQwQfNAjHFeBb7uGbbqbJB7FzXAnGgdFPk6K) | 次观察 | Score 65; Tier Early; LP $284.3K; Vol24H $144.6K; 24H +19.12%; V/LP 0.51x; 池数 5; 分项 L13/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | PVP风险池 | Score 49; Tier Early; LP $268.2K; Vol24H $7.52M; 24H -3.57%; V/LP 28.04x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | PVP风险池 | Score 44; Tier Liquid; LP $2.10M; Vol24H $51.46M; 24H +2.36%; V/LP 24.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | PVP风险池 | Score 43; Tier Early; LP $618.0K; Vol24H $12.85M; 24H +63.53%; V/LP 20.79x; 池数 2; 分项 L16/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| RUBY | SOL | [JBKWfC...8cpump](https://solscan.io/token/JBKWfCwhW91RvkZb1S9HL8x59YuBbnVFxgwpkx8cpump) | PVP风险池 | Score 28; Tier Micro; LP $15.0K; Vol24H $3.51M; 24H +10.24%; V/LP 234.34x; 池数 1; 分项 L2/V17/B17/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [claudius](https://dexscreener.com/solana/4wtklrw7qyqfan59r2nb3diclcnkjxsy9fwdf3yb9jds) | SOL | [46amR3...VSpump](https://solscan.io/token/46amR3aeQE7MJ9QDrgNRqBP3FcsJ9QNYV71L2vVSpump) | PVP风险池 | Score 26; Tier Micro; LP $61.2K; Vol24H $4.67M; 24H +1556.00%; V/LP 76.27x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Tusk](https://dexscreener.com/solana/63jicurhtwbt5tkq2eqxwvrwkfhr1fzjpcvmp6jb1f8b) | SOL | [8mGByx...Ykpump](https://solscan.io/token/8mGByxG4X7YnQeGHaP9B7uheKjt9TzL3WS5wAJYkpump) | PVP风险池 | Score 13; Tier Micro; LP $28.5K; Vol24H $2.72M; 24H +294.00%; V/LP 95.46x; 池数 2; 分项 L4/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Frohorse | SOL | [9p84TE...uMpump](https://solscan.io/token/9p84TE2ZwH8PXU7QMvj8ieK3TWodZPdCjpE8Q2uMpump) | PVP风险池 | Score 10; Tier Micro; LP $40.4K; Vol24H $8.12M; 24H +168.44%; V/LP 200.90x; 池数 2; 分项 L6/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 9; Tier Early; LP $386.5K; Vol24H $27.04M; 24H +51694.00%; V/LP 69.97x; 池数 4; 分项 L15/V17/B0/Buy8/Risk-55 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Early; LP $268.2K; Vol24H $7.52M; 24H -3.57%; V/LP 28.04x; 池数 1; 分项 L13/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 44; Tier Liquid; LP $2.10M; Vol24H $51.46M; 24H +2.36%; V/LP 24.51x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 43; Tier Early; LP $618.0K; Vol24H $12.85M; 24H +63.53%; V/LP 20.79x; 池数 2; 分项 L16/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| RUBY | SOL | [JBKWfC...8cpump](https://solscan.io/token/JBKWfCwhW91RvkZb1S9HL8x59YuBbnVFxgwpkx8cpump) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 28; Tier Micro; LP $15.0K; Vol24H $3.51M; 24H +10.24%; V/LP 234.34x; 池数 1; 分项 L2/V17/B17/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [claudius](https://dexscreener.com/solana/4wtklrw7qyqfan59r2nb3diclcnkjxsy9fwdf3yb9jds) | SOL | [46amR3...VSpump](https://solscan.io/token/46amR3aeQE7MJ9QDrgNRqBP3FcsJ9QNYV71L2vVSpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $61.2K; Vol24H $4.67M; 24H +1556.00%; V/LP 76.27x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Tusk](https://dexscreener.com/solana/63jicurhtwbt5tkq2eqxwvrwkfhr1fzjpcvmp6jb1f8b) | SOL | [8mGByx...Ykpump](https://solscan.io/token/8mGByxG4X7YnQeGHaP9B7uheKjt9TzL3WS5wAJYkpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 13; Tier Micro; LP $28.5K; Vol24H $2.72M; 24H +294.00%; V/LP 95.46x; 池数 2; 分项 L4/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| Frohorse | SOL | [9p84TE...uMpump](https://solscan.io/token/9p84TE2ZwH8PXU7QMvj8ieK3TWodZPdCjpE8Q2uMpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 10; Tier Micro; LP $40.4K; Vol24H $8.12M; 24H +168.44%; V/LP 200.90x; 池数 2; 分项 L6/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 9; Tier Early; LP $386.5K; Vol24H $27.04M; 24H +51694.00%; V/LP 69.97x; 池数 4; 分项 L15/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $51.51M; Vol24H $6.48M; 24H -0.37%; V/LP 0.13x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Mature; LP $8.37M; Vol24H $17.40M; 24H -2.29%; V/LP 2.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 71; Tier Mature; LP $11.06M; Vol24H $1.26M; 24H +3.57%; V/LP 0.11x; 池数 3; 分项 L20/V14/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $1.98M; Vol24H $863.0K; 24H +4.95%; V/LP 0.44x; 池数 2; 分项 L20/V13/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.81M; Vol24H $9.63M; 24H -8.21%; V/LP 2.53x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BLUAI | BSC | [0xed9a...cf9aad](https://bscscan.com/token/0xed9ae3def8d6f052971bb8b6d1975ff267cf9aad) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 59; Tier Liquid; LP $1.07M; Vol24H $5.66M; 24H +77.83%; V/LP 5.31x; 池数 1; 分项 L19/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TROLL | SOL | [5UUH9R...TBhgH2](https://solscan.io/token/5UUH9RTDiSpq6HKS6bp4NdU9PNJpXRXuiw6ShBTBhgH2) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [HBULL](https://dexscreener.com/solana/edx18gjcdijqslaja2pp5c2vma3btrrx4utxkejufrtq) | SOL | [7V6Sk6...k9pump](https://solscan.io/token/7V6Sk63y8Rr1MvcN5mYNp61wgFhy4EeQg5gUASk9pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [MEMESTOCK](https://dexscreener.com/bsc/0x5883a131424cc366626032141c2095fa4bf5dd4f) | BSC | [0xd3F4...837777](https://bscscan.com/token/0xd3F4d386DB69657bb5A61C99276BCF0d97837777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SOLCEX](https://dexscreener.com/solana/4ro3pg1xzgsjenfgcccngqqrhyvqhhjwcl27ohmxmmtg) | SOL | [AMjzRn...dFPk6K](https://solscan.io/token/AMjzRn1TBQwQfNAjHFeBb7uGbbqbJB7FzXAnGgdFPk6K) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BLESS | BSC | [0x7c82...9ae11f](https://bscscan.com/token/0x7c8217517ed4711fe2deccdfeffe8d906b9ae11f) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CYS | BSC | [0x0c69...b507c7](https://bscscan.com/token/0x0c69199c1562233640e0db5ce2c399a88eb507c7) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Jimothy | SOL | [Ge87Et...xTpump](https://solscan.io/token/Ge87EtsjwRQbHaqQmKRno69RFTwh9bfSsm99XNxTpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| SIREN | BSC | [0x997a...fc18e1](https://bscscan.com/token/0x997a58129890bbda032231a52ed1ddc845fc18e1) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 8 / Liquid 8 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
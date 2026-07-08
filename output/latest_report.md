# 自我进化轮巡

**本轮时间 UTC：** 2026-07-08T02:09:26Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮没有出现可直接确认的“干净底部聪明钱扫货”。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 326 |
| 合并后Token | 113 |
| 输出候选 | 25 |
| 主观察 | 0 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 10 |
| 多池Token | 9 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 14 |
| Liquid层 | 2 |
| Mature层 | 1 |
| 需要链上确认 | 11 |
| 紧急精查候选 | 0 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 506，刷新时间 2026-07-06T02:26:30Z，是否过期 否 |
| 链上预检 | 本轮检查 11 个，验证通过 11 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 0 个，BSC Transfer样本 0 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [BABYCZ](https://dexscreener.com/bsc/0x50ccacb74a4dc5bbb3acf3481dbc180c1db7bd3b) | BSC | [0xc7aE...9e4444](https://bscscan.com/token/0xc7aEb1A936FcF98CFE4DD552f6cBf48Ac19e4444) | 次观察 | Score 73; Tier Micro; LP $56.0K; Vol24H $142.4K; 24H -2.49%; V/LP 2.54x; 池数 2; 分项 L7/V8/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 71; Tier Early; LP $318.8K; Vol24H $129.3K; 24H -1.35%; V/LP 0.41x; 池数 1; 分项 L14/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [LMAO!](https://dexscreener.com/solana/afayrfh7huynkv5mbvbnrhwx29m9jzul3ysgtqz69auv) | SOL | [H74CYm...uApump](https://solscan.io/token/H74CYmXgMkYHYuSRsZt6RJb4NYp2u72Vw8BS5huApump) | 次观察 | Score 69; Tier Early; LP $250.1K; Vol24H $107.8K; 24H +0.71%; V/LP 0.43x; 池数 5; 分项 L13/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 68; Tier Micro; LP $73.8K; Vol24H $380.1K; 24H +22.00%; V/LP 5.15x; 池数 2; 分项 L8/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 39; Tier Liquid; LP $1.55M; Vol24H $55.88M; 24H +10.61%; V/LP 36.12x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 34; Tier Early; LP $395.4K; Vol24H $11.58M; 24H +1068.01%; V/LP 29.30x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 33; Tier Early; LP $371.4K; Vol24H $13.65M; 24H +2336.00%; V/LP 36.74x; 池数 2; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 29; Tier Early; LP $138.4K; Vol24H $9.93M; 24H -86.98%; V/LP 71.76x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 28; Tier Early; LP $360.0K; Vol24H $16.16M; 24H +158.44%; V/LP 44.90x; 池数 1; 分项 L14/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | PVP风险池 | Score 28; Tier Early; LP $107.0K; Vol24H $9.39M; 24H +106.00%; V/LP 87.74x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 次观察 | Score 68; Tier Micro; LP $67.0K; Vol24H $378.1K; 24H +18.40%; V/LP 5.64x; 池数 1; 分项 L8/V11/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 次观察 | Score 65; Tier Early; LP $310.7K; Vol24H $112.4K; 24H -9.77%; V/LP 0.36x; 池数 1; 分项 L14/V7/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | PVP风险池 | Score 39; Tier Liquid; LP $1.55M; Vol24H $56.51M; 24H +11.30%; V/LP 36.42x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | PVP风险池 | Score 33; Tier Early; LP $317.9K; Vol24H $12.23M; 24H +855.79%; V/LP 38.47x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | PVP风险池 | Score 32; Tier Early; LP $287.2K; Vol24H $16.41M; 24H +1228.00%; V/LP 57.15x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | PVP风险池 | Score 29; Tier Early; LP $137.4K; Vol24H $9.45M; 24H -84.13%; V/LP 68.82x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | PVP风险池 | Score 27; Tier Early; LP $266.8K; Vol24H $18.86M; 24H -85.81%; V/LP 70.69x; 池数 1; 分项 L13/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | PVP风险池 | Score 27; Tier Micro; LP $72.9K; Vol24H $9.34M; 24H +104.00%; V/LP 128.03x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | PVP风险池 | Score 21; Tier Early; LP $158.6K; Vol24H $17.58M; 24H -67.04%; V/LP 110.85x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | PVP风险池 | Score 16; Tier Early; LP $370.4K; Vol24H $17.72M; 24H +183.49%; V/LP 47.84x; 池数 1; 分项 L14/V17/B0/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 79; Tier Mature; LP $17.93M; Vol24H $9.10M; 24H -1.30%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 成熟池观察 | Score 65; Tier Liquid; LP $3.21M; Vol24H $20.58M; 24H -25.39%; V/LP 6.40x; 池数 4; 分项 L20/V17/B8/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [RTM](https://dexscreener.com/solana/ebnuexqpb5wjkxjsfm3ruft7zb7zbxhzgr7ydhyuvuyy) | SOL | [3d1qHS...XCDM6u](https://solscan.io/token/3d1qHSAkQhoN7kN1C6tvpAArCkXWxwYdBng6taXCDM6u) | 低优先观察 | Score 61; Tier Early; LP $136.6K; Vol24H $421.4K; 24H -42.14%; V/LP 3.08x; 池数 5; 分项 L10/V11/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |
| BABYCZ | BSC | [0xc7ae...9e4444](https://bscscan.com/token/0xc7aeb1a936fcf98cfe4dd552f6cbf48ac19e4444) | 低优先观察 | Score 59; Tier Micro; LP $56.4K; Vol24H $145.6K; 24H +33.28%; V/LP 2.58x; 池数 1; 分项 L7/V8/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |
| [SOLFUNMEME](https://dexscreener.com/solana/61b8wzu42a9mlp3ly64lsofhwsyuc7vwhxd2ypxhypl2) | SOL | [BwUTq7...tapump](https://solscan.io/token/BwUTq7fS6sfUmHDwAiCQZ3asSiPEapW5zDrsbwtapump) | 低优先观察 | Score 58; Tier Micro; LP $75.3K; Vol24H $857.42; 24H +3.62%; V/LP 0.01x; 池数 1; 分项 L8/V0/B22/Buy12/Risk-8 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 低优先观察，不追高 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 39; Tier Liquid; LP $1.55M; Vol24H $56.51M; 24H +11.30%; V/LP 36.42x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $317.9K; Vol24H $12.23M; 24H +855.79%; V/LP 38.47x; 池数 1; 分项 L14/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $287.2K; Vol24H $16.41M; 24H +1228.00%; V/LP 57.15x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $137.4K; Vol24H $9.45M; 24H -84.13%; V/LP 68.82x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Early; LP $266.8K; Vol24H $18.86M; 24H -85.81%; V/LP 70.69x; 池数 1; 分项 L13/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $72.9K; Vol24H $9.34M; 24H +104.00%; V/LP 128.03x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 21; Tier Early; LP $158.6K; Vol24H $17.58M; 24H -67.04%; V/LP 110.85x; 池数 1; 分项 L11/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| EVAA | BSC | [0xaa03...a628c1](https://bscscan.com/token/0xaa036928c9c0df07d525b55ea8ee690bb5a628c1) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；FDV超过早期Alpha主榜上限 | Score 16; Tier Early; LP $370.4K; Vol24H $17.72M; 24H +183.49%; V/LP 47.84x; 池数 1; 分项 L14/V17/B0/Buy3/Risk-42 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $17.93M; Vol24H $9.10M; 24H -1.30%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ANSEM | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $3.21M; Vol24H $20.58M; 24H -25.39%; V/LP 6.40x; 池数 4; 分项 L20/V17/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [ALON](https://dexscreener.com/solana/j7hds6hi2hejmllpkprervqhjhicdyxy4lk18p1zyyvk) | SOL | [7XSmre...t1pump](https://solscan.io/token/7XSmrerjGbVi9uVW8qVHfp7SN1GU1vnxHguzUEt1pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 67 | SOL | [9Avytn...Chpump](https://solscan.io/token/9AvytnUKsLxPxFHFqS6VLxaxt5p6BhYNr53SD2Chpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [COBRA](https://dexscreener.com/solana/9nrjcz8arsdujx5bl7rwnnppsiwfhmepvwdhb9cq2eav) | SOL | [D6sA8h...LWpump](https://solscan.io/token/D6sA8hKpreRfWEqLRo2fyx5UpmcHeEmGsQ1UndLWpump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| NES | BSC | [0x3131...ac3fb5](https://bscscan.com/token/0x3131f6b80c26936ab03f7d9d29eb4ddf36ac3fb5) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| bibi | BSC | [0x0b6d...bd4444](https://bscscan.com/token/0x0b6d8934fc8838b1027b510364a2087317bd4444) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [Cupsey](https://dexscreener.com/solana/dpzkojvewah1wpchd3gwkeegm7g2mxkbw48urniagbvx) | SOL | [6NwarB...9vpump](https://solscan.io/token/6NwarBvDkXhByqVp2Qkq5i9XbtA2B3Bwe8SWGu9vpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| LEVI | SOL | [6baGyq...4ppump](https://solscan.io/token/6baGyq4HLbUn93MQUGFqBktpXP8BRjpoxSsAap4ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| TAC | BSC | [0x1219...f271de](https://bscscan.com/token/0x1219c409fabe2c27bd0d1a565daeed9bd9f271de) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [SAPIJIJU](https://dexscreener.com/solana/g1dza1pdodb91tfamu5tpnyhvmn7r4wz3rmop93akozh) | SOL | [8jayQD...c9pump](https://solscan.io/token/8jayQDfRc3GYxftBJ2VAwjqmRBdYPC9KnjY15rc9pump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 14 / Liquid 2 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
| S0对比 | 尚未做精确历史回放 | 后续用GeckoTerminal OHLCV / 链上数据补齐 |
| 链上确认 | v0.5执行地址/账户预检 + BSC Transfer级钱包行为样本 | 可以初步看到活跃钱包/缓存命中，但仍不能替代完整Swap留存判断 |
| Smart Money | AVE周缓存 + 代理指标 | 无具体钱包映射前，不允许标记真实吸筹 |

### C. 本轮优化调整表
| 调整项 | 触发原因 | 对下轮筛选影响 |
|---|---|---|
| chain_verify_pipeline | 观察池候选需要链上Swap、钱包留存和大额买卖确认；v0.4.1已生成确认标记并强制落地chain_verify_latest.json | 下轮报告继续输出链上确认/紧急精查表，为接BSC RPC/Helius做准备 |
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
| dexscreener_boosts | {'ok': True, 'count': 29, 'expanded': 25} |
| dexscreener_search | {'ok': True, 'count': 340} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
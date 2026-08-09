# 自我进化轮巡

**本轮时间 UTC：** 2026-08-09T16:27:38Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 131 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 247 |
| 合并后Token | 131 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 5 |
| 低优先观察 | 2 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 7 |
| Liquid层 | 8 |
| Mature层 | 3 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 886，刷新时间 2026-08-03T02:01:04Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 2 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 89; Tier Liquid; LP $997.3K; Vol24H $7.06M; 24H +6.72%; V/LP 7.07x; 池数 2; 分项 L18/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 84; Tier Liquid; LP $1.89M; Vol24H $1.69M; 24H +24.10%; V/LP 0.90x; 池数 1; 分项 L20/V15/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 81; Tier Liquid; LP $1.09M; Vol24H $136.5K; 24H -3.26%; V/LP 0.12x; 池数 1; 分项 L19/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 80; Tier Liquid; LP $2.05M; Vol24H $417.4K; 24H -0.26%; V/LP 0.20x; 池数 1; 分项 L20/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 主观察 | Score 77; Tier Liquid; LP $1.71M; Vol24H $6.68M; 24H +42.71%; V/LP 3.90x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 次观察 | Score 75; Tier Early; LP $452.9K; Vol24H $2.22M; 24H -10.45%; V/LP 4.90x; 池数 1; 分项 L15/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 次观察 | Score 74; Tier Early; LP $282.7K; Vol24H $158.2K; 24H +8.92%; V/LP 0.56x; 池数 1; 分项 L13/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 73; Tier Early; LP $124.1K; Vol24H $56.1K; 24H +0.96%; V/LP 0.45x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 次观察 | Score 71; Tier Early; LP $236.2K; Vol24H $59.2K; 24H +19.20%; V/LP 0.25x; 池数 1; 分项 L13/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ClipX | BSC | [0xc269...554444](https://bscscan.com/token/0xc269d59a0d608ea0bd672f2f4616c372d8554444) | PVP风险池 | Score 41; Tier Early; LP $122.9K; Vol24H $2.90M; 24H +16.99%; V/LP 23.58x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 84; Tier Liquid; LP $943.9K; Vol24H $6.80M; 24H -18.48%; V/LP 7.20x; 池数 2; 分项 L18/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 主观察 | Score 81; Tier Liquid; LP $1.09M; Vol24H $129.4K; 24H -5.30%; V/LP 0.12x; 池数 1; 分项 L19/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 主观察 | Score 80; Tier Liquid; LP $2.05M; Vol24H $388.4K; 24H -0.26%; V/LP 0.19x; 池数 4; 分项 L20/V11/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 主观察 | Score 77; Tier Liquid; LP $1.77M; Vol24H $7.68M; 24H +46.49%; V/LP 4.33x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 次观察 | Score 75; Tier Early; LP $455.3K; Vol24H $1.99M; 24H -13.29%; V/LP 4.37x; 池数 1; 分项 L15/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 次观察 | Score 75; Tier Liquid; LP $1.91M; Vol24H $1.79M; 24H +26.99%; V/LP 0.94x; 池数 1; 分项 L20/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 次观察 | Score 74; Tier Early; LP $287.3K; Vol24H $159.4K; 24H +12.40%; V/LP 0.55x; 池数 1; 分项 L13/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 次观察 | Score 73; Tier Early; LP $124.8K; Vol24H $55.9K; 24H +1.69%; V/LP 0.45x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 次观察 | Score 71; Tier Early; LP $237.6K; Vol24H $58.0K; 24H +18.75%; V/LP 0.24x; 池数 1; 分项 L13/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [drooling](https://dexscreener.com/solana/2mqyy3lfjcnauyfufynlgtlcxmb6m2shxqgv2mhx7mpy) | SOL | [B6f27E...hmpump](https://solscan.io/token/B6f27ETGcjgGNB1fqULJbXVmw9FnL8HgBp7R83hmpump) | 次观察 | Score 68; Tier Micro; LP $75.2K; Vol24H $70.8K; 24H +1.20%; V/LP 0.94x; 池数 5; 分项 L8/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | PVP风险池 | Score 42; Tier Early; LP $417.4K; Vol24H $33.45M; 24H +53.03%; V/LP 80.15x; 池数 2; 分项 L15/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| ClipX | BSC | [0xc269...554444](https://bscscan.com/token/0xc269d59a0d608ea0bd672f2f4616c372d8554444) | PVP风险池 | Score 41; Tier Early; LP $120.4K; Vol24H $2.78M; 24H -15.50%; V/LP 23.06x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAVECAT](https://dexscreener.com/solana/fju39s2tyzkmixcqnn45zgctquocnyjpmlmoxrwdtuq5) | SOL | [mNzssX...S3pump](https://solscan.io/token/mNzssXQ9hU1ASJ1CVuu4JjrFBrfeVdR2JzirKS3pump) | PVP风险池 | Score 29; Tier Micro; LP $52.1K; Vol24H $6.56M; 24H -56.16%; V/LP 125.92x; 池数 1; 分项 L7/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [sling](https://dexscreener.com/solana/fakatjxjxnizlog9xoyjaemsbeecanrjagzyiyc433zw) | SOL | [EeB76L...bcpump](https://solscan.io/token/EeB76LHyVZPMRvTpLcxJqqfSz4gg9f9XgsUmFybcpump) | PVP风险池 | Score 29; Tier Early; LP $109.1K; Vol24H $4.60M; 24H +4123.00%; V/LP 42.15x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Bark](https://dexscreener.com/solana/6pidtwpgoxfmhtkjaa6wrn7r45avhwgybm6l5vprbmop) | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | PVP风险池 | Score 28; Tier Micro; LP $95.9K; Vol24H $8.86M; 24H +3331.00%; V/LP 92.39x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [TOAD](https://dexscreener.com/solana/nx9dcwns3ijxm5yaxshmhe4ayjhddyygmhvcmasgfu8) | SOL | [A13oRB...vPpump](https://solscan.io/token/A13oRB9FFaiUjfi6LdCg6p9ka1u8SfGkUFs4SKvPpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Early; LP $417.4K; Vol24H $33.45M; 24H +53.03%; V/LP 80.15x; 池数 2; 分项 L15/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| ClipX | BSC | [0xc269...554444](https://bscscan.com/token/0xc269d59a0d608ea0bd672f2f4616c372d8554444) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 41; Tier Early; LP $120.4K; Vol24H $2.78M; 24H -15.50%; V/LP 23.06x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [RAVECAT](https://dexscreener.com/solana/fju39s2tyzkmixcqnn45zgctquocnyjpmlmoxrwdtuq5) | SOL | [mNzssX...S3pump](https://solscan.io/token/mNzssXQ9hU1ASJ1CVuu4JjrFBrfeVdR2JzirKS3pump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 29; Tier Micro; LP $52.1K; Vol24H $6.56M; 24H -56.16%; V/LP 125.92x; 池数 1; 分项 L7/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [sling](https://dexscreener.com/solana/fakatjxjxnizlog9xoyjaemsbeecanrjagzyiyc433zw) | SOL | [EeB76L...bcpump](https://solscan.io/token/EeB76LHyVZPMRvTpLcxJqqfSz4gg9f9XgsUmFybcpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $109.1K; Vol24H $4.60M; 24H +4123.00%; V/LP 42.15x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Bark](https://dexscreener.com/solana/6pidtwpgoxfmhtkjaa6wrn7r45avhwgybm6l5vprbmop) | SOL | [3fqify...Dmpump](https://solscan.io/token/3fqify4QnaKFsvmFVqmLMUHaRKdiPki6w2H3GyDmpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $95.9K; Vol24H $8.86M; 24H +3331.00%; V/LP 92.39x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [LOUIE](https://dexscreener.com/solana/3vuhjgbgdt5ej3tafvtzjt8wpyjzaf7pshfcihd9oysg) | SOL | [AENK1Y...wvpump](https://solscan.io/token/AENK1YJ9978xp19xQLKat6eNmndf7Jg2FxFfKiwvpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $65.7K; Vol24H $3.68M; 24H +338.00%; V/LP 56.07x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Remus](https://dexscreener.com/solana/flbsnxkr6sddkepbb254yosgjqufbuyz8qvykybwpv47) | SOL | [23e4CN...XYPgme](https://solscan.io/token/23e4CNuJxvBQ7RjNLc8Bh3yN3pQq6jeiTbyzJGXYPgme) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 2; Tier Micro; LP $66.2K; Vol24H $7.96M; 24H +1590.00%; V/LP 120.32x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-55 | 只记录热度，不进入主榜 |
| [RURU](https://dexscreener.com/solana/cd7morpojnj6qzb4y8i8bofkehaxio6rqmbbp42srq85) | SOL | [EtxCL9...jSpump](https://solscan.io/token/EtxCL9DfuQ1ZJcydWY3Mqd5B1XjhZhRKTUdAxpjSpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $41.6K; Vol24H $4.08M; 24H +632.00%; V/LP 98.16x; 池数 6; 分项 L6/V17/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| SPCXB | BSC | [0xbe9d...3103e1](https://bscscan.com/token/0xbe9d156892e55e7154bcd3cb0fea677f9d3103e1) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 79; Tier Liquid; LP $3.93M; Vol24H $4.56M; 24H +3.16%; V/LP 1.16x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| SKYAI | BSC | [0x92aa...3ffb10](https://bscscan.com/token/0x92aa03137385f18539301349dcfc9ebc923ffb10) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Mature; LP $8.41M; Vol24H $17.37M; 24H -7.11%; V/LP 2.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；成熟大池 | Score 73; Tier Mature; LP $12.30M; Vol24H $2.15M; 24H +19.61%; V/LP 0.17x; 池数 3; 分项 L20/V16/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 70; Tier Liquid; LP $1.97M; Vol24H $789.3K; 24H -4.45%; V/LP 0.40x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [NEVERZERO](https://dexscreener.com/solana/dmryq83qiugurjd36qky5y2cefzajqrhuxw8kyvg1z2e) | SOL | [7MsJCv...g2rise](https://solscan.io/token/7MsJCvDi5t5U3Ya2UAs5bR75VJyVMr2FKdzGmeg2rise) | 24H接近横盘；买入笔数占优；LP达主观察门槛；Volume/LP未失真；24H成交不足；LP超过早期Alpha主榜上限；成熟大池 | Score 58; Tier Mature; LP $20.39M; Vol24H $11.4K; 24H +1.79%; V/LP 0.00x; 池数 1; 分项 L20/V0/B22/Buy12/Risk-20 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [SAOF](https://dexscreener.com/solana/aoomx1g2kaxfbvmp5hw2gzeskagag48xunrdr6bd7psn) | SOL | [gRqb4a...abpump](https://solscan.io/token/gRqb4apeTsqyn4rdSZNgAMwUpwb5eqrbrjMUsabpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [UOTF](https://dexscreener.com/solana/5hyulrtc3cc6fbimurxdpeaor9ee7wdh8xehfuo3xpxg) | SOL | [wJuC6t...Eqpump](https://solscan.io/token/wJuC6tNgzfrbgHtES3PDTZiCqJxKTX1W9P4sAEqpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [TTF](https://dexscreener.com/solana/5sjgf5fssu1ehzd25xczawdxbgjo56316kcrnbbt3sdt) | SOL | [wyVF24...qXpump](https://solscan.io/token/wyVF24D5d7WwaRFtDboPcLmRp6PpjFsY9YGhVqXpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [drooling](https://dexscreener.com/solana/2mqyy3lfjcnauyfufynlgtlcxmb6m2shxqgv2mhx7mpy) | SOL | [B6f27E...hmpump](https://solscan.io/token/B6f27ETGcjgGNB1fqULJbXVmw9FnL8HgBp7R83hmpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PUMP](https://dexscreener.com/solana/7q2dqbjtxxp4dqmhec2nsgxwsytq8jaxdygswmag3pfp) | SOL | [9593dF...ysD6A1](https://solscan.io/token/9593dFjsLKKRAaz4LX1eK2DDEgrzfu3idb6yvMysD6A1) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| mubarak | BSC | [0x5c85...6b46f6](https://bscscan.com/token/0x5c85d6c6825ab4032337f11ee92a72df936b46f6) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 7 / Liquid 8 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
# 自我进化轮巡

**本轮时间 UTC：** 2026-06-27T04:47:59Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 135 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 315 |
| 合并后Token | 135 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 5 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 2 |
| 多池Token | 10 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 0 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 8 |
| Early层 | 7 |
| Liquid层 | 10 |
| Mature层 | 0 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 311，刷新时间 2026-06-22T02:56:49Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 3 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 86; Tier Liquid; LP $1.72M; Vol24H $13.22M; 24H +1.56%; V/LP 7.69x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.09M; Vol24H $5.11M; 24H -6.70%; V/LP 4.70x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [MAME](https://dexscreener.com/bsc/0x924f1a4422a89900faafa3f886721fdccd6e086a) | BSC | [0xe92F...c42302](https://bscscan.com/token/0xe92F7Fe3EAf61DF28b7B75f3FaAB199333c42302) | 主观察 | Score 83; Tier Liquid; LP $920.0K; Vol24H $439.8K; 24H +1.99%; V/LP 0.48x; 池数 3; 分项 L18/V11/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 82; Tier Early; LP $276.5K; Vol24H $415.2K; 24H -4.62%; V/LP 1.50x; 池数 1; 分项 L13/V11/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 74; Tier Early; LP $460.9K; Vol24H $1.78M; 24H +13.20%; V/LP 3.85x; 池数 2; 分项 L15/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 72; Tier Early; LP $108.6K; Vol24H $162.5K; 24H +1.34%; V/LP 1.50x; 池数 3; 分项 L10/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 72; Tier Liquid; LP $1.03M; Vol24H $231.0K; 24H +13.13%; V/LP 0.22x; 池数 1; 分项 L19/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 66; Tier Early; LP $157.2K; Vol24H $79.7K; 24H -6.63%; V/LP 0.51x; 池数 6; 分项 L11/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 49; Tier Liquid; LP $940.7K; Vol24H $50.10M; 24H -17.97%; V/LP 53.26x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [piss](https://dexscreener.com/solana/5ebtmzf6jxeumclew59mu2s34cttep2wncqds2wjbrfh) | SOL | [DXXcq4...cC5kbu](https://solscan.io/token/DXXcq4tY5e4PbXybyBMnxZjHVmzv1GVrAXoW5TcC5kbu) | PVP风险池 | Score 25; Tier Micro; LP $75.4K; Vol24H $1.72M; 24H +441.00%; V/LP 22.79x; 池数 1; 分项 L8/V15/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 主观察 | Score 85; Tier Liquid; LP $1.10M; Vol24H $4.87M; 24H +0.29%; V/LP 4.44x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 主观察 | Score 81; Tier Liquid; LP $1.75M; Vol24H $13.24M; 24H +11.43%; V/LP 7.56x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 主观察 | Score 81; Tier Liquid; LP $2.08M; Vol24H $16.33M; 24H -14.31%; V/LP 7.86x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 主观察 | Score 78; Tier Early; LP $288.9K; Vol24H $569.1K; 24H +13.56%; V/LP 1.97x; 池数 1; 分项 L13/V12/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 71; Tier Liquid; LP $1.01M; Vol24H $206.7K; 24H +14.72%; V/LP 0.20x; 池数 1; 分项 L18/V9/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 次观察 | Score 66; Tier Early; LP $105.9K; Vol24H $159.8K; 24H -3.35%; V/LP 1.51x; 池数 2; 分项 L9/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 次观察 | Score 66; Tier Early; LP $156.5K; Vol24H $69.3K; 24H -4.58%; V/LP 0.44x; 池数 5; 分项 L11/V6/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 次观察 | Score 65; Tier Early; LP $472.2K; Vol24H $1.73M; 24H +38.23%; V/LP 3.67x; 池数 2; 分项 L15/V15/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 次观察 | Score 64; Tier Early; LP $426.1K; Vol24H $949.4K; 24H +35.89%; V/LP 2.23x; 池数 2; 分项 L15/V14/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | PVP风险池 | Score 49; Tier Liquid; LP $936.7K; Vol24H $58.93M; 24H -19.97%; V/LP 62.91x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [piss](https://dexscreener.com/solana/5ebtmzf6jxeumclew59mu2s34cttep2wncqds2wjbrfh) | SOL | [DXXcq4...cC5kbu](https://solscan.io/token/DXXcq4tY5e4PbXybyBMnxZjHVmzv1GVrAXoW5TcC5kbu) | PVP风险池 | Score 32; Tier Micro; LP $65.4K; Vol24H $1.32M; 24H -51.55%; V/LP 20.21x; 池数 1; 分项 L7/V15/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [Pondeer](https://dexscreener.com/solana/4btvosm4paw3w5yxdcfqrvhhgkkyni1orgtfn1cpjbxh) | SOL | [5B8qah...hjpump](https://solscan.io/token/5B8qahEJezLtTHPU1Du1AsfAMf4kUVAdaMky7vhjpump) | PVP风险池 | Score 29; Tier Micro; LP $50.6K; Vol24H $2.57M; 24H +461.00%; V/LP 50.76x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [WENDU](https://dexscreener.com/solana/difsa6xdswceyxddexgmv9wiplradmvdjggsdhevr834) | SOL | [H7uiPQ...yXpump](https://solscan.io/token/H7uiPQTTq7d8Rhuqw4V6ntroZhakbLCw9PWzuLyXpump) | PVP风险池 | Score 27; Tier Micro; LP $52.8K; Vol24H $1.30M; 24H +155.00%; V/LP 24.57x; 池数 3; 分项 L7/V14/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [𝕏GIFT](https://dexscreener.com/solana/9hlxx5hqjgjjsve1xsdjjjsnzmnhvafximqg7cbtnpp6) | SOL | [FGnzUz...eFpump](https://solscan.io/token/FGnzUzwqULDuZk3WX4CGdKeeZiSwp9kHQKL5HGeFpump) | PVP风险池 | Score 26; Tier Micro; LP $35.2K; Vol24H $3.70M; 24H -48.60%; V/LP 105.07x; 池数 2; 分项 L5/V17/B8/Buy12/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [SOL](https://dexscreener.com/solana/83s1ifx6usw6ggu2har8pxi9yz9mowh5xemmy6x9kxkk) | SOL | [BUphiK...2kpump](https://solscan.io/token/BUphiKNBKbPgKEfbxpRjWeq4qtsUiTi6GiveTX2kpump) | PVP风险池 | Score 9; Tier Micro; LP $38.9K; Vol24H $4.42M; 24H +578.00%; V/LP 113.77x; 池数 2; 分项 L5/V17/B0/Buy3/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 49; Tier Liquid; LP $936.7K; Vol24H $58.93M; 24H -19.97%; V/LP 62.91x; 池数 1; 分项 L18/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [piss](https://dexscreener.com/solana/5ebtmzf6jxeumclew59mu2s34cttep2wncqds2wjbrfh) | SOL | [DXXcq4...cC5kbu](https://solscan.io/token/DXXcq4tY5e4PbXybyBMnxZjHVmzv1GVrAXoW5TcC5kbu) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 32; Tier Micro; LP $65.4K; Vol24H $1.32M; 24H -51.55%; V/LP 20.21x; 池数 1; 分项 L7/V15/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Pondeer](https://dexscreener.com/solana/4btvosm4paw3w5yxdcfqrvhhgkkyni1orgtfn1cpjbxh) | SOL | [5B8qah...hjpump](https://solscan.io/token/5B8qahEJezLtTHPU1Du1AsfAMf4kUVAdaMky7vhjpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Micro; LP $50.6K; Vol24H $2.57M; 24H +461.00%; V/LP 50.76x; 池数 1; 分项 L6/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [WENDU](https://dexscreener.com/solana/difsa6xdswceyxddexgmv9wiplradmvdjggsdhevr834) | SOL | [H7uiPQ...yXpump](https://solscan.io/token/H7uiPQTTq7d8Rhuqw4V6ntroZhakbLCw9PWzuLyXpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $52.8K; Vol24H $1.30M; 24H +155.00%; V/LP 24.57x; 池数 3; 分项 L7/V14/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [𝕏GIFT](https://dexscreener.com/solana/9hlxx5hqjgjjsve1xsdjjjsnzmnhvafximqg7cbtnpp6) | SOL | [FGnzUz...eFpump](https://solscan.io/token/FGnzUzwqULDuZk3WX4CGdKeeZiSwp9kHQKL5HGeFpump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 26; Tier Micro; LP $35.2K; Vol24H $3.70M; 24H -48.60%; V/LP 105.07x; 池数 2; 分项 L5/V17/B8/Buy12/Risk-40 | 只记录热度，不进入主榜 |
| [SOL](https://dexscreener.com/solana/83s1ifx6usw6ggu2har8pxi9yz9mowh5xemmy6x9kxkk) | SOL | [BUphiK...2kpump](https://solscan.io/token/BUphiKNBKbPgKEfbxpRjWeq4qtsUiTi6GiveTX2kpump) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 9; Tier Micro; LP $38.9K; Vol24H $4.42M; 24H +578.00%; V/LP 113.77x; 池数 2; 分项 L5/V17/B0/Buy3/Risk-40 | 只记录热度，不进入主榜 |
| [TBLK](https://dexscreener.com/solana/5t794kxlnd5o6weboretjqb7hwemjqtyrmdpwfuhkxjr) | SOL | [DZTSLo...Lfpump](https://solscan.io/token/DZTSLoJKieNPPGKgkdhaBdLjjnQBaUnb3oRPHNLfpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 8; Tier Micro; LP $3.7K; Vol24H $1.88M; 24H -94.28%; V/LP 515.12x; 池数 4; 分项 L0/V16/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [FRONT](https://dexscreener.com/solana/dvccn83mpxb1gh5talvfu6wuwzbfgu7ecgbayaytcwrl) | SOL | [26Rre7...WApump](https://solscan.io/token/26Rre7jT3jUaU29s6oS6QbLSwpbV2ZSZmouZAFWApump) | LP未达主观察门槛；24H成交合格；24H涨跌幅过热；卖出笔数占优；LP偏薄；Volume/LP极端偏高 | Score 5; Tier Micro; LP $34.5K; Vol24H $2.36M; 24H +184.00%; V/LP 68.51x; 池数 1; 分项 L5/V16/B0/Buy0/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 77; Tier Liquid; LP $1.11M; Vol24H $2.32M; 24H +3.46%; V/LP 2.09x; 池数 2; 分项 L19/V16/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CARDS | SOL | [CARDSc...dKxYjp](https://solscan.io/token/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $3.39M; Vol24H $3.69M; 24H -4.79%; V/LP 1.09x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| IDOL | BSC | [0x3b4d...25ab07](https://bscscan.com/token/0x3b4de3c7855c03bb9f50ea252cd2c9fa1125ab07) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.18M; Vol24H $9.30M; 24H +2.13%; V/LP 7.88x; 池数 1; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| UB | BSC | [0x40b8...db6fde](https://bscscan.com/token/0x40b8129b786d766267a7a118cf8c07e31cdb6fde) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $3.11M; Vol24H $17.59M; 24H +13.39%; V/LP 5.66x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [MET](https://dexscreener.com/solana/5hbf9jp8k5zdrzp9pokpypfqobse5mgcmw6nqodurgcd) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Liquid; LP $901.5K; Vol24H $1.45M; 24H +9.63%; V/LP 1.61x; 池数 1; 分项 L18/V15/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [M](https://dexscreener.com/bsc/0x688aa9136e2d48c4cd4f117a40029c6bc18506f6) | BSC | [0x22b1...c731Fa](https://bscscan.com/token/0x22b1458e780F8fA71E2F84502cEe8B5A3cc731Fa) | 24H接近横盘；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 58; Tier Micro; LP $86.4K; Vol24H $581.2K; 24H +5.15%; V/LP 6.73x; 池数 11; 分项 L9/V12/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [FRAG](https://dexscreener.com/solana/jpqfphdxnejsaguhgcetz74pu5a5ef1fbov5u3an16b) | SOL | [J4Y92j...szpump](https://solscan.io/token/J4Y92jy5Lr9ho1aV41bhguytnzBbsPhZJahmaVszpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memecoin](https://dexscreener.com/solana/ebpudz8eke1tavcrasmaaegzk3wjveesrxmidmxuyxay) | SOL | [Bb4jR9...d7pump](https://solscan.io/token/Bb4jR951QtVjeFAYFLBYXDSMKjbTDroCLPbFLdd7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Jotchua | SOL | [BcHEaa...ySpump](https://solscan.io/token/BcHEaaTCvycPwwsJ9yQTXdHP9X2gCLkznDbZ8VySpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| KINS | SOL | [Tqj8yF...9bpump](https://solscan.io/token/Tqj8yFmagrg7oorpQkVGYR52r96RFTamvWfth9bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| ARX | BSC | [0xd5f6...1ca715](https://bscscan.com/token/0xd5f6ef5deabe61e6d5cdb49bfb6f156f2c1ca715) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| three | SOL | [FeMbDo...VJpump](https://solscan.io/token/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| BASED | BSC | [0x1d28...958e4d](https://bscscan.com/token/0x1d28d989f9e3ccb8b15d0cec601734514f958e4d) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| O | BSC | [0x500a...3bd1c4](https://bscscan.com/token/0x500a02a20b0b0a3f3efccfc0559543f5743bd1c4) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 8 / Early 7 / Liquid 10 / Mature 0 | 下一步可以按层级分别设置进攻规则 |
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
# 自我进化轮巡

**本轮时间 UTC：** 2026-09-25T13:10:25Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 129 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 209 |
| 合并后Token | 129 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 8 |
| PVP风险池 | 8 |
| 成熟池观察 | 7 |
| 低优先观察 | 0 |
| 多池Token | 4 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 12 |
| Liquid层 | 8 |
| Mature层 | 1 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1508，刷新时间 2026-09-21T02:34:44Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 1 个，SOL签名级 1 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 86; Tier Liquid; LP $2.63M; Vol24H $2.60M; 24H +18.42%; V/LP 0.99x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 83; Tier Liquid; LP $903.5K; Vol24H $2.41M; 24H +4.69%; V/LP 2.67x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 83; Tier Liquid; LP $1.69M; Vol24H $995.4K; 24H +1.93%; V/LP 0.59x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 主观察 | Score 76; Tier Early; LP $199.1K; Vol24H $364.4K; 24H -10.18%; V/LP 1.83x; 池数 1; 分项 L12/V11/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 73; Tier Early; LP $125.8K; Vol24H $59.6K; 24H +2.93%; V/LP 0.47x; 池数 1; 分项 L10/V5/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 72; Tier Early; LP $446.9K; Vol24H $455.0K; 24H -20.59%; V/LP 1.02x; 池数 1; 分项 L15/V11/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WAIF](https://dexscreener.com/solana/dgatrsvp1n3m76kpcvbfhhjwotby8lf8ivwkipanh5tk) | SOL | [wFYBNt...EYpump](https://solscan.io/token/wFYBNtZpcXd2NX9eHo7FLHtJRHjfp9F1iRkm3EYpump) | 次观察 | Score 70; Tier Early; LP $224.7K; Vol24H $210.7K; 24H +24.92%; V/LP 0.94x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 次观察 | Score 68; Tier Liquid; LP $2.40M; Vol24H $2.32M; 24H +33.49%; V/LP 0.97x; 池数 1; 分项 L20/V16/B8/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 67; Tier Early; LP $135.1K; Vol24H $129.7K; 24H +0.88%; V/LP 0.96x; 池数 1; 分项 L10/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 66; Tier Early; LP $369.2K; Vol24H $2.92M; 24H +52.42%; V/LP 7.91x; 池数 1; 分项 L14/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 83; Tier Liquid; LP $905.3K; Vol24H $2.47M; 24H +5.48%; V/LP 2.73x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 主观察 | Score 76; Tier Early; LP $195.9K; Vol24H $352.3K; 24H -12.81%; V/LP 1.80x; 池数 1; 分项 L12/V11/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 次观察 | Score 74; Tier Early; LP $391.3K; Vol24H $67.3K; 24H +24.58%; V/LP 0.17x; 池数 1; 分项 L15/V6/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GSTOCK | BSC | [0xcafd...3f9e20](https://bscscan.com/token/0xcafdbce93477261db8250e42bdae6e66733f9e20) | 次观察 | Score 74; Tier Early; LP $696.5K; Vol24H $6.93M; 24H +2.87%; V/LP 9.96x; 池数 1; 分项 L17/V17/B22/Buy12/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 72; Tier Early; LP $479.1K; Vol24H $464.9K; 24H -10.40%; V/LP 0.97x; 池数 1; 分项 L15/V11/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 69; Tier Early; LP $141.3K; Vol24H $60.5K; 24H +24.16%; V/LP 0.43x; 池数 1; 分项 L11/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 次观察 | Score 68; Tier Liquid; LP $2.39M; Vol24H $2.38M; 24H +34.44%; V/LP 0.99x; 池数 1; 分项 L20/V16/B8/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 68; Tier Liquid; LP $1.06M; Vol24H $6.56M; 24H +170.65%; V/LP 6.17x; 池数 1; 分项 L19/V17/B0/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VSOF](https://dexscreener.com/solana/451hyqbfewuhoivemnkvhzxhk7gxsm27b4q7x2bettwp) | SOL | [CQZW8A...4Epump](https://solscan.io/token/CQZW8AzE7y39g2dBnUVBRFnMkg62FpP6mtDAc4Epump) | 次观察 | Score 65; Tier Early; LP $580.4K; Vol24H $195.2K; 24H +32.71%; V/LP 0.34x; 池数 2; 分项 L16/V9/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [AQUA](https://dexscreener.com/solana/9tt3nbwogwjbqh7b3s1hfcqyf7vjhmg8uncxdjtprnh4) | SOL | [AQVcP6...m1FyY9](https://solscan.io/token/AQVcP67EpMyu4cBZZjqMu91cVsWy1aX98JmcZm1FyY9) | 次观察 | Score 64; Tier Early; LP $192.1K; Vol24H $483.1K; 24H +61.66%; V/LP 2.52x; 池数 5; 分项 L12/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 53; Tier Early; LP $628.5K; Vol24H $15.43M; 24H +0.89%; V/LP 24.55x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| GO | SOL | [D1YZZg...rD4F4n](https://solscan.io/token/D1YZZg9dBZ7AbfknZVbaeVLto36eySwoFYEVhZrD4F4n) | PVP风险池 | Score 32; Tier Early; LP $262.2K; Vol24H $8.61M; 24H +425.32%; V/LP 32.85x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [familiars](https://dexscreener.com/solana/enivh49xwrm3cu9n4tp6cgyncfxf3mz6ce3grmvk1lh4) | SOL | [2PENPm...Uupump](https://solscan.io/token/2PENPmfgJfq6CG3k4byj4oWwHf8SerqakmYHMkUupump) | PVP风险池 | Score 31; Tier Micro; LP $91.7K; Vol24H $3.21M; 24H -68.39%; V/LP 35.00x; 池数 1; 分项 L9/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [NPC](https://dexscreener.com/solana/brjma8ualnp3ditkhfdean5riqrypoayez7khywd4oes) | SOL | [7GUnr7...Zepump](https://solscan.io/token/7GUnr7krtQhJwd6ASY2VUprd9t4c64zcgCsjdmZepump) | PVP风险池 | Score 30; Tier Early; LP $173.6K; Vol24H $3.94M; 24H +879.00%; V/LP 22.71x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| COLLECT | SOL | [nDZknL...HVpump](https://solscan.io/token/nDZknLvfFRp5rgUHdzTrQsmSY5NKzoavqdLjSHVpump) | PVP风险池 | Score 29; Tier Early; LP $134.5K; Vol24H $3.82M; 24H +133.44%; V/LP 28.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 53; Tier Early; LP $628.5K; Vol24H $15.43M; 24H +0.89%; V/LP 24.55x; 池数 1; 分项 L17/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| GO | SOL | [D1YZZg...rD4F4n](https://solscan.io/token/D1YZZg9dBZ7AbfknZVbaeVLto36eySwoFYEVhZrD4F4n) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $262.2K; Vol24H $8.61M; 24H +425.32%; V/LP 32.85x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [familiars](https://dexscreener.com/solana/enivh49xwrm3cu9n4tp6cgyncfxf3mz6ce3grmvk1lh4) | SOL | [2PENPm...Uupump](https://solscan.io/token/2PENPmfgJfq6CG3k4byj4oWwHf8SerqakmYHMkUupump) | 24H未过热但已明显波动；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 31; Tier Micro; LP $91.7K; Vol24H $3.21M; 24H -68.39%; V/LP 35.00x; 池数 1; 分项 L9/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [NPC](https://dexscreener.com/solana/brjma8ualnp3ditkhfdean5riqrypoayez7khywd4oes) | SOL | [7GUnr7...Zepump](https://solscan.io/token/7GUnr7krtQhJwd6ASY2VUprd9t4c64zcgCsjdmZepump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $173.6K; Vol24H $3.94M; 24H +879.00%; V/LP 22.71x; 池数 1; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| COLLECT | SOL | [nDZknL...HVpump](https://solscan.io/token/nDZknLvfFRp5rgUHdzTrQsmSY5NKzoavqdLjSHVpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 29; Tier Early; LP $134.5K; Vol24H $3.82M; 24H +133.44%; V/LP 28.39x; 池数 2; 分项 L10/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TTP](https://dexscreener.com/solana/359uv3h3g2zvff14anztwgekayklgdd7ze3kar68n6xr) | SOL | [5iqjhP...Qtpump](https://solscan.io/token/5iqjhP5ig6JWdXQf6hYAwojZeMf11pTCvH87gCQtpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $72.5K; Vol24H $4.22M; 24H +943.00%; V/LP 58.17x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BRAIN](https://dexscreener.com/solana/hnfhnuzp8wt3u2mfg5gws8hbkvd45rkcwohn1i9bjytk) | SOL | [3znS89...kDpump](https://solscan.io/token/3znS89gifim2Hhhu8wjb2PfSgaCDdma187D5NMkDpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $61.2K; Vol24H $4.33M; 24H +649.00%; V/LP 70.82x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [SWARM](https://dexscreener.com/solana/ftjga524yrs7rpzgccezmuqnfdya8pcvwdy5mfmzk5dy) | SOL | [5g9PWc...rRpump](https://solscan.io/token/5g9PWcRUHpmqm5uKycpShKXJB18sGLeCEzgB3qrRpump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 3; Tier Micro; LP $62.2K; Vol24H $1.33M; 24H +778.00%; V/LP 21.42x; 池数 4; 分项 L7/V15/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $4.43M; Vol24H $15.46M; 24H +3.08%; V/LP 3.49x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $3.26M; Vol24H $11.83M; 24H -7.68%; V/LP 3.63x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $57.49M; Vol24H $3.07M; 24H -0.20%; V/LP 0.05x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 73; Tier Liquid; LP $4.42M; Vol24H $2.14M; 24H +4.79%; V/LP 0.48x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Liquid; LP $2.87M; Vol24H $13.42M; 24H -12.46%; V/LP 4.67x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $3.86M; Vol24H $3.11M; 24H +16.78%; V/LP 0.81x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 68; Tier Early; LP $423.2K; Vol24H $1.82M; 24H +3.97%; V/LP 4.30x; 池数 1; 分项 L15/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| GSTOCK | BSC | [0xcafd...3f9e20](https://bscscan.com/token/0xcafdbce93477261db8250e42bdae6e66733f9e20) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VSOF](https://dexscreener.com/solana/451hyqbfewuhoivemnkvhzxhk7gxsm27b4q7x2bettwp) | SOL | [CQZW8A...4Epump](https://solscan.io/token/CQZW8AzE7y39g2dBnUVBRFnMkg62FpP6mtDAc4Epump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [AQUA](https://dexscreener.com/solana/9tt3nbwogwjbqh7b3s1hfcqyf7vjhmg8uncxdjtprnh4) | SOL | [AQVcP6...m1FyY9](https://solscan.io/token/AQVcP67EpMyu4cBZZjqMu91cVsWy1aX98JmcZm1FyY9) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 7 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 4 / Early 12 / Liquid 8 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
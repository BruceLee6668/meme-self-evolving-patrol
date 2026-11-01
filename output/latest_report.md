# 自我进化轮巡

**本轮时间 UTC：** 2026-11-01T20:04:03Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 153 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 238 |
| 合并后Token | 153 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 9 |
| PVP风险池 | 8 |
| 成熟池观察 | 2 |
| 低优先观察 | 2 |
| 多池Token | 9 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 4 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 13 |
| Liquid层 | 4 |
| Mature层 | 1 |
| 需要链上确认 | 22 |
| 紧急精查候选 | 4 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 2235，刷新时间 2026-10-26T02:30:11Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 1 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 主观察 | Score 85; Tier Early; LP $264.6K; Vol24H $1.03M; 24H +4.27%; V/LP 3.90x; 池数 2; 分项 L13/V14/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 主观察 | Score 80; Tier Early; LP $403.9K; Vol24H $2.47M; 24H -23.62%; V/LP 6.12x; 池数 1; 分项 L15/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| GANG | BSC | [0x0c63...20b405](https://bscscan.com/token/0x0c6302401aa5325c2e36f170f52c00b1d220b405) | 主观察 | Score 78; Tier Early; LP $228.3K; Vol24H $579.6K; 24H -3.31%; V/LP 2.54x; 池数 1; 分项 L12/V12/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [TART](https://dexscreener.com/bsc/0x30000a407fabebe29439f8e437050512ff6661be) | BSC | [0x7AB8...750314](https://bscscan.com/token/0x7AB8d02CBb51Ff7223fDe700eAaa2a91Bf750314) | 次观察 | Score 75; Tier Liquid; LP $826.1K; Vol24H $731.0K; 24H +36.95%; V/LP 0.88x; 池数 4; 分项 L18/V13/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 次观察 | Score 75; Tier Early; LP $398.3K; Vol24H $54.6K; 24H -2.23%; V/LP 0.14x; 池数 1; 分项 L15/V5/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 74; Tier Early; LP $201.6K; Vol24H $150.6K; 24H +2.78%; V/LP 0.75x; 池数 1; 分项 L12/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 次观察 | Score 74; Tier Early; LP $377.3K; Vol24H $1.03M; 24H -8.95%; V/LP 2.72x; 池数 1; 分项 L14/V14/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [UODF](https://dexscreener.com/solana/ejdxaggz5iue3wgcsyqqlj6xmqy3byst9evqemhad1g5) | SOL | [emXJL3...n7pump](https://solscan.io/token/emXJL3vjwvyMjSf7pj7bmJDm29F9SBcYxtFURn7pump) | 次观察 | Score 72; Tier Early; LP $445.3K; Vol24H $159.3K; 24H +9.86%; V/LP 0.36x; 池数 1; 分项 L15/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GTA6 | SOL | [4kjruq...pQzDnz](https://solscan.io/token/4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz) | 次观察 | Score 72; Tier Early; LP $323.6K; Vol24H $992.8K; 24H +56.62%; V/LP 3.07x; 池数 1; 分项 L14/V14/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CBUCKS](https://dexscreener.com/solana/b4cp45pgifvm5faxfh6aev8qz3eunqnqgbw7kuc7mhnb) | SOL | [DtcicP...xZpump](https://solscan.io/token/DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump) | 次观察 | Score 70; Tier Early; LP $122.5K; Vol24H $72.6K; 24H +0.92%; V/LP 0.59x; 池数 1; 分项 L10/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 主观察 | Score 85; Tier Early; LP $262.8K; Vol24H $1.08M; 24H +6.05%; V/LP 4.10x; 池数 1; 分项 L13/V14/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 84; Tier Liquid; LP $825.1K; Vol24H $725.1K; 24H +13.95%; V/LP 0.88x; 池数 1; 分项 L18/V13/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 主观察 | Score 78; Tier Early; LP $371.4K; Vol24H $1.10M; 24H -16.61%; V/LP 2.96x; 池数 1; 分项 L14/V14/B17/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 主观察 | Score 76; Tier Early; LP $410.3K; Vol24H $69.6K; 24H +1.49%; V/LP 0.17x; 池数 1; 分项 L15/V6/B22/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 次观察 | Score 74; Tier Early; LP $195.0K; Vol24H $154.3K; 24H -5.99%; V/LP 0.79x; 池数 1; 分项 L12/V8/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| LITY | BSC | [0xd705...c949c8](https://bscscan.com/token/0xd7057e7c56b9c2d5f0a3e639d07610db31c949c8) | 次观察 | Score 74; Tier Liquid; LP $1.18M; Vol24H $377.3K; 24H +73.18%; V/LP 0.32x; 池数 1; 分项 L19/V11/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [AODF](https://dexscreener.com/solana/cr6fx4rbycdxvpvzrst8zjndr2udtpfy9cyoscssugu1) | SOL | [pvRLSb...vBpump](https://solscan.io/token/pvRLSbbBJ93DQW4i2eNwQN3NXPvQafdv5HAA6vBpump) | 次观察 | Score 70; Tier Early; LP $242.8K; Vol24H $161.0K; 24H +14.00%; V/LP 0.66x; 池数 2; 分项 L13/V8/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 次观察 | Score 70; Tier Early; LP $375.8K; Vol24H $2.24M; 24H -32.93%; V/LP 5.95x; 池数 1; 分项 L14/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [jeff](https://dexscreener.com/solana/jcxwfczgjgjc8nza5qb6jp3cgvqw4vgug4tqj87g5zny) | SOL | [HAsTKX...gqwP6k](https://solscan.io/token/HAsTKXYvv65zM7J6Cu5o5PcZsiKMQYo5oz4WPjgqwP6k) | 次观察 | Score 68; Tier Early; LP $110.8K; Vol24H $192.6K; 24H -14.87%; V/LP 1.74x; 池数 2; 分项 L10/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Peekhole](https://dexscreener.com/solana/g5t63jxflosyapfvystqn1wwqm7yx9wbz7xnffoutczf) | SOL | [2Nyb2G...VDpump](https://solscan.io/token/2Nyb2GXVoXM42hVQxJg5RppTbiN5SCZFL4LtZVVDpump) | 次观察 | Score 68; Tier Micro; LP $52.8K; Vol24H $261.6K; 24H -2.87%; V/LP 4.96x; 池数 1; 分项 L7/V10/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EXFIL](https://dexscreener.com/solana/2zpfdgd48k7b2u9yqz4hjspaptovu9uiebfqyxeoexkv) | SOL | [6FhVPc...y6pump](https://solscan.io/token/6FhVPctYg363pQbs4iSvqyHe2cJzfsvFD96gePy6pump) | 次观察 | Score 67; Tier Early; LP $172.3K; Vol24H $94.5K; 24H -7.55%; V/LP 0.55x; 池数 1; 分项 L11/V7/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JCT | BSC | [0xea37...b17707](https://bscscan.com/token/0xea37a8de1de2d9d10772eeb569e28bfa5cb17707) | 次观察 | Score 66; Tier Liquid; LP $832.8K; Vol24H $8.91M; 24H -1.07%; V/LP 10.70x; 池数 1; 分项 L18/V17/B22/Buy3/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| GTA6 | SOL | [4kjruq...pQzDnz](https://solscan.io/token/4kjruqGHDsSqkMdFfCjV7Vb62HPFhtXyWc2t6JpQzDnz) | 次观察 | Score 66; Tier Early; LP $328.7K; Vol24H $613.4K; 24H +74.85%; V/LP 1.87x; 池数 1; 分项 L14/V12/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [AAPLCAT](https://dexscreener.com/solana/6bnptaekgetqfgqgdwidhfqagamhusyqxqjnllw74exw) | SOL | [GYKnd6...y5pump](https://solscan.io/token/GYKnd6jGUSQoBUnj6LdGCBtCWYDgr2Zd6QwNPcy5pump) | PVP风险池 | Score 39; Tier Micro; LP $67.6K; Vol24H $4.52M; 24H +34.18%; V/LP 66.89x; 池数 1; 分项 L8/V17/B8/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| FOCO | SOL | [7ttfwu...Gmpump](https://solscan.io/token/7ttfwuBSnbNTgf32gUAT7v9bjdDWsn6pYpp7nmGmpump) | PVP风险池 | Score 38; Tier Micro; LP $69.6K; Vol24H $1.88M; 24H -10.68%; V/LP 27.09x; 池数 1; 分项 L8/V16/B17/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [AAPLCAT](https://dexscreener.com/solana/6bnptaekgetqfgqgdwidhfqagamhusyqxqjnllw74exw) | SOL | [GYKnd6...y5pump](https://solscan.io/token/GYKnd6jGUSQoBUnj6LdGCBtCWYDgr2Zd6QwNPcy5pump) | 24H未过热但已明显波动；买入笔数占优；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 39; Tier Micro; LP $67.6K; Vol24H $4.52M; 24H +34.18%; V/LP 66.89x; 池数 1; 分项 L8/V17/B8/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| FOCO | SOL | [7ttfwu...Gmpump](https://solscan.io/token/7ttfwuBSnbNTgf32gUAT7v9bjdDWsn6pYpp7nmGmpump) | 24H波动可控；买卖基本均衡；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Micro; LP $69.6K; Vol24H $1.88M; 24H -10.68%; V/LP 27.09x; 池数 1; 分项 L8/V16/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| Anakin | SOL | [ExxzYB...6Xpump](https://solscan.io/token/ExxzYBTt3jwU5MUxuw2F4toYbTLdFwThSjyaCn6Xpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $144.2K; Vol24H $3.64M; 24H +271.23%; V/LP 25.21x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AIN | BSC | [0x9558...84f4a3](https://bscscan.com/token/0x9558a9254890b2a8b057a789f413631b9084f4a3) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；成熟大市值 | Score 29; Tier Early; LP $126.0K; Vol24H $3.25M; 24H +22.62%; V/LP 25.78x; 池数 1; 分项 L10/V17/B17/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| ANSEM | SOL | [CvRJ8M...DTpump](https://solscan.io/token/CvRJ8MrnB1AwjrgX25uyeLJiXNSugTo2ZHh8UXDTpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $75.5K; Vol24H $2.63M; 24H +793.22%; V/LP 34.78x; 池数 4; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [KIM](https://dexscreener.com/solana/abeqlwad4nqi37xvtzcpuo953chclqbucuyc8mhdp4eq) | SOL | [8pjfN5...x1pump](https://solscan.io/token/8pjfN5Ayb4rucGpYE3tZWN6v3EysizjPx1v62zx1pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $46.1K; Vol24H $6.73M; 24H +411.00%; V/LP 145.91x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| BLUE | SOL | [CPoGSm...rzpump](https://solscan.io/token/CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $35.5K; Vol24H $3.82M; 24H +271.25%; V/LP 107.77x; 池数 2; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [REGRETAMINE](https://dexscreener.com/solana/8ydjl2ehenultqzus1wbhdqm2tw1jcdiwazttokq7pq8) | SOL | [Dbyy9L...3t5xeT](https://solscan.io/token/Dbyy9LSMVHjxw2ZnPPRrCheSLVeuHq2GMkpxUs3t5xeT) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 11; Tier Micro; LP $28.1K; Vol24H $1.71M; 24H +189.00%; V/LP 60.80x; 池数 2; 分项 L4/V15/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 75; Tier Liquid; LP $2.43M; Vol24H $885.3K; 24H -3.66%; V/LP 0.36x; 池数 1; 分项 L20/V13/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $58.05M; Vol24H $3.41M; 24H +0.02%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [IOF](https://dexscreener.com/solana/7wcareycymxe2olsuaptqg4ybx5hfh1msinrhq4pvhjm) | SOL | [2sY7rk...6Bpump](https://solscan.io/token/2sY7rkMCQyFNcSpHm3fciJf2ptYRg3cYpn4srN6Bpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| LITY | BSC | [0xd705...c949c8](https://bscscan.com/token/0xd7057e7c56b9c2d5f0a3e639d07610db31c949c8) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [AODF](https://dexscreener.com/solana/cr6fx4rbycdxvpvzrst8zjndr2udtpfy9cyoscssugu1) | SOL | [pvRLSb...vBpump](https://solscan.io/token/pvRLSbbBJ93DQW4i2eNwQN3NXPvQafdv5HAA6vBpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [DESSA](https://dexscreener.com/solana/dextcer4k9dwbxtmu8znvvwgevvmvhmb183pf2xxzwvh) | SOL | [npz2Fh...Svpump](https://solscan.io/token/npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [jeff](https://dexscreener.com/solana/jcxwfczgjgjc8nza5qb6jp3cgvqw4vgug4tqj87g5zny) | SOL | [HAsTKX...gqwP6k](https://solscan.io/token/HAsTKXYvv65zM7J6Cu5o5PcZsiKMQYo5oz4WPjgqwP6k) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [Peekhole](https://dexscreener.com/solana/g5t63jxflosyapfvystqn1wwqm7yx9wbz7xnffoutczf) | SOL | [2Nyb2G...VDpump](https://solscan.io/token/2Nyb2GXVoXM42hVQxJg5RppTbiN5SCZFL4LtZVVDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [Dacity](https://dexscreener.com/solana/g2uurbmvdzdfp4qyobjrskbxsi7d6v4bpp9thps36y4b) | SOL | [nxPqZ4...Rjpump](https://solscan.io/token/nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [XCAT](https://dexscreener.com/solana/8kxzr2bikmkcgzhp4srlgyhbpsqqwzk2echqhxqrd589) | SOL | [1226TM...e5xfun](https://solscan.io/token/1226TMaWZiZYWdP7CBZBqfJGXoWXaKXJJiKf45e5xfun) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 2 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 7 / Early 13 / Liquid 4 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
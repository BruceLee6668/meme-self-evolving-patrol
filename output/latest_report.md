# 自我进化轮巡

**本轮时间 UTC：** 2026-09-15T10:52:13Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 122 个合并Token中筛出 2 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 221 |
| 合并后Token | 122 |
| 输出候选 | 25 |
| 主观察 | 2 |
| 次观察 | 3 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 6 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 12 |
| Liquid层 | 5 |
| Mature层 | 2 |
| 需要链上确认 | 14 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1323，刷新时间 2026-09-14T02:37:35Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 2 个，BSC Transfer样本 0 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $2.80M; Vol24H $10.52M; 24H +1.55%; V/LP 3.76x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 主观察 | Score 80; Tier Early; LP $520.3K; Vol24H $1.69M; 24H +7.39%; V/LP 3.24x; 池数 1; 分项 L16/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 72; Tier Micro; LP $82.3K; Vol24H $383.8K; 24H +22.00%; V/LP 4.66x; 池数 2; 分项 L8/V11/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 72; Tier Early; LP $585.0K; Vol24H $2.34M; 24H -34.87%; V/LP 4.00x; 池数 1; 分项 L16/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VJRA](https://dexscreener.com/solana/7trxshpnnefuerqosc6evbmcb6subfiqvuj9ngwnband) | SOL | [6eAecV...iQHCya](https://solscan.io/token/6eAecVV5kkahx9RLrMWW2RPuRdWqBJkHePAaX8iQHCya) | 次观察 | Score 70; Tier Early; LP $138.8K; Vol24H $70.2K; 24H +0.18%; V/LP 0.51x; 池数 1; 分项 L10/V6/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| b-money | BSC | [0xf497...da7777](https://bscscan.com/token/0xf49725118cb0707b8706ffffe895f3ab16da7777) | 次观察 | Score 68; Tier Early; LP $265.7K; Vol24H $1.71M; 24H -49.31%; V/LP 6.43x; 池数 1; 分项 L13/V15/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | 次观察 | Score 66; Tier Early; LP $194.8K; Vol24H $937.8K; 24H -54.62%; V/LP 4.81x; 池数 1; 分项 L12/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Fapcoin](https://dexscreener.com/solana/aypfy111g9nt1jvunymtjd9is2m8c3pbveosmx9echeu) | SOL | [8vGr1e...Mrpump](https://solscan.io/token/8vGr1eX9vfpootWiUPYa5kYoGx9bTuRy2Xc4dNMrpump) | 次观察 | Score 64; Tier Early; LP $189.5K; Vol24H $124.3K; 24H -9.31%; V/LP 0.66x; 池数 1; 分项 L12/V8/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 52; Tier Early; LP $456.6K; Vol24H $154.79M; 24H -24.99%; V/LP 338.99x; 池数 1; 分项 L15/V17/B17/Buy12/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [biketyson](https://dexscreener.com/solana/41rztmb7jhptymxzrywdqnbecjrhkb8khyajrq9cyxjx) | SOL | [CbyTNf...Pwpump](https://solscan.io/token/CbyTNf7UPzvewHh4Zp6umogM2RWahhmGRJWLJnPwpump) | PVP风险池 | Score 41; Tier Early; LP $301.7K; Vol24H $12.76M; 24H +62.57%; V/LP 42.27x; 池数 2; 分项 L14/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $2.75M; Vol24H $8.73M; 24H -5.73%; V/LP 3.18x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 主观察 | Score 80; Tier Early; LP $512.8K; Vol24H $1.30M; 24H -1.94%; V/LP 2.54x; 池数 2; 分项 L16/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 次观察 | Score 73; Tier Early; LP $508.8K; Vol24H $2.58M; 24H -48.94%; V/LP 5.07x; 池数 1; 分项 L16/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 71; Tier Micro; LP $74.1K; Vol24H $293.9K; 24H -20.51%; V/LP 3.96x; 池数 2; 分项 L8/V10/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | 次观察 | Score 66; Tier Early; LP $191.0K; Vol24H $1.01M; 24H -46.37%; V/LP 5.26x; 池数 1; 分项 L12/V14/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 43; Tier Early; LP $424.4K; Vol24H $46.58M; 24H -34.52%; V/LP 109.74x; 池数 1; 分项 L15/V17/B8/Buy12/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| biketyson | SOL | [CbyTNf...Pwpump](https://solscan.io/token/CbyTNf7UPzvewHh4Zp6umogM2RWahhmGRJWLJnPwpump) | PVP风险池 | Score 40; Tier Early; LP $291.8K; Vol24H $12.23M; 24H +32.50%; V/LP 41.92x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | PVP风险池 | Score 38; Tier Early; LP $577.6K; Vol24H $23.10M; 24H +36.49%; V/LP 39.99x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BEM | BSC | [0x5ce0...8b695a](https://bscscan.com/token/0x5ce033b2bfca3af30b3e8c8457deaf776a8b695a) | PVP风险池 | Score 38; Tier Early; LP $163.5K; Vol24H $3.47M; 24H -29.55%; V/LP 21.25x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BORT | BSC | [0x2a84...374444](https://bscscan.com/token/0x2a846aaaf896ef393ccb76398c1d96ea97374444) | PVP风险池 | Score 34; Tier Early; LP $428.1K; Vol24H $8.58M; 24H +471.89%; V/LP 20.05x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [HUHCAT](https://dexscreener.com/solana/bnpwtuygve7g1v2nfarqvcfvcu4czjvwamduxevqyvrd) | SOL | [A9AHYe...FHKRdH](https://solscan.io/token/A9AHYeqb7nQk7LZUraw7rBCzYRjy2DRvE6NqWfFHKRdH) | PVP风险池 | Score 27; Tier Micro; LP $77.2K; Vol24H $5.46M; 24H +1497.00%; V/LP 70.73x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BRAIN](https://dexscreener.com/solana/5bit6a2sp9bfkxqcuwacataaar6wmqqz8zpjdm2tuarj) | SOL | [9LuwgF...L2pump](https://solscan.io/token/9LuwgFQemAoV9rgVBBtwbRSxBmamcRRbysEK8yL2pump) | PVP风险池 | Score 26; Tier Micro; LP $53.3K; Vol24H $5.54M; 24H +566.00%; V/LP 104.02x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [bruh](https://dexscreener.com/solana/f6snsqpyaxts6ghdw1vrsbvphjjffmfxk5rzegf57c56) | SOL | [6tRotG...BnpYmq](https://solscan.io/token/6tRotGypA5QJKwmfgGFe4yp36eNQ4Vz7m8MNNpBnpYmq) | PVP风险池 | Score 0; Tier Micro; LP $41.5K; Vol24H $2.93M; 24H +418.00%; V/LP 70.71x; 池数 5; 分项 L6/V17/B0/Buy8/Risk-65 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 成熟池观察 | Score 79; Tier Mature; LP $20.65M; Vol24H $9.37M; 24H +1.20%; V/LP 0.45x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 成熟池观察 | Score 79; Tier Liquid; LP $2.80M; Vol24H $7.82M; 24H -1.42%; V/LP 2.79x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 24H未过热但已明显波动；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 43; Tier Early; LP $424.4K; Vol24H $46.58M; 24H -34.52%; V/LP 109.74x; 池数 1; 分项 L15/V17/B8/Buy12/Risk-33 | 只记录热度，不进入主榜 |
| biketyson | SOL | [CbyTNf...Pwpump](https://solscan.io/token/CbyTNf7UPzvewHh4Zp6umogM2RWahhmGRJWLJnPwpump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 40; Tier Early; LP $291.8K; Vol24H $12.23M; 24H +32.50%; V/LP 41.92x; 池数 2; 分项 L13/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $577.6K; Vol24H $23.10M; 24H +36.49%; V/LP 39.99x; 池数 1; 分项 L16/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| BEM | BSC | [0x5ce0...8b695a](https://bscscan.com/token/0x5ce033b2bfca3af30b3e8c8457deaf776a8b695a) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 38; Tier Early; LP $163.5K; Vol24H $3.47M; 24H -29.55%; V/LP 21.25x; 池数 1; 分项 L11/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BORT | BSC | [0x2a84...374444](https://bscscan.com/token/0x2a846aaaf896ef393ccb76398c1d96ea97374444) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Early; LP $428.1K; Vol24H $8.58M; 24H +471.89%; V/LP 20.05x; 池数 1; 分项 L15/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [HUHCAT](https://dexscreener.com/solana/bnpwtuygve7g1v2nfarqvcfvcu4czjvwamduxevqyvrd) | SOL | [A9AHYe...FHKRdH](https://solscan.io/token/A9AHYeqb7nQk7LZUraw7rBCzYRjy2DRvE6NqWfFHKRdH) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $77.2K; Vol24H $5.46M; 24H +1497.00%; V/LP 70.73x; 池数 1; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [BRAIN](https://dexscreener.com/solana/5bit6a2sp9bfkxqcuwacataaar6wmqqz8zpjdm2tuarj) | SOL | [9LuwgF...L2pump](https://solscan.io/token/9LuwgFQemAoV9rgVBBtwbRSxBmamcRRbysEK8yL2pump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 26; Tier Micro; LP $53.3K; Vol24H $5.54M; 24H +566.00%; V/LP 104.02x; 池数 1; 分项 L7/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [bruh](https://dexscreener.com/solana/f6snsqpyaxts6ghdw1vrsbvphjjffmfxk5rzegf57c56) | SOL | [6tRotG...BnpYmq](https://solscan.io/token/6tRotGypA5QJKwmfgGFe4yp36eNQ4Vz7m8MNNpBnpYmq) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高；年轻币短期暴拉 | Score 0; Tier Micro; LP $41.5K; Vol24H $2.93M; 24H +418.00%; V/LP 70.71x; 池数 5; 分项 L6/V17/B0/Buy8/Risk-65 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $20.65M; Vol24H $9.37M; 24H +1.20%; V/LP 0.45x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $2.80M; Vol24H $7.82M; 24H -1.42%; V/LP 2.79x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [ANSEM](https://dexscreener.com/solana/fnzky6x7entq1er3d225dqyt7ybfka4pskbmqhb8l3cc) | SOL | [9cRCn9...TGpump](https://solscan.io/token/9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.05M; Vol24H $3.16M; 24H -16.16%; V/LP 1.54x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 73; Tier Liquid; LP $1.29M; Vol24H $5.82M; 24H -2.91%; V/LP 4.51x; 池数 5; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $26.00M; Vol24H $13.30M; 24H -0.98%; V/LP 0.51x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ZCAT | SOL | [HcRLc9...qiDeJR](https://solscan.io/token/HcRLc9VDgjLeK154xDawfb1dmVJ98DoSqcwTHGqiDeJR) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 68; Tier Liquid; LP $1.28M; Vol24H $3.23M; 24H +10.03%; V/LP 2.53x; 池数 1; 分项 L19/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Sue | BSC | [0x2ab8...2b7777](https://bscscan.com/token/0x2ab8a4dd2191989ac2898006df350b236d2b7777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| biketyson | SOL | [CbyTNf...Pwpump](https://solscan.io/token/CbyTNf7UPzvewHh4Zp6umogM2RWahhmGRJWLJnPwpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| POWER | BSC | [0x9dc4...ea1223](https://bscscan.com/token/0x9dc44ae5be187eca9e2a67e33f27a4c91cea1223) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| BEM | BSC | [0x5ce0...8b695a](https://bscscan.com/token/0x5ce033b2bfca3af30b3e8c8457deaf776a8b695a) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| fone | SOL | [CTPoyC...gGpump](https://solscan.io/token/CTPoyCwkjMvoJwU4xvZZqoD8tiYk6yDchySiN5gGpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 6 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 12 / Liquid 5 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
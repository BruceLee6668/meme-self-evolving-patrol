# 自我进化轮巡

**本轮时间 UTC：** 2026-09-21T05:47:39Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 138 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 212 |
| 合并后Token | 138 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 3 |
| 多池Token | 9 |
| 多池冲突 | 2 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 12 |
| Liquid层 | 6 |
| Mature层 | 3 |
| 需要链上确认 | 17 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1508，刷新时间 2026-09-21T02:34:44Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 2 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 主观察 | Score 85; Tier Liquid; LP $1.83M; Vol24H $2.37M; 24H +17.86%; V/LP 1.30x; 池数 1; 分项 L20/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 82; Tier Liquid; LP $1.67M; Vol24H $751.3K; 24H -3.53%; V/LP 0.45x; 池数 1; 分项 L20/V13/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| APM | BSC | [0x72a2...a0921e](https://bscscan.com/token/0x72a22faa6a522c81a8f5d508381e18af3da0921e) | 主观察 | Score 80; Tier Liquid; LP $1.83M; Vol24H $2.40M; 24H +10.39%; V/LP 1.31x; 池数 1; 分项 L20/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [WOJAK](https://dexscreener.com/solana/fdry5i5kuadz1ik8gps26qjj9rw9mpufxmeggc2hnsp7) | SOL | [8J69rb...5rpump](https://solscan.io/token/8J69rbLTzWWgUJziFY8jeu5tDwEPBwUz4pKBMr5rpump) | 主观察 | Score 77; Tier Early; LP $370.5K; Vol24H $1.09M; 24H -14.52%; V/LP 2.95x; 池数 1; 分项 L14/V14/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 次观察 | Score 72; Tier Early; LP $332.0K; Vol24H $196.6K; 24H +17.42%; V/LP 0.59x; 池数 2; 分项 L14/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 次观察 | Score 67; Tier Early; LP $600.6K; Vol24H $984.4K; 24H +71.64%; V/LP 1.64x; 池数 1; 分项 L16/V14/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 67; Tier Early; LP $362.8K; Vol24H $537.0K; 24H +18.39%; V/LP 1.48x; 池数 1; 分项 L14/V12/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 64; Tier Early; LP $116.2K; Vol24H $298.4K; 24H +39.48%; V/LP 2.57x; 池数 1; 分项 L10/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| JEANPHIL | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | PVP风险池 | Score 48; Tier Early; LP $222.7K; Vol24H $17.47M; 24H +11.87%; V/LP 78.43x; 池数 2; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 39; Tier Liquid; LP $3.36M; Vol24H $67.97M; 24H -16.08%; V/LP 20.24x; 池数 1; 分项 L20/V17/B17/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 主观察 | Score 86; Tier Early; LP $447.6K; Vol24H $672.1K; 24H -3.43%; V/LP 1.50x; 池数 1; 分项 L15/V13/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.25M; Vol24H $1.66M; 24H -0.58%; V/LP 0.39x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 81; Tier Liquid; LP $1.65M; Vol24H $653.7K; 24H -2.74%; V/LP 0.40x; 池数 1; 分项 L20/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 主观察 | Score 77; Tier Liquid; LP $1.88M; Vol24H $2.67M; 24H +33.83%; V/LP 1.42x; 池数 1; 分项 L20/V17/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 次观察 | Score 72; Tier Early; LP $336.2K; Vol24H $195.5K; 24H +17.95%; V/LP 0.58x; 池数 2; 分项 L14/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VSOF](https://dexscreener.com/solana/ddvn2ktwmiz24i5zec12hgxcz3mkef9ccag5fpgjrh6f) | SOL | [wFDy7P...EPpump](https://solscan.io/token/wFDy7PZiyNz2YxP4GsnHMhNBGNjEwhMUxiCNyEPpump) | 次观察 | Score 71; Tier Early; LP $238.0K; Vol24H $196.8K; 24H +22.14%; V/LP 0.83x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 次观察 | Score 69; Tier Early; LP $444.6K; Vol24H $268.4K; 24H +40.94%; V/LP 0.60x; 池数 1; 分项 L15/V10/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 次观察 | Score 65; Tier Early; LP $659.7K; Vol24H $9.63M; 24H -14.54%; V/LP 14.60x; 池数 1; 分项 L17/V17/B17/Buy8/Risk-18 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | PVP风险池 | Score 48; Tier Early; LP $214.9K; Vol24H $16.38M; 24H +11.26%; V/LP 76.24x; 池数 2; 分项 L12/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [TIPPED](https://dexscreener.com/solana/cjieb7fumhefmaefjaxqjnkvxnmvabm3dhhp8rtgbeg1) | SOL | [tipp4C...rKf5BS](https://solscan.io/token/tipp4C4Jnpft26HC9VXNjUPidojZqxXf8nzKvrKf5BS) | PVP风险池 | Score 42; Tier Micro; LP $60.9K; Vol24H $1.92M; 24H -16.98%; V/LP 31.56x; 池数 1; 分项 L7/V16/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [METCAT](https://dexscreener.com/solana/dk24kwogiwjyvfmbnm8vcwxmydyeegbmnuudlltiiw9y) | SOL | [4yFh2v...n3FVcg](https://solscan.io/token/4yFh2vMdY99TWv7uEaDBP16Ar3qmNaU4HtMbD6n3FVcg) | PVP风险池 | Score 33; Tier Micro; LP $31.2K; Vol24H $56.49M; 24H -5.70%; V/LP 1808.03x; 池数 1; 分项 L5/V17/B22/Buy8/Risk-43 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [JEANJAK](https://dexscreener.com/solana/7kxuejaz8xch5g2xmkaucmeraxvvvzndf7qrydisw7o5) | SOL | [CDAC33...dXpump](https://solscan.io/token/CDAC33JvozJ1UjxBMkvZgJcVXoxdH9iGxeBXUJdXpump) | PVP风险池 | Score 33; Tier Early; LP $109.6K; Vol24H $4.60M; 24H +1267.00%; V/LP 42.00x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Stamp | SOL | [EKtmPP...Siinsc](https://solscan.io/token/EKtmPPLaCbEEKiwoHHtV7TsRsmPXs5CMGtQtZFSiinsc) | PVP风险池 | Score 32; Tier Early; LP $265.0K; Vol24H $12.94M; 24H +451.62%; V/LP 48.82x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | PVP风险池 | Score 30; Tier Liquid; LP $2.90M; Vol24H $69.20M; 24H -48.70%; V/LP 23.87x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | PVP风险池 | Score 28; Tier Early; LP $138.2K; Vol24H $209.09M; 24H +0.81%; V/LP 1513.08x; 池数 1; 分项 L10/V17/B22/Buy0/Risk-45 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 48; Tier Early; LP $214.9K; Vol24H $16.38M; 24H +11.26%; V/LP 76.24x; 池数 2; 分项 L12/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [TIPPED](https://dexscreener.com/solana/cjieb7fumhefmaefjaxqjnkvxnmvabm3dhhp8rtgbeg1) | SOL | [tipp4C...rKf5BS](https://solscan.io/token/tipp4C4Jnpft26HC9VXNjUPidojZqxXf8nzKvrKf5BS) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 42; Tier Micro; LP $60.9K; Vol24H $1.92M; 24H -16.98%; V/LP 31.56x; 池数 1; 分项 L7/V16/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [METCAT](https://dexscreener.com/solana/dk24kwogiwjyvfmbnm8vcwxmydyeegbmnuudlltiiw9y) | SOL | [4yFh2v...n3FVcg](https://solscan.io/token/4yFh2vMdY99TWv7uEaDBP16Ar3qmNaU4HtMbD6n3FVcg) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高；非主流报价池 | Score 33; Tier Micro; LP $31.2K; Vol24H $56.49M; 24H -5.70%; V/LP 1808.03x; 池数 1; 分项 L5/V17/B22/Buy8/Risk-43 | 只记录热度，不进入主榜 |
| [JEANJAK](https://dexscreener.com/solana/7kxuejaz8xch5g2xmkaucmeraxvvvzndf7qrydisw7o5) | SOL | [CDAC33...dXpump](https://solscan.io/token/CDAC33JvozJ1UjxBMkvZgJcVXoxdH9iGxeBXUJdXpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 33; Tier Early; LP $109.6K; Vol24H $4.60M; 24H +1267.00%; V/LP 42.00x; 池数 1; 分项 L10/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| Stamp | SOL | [EKtmPP...Siinsc](https://solscan.io/token/EKtmPPLaCbEEKiwoHHtV7TsRsmPXs5CMGtQtZFSiinsc) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $265.0K; Vol24H $12.94M; 24H +451.62%; V/LP 48.82x; 池数 2; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 30; Tier Liquid; LP $2.90M; Vol24H $69.20M; 24H -48.70%; V/LP 23.87x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-42 | 只记录热度，不进入主榜 |
| [MET](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [METvsv...n6mWQL](https://solscan.io/token/METvsvVRapdj9cFLzq4Tr43xK4tAjQfwX76z3n6mWQL) | 24H接近横盘；LP达主观察门槛；24H成交合格；卖出笔数占优；Volume/LP极端偏高；非主流报价池；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 28; Tier Early; LP $138.2K; Vol24H $209.09M; 24H +0.81%; V/LP 1513.08x; 池数 1; 分项 L10/V17/B22/Buy0/Risk-45 | 只记录热度，不进入主榜 |
| ZEBRA | SOL | [EqFG72...BnwN8Q](https://solscan.io/token/EqFG72Z35r8cAV8mKu3UK2L8NUTR1ZNyMr88E4BnwN8Q) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $76.0K; Vol24H $6.38M; 24H +1057.38%; V/LP 83.96x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Liquid; LP $3.53M; Vol24H $4.63M; 24H -15.89%; V/LP 1.31x; 池数 2; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $56.68M; Vol24H $4.28M; 24H +1.58%; V/LP 0.08x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 74; Tier Early; LP $448.6K; Vol24H $3.11M; 24H -1.53%; V/LP 6.93x; 池数 1; 分项 L15/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $27.86M; Vol24H $23.02M; 24H +1.45%; V/LP 0.83x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 65; Tier Mature; LP $7.32M; Vol24H $7.28M; 24H +40.14%; V/LP 0.99x; 池数 2; 分项 L20/V17/B8/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BP | SOL | [BPxxfR...VBjPCy](https://solscan.io/token/BPxxfRCXkUVhig4HS1Lh7kZqV6SPJhzfEk4x6fVBjPCy) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 60; Tier Liquid; LP $3.97M; Vol24H $13.95M; 24H +41.93%; V/LP 3.51x; 池数 1; 分项 L20/V17/B8/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/9wnusyffb3n74db7zcj9xrv4nf3nr8p689eq5zrow1ez) | SOL | [ireZB2...tQpump](https://solscan.io/token/ireZB2cgtfvFcVQGLYRAzaugVapAzsjgJ1cMetQpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [VSOF](https://dexscreener.com/solana/ddvn2ktwmiz24i5zec12hgxcz3mkef9ccag5fpgjrh6f) | SOL | [wFDy7P...EPpump](https://solscan.io/token/wFDy7PZiyNz2YxP4GsnHMhNBGNjEwhMUxiCNyEPpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [CWD](https://dexscreener.com/solana/flfqvzznqqxf8gxlyewrcgeldbyzx9rtjkfxifagnxhs) | SOL | [D7unee...F8a7EN](https://solscan.io/token/D7uneejj16Wehftz7uUK9uqeWisWgaYwsscu2EF8a7EN) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [OTC](https://dexscreener.com/solana/da4pm4xsdy4m9v4cgakkbvh1pw1ysctqqa5nekghukpt) | SOL | [MukLDt...udpump](https://solscan.io/token/MukLDtJ8Cx9DxLbeyLRSWPSposTMWuwHANbuaudpump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 4 / Early 12 / Liquid 6 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
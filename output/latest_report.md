# 自我进化轮巡

**本轮时间 UTC：** 2026-09-30T13:15:13Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 138 个合并Token中筛出 4 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 225 |
| 合并后Token | 138 |
| 输出候选 | 25 |
| 主观察 | 4 |
| 次观察 | 4 |
| PVP风险池 | 8 |
| 成熟池观察 | 6 |
| 低优先观察 | 3 |
| 多池Token | 7 |
| 多池冲突 | 4 |
| Symbol桥接合并 | 3 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 7 |
| Early层 | 10 |
| Liquid层 | 6 |
| Mature层 | 2 |
| 需要链上确认 | 18 |
| 紧急精查候选 | 2 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1651，刷新时间 2026-09-28T02:48:12Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 4 个，BSC Transfer样本 1 个，SOL签名级 3 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $3.31M; Vol24H $4.72M; 24H -7.14%; V/LP 1.43x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 主观察 | Score 81; Tier Liquid; LP $2.31M; Vol24H $3.16M; 24H -21.73%; V/LP 1.37x; 池数 8; 分项 L20/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 主观察 | Score 80; Tier Early; LP $272.8K; Vol24H $1.02M; 24H -9.97%; V/LP 3.75x; 池数 1; 分项 L13/V14/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| TART | BSC | [0x7ab8...750314](https://bscscan.com/token/0x7ab8d02cbb51ff7223fde700eaaa2a91bf750314) | 主观察 | Score 78; Tier Early; LP $433.2K; Vol24H $209.9K; 24H +3.78%; V/LP 0.48x; 池数 1; 分项 L15/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [NPC](https://dexscreener.com/solana/gakq4tpvxvzqtvnuapwnk4exggb3e3djhgnw4b9bm8ft) | SOL | [ESEdbg...sNpump](https://solscan.io/token/ESEdbgAw2mgkVTPhCz1pbBbKdAmFAFgqu9i1gpsNpump) | 次观察 | Score 78; Tier Micro; LP $71.1K; Vol24H $544.4K; 24H +5.13%; V/LP 7.66x; 池数 1; 分项 L8/V12/B22/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WOTF](https://dexscreener.com/solana/d3qnza8tklggt3vg9jkqy7zwcz2fctvekzth6jf2kmzy) | SOL | [drLg3v...T7pump](https://solscan.io/token/drLg3vH1p7KVK7YrXSNSPJxtGVDwLy3mHsVofT7pump) | 次观察 | Score 74; Tier Early; LP $574.6K; Vol24H $213.7K; 24H +12.05%; V/LP 0.37x; 池数 1; 分项 L16/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 73; Tier Liquid; LP $1.16M; Vol24H $286.2K; 24H +10.20%; V/LP 0.25x; 池数 1; 分项 L19/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 71; Tier Early; LP $340.9K; Vol24H $451.4K; 24H -13.94%; V/LP 1.32x; 池数 1; 分项 L14/V11/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 次观察 | Score 69; Tier Liquid; LP $760.2K; Vol24H $4.30M; 24H -26.24%; V/LP 5.66x; 池数 2; 分项 L17/V17/B8/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [Pumpoween](https://dexscreener.com/solana/8nvfb1unnk9adtl5hoof8hahf2rt4glpwx9cteadikhg) | SOL | [5Gefef...vFpump](https://solscan.io/token/5GefefPX1mDs6ZJB1apYmz6fCTCiNJpHturZ9bvFpump) | 次观察 | Score 64; Tier Micro; LP $97.3K; Vol24H $178.1K; 24H +5.62%; V/LP 1.83x; 池数 1; 分项 L9/V9/B22/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 主观察 | Score 91; Tier Liquid; LP $3.30M; Vol24H $4.73M; 24H -2.68%; V/LP 1.43x; 池数 2; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 主观察 | Score 84; Tier Liquid; LP $4.35M; Vol24H $1.48M; 24H +1.26%; V/LP 0.34x; 池数 1; 分项 L20/V15/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 78; Tier Early; LP $706.5K; Vol24H $3.70M; 24H -21.96%; V/LP 5.24x; 池数 2; 分项 L17/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 主观察 | Score 76; Tier Early; LP $362.7K; Vol24H $449.5K; 24H -1.38%; V/LP 1.24x; 池数 1; 分项 L14/V11/B22/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [WOTF](https://dexscreener.com/solana/d3qnza8tklggt3vg9jkqy7zwcz2fctvekzth6jf2kmzy) | SOL | [drLg3v...T7pump](https://solscan.io/token/drLg3vH1p7KVK7YrXSNSPJxtGVDwLy3mHsVofT7pump) | 次观察 | Score 74; Tier Early; LP $606.8K; Vol24H $210.4K; 24H +13.40%; V/LP 0.35x; 池数 1; 分项 L16/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 次观察 | Score 73; Tier Liquid; LP $1.17M; Vol24H $288.2K; 24H +14.02%; V/LP 0.25x; 池数 1; 分项 L19/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 66; Tier Early; LP $644.5K; Vol24H $918.9K; 24H +208.00%; V/LP 1.43x; 池数 1; 分项 L17/V13/B0/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 64; Tier Early; LP $158.9K; Vol24H $582.7K; 24H -58.25%; V/LP 3.67x; 池数 1; 分项 L11/V12/B8/Buy12/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [PARASITE](https://dexscreener.com/solana/4zlrghwkdxyatovp8ukv66cskwgo9e7kaagycw1vfh7e) | SOL | [3kmygW...pmpump](https://solscan.io/token/3kmygWKZBkCYrgZHKfiuB9UFKTcDLTFFsKo3BWpmpump) | PVP风险池 | Score 36; Tier Micro; LP $87.8K; Vol24H $5.16M; 24H -69.37%; V/LP 58.76x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [AIRPAD](https://dexscreener.com/solana/4apfqygn4x18tcfwxv6pvwymfvvjpm2jts5yhdyvdsem) | SOL | [6ZG6fM...mQpump](https://solscan.io/token/6ZG6fMHaE7NpubJr16G8nFLBg91rH5kU5SVpqUmQpump) | PVP风险池 | Score 32; Tier Early; LP $107.9K; Vol24H $4.89M; 24H +804.00%; V/LP 45.34x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [terrafying](https://dexscreener.com/solana/56cvmnuznzzvda4c4bwctu1smdikapdfudlxs1r5q3jv) | SOL | [FUuH1a...A3fvR3](https://solscan.io/token/FUuH1aufXBQQwUJGQPErV9Pa7d1dvv4iuRhrf1A3fvR3) | PVP风险池 | Score 31; Tier Micro; LP $19.8K; Vol24H $1.15M; 24H -1.25%; V/LP 58.24x; 池数 3; 分项 L3/V14/B22/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CROCS](https://dexscreener.com/solana/glawm3vfovjbeck7k1ujq1z6bvxzfb319vven3bahz2b) | SOL | [6Vuz12...TWpump](https://solscan.io/token/6Vuz122BbhCoBSXLH94JdMamHAJhRGBKGJJ1i2TWpump) | PVP风险池 | Score 24; Tier Micro; LP $30.4K; Vol24H $1.18M; 24H -0.57%; V/LP 38.71x; 池数 1; 分项 L4/V14/B22/Buy0/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| THESIS | BSC | [0x4519...dd7777](https://bscscan.com/token/0x4519cacc591aecc5f8476bebee43b11ffedd7777) | PVP风险池 | Score 20; Tier Micro; LP $75.3K; Vol24H $1.65M; 24H +449.91%; V/LP 21.91x; 池数 1; 分项 L8/V15/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [POND](https://dexscreener.com/solana/9laz2p55tfbxoidrwzqnu8skzr9534zkhw9hmzpdxz7e) | SOL | [84D3Vo...kHpump](https://solscan.io/token/84D3VopU3g5qo7jUwzQK4P4BnVPQWr2MzeaRCFkHpump) | PVP风险池 | Score 20; Tier Micro; LP $42.4K; Vol24H $1.19M; 24H -63.63%; V/LP 27.98x; 池数 1; 分项 L6/V14/B8/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| RESI | SOL | [reside...xQ5q1y](https://solscan.io/token/resideK2Ejv9apu1op2VBv89poumxCDCs8nzBxQ5q1y) | PVP风险池 | Score 15; Tier Micro; LP $46.8K; Vol24H $5.72M; 24H +291.83%; V/LP 122.20x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [PARASITE](https://dexscreener.com/solana/4zlrghwkdxyatovp8ukv66cskwgo9e7kaagycw1vfh7e) | SOL | [3kmygW...pmpump](https://solscan.io/token/3kmygWKZBkCYrgZHKfiuB9UFKTcDLTFFsKo3BWpmpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $87.8K; Vol24H $5.16M; 24H -69.37%; V/LP 58.76x; 池数 2; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [AIRPAD](https://dexscreener.com/solana/4apfqygn4x18tcfwxv6pvwymfvvjpm2jts5yhdyvdsem) | SOL | [6ZG6fM...mQpump](https://solscan.io/token/6ZG6fMHaE7NpubJr16G8nFLBg91rH5kU5SVpqUmQpump) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $107.9K; Vol24H $4.89M; 24H +804.00%; V/LP 45.34x; 池数 1; 分项 L9/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [terrafying](https://dexscreener.com/solana/56cvmnuznzzvda4c4bwctu1smdikapdfudlxs1r5q3jv) | SOL | [FUuH1a...A3fvR3](https://solscan.io/token/FUuH1aufXBQQwUJGQPErV9Pa7d1dvv4iuRhrf1A3fvR3) | 24H接近横盘；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 31; Tier Micro; LP $19.8K; Vol24H $1.15M; 24H -1.25%; V/LP 58.24x; 池数 3; 分项 L3/V14/B22/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [CROCS](https://dexscreener.com/solana/glawm3vfovjbeck7k1ujq1z6bvxzfb319vven3bahz2b) | SOL | [6Vuz12...TWpump](https://solscan.io/token/6Vuz122BbhCoBSXLH94JdMamHAJhRGBKGJJ1i2TWpump) | 24H接近横盘；LP未达主观察门槛；24H成交合格；卖出笔数占优；LP偏薄；Volume/LP极端偏高 | Score 24; Tier Micro; LP $30.4K; Vol24H $1.18M; 24H -0.57%; V/LP 38.71x; 池数 1; 分项 L4/V14/B22/Buy0/Risk-40 | 只记录热度，不进入主榜 |
| THESIS | BSC | [0x4519...dd7777](https://bscscan.com/token/0x4519cacc591aecc5f8476bebee43b11ffedd7777) | 买卖基本均衡；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 20; Tier Micro; LP $75.3K; Vol24H $1.65M; 24H +449.91%; V/LP 21.91x; 池数 1; 分项 L8/V15/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [POND](https://dexscreener.com/solana/9laz2p55tfbxoidrwzqnu8skzr9534zkhw9hmzpdxz7e) | SOL | [84D3Vo...kHpump](https://solscan.io/token/84D3VopU3g5qo7jUwzQK4P4BnVPQWr2MzeaRCFkHpump) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 20; Tier Micro; LP $42.4K; Vol24H $1.19M; 24H -63.63%; V/LP 27.98x; 池数 1; 分项 L6/V14/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| RESI | SOL | [reside...xQ5q1y](https://solscan.io/token/resideK2Ejv9apu1op2VBv89poumxCDCs8nzBxQ5q1y) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $46.8K; Vol24H $5.72M; 24H +291.83%; V/LP 122.20x; 池数 1; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [BSC](https://dexscreener.com/bsc/0x9d4fcd21260c87a700ad914b386669eb23bbb590) | BSC | [0xa415...aB361e](https://bscscan.com/token/0xa41571ee6a7928720C653e2dA72d186aF8aB361e) | 买入笔数占优；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；年轻币短期暴拉 | Score 10; Tier Early; LP $187.3K; Vol24H $3.86M; 24H +301355.00%; V/LP 20.59x; 池数 4; 分项 L12/V17/B0/Buy12/Risk-55 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 79; Tier Mature; LP $27.35M; Vol24H $13.33M; 24H -0.61%; V/LP 0.49x; 池数 3; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $3.99M; Vol24H $8.74M; 24H +7.13%; V/LP 2.19x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $57.81M; Vol24H $3.51M; 24H +0.64%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.83M; Vol24H $13.39M; 24H +21.29%; V/LP 4.74x; 池数 1; 分项 L20/V17/B17/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| MarsCoin | BSC | [0xfe18...5c7777](https://bscscan.com/token/0xfe189e97832da1573e4e4ff034f4ffc3a15c7777) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 69; Tier Early; LP $599.4K; Vol24H $2.51M; 24H -4.18%; V/LP 4.19x; 池数 1; 分项 L16/V16/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| CAP | BSC | [0x9999...9b9999](https://bscscan.com/token/0x99991c6aabba5a096f24f250b73580f5179b9999) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；市值超过早期Alpha主榜上限 | Score 66; Tier Liquid; LP $1.17M; Vol24H $1.69M; 24H +8.77%; V/LP 1.45x; 池数 1; 分项 L19/V15/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| PUMP | SOL | [pumpCm...7H9Dfn](https://solscan.io/token/pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WOTF](https://dexscreener.com/solana/d3qnza8tklggt3vg9jkqy7zwcz2fctvekzth6jf2kmzy) | SOL | [drLg3v...T7pump](https://solscan.io/token/drLg3vH1p7KVK7YrXSNSPJxtGVDwLy3mHsVofT7pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| WKC | BSC | [0x6ec9...128edb](https://bscscan.com/token/0x6ec90334d89dbdc89e08a133271be3d104128edb) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [VSOF](https://dexscreener.com/solana/fbzxadhfjj6rwy6fnjewx1lnszquknpxm3kqhgd9xl7s) | SOL | [nktiJ9...Kupump](https://solscan.io/token/nktiJ91NxzY8Dq1JB6YvZq97bpCiELxrRgBzwKupump) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [CATE](https://dexscreener.com/solana/hmzvseemtzhhvznw9uwbag85hctmfnkbhzux16cy7ca3) | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| $BANANA | BSC | [0x3d4f...a9a760](https://bscscan.com/token/0x3d4f0513e8a29669b960f9dbca61861548a9a760) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 7 / Early 10 / Liquid 6 / Mature 2 | 下一步可以按层级分别设置进攻规则 |
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
# 自我进化轮巡

**本轮时间 UTC：** 2026-09-24T22:56:15Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 133 个合并Token中筛出 5 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 210 |
| 合并后Token | 133 |
| 输出候选 | 25 |
| 主观察 | 5 |
| 次观察 | 11 |
| PVP风险池 | 8 |
| 成熟池观察 | 1 |
| 低优先观察 | 0 |
| 多池Token | 7 |
| 多池冲突 | 3 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 4 |
| Early层 | 16 |
| Liquid层 | 4 |
| Mature层 | 1 |
| 需要链上确认 | 24 |
| 紧急精查候选 | 1 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1508，刷新时间 2026-09-21T02:34:44Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 5 个，BSC Transfer样本 3 个，SOL签名级 2 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 主观察 | Score 84; Tier Early; LP $319.3K; Vol24H $2.03M; 24H -0.07%; V/LP 6.36x; 池数 2; 分项 L14/V16/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 83; Tier Liquid; LP $1.73M; Vol24H $982.1K; 24H +7.18%; V/LP 0.57x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 83; Tier Liquid; LP $1.36M; Vol24H $1.25M; 24H +5.77%; V/LP 0.92x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 80; Tier Liquid; LP $2.74M; Vol24H $2.24M; 24H +38.41%; V/LP 0.82x; 池数 1; 分项 L20/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 77; Tier Early; LP $594.0K; Vol24H $2.55M; 24H +16.32%; V/LP 4.29x; 池数 2; 分项 L16/V17/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 次观察 | Score 76; Tier Liquid; LP $2.17M; Vol24H $1.81M; 24H +11.70%; V/LP 0.83x; 池数 1; 分项 L20/V15/B17/Buy0/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，不直接进攻 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 次观察 | Score 74; Tier Early; LP $353.6K; Vol24H $112.2K; 24H +22.06%; V/LP 0.32x; 池数 1; 分项 L14/V7/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/bdf5xmz4gt1ete64perjqajajapdmhanxcuhfq1nepsd) | SOL | [txyCte...jDpump](https://solscan.io/token/txyCteRRStX5G1ygidKoDcGV2mMfFjtcHJshTjDpump) | 次观察 | Score 73; Tier Early; LP $248.3K; Vol24H $109.8K; 24H +22.14%; V/LP 0.44x; 池数 2; 分项 L13/V7/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [TART](https://dexscreener.com/bsc/0x30000a407fabebe29439f8e437050512ff6661be) | BSC | [0x7AB8...750314](https://bscscan.com/token/0x7AB8d02CBb51Ff7223fDe700eAaa2a91Bf750314) | 次观察 | Score 72; Tier Early; LP $453.9K; Vol24H $172.4K; 24H -1.36%; V/LP 0.38x; 池数 1; 分项 L15/V8/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 72; Tier Early; LP $484.7K; Vol24H $442.1K; 24H -14.32%; V/LP 0.91x; 池数 1; 分项 L15/V11/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 主观察 | Score 83; Tier Liquid; LP $1.71M; Vol24H $992.5K; 24H +6.60%; V/LP 0.58x; 池数 1; 分项 L20/V14/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 主观察 | Score 80; Tier Liquid; LP $2.64M; Vol24H $2.37M; 24H +27.80%; V/LP 0.90x; 池数 1; 分项 L20/V16/B8/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 主观察 | Score 79; Tier Liquid; LP $2.14M; Vol24H $1.34M; 24H -8.08%; V/LP 0.63x; 池数 1; 分项 L20/V15/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 主观察 | Score 78; Tier Liquid; LP $913.6K; Vol24H $2.31M; 24H +9.34%; V/LP 2.53x; 池数 1; 分项 L18/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 主观察 | Score 76; Tier Early; LP $574.0K; Vol24H $2.40M; 24H +8.32%; V/LP 4.18x; 池数 1; 分项 L16/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 次观察 | Score 74; Tier Early; LP $350.3K; Vol24H $89.9K; 24H +14.94%; V/LP 0.26x; 池数 1; 分项 L14/V7/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 次观察 | Score 74; Tier Early; LP $559.4K; Vol24H $493.1K; 24H +16.67%; V/LP 0.88x; 池数 1; 分项 L16/V12/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/bdf5xmz4gt1ete64perjqajajapdmhanxcuhfq1nepsd) | SOL | [txyCte...jDpump](https://solscan.io/token/txyCteRRStX5G1ygidKoDcGV2mMfFjtcHJshTjDpump) | 次观察 | Score 73; Tier Early; LP $244.9K; Vol24H $89.8K; 24H +17.04%; V/LP 0.37x; 池数 2; 分项 L13/V7/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [REVS](https://dexscreener.com/solana/3iodstfu18uxoggmmjud6tztkvw72uqapddbjes42ppk) | SOL | [EyWrMX...9KREVS](https://solscan.io/token/EyWrMXBb5DXppWs5uNa6repSEDoDSachbjeixU9KREVS) | 次观察 | Score 71; Tier Early; LP $124.7K; Vol24H $155.2K; 24H +18.79%; V/LP 1.24x; 池数 5; 分项 L10/V8/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [CALI](https://dexscreener.com/solana/2i2iulr7uwk1sdrb17t5futimnfql7fyy7rh69brzihc) | SOL | [8k4sBt...k5PbAA](https://solscan.io/token/8k4sBtEeK4pf26noKqApv8NBTnuSJcbdwpKYknk5PbAA) | 次观察 | Score 68; Tier Early; LP $158.1K; Vol24H $908.8K; 24H +11.95%; V/LP 5.75x; 池数 1; 分项 L11/V13/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| PEPENOM | SOL | [EpEfnZ...fQpump](https://solscan.io/token/EpEfnZxQyiBXppSKi8sncc8w4corn1UJbF9G91fQpump) | 次观察 | Score 68; Tier Early; LP $124.7K; Vol24H $50.1K; 24H -8.47%; V/LP 0.40x; 池数 1; 分项 L10/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 67; Tier Early; LP $200.6K; Vol24H $192.6K; 24H -10.14%; V/LP 0.96x; 池数 1; 分项 L12/V9/B17/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [ARENA](https://dexscreener.com/solana/rbhypns9j1wybsssvorm9nxt8hlvsdv3yeczwgmv68t) | SOL | [4G5YDq...4Tqbzi](https://solscan.io/token/4G5YDqDvwgwSS3nLPDGDpGuetbG7rZYzNSBb1U4Tqbzi) | 次观察 | Score 65; Tier Micro; LP $51.7K; Vol24H $55.0K; 24H +23.26%; V/LP 1.06x; 池数 8; 分项 L7/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [VSOF](https://dexscreener.com/solana/451hyqbfewuhoivemnkvhzxhk7gxsm27b4q7x2bettwp) | SOL | [CQZW8A...4Epump](https://solscan.io/token/CQZW8AzE7y39g2dBnUVBRFnMkg62FpP6mtDAc4Epump) | 次观察 | Score 65; Tier Early; LP $525.5K; Vol24H $188.9K; 24H +29.23%; V/LP 0.36x; 池数 1; 分项 L16/V9/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [GATO](https://dexscreener.com/solana/5e3dxlxgwmtdcoka51wyyakttjfzbwqcoyuhbui5gt2m) | SOL | [HsprHx...k6pump](https://solscan.io/token/HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump) | 次观察 | Score 65; Tier Early; LP $138.9K; Vol24H $265.0K; 24H +10.91%; V/LP 1.91x; 池数 1; 分项 L11/V10/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [TEXTIT](https://dexscreener.com/solana/8v6b3ctop5bvqwxersrueujdcfemdyqjkj7tutsxq1cm) | SOL | [udPEzB...wdpump](https://solscan.io/token/udPEzBjbGMzYZbuLtByqLYhc4TEs6EebG8R7fwdpump) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 45; Tier Early; LP $304.8K; Vol24H $6.66M; 24H +20.85%; V/LP 21.84x; 池数 1; 分项 L14/V17/B17/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| TAKE | BSC | [0xe747...c0e197](https://bscscan.com/token/0xe747e54783ba3f77a8e5251a3cba19ebe9c0e197) | 24H未过热但已明显波动；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 37; Tier Early; LP $427.6K; Vol24H $22.86M; 24H -38.83%; V/LP 53.46x; 池数 1; 分项 L15/V17/B8/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| GO | SOL | [D1YZZg...rD4F4n](https://solscan.io/token/D1YZZg9dBZ7AbfknZVbaeVLto36eySwoFYEVhZrD4F4n) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $256.9K; Vol24H $7.67M; 24H +4711.36%; V/LP 29.85x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| familiars | SOL | [2PENPm...Uupump](https://solscan.io/token/2PENPmfgJfq6CG3k4byj4oWwHf8SerqakmYHMkUupump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Early; LP $144.7K; Vol24H $10.84M; 24H +3573.73%; V/LP 74.93x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [NPC](https://dexscreener.com/solana/brjma8ualnp3ditkhfdean5riqrypoayez7khywd4oes) | SOL | [7GUnr7...Zepump](https://solscan.io/token/7GUnr7krtQhJwd6ASY2VUprd9t4c64zcgCsjdmZepump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $86.7K; Vol24H $4.43M; 24H +1437.00%; V/LP 51.05x; 池数 1; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [goon](https://dexscreener.com/solana/9pyormkwiwyaalgwknnbjseqkk79hporalgqhmfy4fuv) | SOL | [HSUMi4...9Apump](https://solscan.io/token/HSUMi4rMgjrx7zRUabw3ogGu1pa5hmF2eVcXj9Apump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高；非主流报价池 | Score 27; Tier Early; LP $158.9K; Vol24H $4.17M; 24H +185.00%; V/LP 26.25x; 池数 2; 分项 L11/V17/B0/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| FUNKOS | SOL | [BDKC1A...eAfunk](https://solscan.io/token/BDKC1AV3saXrN8jKnWB2TTQmDD6z8CFdY55ku7eAfunk) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；LP偏薄；Volume/LP极端偏高 | Score 20; Tier Micro; LP $23.2K; Vol24H $2.98M; 24H +25.59%; V/LP 128.69x; 池数 1; 分项 L3/V17/B8/Buy8/Risk-40 | 只记录热度，不进入主榜 |
| [SI](https://dexscreener.com/solana/3odkxofb7kvujarfolbcqbbzv93r9njjr9kqth5ckdkt) | SOL | [82ezhR...ompump](https://solscan.io/token/82ezhRLKdKwkSC9jkM3js1yf93VbmvLXNMPkBmompump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $47.6K; Vol24H $3.26M; 24H +402.00%; V/LP 68.48x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| USELESS | SOL | [Dz9mQ9...8Mbonk](https://solscan.io/token/Dz9mQ9NzkBcCsuGPFJ3r1bS4wgqKMHBPiVuniW8Mbonk) | 24H接近横盘；买入笔数占优；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 83; Tier Mature; LP $5.70M; Vol24H $2.72M; 24H -4.83%; V/LP 0.48x; 池数 1; 分项 L20/V17/B22/Buy12/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| LAB | BSC | [0x7ec4...25593a](https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [USDF](https://dexscreener.com/solana/bdf5xmz4gt1ete64perjqajajapdmhanxcuhfq1nepsd) | SOL | [txyCte...jDpump](https://solscan.io/token/txyCteRRStX5G1ygidKoDcGV2mMfFjtcHJshTjDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [REVS](https://dexscreener.com/solana/3iodstfu18uxoggmmjud6tztkvw72uqapddbjes42ppk) | SOL | [EyWrMX...9KREVS](https://solscan.io/token/EyWrMXBb5DXppWs5uNa6repSEDoDSachbjeixU9KREVS) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；多池数据冲突，需链上/聚合源复核 |
| [CALI](https://dexscreener.com/solana/2i2iulr7uwk1sdrb17t5futimnfql7fyy7rh69brzihc) | SOL | [8k4sBt...k5PbAA](https://solscan.io/token/8k4sBtEeK4pf26noKqApv8NBTnuSJcbdwpKYknk5PbAA) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| 4 | BSC | [0x0a43...e14444](https://bscscan.com/token/0x0a43fc31a73013089df59194872ecae4cae14444) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| Broccoli | BSC | [0x6d5a...ed6714](https://bscscan.com/token/0x6d5ad1592ed9d6d1df9b93c793ab759573ed6714) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| [neet](https://dexscreener.com/solana/5wnu5qhdprgrl37ffcd6tmmqzugqgxwafgz477rshthy) | SOL | [Ce2gx9...o3pump](https://solscan.io/token/Ce2gx9KGXJ6C9Mp5b5x1sn9Mg87JwEbrQby4Zqo3pump) | signature_sample_only | solana_swap_retention_not_parsed_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
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
| 主观察候选 | 5 个 | 主榜继续稀缺，但必须结合合约地址进入链上确认 |
| PVP风险池 | 8 个 | v0.3已单独展示明细，便于判断噪声来源 |
| 成熟池观察 | 1 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 4 / Early 16 / Liquid 4 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 330} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
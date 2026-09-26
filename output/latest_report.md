# 自我进化轮巡

**本轮时间 UTC：** 2026-09-26T18:13:29Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 148 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 247 |
| 合并后Token | 148 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 6 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 4 |
| 多池Token | 8 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 6 |
| Early层 | 11 |
| Liquid层 | 7 |
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
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 3 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 85; Tier Liquid; LP $1.35M; Vol24H $2.15M; 24H +4.60%; V/LP 1.59x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 83; Tier Liquid; LP $974.8K; Vol24H $2.15M; 24H +6.70%; V/LP 2.21x; 池数 1; 分项 L18/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 83; Tier Liquid; LP $907.6K; Vol24H $2.25M; 24H -9.86%; V/LP 2.47x; 池数 1; 分项 L18/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 次观察 | Score 75; Tier Early; LP $189.2K; Vol24H $216.8K; 24H -5.50%; V/LP 1.15x; 池数 1; 分项 L12/V9/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 74; Tier Early; LP $490.2K; Vol24H $513.7K; 24H +7.53%; V/LP 1.05x; 池数 1; 分项 L16/V12/B22/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 次观察 | Score 73; Tier Early; LP $434.9K; Vol24H $223.0K; 24H +21.50%; V/LP 0.51x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WAIF](https://dexscreener.com/solana/dgatrsvp1n3m76kpcvbfhhjwotby8lf8ivwkipanh5tk) | SOL | [wFYBNt...EYpump](https://solscan.io/token/wFYBNtZpcXd2NX9eHo7FLHtJRHjfp9F1iRkm3EYpump) | 次观察 | Score 71; Tier Early; LP $259.6K; Vol24H $214.1K; 24H +16.95%; V/LP 0.82x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| ClipX | BSC | [0xc269...554444](https://bscscan.com/token/0xc269d59a0d608ea0bd672f2f4616c372d8554444) | 次观察 | Score 65; Tier Early; LP $188.5K; Vol24H $687.4K; 24H +77.25%; V/LP 3.65x; 池数 1; 分项 L12/V13/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 64; Tier Early; LP $248.6K; Vol24H $1.29M; 24H +44.87%; V/LP 5.18x; 池数 3; 分项 L13/V14/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 52; Tier Early; LP $612.7K; Vol24H $42.21M; 24H -0.71%; V/LP 68.89x; 池数 1; 分项 L16/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 主观察 | Score 85; Tier Liquid; LP $1.34M; Vol24H $1.94M; 24H +3.59%; V/LP 1.44x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 主观察 | Score 83; Tier Liquid; LP $920.7K; Vol24H $1.82M; 24H -8.83%; V/LP 1.98x; 池数 1; 分项 L18/V16/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 主观察 | Score 78; Tier Liquid; LP $971.9K; Vol24H $2.07M; 24H +13.30%; V/LP 2.13x; 池数 1; 分项 L18/V16/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 次观察 | Score 73; Tier Early; LP $438.5K; Vol24H $221.2K; 24H +17.43%; V/LP 0.50x; 池数 1; 分项 L15/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [WAIF](https://dexscreener.com/solana/dgatrsvp1n3m76kpcvbfhhjwotby8lf8ivwkipanh5tk) | SOL | [wFYBNt...EYpump](https://solscan.io/token/wFYBNtZpcXd2NX9eHo7FLHtJRHjfp9F1iRkm3EYpump) | 次观察 | Score 71; Tier Early; LP $264.1K; Vol24H $214.6K; 24H +17.06%; V/LP 0.81x; 池数 1; 分项 L13/V9/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 次观察 | Score 70; Tier Early; LP $311.5K; Vol24H $2.43M; 24H -42.61%; V/LP 7.80x; 池数 1; 分项 L14/V16/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 次观察 | Score 69; Tier Early; LP $493.3K; Vol24H $569.1K; 24H +10.08%; V/LP 1.15x; 池数 1; 分项 L16/V12/B17/Buy3/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 次观察 | Score 68; Tier Early; LP $193.2K; Vol24H $123.5K; 24H +20.50%; V/LP 0.64x; 池数 1; 分项 L12/V7/B17/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 次观察 | Score 65; Tier Early; LP $254.2K; Vol24H $1.30M; 24H +43.34%; V/LP 5.11x; 池数 3; 分项 L13/V15/B8/Buy8/Risk-3 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | PVP风险池 | Score 52; Tier Early; LP $611.4K; Vol24H $35.00M; 24H -0.94%; V/LP 57.26x; 池数 1; 分项 L16/V17/B22/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| e | SOL | [CbcyNo...kzpKoU](https://solscan.io/token/CbcyNo7m1amFWqEQm2m4PLv1UNvpcL3C1Ujm6AkzpKoU) | PVP风险池 | Score 35; Tier Early; LP $527.2K; Vol24H $52.95M; 24H +30876.74%; V/LP 100.42x; 池数 2; 分项 L16/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | PVP风险池 | Score 34; Tier Liquid; LP $1.40M; Vol24H $40.71M; 24H +320.00%; V/LP 29.16x; 池数 2; 分项 L20/V17/B0/Buy3/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | PVP风险池 | Score 32; Tier Early; LP $284.6K; Vol24H $7.35M; 24H +378.00%; V/LP 25.81x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [YAP](https://dexscreener.com/solana/ax9gpobxtkb19nmj4ejhnsy163xuugmfkrlpeleqk7lx) | SOL | [jLz71Q...u9dyap](https://solscan.io/token/jLz71QZfjnZZMLjUaCBw7KmUyftkkNq8NkWi2u9dyap) | PVP风险池 | Score 31; Tier Early; LP $213.7K; Vol24H $8.72M; 24H +282.00%; V/LP 40.79x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| KARDASHEV | SOL | [5wW9mh...L7hUnp](https://solscan.io/token/5wW9mhbwq1HTFh341iimpmrqBB4mfxdXiYhdYBL7hUnp) | PVP风险池 | Score 28; Tier Micro; LP $94.2K; Vol24H $8.37M; 24H +1463.73%; V/LP 88.82x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| BANK | BSC | [0x3aee...ebf2bf](https://bscscan.com/token/0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 52; Tier Early; LP $611.4K; Vol24H $35.00M; 24H -0.94%; V/LP 57.26x; 池数 1; 分项 L16/V17/B22/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| e | SOL | [CbcyNo...kzpKoU](https://solscan.io/token/CbcyNo7m1amFWqEQm2m4PLv1UNvpcL3C1Ujm6AkzpKoU) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 35; Tier Early; LP $527.2K; Vol24H $52.95M; 24H +30876.74%; V/LP 100.42x; 池数 2; 分项 L16/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [PAID](https://dexscreener.com/solana/6e3jzltf4tqbwzm3f7a66jf8tfzn6mrqvrbdfgcnwara) | SOL | [98kfF7...zypump](https://solscan.io/token/98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump) | 买卖基本均衡；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 34; Tier Liquid; LP $1.40M; Vol24H $40.71M; 24H +320.00%; V/LP 29.16x; 池数 2; 分项 L20/V17/B0/Buy3/Risk-30 | 只记录热度，不进入主榜 |
| [ELON](https://dexscreener.com/solana/6tuhhpysinf41v39kw3jmpvuaxehcabcbhzqqfnwr6xf) | SOL | [GY9mZf...zxpump](https://solscan.io/token/GY9mZfyPpxXxBXBxS2hB2XjhP3kfUsywTvgveozxpump) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $284.6K; Vol24H $7.35M; 24H +378.00%; V/LP 25.81x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [YAP](https://dexscreener.com/solana/ax9gpobxtkb19nmj4ejhnsy163xuugmfkrlpeleqk7lx) | SOL | [jLz71Q...u9dyap](https://solscan.io/token/jLz71QZfjnZZMLjUaCBw7KmUyftkkNq8NkWi2u9dyap) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 31; Tier Early; LP $213.7K; Vol24H $8.72M; 24H +282.00%; V/LP 40.79x; 池数 2; 分项 L12/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| KARDASHEV | SOL | [5wW9mh...L7hUnp](https://solscan.io/token/5wW9mhbwq1HTFh341iimpmrqBB4mfxdXiYhdYBL7hUnp) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 28; Tier Micro; LP $94.2K; Vol24H $8.37M; 24H +1463.73%; V/LP 88.82x; 池数 2; 分项 L9/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [Cream](https://dexscreener.com/solana/cprowxcgq3elsnqsgdmlmavrnnsmyn4k1ddc6efgdd91) | SOL | [CMuvWQ...BaeVgR](https://solscan.io/token/CMuvWQ6qQbSt7NUQdPGcVKCoDgETieuqS68qu6BaeVgR) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 27; Tier Micro; LP $79.5K; Vol24H $7.56M; 24H +898.00%; V/LP 95.13x; 池数 2; 分项 L8/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [DEBT](https://dexscreener.com/solana/ep88ktqm6491wem1zjseryxyyjuolh5ceyz5exyxr1cb) | SOL | [FYM6Ph...M9eFkt](https://solscan.io/token/FYM6PhwAS3QwTBwvgLj8JYeMgpNfKsWtW3hGxPM9eFkt) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 14; Tier Micro; LP $34.8K; Vol24H $7.34M; 24H +112.00%; V/LP 210.90x; 池数 1; 分项 L5/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| STONK | SOL | [6GmAFS...MpUNgx](https://solscan.io/token/6GmAFSYs4gk3FDao5FzzySQpPZaWsa4rUJHacpMpUNgx) | 24H接近横盘；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 79; Tier Liquid; LP $3.27M; Vol24H $16.01M; 24H -1.66%; V/LP 4.90x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| AKE | BSC | [0x2c3a...12f7db](https://bscscan.com/token/0x2c3a8ee94ddd97244a93bc48298f97d2c412f7db) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 74; Tier Liquid; LP $2.84M; Vol24H $6.10M; 24H +6.15%; V/LP 2.15x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| ARK | BSC | [0xcae1...618b9d](https://bscscan.com/token/0xcae117ca6bc8a341d2e7207f30e180f0e5618b9d) | 24H接近横盘；LP达主观察门槛；24H成交合格；Volume/LP未失真；卖出笔数占优；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $57.25M; Vol24H $3.18M; 24H -2.14%; V/LP 0.06x; 池数 1; 分项 L20/V17/B22/Buy0/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 24H波动可控；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限 | Score 69; Tier Liquid; LP $2.97M; Vol24H $6.29M; 24H -18.05%; V/LP 2.11x; 池数 4; 分项 L20/V17/B17/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WOTF](https://dexscreener.com/solana/6xey1prnevdasqxuzuwp8rvjpfssp3ffv4xpge1ze6sc) | SOL | [kgLfVJ...HJpump](https://solscan.io/token/kgLfVJiPwuEXXQBcY2AV3zh6MCkJvZfWLcNHjHJpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [WAIF](https://dexscreener.com/solana/dgatrsvp1n3m76kpcvbfhhjwotby8lf8ivwkipanh5tk) | SOL | [wFYBNt...EYpump](https://solscan.io/token/wFYBNtZpcXd2NX9eHo7FLHtJRHjfp9F1iRkm3EYpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [JEANPHIL](https://dexscreener.com/solana/4r8cimnjwdnoes3fqi1ccpfjygpxazahawphrn3rzenj) | SOL | [GTBxUi...yDpump](https://solscan.io/token/GTBxUiw6wJdmmkCGZgRHLyYxqu1vG4KtRpeox6yDpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [EMBER](https://dexscreener.com/solana/2y6pcqa4fep3jlifdan9jvmw7lsk8f3gwstfy8p7trae) | SOL | [5dvXTZ...k4QEC6](https://solscan.io/token/5dvXTZ5qwgafnHtwu3Ls3QrWx1U4LQsFeCuJgkk4QEC6) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 龙虾 | BSC | [0xeccb...7e4444](https://bscscan.com/token/0xeccbb861c0dda7efd964010085488b69317e4444) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核 |
| [USDF](https://dexscreener.com/solana/azyy8ibm2bbpab4bs9jkdm5mbcchohbcjzcnpyacvdcj) | SOL | [DRMnFy...Gjpump](https://solscan.io/token/DRMnFyekQiCTMrajtgsTycqp4ie6r1tZnh6qpAGjpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [memestock](https://dexscreener.com/bsc/0x7bdc9582aca6ca25e5db1f2c8e59003b880672cb) | BSC | [0x6FF4...057777](https://bscscan.com/token/0x6FF45323817d1d53bbb8A8dFbA9245aE74057777) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| BREW | BSC | [0xfa6d...3f2159](https://bscscan.com/token/0xfa6d9b504848606eb9aec04ccc161d169b3f2159) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| COLLECT | BSC | [0x4b3d...a087d3](https://bscscan.com/token/0x4b3d30992f003c8167699735f5ab2831b2a087d3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| CLO | BSC | [0x81d3...bf89d2](https://bscscan.com/token/0x81d3a238b02827f62b9f390f947d36d4a5bf89d2) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| 成熟池观察 | 4 个 | 成熟资产不占早期Alpha主榜 |
| 合约地址覆盖 | 可用 25，缺失 0 | 地址缺失会阻断BSC RPC/Helius精查，需要优先补齐 |
| LP层级 | Micro 6 / Early 11 / Liquid 7 / Mature 1 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 333} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
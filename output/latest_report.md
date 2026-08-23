# 自我进化轮巡

**本轮时间 UTC：** 2026-08-23T21:15:20Z
**版本：** 0.5.0-ave-cache-wallet-behavior-prep
**S0 时间锚点：** 2026-06-16T16:15:17+09:00

## 一句话结论
本轮从 138 个合并Token中筛出 3 个主观察候选。v0.5已在v0.4.1基础上增加AVE周缓存真实接口接入框架、Smart Wallet持久保存、wallet_behavior_latest.json，以及BSC Transfer级钱包行为样本。注意：BSC当前是Transfer样本，不等同完整Swap解码。
合约地址可用 25 个，缺失 0 个；缺失地址的候选不能进入后续链上精查。

## 本轮扫描摘要
| 指标 | 数量 |
|---|---:|
| 原始池子记录 | 246 |
| 合并后Token | 138 |
| 输出候选 | 25 |
| 主观察 | 3 |
| 次观察 | 2 |
| PVP风险池 | 8 |
| 成熟池观察 | 4 |
| 低优先观察 | 8 |
| 多池Token | 10 |
| 多池冲突 | 1 |
| Symbol桥接合并 | 1 |
| 合约地址可用 | 25 |
| 合约地址缺失 | 0 |
| Micro层 | 5 |
| Early层 | 11 |
| Liquid层 | 6 |
| Mature层 | 3 |
| 需要链上确认 | 13 |
| 紧急精查候选 | 3 |

## v0.5 数据确认状态
| 项目 | 状态 |
|---|---|
| AVE Smart Wallet周缓存 | active，钱包数 1035，刷新时间 2026-08-17T00:45:08Z，是否过期 否 |
| 链上预检 | 本轮检查 12 个，验证通过 12 个，失败 0 个 |
| Helius状态 | 未配置，SOL使用公共RPC或跳过增强解析 |
| 当前精查层级 | 0.5.0-chain-preflight-plus-wallet-behavior：地址/账户预检 + v0.5钱包行为样本，完整Swap留存仍待下一版 |
| 钱包行为样本 | 本轮检查 3 个，BSC Transfer样本 3 个，SOL签名级 0 个，AVE钱包命中 0 个 |

## 第一部分：生成结果表格

### A. 上次记录结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 91; Tier Liquid; LP $3.96M; Vol24H $3.41M; 24H +0.32%; V/LP 0.86x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 主观察 | Score 86; Tier Liquid; LP $1.93M; Vol24H $11.98M; 24H -6.90%; V/LP 6.21x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 主观察 | Score 85; Tier Liquid; LP $2.04M; Vol24H $2.02M; 24H +0.51%; V/LP 0.99x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 次观察 | Score 73; Tier Early; LP $445.8K; Vol24H $51.7K; 24H +19.33%; V/LP 0.12x; 池数 1; 分项 L15/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 次观察 | Score 67; Tier Early; LP $145.5K; Vol24H $590.4K; 24H +22.12%; V/LP 4.06x; 池数 3; 分项 L11/V12/B17/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [BARRON](https://dexscreener.com/solana/bjfpiz79shxybx59ghz7p9r9dfqpksm4xzu46mnmshcz) | SOL | [ECY31g...nSpump](https://solscan.io/token/ECY31gWwxy4s2VnMkYhmqDkrV75KrwR2yTtsnrnSpump) | 次观察 | Score 64; Tier Early; LP $241.8K; Vol24H $362.0K; 24H -33.47%; V/LP 1.50x; 池数 3; 分项 L13/V11/B8/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 47; Tier Liquid; LP $1.62M; Vol24H $55.37M; 24H -46.00%; V/LP 34.16x; 池数 3; 分项 L20/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 46; Tier Micro; LP $70.8K; Vol24H $23.20M; 24H +1.57%; V/LP 327.54x; 池数 1; 分项 L8/V17/B22/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | PVP风险池 | Score 43; Tier Liquid; LP $1.65M; Vol24H $39.91M; 24H +208.85%; V/LP 24.21x; 池数 1; 分项 L20/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 42; Tier Early; LP $393.7K; Vol24H $9.85M; 24H -27.57%; V/LP 25.01x; 池数 24; 分项 L15/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |

### B. 本轮扫描结果表
| Token | 链 | 合约地址 | 状态 | 核心指标 | 聪明钱包判断 | Smart Money数据来源 | 操作结论 |
|---|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 主观察 | Score 91; Tier Liquid; LP $4.26M; Vol24H $2.83M; 24H -6.25%; V/LP 0.66x; 池数 1; 分项 L20/V17/B22/Buy8/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 主观察 | Score 86; Tier Liquid; LP $1.93M; Vol24H $8.98M; 24H -4.54%; V/LP 4.65x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 主观察 | Score 85; Tier Liquid; LP $2.02M; Vol24H $1.91M; 24H +1.88%; V/LP 0.94x; 池数 1; 分项 L20/V16/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 | ave_weekly_cache_available_plus_chain_behavior | 保留主观察，等待链上钱包留存确认；不因代理指标直接买入 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 次观察 | Score 73; Tier Early; LP $449.5K; Vol24H $50.3K; 24H +19.78%; V/LP 0.11x; 池数 1; 分项 L15/V5/B17/Buy12/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 次观察 | Score 71; Tier Early; LP $135.3K; Vol24H $594.4K; 24H +5.98%; V/LP 4.39x; 池数 3; 分项 L10/V12/B22/Buy3/Risk-0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 次观察，等成交/LP结构继续改善 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | PVP风险池 | Score 51; Tier Early; LP $411.7K; Vol24H $10.35M; 24H -24.92%; V/LP 25.14x; 池数 23; 分项 L15/V17/B17/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；多池数据存在冲突，降置信度；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | PVP风险池 | Score 47; Tier Liquid; LP $1.59M; Vol24H $56.19M; 24H -48.75%; V/LP 35.28x; 池数 2; 分项 L20/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | PVP风险池 | Score 41; Tier Micro; LP $73.2K; Vol24H $23.18M; 24H -8.64%; V/LP 316.83x; 池数 1; 分项 L8/V17/B17/Buy8/Risk-33 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | PVP风险池 | Score 39; Tier Liquid; LP $1.82M; Vol24H $40.23M; 24H +398.40%; V/LP 22.09x; 池数 1; 分项 L20/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | PVP风险池 | Score 36; Tier Micro; LP $94.9K; Vol24H $5.60M; 24H -59.45%; V/LP 58.96x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | PVP风险池 | Score 32; Tier Early; LP $289.5K; Vol24H $11.01M; 24H +643.44%; V/LP 38.05x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [CATLIST](https://dexscreener.com/solana/gyz6rxjfnb3yjp2j2e7hmonojgqekzuxeeujurncqj1w) | SOL | [BKaXDg...g7pump](https://solscan.io/token/BKaXDgZxUSC9njpX89xpQ5USh2pnK1yzZvgk8Mg7pump) | PVP风险池 | Score 30; Tier Micro; LP $54.5K; Vol24H $6.18M; 24H +468.00%; V/LP 113.45x; 池数 1; 分项 L7/V17/B0/Buy12/Risk-30 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [YOMOGI](https://dexscreener.com/solana/6wbryqvrcl3sxtkeaxwmopqy5wquxo5ujev8w7xyungb) | SOL | [4978aT...gzpump](https://solscan.io/token/4978aTN9W3CDuUREGxAQaBYqhPXt8142N4o4Sfgzpump) | PVP风险池 | Score 15; Tier Micro; LP $41.0K; Vol24H $8.82M; 24H +304.00%; V/LP 215.08x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 只记录热度，不进入主榜 |
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 成熟池观察 | Score 74; Tier Mature; LP $17.53M; Vol24H $5.54M; 24H +4.87%; V/LP 0.32x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 成熟池观察 | Score 74; Tier Mature; LP $18.49M; Vol24H $20.13M; 24H +0.79%; V/LP 1.09x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 钱包级数据不可用；当前仅代理指标；资产偏成熟，不按早期吸筹处理；AVE周缓存可用，等待本轮链上行为映射 | ave_weekly_cache_available_plus_chain_behavior | 成熟池观察，不占用早期Alpha主榜 |

### C. PVP风险池明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 24H波动可控；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 51; Tier Early; LP $411.7K; Vol24H $10.35M; 24H -24.92%; V/LP 25.14x; 池数 23; 分项 L15/V17/B17/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 24H未过热但已明显波动；买卖略偏买入；LP达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 47; Tier Liquid; LP $1.59M; Vol24H $56.19M; 24H -48.75%; V/LP 35.28x; 池数 2; 分项 L20/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 24H波动可控；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高；非主流报价池 | Score 41; Tier Micro; LP $73.2K; Vol24H $23.18M; 24H -8.64%; V/LP 316.83x; 池数 1; 分项 L8/V17/B17/Buy8/Risk-33 | 只记录热度，不进入主榜 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 39; Tier Liquid; LP $1.82M; Vol24H $40.23M; 24H +398.40%; V/LP 22.09x; 池数 1; 分项 L20/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | 24H未过热但已明显波动；买卖略偏买入；LP未达主观察门槛；24H成交合格；Volume/LP极端偏高 | Score 36; Tier Micro; LP $94.9K; Vol24H $5.60M; 24H -59.45%; V/LP 58.96x; 池数 1; 分项 L9/V17/B8/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| BNBCAT | BSC | [0x3efb...6a7777](https://bscscan.com/token/0x3efbfff95576e1d23cf6ead0acd2e73f4d6a7777) | 买卖略偏买入；LP达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 32; Tier Early; LP $289.5K; Vol24H $11.01M; 24H +643.44%; V/LP 38.05x; 池数 1; 分项 L13/V17/B0/Buy8/Risk-30 | 只记录热度，不进入主榜 |
| [CATLIST](https://dexscreener.com/solana/gyz6rxjfnb3yjp2j2e7hmonojgqekzuxeeujurncqj1w) | SOL | [BKaXDg...g7pump](https://solscan.io/token/BKaXDgZxUSC9njpX89xpQ5USh2pnK1yzZvgk8Mg7pump) | 买入笔数占优；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；Volume/LP极端偏高 | Score 30; Tier Micro; LP $54.5K; Vol24H $6.18M; 24H +468.00%; V/LP 113.45x; 池数 1; 分项 L7/V17/B0/Buy12/Risk-30 | 只记录热度，不进入主榜 |
| [YOMOGI](https://dexscreener.com/solana/6wbryqvrcl3sxtkeaxwmopqy5wquxo5ujev8w7xyungb) | SOL | [4978aT...gzpump](https://solscan.io/token/4978aTN9W3CDuUREGxAQaBYqhPXt8142N4o4Sfgzpump) | 买卖略偏买入；LP未达主观察门槛；24H成交合格；24H涨跌幅过热；LP偏薄；Volume/LP极端偏高 | Score 15; Tier Micro; LP $41.0K; Vol24H $8.82M; 24H +304.00%; V/LP 215.08x; 池数 2; 分项 L6/V17/B0/Buy8/Risk-40 | 只记录热度，不进入主榜 |

### D. 成熟池观察明细表
| Token | 链 | 合约地址 | 触发原因 | 核心指标 | 处理 |
|---|---|---|---|---|---|
| [BOME](https://dexscreener.com/solana/dsuvc5qf5ljhhv5e2td184ixotsncnwj7i4jja4xsrmt) | SOL | [ukHH6c...Z74J82](https://solscan.io/token/ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池 | Score 74; Tier Mature; LP $17.53M; Vol24H $5.54M; 24H +4.87%; V/LP 0.32x; 池数 3; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| BTCB | BSC | [0x7130...3ead9c](https://bscscan.com/token/0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 74; Tier Mature; LP $18.49M; Vol24H $20.13M; 24H +0.79%; V/LP 1.09x; 池数 1; 分项 L20/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [RAY](https://dexscreener.com/solana/2axxcn6on9bbt5owwmth53c7qhuxvhleu718kqt8rvy2) | SOL | [4k3Dyj...QrkX6R](https://solscan.io/token/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大市值 | Score 73; Tier Liquid; LP $1.31M; Vol24H $2.77M; 24H +4.63%; V/LP 2.12x; 池数 2; 分项 L19/V17/B22/Buy3/Risk-12 | 成熟池观察，不占用早期Alpha主榜 |
| [JUP](https://dexscreener.com/solana/3xngdc58axytrj64stqz5trdqwvtwhlr888irbbwznee) | SOL | [JUPyiw...NsDvCN](https://solscan.io/token/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) | 24H接近横盘；买卖基本均衡；LP达主观察门槛；24H成交合格；Volume/LP未失真；非主流报价池；LP超过早期Alpha主榜上限；FDV超过早期Alpha主榜上限；市值超过早期Alpha主榜上限；成熟大池；成熟大市值 | Score 71; Tier Mature; LP $163.10M; Vol24H $95.05M; 24H -2.47%; V/LP 0.58x; 池数 2; 分项 L20/V17/B22/Buy3/Risk-15 | 成熟池观察，不占用早期Alpha主榜 |

### E. 链上确认/紧急精查表
| Token | 链 | 合约地址 | 是否需要链上确认 | 紧急精查 | 预检状态 | 原因 |
|---|---|---|---|---|---|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | 是 | 是 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认；满足紧急精查候选：LP合格、低波动、买盘占优、非多池冲突 |
| [UOTF](https://dexscreener.com/solana/gertjb3hmeppgdaspb1ryrxvdmmqv2ukxszhzeytgptu) | SOL | [HXRgj1...Uhpump](https://solscan.io/token/HXRgj1EdGa2Y31RGAmnSXS5VMob5iqz5NA9q3pUhpump) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| [App](https://dexscreener.com/solana/95xzpaggkdazgfdenx1dxfkuyzfvk53geu7mfa58qffw) | SOL | [49nkLr...Ta8pTL](https://solscan.io/token/49nkLrXi8nCZBVKsShDNasEtPe4Vn1mx9Xbr3kTa8pTL) | 是 | 否 | verified / address_preflight_v0.4 | 观察池候选需要链上Swap/钱包留存确认 |
| 牛来 | BSC | [0xbeea...377777](https://bscscan.com/token/0xbeea1d618e533a387d941f58a7d4c9b7bd377777) | 是 | 否 | verified / address_preflight_v0.4 | 多池数据冲突，需链上/聚合源复核；PVP候选仅记录，非紧急精查 |
| CATE | SOL | [Ai66LH...5ppump](https://solscan.io/token/Ai66LHZG9MCzg1WKdawwqduVAXpNDUuV8M3uyq5ppump) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| [RAYCAT](https://dexscreener.com/solana/987vwvjz5frjwcy9zwc2trugl8fbmt1af4purt7xjpjd) | SOL | [CFNRDa...jNupFL](https://solscan.io/token/CFNRDaxFcvRwRSNnA5cHrCCr6AHhk9dNkHWpRUjNupFL) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| CYBERLEEK | SOL | [ApZuxd...iipbKg](https://solscan.io/token/ApZuxdpzMrbEYTGEzeY9afh5pj9d6qPRJCTgQYiipbKg) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |
| Bicat | BSC | [0xdbc6...207777](https://bscscan.com/token/0xdbc6333a7d8bcd95f96641eda4d095e69f207777) | 是 | 否 | verified / address_preflight_v0.4 | PVP候选仅记录，非紧急精查 |

### F. 钱包行为 / AVE命中样本表
| Token | 链 | 合约地址 | 行为状态 | 行为层级 | AVE命中 | 判断 |
|---|---|---|---|---|---:|---|
| TUT | BSC | [0xcaae...b799f3](https://bscscan.com/token/0xcaae2a2f939f51d97cdfa9a86e79e3f085b799f3) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| KII | BSC | [0xeec6...197886](https://bscscan.com/token/0xeec6574eabba52bac3f0277f2cd5ac7e67197886) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |
| NVDAB | BSC | [0x02fc...8a7436](https://bscscan.com/token/0x02fca66c1d1afb4e2a7884261eb00f63598a7436) | checked | bsc_transfer_activity_v0.5 | 0 | 钱包级数据不可用；当前仅代理指标；AVE周缓存可用，等待本轮链上行为映射；本轮行为未命中AVE缓存钱包 |

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
| LP层级 | Micro 5 / Early 11 / Liquid 6 / Mature 3 | 下一步可以按层级分别设置进攻规则 |
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
| dexscreener_search | {'ok': True, 'count': 360} |
| geckoterminal_bsc_trending | {'ok': True, 'count': 20} |
| geckoterminal_solana_trending | {'ok': True, 'count': 20} |

## 数据限制
- This v0.4 scan uses free public sources plus lightweight chain address/account preflight when enabled.
- AVE Smart Money weekly cache structure is connected; real AVE API refresh is handled by the weekly workflow/cache file.
- S0 exact historical replay is not implemented yet; candidates are marked with current metrics only.
- Wallet-level buy/sell retention is not implemented yet; v0.4 only preflights token contract/account existence.
- v0.4 adds chain preflight status and Smart Wallet cache status on top of contract-address output, liquidity tiers, visible PVP/mature detail tables, and chain-verify flags.
- Contract addresses are extracted from DEXScreener baseToken or GeckoTerminal relationships when available; missing addresses are explicitly marked unavailable.
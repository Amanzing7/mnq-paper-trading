# Backtest on recent history (about 60 days of free 5-minute data)

Data: 2026-08-28 to 2026-11-06, $1,000 account, 1 contract(s).

| Filter | Trades | Win % | Net $ | Return % | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| No filter (baseline) | 46 | 73.9 | 300.5 | 30.0 | 170.75 | 1.28 |
| 1 Daily EMA trend | 22 | 77.3 | 140.25 | 14.0 | 268.25 | 1.29 |
| 2 Range size vs daily ATR | 38 | 81.6 | 518.75 | 51.9 | 170.75 | 1.65 |
| 3 60m ADX trend strength | 28 | 67.9 | -87.0 | -8.7 | 254.0 | 0.9 |
| 4 Globex VWAP bias | 33 | 72.7 | 174.75 | 17.5 | 254.5 | 1.23 |
| 5 Breakout volume | 16 | 56.2 | -208.0 | -20.8 | 408.75 | 0.68 |

With only ~40 trading days this is a smoke test, not proof.

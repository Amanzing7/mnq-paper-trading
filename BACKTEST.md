# Backtest on recent history

Each filter row is its own $1,000 account. Futures use ~60 days of Yahoo data; Hyperliquid perps only have ~17 days of 5-minute history. These samples are tiny: a smoke test, not proof.

Avg R is profit per trade in units of the risk planned at entry, so markets and venues can be compared without caring about position size. Perp tests skip bars when the underlying futures market is closed (Friday 17:00 to Sunday 18:00 New York time, and 17:00-18:00 daily), and size every trade to the same dollar risk (up to a notional cap).

## MNQ: Micro Nasdaq-100

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 46 | 71.7 | 199.5 | 0.047 | 223.25 | 1.17 |
| 1 daily EMA | 23 | 73.9 | 61.5 | 0.079 | 312.0 | 1.11 |
| 2 range/ATR | 38 | 78.9 | 417.75 | 0.16 | 170.75 | 1.47 |
| 3 60m ADX | 28 | 67.9 | -81.5 | -0.013 | 252.25 | 0.9 |
| 4 Globex VWAP | 33 | 69.7 | 72.25 | 0.015 | 245.75 | 1.08 |
| 5 volume | 15 | 53.3 | -258.25 | -0.228 | 396.5 | 0.59 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 46 | 71.7 | 199.5 | 0.047 | 1.17 |
| no cap | 50 | 68.0 | -322.0 | -0.007 | 0.82 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 46 | 71.7 | 199.5 | 0.047 | 1.17 |
| 10 bps | 35 | 74.3 | 241.75 | 0.091 | 1.25 |
| 15 bps | 21 | 71.4 | 121.5 | 0.053 | 1.17 |
| 20 bps | 9 | 66.7 | -14.25 | -0.016 | 0.96 |
| 30 bps | 0 |  |  |  |  |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 40 | 72.5 | 440.0 | 0.048 | 1.72 |
| Original | 46 | 71.7 | 199.5 | 0.047 | 1.17 |
| London | 36 | 72.2 | 333.25 | 0.061 | 1.33 |
| NY | 1 | 100.0 | 47.75 | 0.48 | inf |

## MES: Micro S&P 500

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 50 | 74.0 | -76.88 | 0.006 | 132.0 | 0.85 |
| 1 daily EMA | 22 | 68.2 | -60.5 | -0.118 | 103.12 | 0.71 |
| 2 range/ATR | 34 | 70.6 | -85.38 | -0.01 | 118.75 | 0.8 |
| 3 60m ADX | 36 | 75.0 | -34.0 | 0.025 | 127.62 | 0.9 |
| 4 Globex VWAP | 36 | 66.7 | -176.5 | -0.1 | 203.5 | 0.61 |
| 5 volume | 17 | 58.8 | -155.5 | -0.178 | 201.0 | 0.47 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 50 | 74.0 | -76.88 | 0.006 | 0.85 |
| no cap | 50 | 74.0 | -76.88 | 0.006 | 0.85 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 50 | 74.0 | -76.88 | 0.006 | 0.85 |
| 10 bps | 13 | 61.5 | -98.88 | -0.077 | 0.63 |
| 15 bps | 4 | 25.0 | -136.62 | -0.481 | 0.16 |
| 20 bps | 1 | 0.0 | -26.5 | -0.252 | 0.0 |
| 30 bps | 0 |  |  |  |  |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 46 | 63.0 | -80.88 | -0.206 | 0.85 |
| Original | 50 | 74.0 | -76.88 | 0.006 | 0.85 |
| London | 49 | 71.4 | 165.25 | 0.011 | 1.24 |
| NY | 44 | 61.4 | -534.75 | -0.075 | 0.68 |

## MYM: Micro Dow

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 50 | 70.0 | -123.25 | -0.1 | 197.5 | 0.65 |
| 1 daily EMA | 27 | 63.0 | -101.25 | -0.213 | 165.0 | 0.52 |
| 2 range/ATR | 26 | 46.2 | -190.0 | -0.413 | 238.75 | 0.43 |
| 3 60m ADX | 27 | 70.4 | -49.0 | -0.086 | 90.75 | 0.75 |
| 4 Globex VWAP | 34 | 70.6 | -66.75 | -0.094 | 138.0 | 0.7 |
| 5 volume | 20 | 85.0 | 50.25 | 0.133 | 58.5 | 1.63 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 50 | 70.0 | -123.25 | -0.1 | 0.65 |
| no cap | 50 | 70.0 | -123.25 | -0.1 | 0.65 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 50 | 70.0 | -123.25 | -0.1 | 0.65 |
| 10 bps | 8 | 62.5 | -10.0 | -0.129 | 0.9 |
| 15 bps | 2 | 100.0 | 52.25 | 0.464 | inf |
| 20 bps | 1 | 100.0 | 29.75 | 0.469 | inf |
| 30 bps | 0 |  |  |  |  |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 47 | 76.6 | 48.5 | -0.026 | 1.21 |
| Original | 50 | 70.0 | -123.25 | -0.1 | 0.65 |
| London | 49 | 71.4 | 146.25 | 0.019 | 1.29 |
| NY | 40 | 57.5 | -453.25 | -0.11 | 0.7 |

## M2K: Micro Russell 2000

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 50 | 60.0 | -163.0 | -0.281 | 168.5 | 0.46 |
| 1 daily EMA | 28 | 57.1 | -95.75 | -0.272 | 95.75 | 0.48 |
| 2 range/ATR | 30 | 56.7 | -129.75 | -0.3 | 140.0 | 0.46 |
| 3 60m ADX | 33 | 60.6 | -88.75 | -0.251 | 92.25 | 0.53 |
| 4 Globex VWAP | 27 | 63.0 | -87.25 | -0.249 | 89.25 | 0.49 |
| 5 volume | 17 | 70.6 | -14.75 | -0.129 | 29.5 | 0.8 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 50 | 60.0 | -163.0 | -0.281 | 0.46 |
| no cap | 50 | 60.0 | -163.0 | -0.281 | 0.46 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 50 | 60.0 | -163.0 | -0.281 | 0.46 |
| 10 bps | 17 | 58.8 | -79.5 | -0.229 | 0.51 |
| 15 bps | 7 | 57.1 | -42.75 | -0.231 | 0.49 |
| 20 bps | 0 |  |  |  |  |
| 30 bps | 0 |  |  |  |  |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 46 | 67.4 | -36.0 | -0.176 | 0.83 |
| Original | 50 | 60.0 | -163.0 | -0.281 | 0.46 |
| London | 50 | 62.0 | -198.5 | -0.141 | 0.62 |
| NY | 48 | 56.2 | -574.0 | -0.146 | 0.59 |

## MCL: Micro WTI crude

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 50 | 66.0 | -173.0 | -0.113 | 242.5 | 0.72 |
| 1 daily EMA | 35 | 65.7 | -188.5 | -0.119 | 249.0 | 0.59 |
| 2 range/ATR | 36 | 58.3 | -215.0 | -0.219 | 281.0 | 0.61 |
| 3 60m ADX | 27 | 63.0 | -129.5 | -0.15 | 233.5 | 0.67 |
| 4 Globex VWAP | 33 | 66.7 | -71.0 | -0.104 | 156.0 | 0.81 |
| 5 volume | 25 | 68.0 | -27.0 | -0.074 | 98.5 | 0.91 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| no cap | 50 | 66.0 | -173.0 | -0.113 | 0.72 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| 10 bps | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| 15 bps | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| 20 bps | 44 | 61.4 | -209.5 | -0.177 | 0.66 |
| 30 bps | 23 | 65.2 | -59.5 | -0.093 | 0.83 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 47 | 74.5 | 26.5 | -0.027 | 1.09 |
| Original | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| London | 49 | 69.4 | -60.5 | -0.017 | 0.94 |
| NY | 49 | 61.2 | -337.0 | -0.127 | 0.75 |

## MGC: Micro gold

2026-09-01 to 2026-11-10

Daily data: 252 rows, 2025-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 72.3 | 220.49 | 0.047 | 478.01 | 1.2 |
| 1 daily EMA | 30 | 80.0 | 360.99 | 0.163 | 276.51 | 1.68 |
| 2 range/ATR | 46 | 71.7 | 201.49 | 0.039 | 497.01 | 1.18 |
| 3 60m ADX | 28 | 78.6 | 341.99 | 0.144 | 304.51 | 1.61 |
| 4 Globex VWAP | 25 | 76.0 | 264.5 | 0.101 | 308.51 | 1.55 |
| 5 volume | 15 | 66.7 | -57.01 | -0.034 | 316.01 | 0.89 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 47 | 72.3 | 220.49 | 0.047 | 1.2 |
| no cap | 50 | 74.0 | 475.49 | 0.074 | 1.43 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 47 | 72.3 | 220.49 | 0.047 | 1.2 |
| 10 bps | 45 | 71.1 | 186.49 | 0.03 | 1.17 |
| 15 bps | 31 | 71.0 | 170.99 | 0.034 | 1.2 |
| 20 bps | 20 | 75.0 | 238.99 | 0.099 | 1.43 |
| 30 bps | 5 | 80.0 | 130.5 | 0.18 | 1.98 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 45 | 68.9 | 140.01 | -0.017 | 1.17 |
| Original | 47 | 72.3 | 220.49 | 0.047 | 1.2 |
| London | 47 | 61.7 | -471.49 | -0.118 | 0.73 |
| NY | 15 | 86.7 | 605.49 | 0.332 | 5.55 |

## XYZ100: XYZ100-USDC (Nasdaq-100 perp)

2026-10-24 to 2026-11-10

Daily data: 394 rows, 2025-10-13 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 70.8 | -11.49 | -0.069 | 70.81 | 0.92 |
| 1 daily EMA | 23 | 69.6 | -10.99 | -0.175 | 27.82 | 0.81 |
| 2 range/ATR | 34 | 79.4 | 12.73 | 0.006 | 26.16 | 1.22 |
| 3 60m ADX | 35 | 65.7 | -46.52 | -0.168 | 63.09 | 0.61 |
| 4 Globex VWAP | 37 | 73.0 | 24.93 | -0.01 | 33.73 | 1.27 |
| 5 volume | 16 | 68.8 | -2.16 | 0.022 | 39.26 | 0.97 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 70.8 | 47.63 | 1.39 |

Average stop distance 45.9 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 70.8 | -11.49 | -0.069 | 0.92 |
| 40 bps | 30 | 80.0 | 7.99 | -0.063 | 1.18 |
| 30 bps | 24 | 79.2 | -1.29 | -0.112 | 0.96 |
| 25 bps | 20 | 80.0 | 0.66 | -0.129 | 1.03 |
| 20 bps | 16 | 75.0 | -7.51 | -0.241 | 0.63 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 70.8 | -11.49 | -0.069 | 0.92 |
| 10 bps | 47 | 72.3 | -8.33 | -0.023 | 0.94 |
| 15 bps | 38 | 71.1 | -3.48 | 0.018 | 0.97 |
| 20 bps | 32 | 68.8 | -3.97 | 0.017 | 0.97 |
| 30 bps | 24 | 62.5 | -10.19 | -0.025 | 0.91 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 75.0 | 16.61 | -0.123 | 1.73 |
| Original | 12 | 75.0 | -17.04 | -0.132 | 0.42 |
| London | 12 | 91.7 | 32.26 | 0.184 | 7.33 |
| NY | 12 | 41.7 | -43.32 | -0.205 | 0.5 |

## SP500: SP500-USDC (S&P 500 perp)

2026-10-24 to 2026-11-10

Daily data: 238 rows, 2026-03-18 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 52.1 | -40.43 | -0.272 | 49.03 | 0.61 |
| 1 daily EMA | 19 | 42.1 | -7.23 | -0.212 | 23.07 | 0.76 |
| 2 range/ATR | 34 | 55.9 | -22.32 | -0.221 | 31.75 | 0.56 |
| 3 60m ADX | 38 | 47.4 | -63.54 | -0.359 | 68.9 | 0.35 |
| 4 Globex VWAP | 33 | 60.6 | -8.17 | -0.19 | 28.8 | 0.88 |
| 5 volume | 17 | 58.8 | -31.53 | -0.262 | 38.53 | 0.53 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 70.8 | 21.4 | 1.27 |

Average stop distance 25.7 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 52.1 | -40.43 | -0.272 | 0.61 |
| 40 bps | 42 | 52.4 | -30.47 | -0.299 | 0.57 |
| 30 bps | 37 | 48.6 | -39.8 | -0.362 | 0.38 |
| 25 bps | 34 | 44.1 | -48.69 | -0.426 | 0.24 |
| 20 bps | 30 | 43.3 | -34.73 | -0.421 | 0.24 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 52.1 | -40.43 | -0.272 | 0.61 |
| 10 bps | 34 | 67.6 | -26.51 | -0.145 | 0.71 |
| 15 bps | 24 | 66.7 | -13.52 | -0.082 | 0.81 |
| 20 bps | 18 | 66.7 | -5.7 | -0.023 | 0.9 |
| 30 bps | 11 | 63.6 | -0.63 | 0.031 | 0.98 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | 8.6 | -0.23 | 1.92 |
| Original | 12 | 33.3 | -19.06 | -0.423 | 0.1 |
| London | 12 | 66.7 | -1.89 | -0.212 | 0.88 |
| NY | 12 | 50.0 | -28.08 | -0.223 | 0.52 |

## GOLD: GOLD-USDC (gold perp)

2026-10-24 to 2026-11-10

Daily data: 324 rows, 2025-12-22 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 12.5 | -251.68 | -1.013 | 256.96 | 0.06 |
| 1 daily EMA | 26 | 7.7 | -133.08 | -1.17 | 137.72 | 0.06 |
| 2 range/ATR | 35 | 5.7 | -174.68 | -1.063 | 175.01 | 0.01 |
| 3 60m ADX | 38 | 15.8 | -204.06 | -0.946 | 209.33 | 0.07 |
| 4 Globex VWAP | 29 | 13.8 | -139.16 | -0.974 | 143.79 | 0.09 |
| 5 volume | 19 | 21.1 | -99.06 | -0.684 | 99.7 | 0.06 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 70.8 | 40.07 | 1.43 |

Average stop distance 31.7 bps of price (target is half of that). Assumed round-trip cost about 22.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 12.5 | -251.68 | -1.013 | 0.06 |
| 40 bps | 37 | 0.0 | -190.63 | -1.209 | 0.0 |
| 30 bps | 32 | 0.0 | -169.19 | -1.327 | 0.0 |
| 25 bps | 27 | 0.0 | -159.86 | -1.53 | 0.0 |
| 20 bps | 20 | 0.0 | -120.31 | -1.768 | 0.0 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 12.5 | -251.68 | -1.013 | 0.06 |
| 10 bps | 43 | 14.0 | -222.19 | -0.822 | 0.06 |
| 15 bps | 34 | 17.6 | -160.88 | -0.558 | 0.09 |
| 20 bps | 28 | 21.4 | -131.37 | -0.474 | 0.1 |
| 30 bps | 16 | 37.5 | -82.5 | -0.386 | 0.15 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 8.3 | -68.82 | -1.323 | 0.07 |
| Original | 12 | 8.3 | -50.78 | -1.09 | 0.01 |
| London | 12 | 0.0 | -87.25 | -1.323 | 0.0 |
| NY | 12 | 33.3 | -44.83 | -0.316 | 0.17 |

## WTIOIL: WTIOIL-USDC (WTI crude perp)

2026-10-24 to 2026-11-10

Daily data: 309 rows, 2026-01-06 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 66.7 | -26.11 | -0.11 | 67.88 | 0.88 |
| 1 daily EMA | 31 | 67.7 | -36.28 | -0.087 | 52.0 | 0.74 |
| 2 range/ATR | 41 | 68.3 | -26.38 | -0.092 | 60.91 | 0.86 |
| 3 60m ADX | 39 | 71.8 | 10.4 | -0.041 | 45.52 | 1.07 |
| 4 Globex VWAP | 37 | 64.9 | -42.66 | -0.122 | 60.91 | 0.77 |
| 5 volume | 9 | 55.6 | -15.13 | -0.166 | 40.85 | 0.72 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 66.7 | 34.77 | 1.19 |

Average stop distance 52.3 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 66.7 | -26.11 | -0.11 | 0.88 |
| 40 bps | 20 | 55.0 | -54.22 | -0.375 | 0.37 |
| 30 bps | 14 | 50.0 | -46.93 | -0.481 | 0.24 |
| 25 bps | 8 | 50.0 | -24.91 | -0.527 | 0.18 |
| 20 bps | 6 | 50.0 | -19.03 | -0.546 | 0.14 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 66.7 | -26.11 | -0.11 | 0.88 |
| 10 bps | 47 | 66.0 | -26.45 | -0.115 | 0.87 |
| 15 bps | 46 | 65.2 | -27.54 | -0.122 | 0.87 |
| 20 bps | 42 | 69.0 | -7.08 | -0.048 | 0.96 |
| 30 bps | 34 | 73.5 | 20.82 | 0.043 | 1.14 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -21.62 | -0.31 | 0.57 |
| Original | 12 | 58.3 | -19.12 | -0.289 | 0.63 |
| London | 12 | 91.7 | 44.97 | 0.292 | 3.11 |
| NY | 12 | 58.3 | -30.33 | -0.132 | 0.65 |

## BRENTOIL: BRENTOIL-USDC (Brent crude perp)

2026-10-24 to 2026-11-10

Daily data: 252 rows, 2026-03-04 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 70.8 | 4.24 | -0.052 | 52.19 | 1.02 |
| 1 daily EMA | 32 | 71.9 | -25.95 | -0.012 | 50.97 | 0.82 |
| 2 range/ATR | 38 | 73.7 | 4.43 | 0.004 | 48.22 | 1.03 |
| 3 60m ADX | 37 | 73.0 | 22.46 | -0.002 | 49.48 | 1.17 |
| 4 Globex VWAP | 36 | 69.4 | -19.1 | -0.066 | 35.89 | 0.87 |
| 5 volume | 14 | 71.4 | 5.89 | -0.053 | 21.65 | 1.11 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 70.8 | 64.3 | 1.4 |

Average stop distance 50.2 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 70.8 | 4.24 | -0.052 | 1.02 |
| 40 bps | 19 | 68.4 | -17.82 | -0.189 | 0.66 |
| 30 bps | 12 | 66.7 | -13.64 | -0.267 | 0.51 |
| 25 bps | 9 | 66.7 | -9.97 | -0.3 | 0.45 |
| 20 bps | 7 | 57.1 | -14.45 | -0.481 | 0.21 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 70.8 | 4.24 | -0.052 | 1.02 |
| 10 bps | 48 | 70.8 | 4.24 | -0.052 | 1.02 |
| 15 bps | 43 | 72.1 | 13.38 | -0.004 | 1.08 |
| 20 bps | 41 | 73.2 | 18.68 | 0.022 | 1.11 |
| 30 bps | 36 | 72.2 | 17.88 | 0.02 | 1.12 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 66.7 | 1.31 | -0.205 | 1.04 |
| Original | 12 | 66.7 | -25.74 | -0.161 | 0.53 |
| London | 12 | 83.3 | 25.66 | 0.166 | 1.7 |
| NY | 12 | 66.7 | 3.01 | -0.006 | 1.05 |

## LT_US100: Lighter US100 (Nasdaq-100)

2026-10-24 to 2026-11-10

Daily data: 175 rows, 2026-05-20 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 62.5 | -48.08 | -0.173 | 88.56 | 0.73 |
| 1 daily EMA | 22 | 63.6 | -22.8 | -0.227 | 41.15 | 0.67 |
| 2 range/ATR | 34 | 67.6 | -26.66 | -0.146 | 56.04 | 0.72 |
| 3 60m ADX | 35 | 54.3 | -80.84 | -0.316 | 98.05 | 0.48 |
| 4 Globex VWAP | 33 | 63.6 | -7.65 | -0.123 | 36.28 | 0.93 |
| 5 volume | 17 | 58.8 | -21.99 | -0.216 | 35.03 | 0.67 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 62.5 | 7.75 | 1.05 |

Average stop distance 47.0 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 62.5 | -48.08 | -0.173 | 0.73 |
| 40 bps | 30 | 66.7 | -31.33 | -0.231 | 0.61 |
| 30 bps | 24 | 62.5 | -41.2 | -0.327 | 0.39 |
| 25 bps | 21 | 66.7 | -24.25 | -0.277 | 0.48 |
| 20 bps | 17 | 64.7 | -23.22 | -0.33 | 0.4 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 62.5 | -48.08 | -0.173 | 0.73 |
| 10 bps | 47 | 63.8 | -44.66 | -0.132 | 0.75 |
| 15 bps | 42 | 61.9 | -42.35 | -0.134 | 0.75 |
| 20 bps | 31 | 61.3 | -24.86 | -0.087 | 0.82 |
| 30 bps | 24 | 62.5 | -6.87 | -0.019 | 0.94 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 75.0 | 19.34 | -0.083 | 1.84 |
| Original | 12 | 66.7 | -29.83 | -0.209 | 0.29 |
| London | 12 | 66.7 | 4.66 | -0.195 | 1.16 |
| NY | 12 | 41.7 | -42.24 | -0.205 | 0.51 |

## LT_US500: Lighter US500 (S&P 500)

2026-10-24 to 2026-11-10

Daily data: 176 rows, 2026-05-19 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 50.0 | -36.41 | -0.445 | 45.02 | 0.66 |
| 1 daily EMA | 21 | 47.6 | -4.44 | -0.357 | 28.45 | 0.86 |
| 2 range/ATR | 32 | 53.1 | -51.95 | -0.526 | 56.0 | 0.36 |
| 3 60m ADX | 38 | 42.1 | -59.51 | -0.544 | 63.57 | 0.39 |
| 4 Globex VWAP | 34 | 58.8 | 0.94 | -0.209 | 29.97 | 1.01 |
| 5 volume | 16 | 50.0 | -2.51 | -0.456 | 15.0 | 0.94 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 64.6 | 22.07 | 1.3 |

Average stop distance 25.3 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 50.0 | -36.41 | -0.445 | 0.66 |
| 40 bps | 42 | 50.0 | -29.41 | -0.495 | 0.61 |
| 30 bps | 38 | 44.7 | -45.74 | -0.59 | 0.39 |
| 25 bps | 34 | 41.2 | -46.15 | -0.658 | 0.29 |
| 20 bps | 30 | 36.7 | -50.62 | -0.768 | 0.19 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 50.0 | -36.41 | -0.445 | 0.66 |
| 10 bps | 32 | 62.5 | -14.28 | -0.205 | 0.83 |
| 15 bps | 24 | 75.0 | 15.61 | 0.084 | 1.31 |
| 20 bps | 18 | 72.2 | 14.21 | 0.095 | 1.32 |
| 30 bps | 10 | 70.0 | 9.33 | 0.11 | 1.29 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 66.7 | 4.28 | -0.354 | 1.32 |
| Original | 12 | 25.0 | -23.32 | -0.788 | 0.11 |
| London | 12 | 41.7 | -13.66 | -0.644 | 0.46 |
| NY | 12 | 66.7 | -3.7 | 0.007 | 0.91 |

## LT_XAU: Lighter XAU (gold)

2026-10-24 to 2026-11-10

Daily data: 387 rows, 2025-10-20 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 72.9 | 9.27 | -0.017 | 48.14 | 1.09 |
| 1 daily EMA | 31 | 74.2 | -2.42 | -0.028 | 32.91 | 0.97 |
| 2 range/ATR | 37 | 75.7 | 6.17 | -0.029 | 45.12 | 1.09 |
| 3 60m ADX | 38 | 71.1 | 5.79 | -0.019 | 35.69 | 1.06 |
| 4 Globex VWAP | 30 | 76.7 | 27.17 | 0.091 | 33.6 | 1.51 |
| 5 volume | 18 | 72.2 | 9.29 | 0.085 | 26.23 | 1.21 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 75.0 | 63.93 | 1.76 |

Average stop distance 35.2 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 72.9 | 9.27 | -0.017 | 1.09 |
| 40 bps | 34 | 76.5 | 3.05 | -0.031 | 1.06 |
| 30 bps | 27 | 77.8 | -3.63 | -0.066 | 0.91 |
| 25 bps | 23 | 73.9 | -15.63 | -0.144 | 0.63 |
| 20 bps | 15 | 73.3 | -13.69 | -0.196 | 0.46 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 72.9 | 9.27 | -0.017 | 1.09 |
| 10 bps | 45 | 71.1 | 8.2 | -0.028 | 1.08 |
| 15 bps | 39 | 71.8 | 14.91 | 0.019 | 1.16 |
| 20 bps | 33 | 72.7 | 22.96 | 0.064 | 1.28 |
| 30 bps | 21 | 66.7 | 12.91 | 0.045 | 1.2 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 91.7 | 27.43 | 0.194 | 4.66 |
| Original | 12 | 75.0 | -6.95 | -0.084 | 0.75 |
| London | 12 | 50.0 | -19.53 | -0.295 | 0.49 |
| NY | 12 | 75.0 | 8.32 | 0.115 | 1.25 |

## LT_WTI: Lighter WTI (crude)

2026-10-24 to 2026-11-10

Daily data: 266 rows, 2026-02-18 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 64.6 | -50.53 | -0.137 | 77.85 | 0.78 |
| 1 daily EMA | 31 | 64.5 | -46.27 | -0.126 | 53.68 | 0.7 |
| 2 range/ATR | 41 | 68.3 | -21.19 | -0.084 | 58.53 | 0.89 |
| 3 60m ADX | 38 | 71.1 | 8.44 | -0.047 | 43.05 | 1.06 |
| 4 Globex VWAP | 38 | 63.2 | -69.11 | -0.148 | 85.9 | 0.66 |
| 5 volume | 12 | 41.7 | -73.69 | -0.493 | 73.69 | 0.31 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 64.6 | 4.44 | 1.02 |

Average stop distance 52.8 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 64.6 | -50.53 | -0.137 | 0.78 |
| 40 bps | 19 | 57.9 | -42.08 | -0.338 | 0.4 |
| 30 bps | 15 | 60.0 | -26.79 | -0.326 | 0.43 |
| 25 bps | 10 | 60.0 | -17.29 | -0.363 | 0.36 |
| 20 bps | 8 | 50.0 | -21.52 | -0.541 | 0.2 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 64.6 | -50.53 | -0.137 | 0.78 |
| 10 bps | 47 | 63.8 | -50.97 | -0.144 | 0.78 |
| 15 bps | 46 | 65.2 | -44.75 | -0.116 | 0.8 |
| 20 bps | 40 | 67.5 | -29.01 | -0.056 | 0.86 |
| 30 bps | 33 | 66.7 | -23.75 | -0.052 | 0.87 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -19.35 | -0.315 | 0.59 |
| Original | 12 | 66.7 | -3.34 | -0.161 | 0.91 |
| London | 12 | 83.3 | 29.94 | 0.181 | 1.82 |
| NY | 12 | 50.0 | -57.79 | -0.254 | 0.45 |

## LT_BRENT: Lighter BRENTOIL (Brent)

2026-10-24 to 2026-11-10

Daily data: 232 rows, 2026-03-24 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 48 | 70.8 | 33.8 | -0.052 | 47.92 | 1.21 |
| 1 daily EMA | 30 | 76.7 | 27.92 | 0.072 | 40.25 | 1.3 |
| 2 range/ATR | 39 | 76.9 | 42.01 | 0.057 | 37.7 | 1.32 |
| 3 60m ADX | 40 | 70.0 | 18.36 | -0.046 | 45.02 | 1.12 |
| 4 Globex VWAP | 36 | 72.2 | 13.41 | -0.023 | 38.49 | 1.11 |
| 5 volume | 15 | 86.7 | 49.07 | 0.185 | 21.62 | 2.79 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 48 | 70.8 | 87.02 | 1.64 |

Average stop distance 49.5 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 48 | 70.8 | 33.8 | -0.052 | 1.21 |
| 40 bps | 22 | 59.1 | -39.73 | -0.326 | 0.5 |
| 30 bps | 14 | 57.1 | -24.76 | -0.412 | 0.4 |
| 25 bps | 12 | 50.0 | -31.09 | -0.546 | 0.25 |
| 20 bps | 7 | 57.1 | -10.82 | -0.498 | 0.31 |

Minimum stop-width test (no filter):

| Skip stops narrower than | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| nothing | 48 | 70.8 | 33.8 | -0.052 | 1.21 |
| 10 bps | 47 | 72.3 | 38.59 | -0.019 | 1.25 |
| 15 bps | 42 | 73.8 | 46.59 | 0.032 | 1.32 |
| 20 bps | 41 | 73.2 | 44.62 | 0.024 | 1.31 |
| 30 bps | 34 | 76.5 | 58.56 | 0.097 | 1.49 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -13.4 | -0.351 | 0.67 |
| Original | 12 | 66.7 | -7.59 | -0.163 | 0.81 |
| London | 12 | 91.7 | 47.27 | 0.309 | 3.21 |
| NY | 12 | 66.7 | 7.51 | -0.001 | 1.13 |

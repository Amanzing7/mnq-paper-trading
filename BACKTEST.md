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

## MCL: Micro WTI crude

2026-09-01 to 2026-11-10

Daily data: 1 rows, 2026-11-10 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 50 | 66.0 | -173.0 | -0.113 | 242.5 | 0.72 |
| 1 daily EMA | 0 |  |  |  |  |  |
| 2 range/ATR | 0 |  |  |  |  |  |
| 3 60m ADX | 27 | 63.0 | -129.5 | -0.15 | 233.5 | 0.67 |
| 4 Globex VWAP | 33 | 66.7 | -71.0 | -0.104 | 156.0 | 0.81 |
| 5 volume | 25 | 68.0 | -27.0 | -0.074 | 98.5 | 0.91 |

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| $150 cap (as now) | 50 | 66.0 | -173.0 | -0.113 | 0.72 |
| no cap | 50 | 66.0 | -173.0 | -0.113 | 0.72 |

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

## XYZ100: XYZ100-USDC (Nasdaq-100 perp)

2026-10-24 to 2026-11-10

Daily data: 394 rows, 2025-10-13 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 70.2 | -20.62 | -0.08 | 70.81 | 0.86 |
| 1 daily EMA | 23 | 69.6 | -10.99 | -0.175 | 27.82 | 0.81 |
| 2 range/ATR | 34 | 79.4 | 12.73 | 0.006 | 26.16 | 1.22 |
| 3 60m ADX | 33 | 63.6 | -58.65 | -0.203 | 63.09 | 0.51 |
| 4 Globex VWAP | 36 | 72.2 | 15.8 | -0.023 | 33.73 | 1.17 |
| 5 volume | 15 | 66.7 | -11.29 | -0.007 | 39.26 | 0.82 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 70.2 | 37.63 | 1.31 |

Average stop distance 44.9 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 70.2 | -20.62 | -0.08 | 0.86 |
| 40 bps | 30 | 80.0 | 7.99 | -0.063 | 1.18 |
| 30 bps | 24 | 79.2 | -1.29 | -0.112 | 0.96 |
| 25 bps | 20 | 80.0 | 0.66 | -0.129 | 1.03 |
| 20 bps | 16 | 75.0 | -7.51 | -0.241 | 0.63 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 75.0 | 16.61 | -0.123 | 1.73 |
| Original | 12 | 75.0 | -17.04 | -0.132 | 0.42 |
| London | 12 | 91.7 | 32.26 | 0.184 | 7.33 |
| NY | 11 | 36.4 | -52.45 | -0.265 | 0.39 |

## SP500: SP500-USDC (S&P 500 perp)

2026-10-24 to 2026-11-10

Daily data: 238 rows, 2026-03-18 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 53.2 | -21.56 | -0.254 | 39.17 | 0.75 |
| 1 daily EMA | 19 | 42.1 | -7.23 | -0.212 | 23.07 | 0.76 |
| 2 range/ATR | 34 | 55.9 | -22.32 | -0.221 | 31.75 | 0.56 |
| 3 60m ADX | 35 | 48.6 | -44.57 | -0.324 | 49.93 | 0.4 |
| 4 Globex VWAP | 33 | 60.6 | -8.17 | -0.19 | 28.8 | 0.88 |
| 5 volume | 16 | 62.5 | -12.66 | -0.209 | 28.67 | 0.74 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 72.3 | 38.54 | 1.63 |

Average stop distance 25.0 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 53.2 | -21.56 | -0.254 | 0.75 |
| 40 bps | 42 | 52.4 | -30.47 | -0.299 | 0.57 |
| 30 bps | 37 | 48.6 | -39.8 | -0.362 | 0.38 |
| 25 bps | 34 | 44.1 | -48.69 | -0.426 | 0.24 |
| 20 bps | 30 | 43.3 | -34.73 | -0.421 | 0.24 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | 8.6 | -0.23 | 1.92 |
| Original | 12 | 33.3 | -19.06 | -0.423 | 0.1 |
| London | 12 | 66.7 | -1.89 | -0.212 | 0.88 |
| NY | 11 | 54.5 | -9.2 | -0.144 | 0.77 |

## GOLD: GOLD-USDC (gold perp)

2026-10-24 to 2026-11-10

Daily data: 324 rows, 2025-12-22 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 10.6 | -256.32 | -1.039 | 256.96 | 0.04 |
| 1 daily EMA | 25 | 4.0 | -137.72 | -1.226 | 137.72 | 0.03 |
| 2 range/ATR | 35 | 5.7 | -174.68 | -1.063 | 175.01 | 0.01 |
| 3 60m ADX | 37 | 13.5 | -208.69 | -0.978 | 209.33 | 0.05 |
| 4 Globex VWAP | 28 | 10.7 | -143.79 | -1.017 | 143.79 | 0.06 |
| 5 volume | 19 | 21.1 | -99.06 | -0.684 | 99.7 | 0.06 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 70.2 | 30.07 | 1.33 |

Average stop distance 30.7 bps of price (target is half of that). Assumed round-trip cost about 22.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 10.6 | -256.32 | -1.039 | 0.04 |
| 40 bps | 37 | 0.0 | -190.63 | -1.209 | 0.0 |
| 30 bps | 32 | 0.0 | -169.19 | -1.327 | 0.0 |
| 25 bps | 27 | 0.0 | -159.86 | -1.53 | 0.0 |
| 20 bps | 20 | 0.0 | -120.31 | -1.768 | 0.0 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 8.3 | -68.82 | -1.323 | 0.07 |
| Original | 12 | 8.3 | -50.78 | -1.09 | 0.01 |
| London | 12 | 0.0 | -87.25 | -1.323 | 0.0 |
| NY | 11 | 27.3 | -49.47 | -0.366 | 0.09 |

## WTIOIL: WTIOIL-USDC (WTI crude perp)

2026-10-24 to 2026-11-10

Daily data: 309 rows, 2026-01-06 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 66.0 | -35.29 | -0.122 | 67.88 | 0.83 |
| 1 daily EMA | 31 | 67.7 | -36.28 | -0.087 | 52.0 | 0.74 |
| 2 range/ATR | 40 | 67.5 | -35.56 | -0.106 | 60.91 | 0.81 |
| 3 60m ADX | 38 | 71.1 | 1.22 | -0.054 | 45.52 | 1.01 |
| 4 Globex VWAP | 37 | 64.9 | -42.66 | -0.122 | 60.91 | 0.77 |
| 5 volume | 8 | 50.0 | -24.32 | -0.244 | 40.85 | 0.55 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 66.0 | 24.77 | 1.14 |

Average stop distance 51.4 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 66.0 | -35.29 | -0.122 | 0.83 |
| 40 bps | 20 | 55.0 | -54.22 | -0.375 | 0.37 |
| 30 bps | 14 | 50.0 | -46.93 | -0.481 | 0.24 |
| 25 bps | 8 | 50.0 | -24.91 | -0.527 | 0.18 |
| 20 bps | 6 | 50.0 | -19.03 | -0.546 | 0.14 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -21.62 | -0.31 | 0.57 |
| Original | 12 | 58.3 | -19.12 | -0.289 | 0.63 |
| London | 12 | 91.7 | 44.97 | 0.292 | 3.11 |
| NY | 11 | 54.5 | -39.52 | -0.186 | 0.54 |

## BRENTOIL: BRENTOIL-USDC (Brent crude perp)

2026-10-24 to 2026-11-10

Daily data: 252 rows, 2026-03-04 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 70.2 | -4.76 | -0.062 | 52.19 | 0.97 |
| 1 daily EMA | 32 | 71.9 | -25.95 | -0.012 | 50.97 | 0.82 |
| 2 range/ATR | 37 | 73.0 | -4.56 | -0.008 | 48.22 | 0.97 |
| 3 60m ADX | 36 | 72.2 | 13.47 | -0.015 | 49.48 | 1.1 |
| 4 Globex VWAP | 36 | 69.4 | -19.1 | -0.066 | 35.89 | 0.87 |
| 5 volume | 14 | 71.4 | 5.89 | -0.053 | 21.65 | 1.11 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 70.2 | 54.3 | 1.34 |

Average stop distance 49.7 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 70.2 | -4.76 | -0.062 | 0.97 |
| 40 bps | 19 | 68.4 | -17.82 | -0.189 | 0.66 |
| 30 bps | 12 | 66.7 | -13.64 | -0.267 | 0.51 |
| 25 bps | 9 | 66.7 | -9.97 | -0.3 | 0.45 |
| 20 bps | 7 | 57.1 | -14.45 | -0.481 | 0.21 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 66.7 | 1.31 | -0.205 | 1.04 |
| Original | 12 | 66.7 | -25.74 | -0.161 | 0.53 |
| London | 12 | 83.3 | 25.66 | 0.166 | 1.7 |
| NY | 11 | 63.6 | -5.99 | -0.048 | 0.9 |

## LT_US100: Lighter US100 (Nasdaq-100)

2026-10-24 to 2026-11-10

Daily data: 175 rows, 2026-05-20 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 61.7 | -57.38 | -0.187 | 88.56 | 0.68 |
| 1 daily EMA | 22 | 63.6 | -22.8 | -0.227 | 41.15 | 0.67 |
| 2 range/ATR | 34 | 67.6 | -26.66 | -0.146 | 56.04 | 0.72 |
| 3 60m ADX | 34 | 52.9 | -90.14 | -0.339 | 98.05 | 0.42 |
| 4 Globex VWAP | 33 | 63.6 | -7.65 | -0.123 | 36.28 | 0.93 |
| 5 volume | 17 | 58.8 | -21.99 | -0.216 | 35.03 | 0.67 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 61.7 | -2.24 | 0.98 |

Average stop distance 46.1 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 61.7 | -57.38 | -0.187 | 0.68 |
| 40 bps | 30 | 66.7 | -31.33 | -0.231 | 0.61 |
| 30 bps | 24 | 62.5 | -41.2 | -0.327 | 0.39 |
| 25 bps | 21 | 66.7 | -24.25 | -0.277 | 0.48 |
| 20 bps | 17 | 64.7 | -23.22 | -0.33 | 0.4 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 75.0 | 19.34 | -0.083 | 1.84 |
| Original | 12 | 66.7 | -29.83 | -0.209 | 0.29 |
| London | 12 | 66.7 | 4.66 | -0.195 | 1.16 |
| NY | 11 | 36.4 | -51.54 | -0.266 | 0.4 |

## LT_US500: Lighter US500 (S&P 500)

2026-10-24 to 2026-11-10

Daily data: 176 rows, 2026-05-19 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 46 | 52.2 | -17.71 | -0.43 | 45.02 | 0.8 |
| 1 daily EMA | 20 | 50.0 | -1.77 | -0.354 | 27.26 | 0.94 |
| 2 range/ATR | 30 | 56.7 | -33.25 | -0.509 | 41.57 | 0.47 |
| 3 60m ADX | 34 | 44.1 | -45.11 | -0.558 | 49.17 | 0.42 |
| 4 Globex VWAP | 33 | 60.6 | 3.61 | -0.203 | 29.97 | 1.06 |
| 5 volume | 15 | 53.3 | 0.16 | -0.458 | 14.39 | 1.0 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 46 | 67.4 | 37.17 | 1.64 |

Average stop distance 24.8 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 46 | 52.2 | -17.71 | -0.43 | 0.8 |
| 40 bps | 41 | 51.2 | -26.74 | -0.497 | 0.63 |
| 30 bps | 37 | 45.9 | -43.06 | -0.595 | 0.4 |
| 25 bps | 33 | 42.4 | -43.47 | -0.665 | 0.3 |
| 20 bps | 30 | 36.7 | -50.62 | -0.768 | 0.19 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 66.7 | 4.28 | -0.354 | 1.32 |
| Original | 12 | 25.0 | -23.32 | -0.788 | 0.11 |
| London | 11 | 45.5 | -10.99 | -0.664 | 0.51 |
| NY | 11 | 72.7 | 12.32 | 0.111 | 1.49 |

## LT_XAU: Lighter XAU (gold)

2026-10-24 to 2026-11-10

Daily data: 387 rows, 2025-10-20 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 72.3 | 7.22 | -0.02 | 48.14 | 1.07 |
| 1 daily EMA | 30 | 73.3 | -4.47 | -0.033 | 32.91 | 0.94 |
| 2 range/ATR | 37 | 75.7 | 6.17 | -0.029 | 45.12 | 1.09 |
| 3 60m ADX | 37 | 70.3 | 3.74 | -0.022 | 35.69 | 1.04 |
| 4 Globex VWAP | 29 | 75.9 | 25.12 | 0.09 | 33.6 | 1.48 |
| 5 volume | 17 | 70.6 | 7.24 | 0.084 | 26.23 | 1.17 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 74.5 | 60.15 | 1.71 |

Average stop distance 34.4 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 72.3 | 7.22 | -0.02 | 1.07 |
| 40 bps | 34 | 76.5 | 3.05 | -0.031 | 1.06 |
| 30 bps | 27 | 77.8 | -3.63 | -0.066 | 0.91 |
| 25 bps | 23 | 73.9 | -15.63 | -0.144 | 0.63 |
| 20 bps | 15 | 73.3 | -13.69 | -0.196 | 0.46 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 91.7 | 27.43 | 0.194 | 4.66 |
| Original | 12 | 75.0 | -6.95 | -0.084 | 0.75 |
| London | 12 | 50.0 | -19.53 | -0.295 | 0.49 |
| NY | 11 | 72.7 | 6.27 | 0.116 | 1.19 |

## LT_WTI: Lighter WTI (crude)

2026-10-24 to 2026-11-10

Daily data: 266 rows, 2026-02-18 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 63.8 | -59.89 | -0.15 | 77.85 | 0.74 |
| 1 daily EMA | 31 | 64.5 | -46.27 | -0.126 | 53.68 | 0.7 |
| 2 range/ATR | 40 | 67.5 | -30.55 | -0.097 | 58.53 | 0.84 |
| 3 60m ADX | 37 | 70.3 | -0.91 | -0.061 | 43.05 | 0.99 |
| 4 Globex VWAP | 38 | 63.2 | -69.11 | -0.148 | 85.9 | 0.66 |
| 5 volume | 12 | 41.7 | -73.69 | -0.493 | 73.69 | 0.31 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 63.8 | -5.56 | 0.97 |

Average stop distance 51.9 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 63.8 | -59.89 | -0.15 | 0.74 |
| 40 bps | 19 | 57.9 | -42.08 | -0.338 | 0.4 |
| 30 bps | 15 | 60.0 | -26.79 | -0.326 | 0.43 |
| 25 bps | 10 | 60.0 | -17.29 | -0.363 | 0.36 |
| 20 bps | 8 | 50.0 | -21.52 | -0.541 | 0.2 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -19.35 | -0.315 | 0.59 |
| Original | 12 | 66.7 | -3.34 | -0.161 | 0.91 |
| London | 12 | 83.3 | 29.94 | 0.181 | 1.82 |
| NY | 11 | 45.5 | -67.14 | -0.32 | 0.37 |

## LT_BRENT: Lighter BRENTOIL (Brent)

2026-10-24 to 2026-11-10

Daily data: 232 rows, 2026-03-24 to 2026-11-10.

| Filter | Trades | Win % | Net $ | Avg R | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|---|
| 0 none | 47 | 70.2 | 24.59 | -0.063 | 47.92 | 1.15 |
| 1 daily EMA | 30 | 76.7 | 27.92 | 0.072 | 40.25 | 1.3 |
| 2 range/ATR | 38 | 76.3 | 32.8 | 0.047 | 37.7 | 1.25 |
| 3 60m ADX | 39 | 69.2 | 9.15 | -0.059 | 45.02 | 1.06 |
| 4 Globex VWAP | 36 | 72.2 | 13.41 | -0.023 | 38.49 | 1.11 |
| 5 volume | 15 | 86.7 | 49.07 | 0.185 | 21.62 | 2.79 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 47 | 70.2 | 77.02 | 1.57 |

Average stop distance 48.8 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Stop-width cap test (no filter):

| Cap | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| no cap | 47 | 70.2 | 24.59 | -0.063 | 1.15 |
| 40 bps | 22 | 59.1 | -39.73 | -0.326 | 0.5 |
| 30 bps | 14 | 57.1 | -24.76 | -0.412 | 0.4 |
| 25 bps | 12 | 50.0 | -31.09 | -0.546 | 0.25 |
| 20 bps | 7 | 57.1 | -10.82 | -0.498 | 0.31 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Avg R | Profit factor |
|---|---|---|---|---|---|
| Asia | 12 | 58.3 | -13.4 | -0.351 | 0.67 |
| Original | 12 | 66.7 | -7.59 | -0.163 | 0.81 |
| London | 12 | 91.7 | 47.27 | 0.309 | 3.21 |
| NY | 11 | 63.6 | -1.7 | -0.043 | 0.97 |

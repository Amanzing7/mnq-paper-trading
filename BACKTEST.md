# Backtest on recent history

Each filter row is its own $1,000 account. Futures use ~60 days of Yahoo data; Hyperliquid perps only have ~17 days of 5-minute history. These samples are tiny: a smoke test, not proof.

## MNQ: Micro Nasdaq-100

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 46 | 71.7 | 199.5 | 223.25 | 1.17 |
| 1 daily EMA | 23 | 73.9 | 61.5 | 312.0 | 1.11 |
| 2 range/ATR | 38 | 78.9 | 417.75 | 170.75 | 1.47 |
| 3 60m ADX | 28 | 67.9 | -81.5 | 252.25 | 0.9 |
| 4 Globex VWAP | 33 | 69.7 | 72.25 | 245.75 | 1.08 |
| 5 volume | 15 | 53.3 | -258.25 | 396.5 | 0.59 |

## MES: Micro S&P 500

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 74.0 | -76.88 | 132.0 | 0.85 |
| 1 daily EMA | 22 | 68.2 | -60.5 | 103.12 | 0.71 |
| 2 range/ATR | 34 | 70.6 | -85.38 | 118.75 | 0.8 |
| 3 60m ADX | 36 | 75.0 | -34.0 | 127.62 | 0.9 |
| 4 Globex VWAP | 36 | 66.7 | -176.5 | 203.5 | 0.61 |
| 5 volume | 16 | 56.2 | -172.12 | 201.0 | 0.42 |

## MYM: Micro Dow

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 70.0 | -123.25 | 197.5 | 0.65 |
| 1 daily EMA | 27 | 63.0 | -101.25 | 165.0 | 0.52 |
| 2 range/ATR | 26 | 46.2 | -190.0 | 238.75 | 0.43 |
| 3 60m ADX | 27 | 70.4 | -49.0 | 90.75 | 0.75 |
| 4 Globex VWAP | 34 | 70.6 | -66.75 | 138.0 | 0.7 |
| 5 volume | 20 | 85.0 | 50.25 | 58.5 | 1.63 |

## M2K: Micro Russell 2000

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 60.0 | -163.0 | 168.5 | 0.46 |
| 1 daily EMA | 28 | 57.1 | -95.75 | 95.75 | 0.48 |
| 2 range/ATR | 30 | 56.7 | -129.75 | 140.0 | 0.46 |
| 3 60m ADX | 33 | 60.6 | -88.75 | 92.25 | 0.53 |
| 4 Globex VWAP | 27 | 63.0 | -87.25 | 89.25 | 0.49 |
| 5 volume | 17 | 70.6 | -14.75 | 29.5 | 0.8 |

## MCL: Micro WTI crude

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 66.0 | -173.0 | 242.5 | 0.72 |
| 1 daily EMA | 0 |  |  |  |  |
| 2 range/ATR | 0 |  |  |  |  |
| 3 60m ADX | 27 | 63.0 | -129.5 | 233.5 | 0.67 |
| 4 Globex VWAP | 33 | 66.7 | -71.0 | 156.0 | 0.81 |
| 5 volume | 25 | 68.0 | -27.0 | 98.5 | 0.91 |

## MGC: Micro gold

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 47 | 72.3 | 220.49 | 478.01 | 1.2 |
| 1 daily EMA | 30 | 80.0 | 360.99 | 276.51 | 1.68 |
| 2 range/ATR | 46 | 71.7 | 201.49 | 497.01 | 1.18 |
| 3 60m ADX | 28 | 78.6 | 341.99 | 304.51 | 1.61 |
| 4 Globex VWAP | 24 | 79.2 | 316.99 | 308.51 | 1.74 |
| 5 volume | 15 | 66.7 | -57.01 | 316.01 | 0.89 |

## XYZ100: XYZ100-USDC (Nasdaq-100 perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 55.2 | -48.62 | 78.2 | 0.71 |
| 1 daily EMA | 32 | 53.1 | -31.06 | 41.74 | 0.57 |
| 2 range/ATR | 37 | 81.1 | 9.59 | 24.88 | 1.16 |
| 3 60m ADX | 44 | 54.5 | -75.05 | 78.79 | 0.43 |
| 4 Globex VWAP | 50 | 60.0 | -5.85 | 36.73 | 0.95 |
| 5 volume | 21 | 42.9 | -24.95 | 50.07 | 0.65 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | 11.26 | 1.4 |
| Original | 17 | 58.8 | -22.84 | 0.37 |
| London | 16 | 75.0 | 22.94 | 3.21 |
| NY | 17 | 29.4 | -59.99 | 0.36 |

## SP500: SP500-USDC (S&P 500 perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 35.8 | -54.49 | 65.88 | 0.53 |
| 1 daily EMA | 27 | 25.9 | -24.18 | 37.55 | 0.46 |
| 2 range/ATR | 37 | 48.6 | -30.54 | 37.64 | 0.46 |
| 3 60m ADX | 49 | 32.7 | -71.27 | 73.69 | 0.27 |
| 4 Globex VWAP | 45 | 42.2 | -31.09 | 42.47 | 0.64 |
| 5 volume | 25 | 36.0 | -29.29 | 44.59 | 0.54 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 41.2 | -1.27 | 0.93 |
| Original | 17 | 23.5 | -27.1 | 0.07 |
| London | 16 | 43.8 | -12.21 | 0.48 |
| NY | 17 | 35.3 | -13.91 | 0.68 |

## WTIOIL: WTIOIL-USDC (WTI crude perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 58.2 | -84.65 | 112.79 | 0.68 |
| 1 daily EMA | 40 | 55.0 | -76.5 | 77.82 | 0.57 |
| 2 range/ATR | 44 | 68.2 | -32.67 | 61.33 | 0.83 |
| 3 60m ADX | 44 | 65.9 | -23.21 | 66.05 | 0.87 |
| 4 Globex VWAP | 53 | 58.5 | -83.88 | 92.7 | 0.64 |
| 5 volume | 14 | 57.1 | -18.54 | 46.87 | 0.69 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -28.55 | 0.55 |
| Original | 17 | 52.9 | -36.91 | 0.47 |
| London | 16 | 68.8 | 24.91 | 1.7 |
| NY | 17 | 52.9 | -44.1 | 0.55 |

## BRENTOIL: BRENTOIL-USDC (Brent crude perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 56.7 | -73.27 | 96.5 | 0.71 |
| 1 daily EMA | 44 | 54.5 | -79.36 | 88.0 | 0.59 |
| 2 range/ATR | 43 | 65.1 | -35.41 | 66.32 | 0.81 |
| 3 60m ADX | 41 | 65.9 | -12.12 | 57.75 | 0.92 |
| 4 Globex VWAP | 50 | 58.0 | -71.56 | 80.07 | 0.65 |
| 5 volume | 18 | 61.1 | -15.16 | 37.28 | 0.78 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -9.67 | 0.81 |
| Original | 17 | 52.9 | -43.01 | 0.41 |
| London | 16 | 68.8 | 3.86 | 1.07 |
| NY | 17 | 47.1 | -24.45 | 0.68 |

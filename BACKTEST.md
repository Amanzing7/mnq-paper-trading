# Backtest on recent history

Each filter row is its own $1,000 account. Futures use ~60 days of Yahoo data; Hyperliquid perps only have ~17 days of 5-minute history. These samples are tiny: a smoke test, not proof.

## MNQ: Micro Nasdaq-100

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 46 | 73.9 | 341.25 | 170.75 | 1.32 |
| 1 daily EMA | 23 | 78.3 | 205.25 | 268.25 | 1.42 |
| 2 range/ATR | 38 | 81.6 | 559.5 | 170.75 | 1.7 |
| 3 60m ADX | 28 | 67.9 | -92.0 | 254.0 | 0.89 |
| 4 Globex VWAP | 33 | 72.7 | 215.5 | 254.5 | 1.28 |
| 5 volume | 15 | 53.3 | -270.75 | 408.75 | 0.58 |

## MES: Micro S&P 500

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 72.0 | -117.5 | 153.62 | 0.78 |
| 1 daily EMA | 22 | 68.2 | -63.62 | 103.75 | 0.7 |
| 2 range/ATR | 34 | 70.6 | -88.5 | 118.12 | 0.8 |
| 3 60m ADX | 36 | 75.0 | -32.75 | 127.0 | 0.91 |
| 4 Globex VWAP | 36 | 63.9 | -216.5 | 240.38 | 0.56 |
| 5 volume | 16 | 56.2 | -170.25 | 199.12 | 0.42 |

## MYM: Micro Dow

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 70.0 | -122.25 | 197.5 | 0.65 |
| 1 daily EMA | 27 | 63.0 | -100.25 | 165.0 | 0.53 |
| 2 range/ATR | 26 | 46.2 | -190.0 | 238.75 | 0.43 |
| 3 60m ADX | 27 | 70.4 | -49.0 | 90.75 | 0.75 |
| 4 Globex VWAP | 34 | 70.6 | -65.75 | 138.0 | 0.71 |
| 5 volume | 19 | 89.5 | 66.75 | 58.5 | 2.14 |

## M2K: Micro Russell 2000

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 64.0 | -145.0 | 150.75 | 0.5 |
| 1 daily EMA | 28 | 64.3 | -78.5 | 78.5 | 0.54 |
| 2 range/ATR | 30 | 56.7 | -129.5 | 140.0 | 0.46 |
| 3 60m ADX | 33 | 66.7 | -70.75 | 74.5 | 0.59 |
| 4 Globex VWAP | 27 | 63.0 | -86.75 | 88.75 | 0.49 |
| 5 volume | 16 | 75.0 | -16.25 | 30.25 | 0.78 |

## MCL: Micro WTI crude

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 50 | 64.0 | -195.0 | 257.0 | 0.69 |
| 1 daily EMA | 0 |  |  |  |  |
| 2 range/ATR | 0 |  |  |  |  |
| 3 60m ADX | 28 | 64.3 | -115.5 | 220.0 | 0.7 |
| 4 Globex VWAP | 33 | 63.6 | -93.0 | 156.0 | 0.76 |
| 5 volume | 25 | 68.0 | -21.0 | 112.0 | 0.93 |

## MGC: Micro gold

2026-09-01 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 47 | 72.3 | 212.99 | 472.01 | 1.19 |
| 1 daily EMA | 30 | 80.0 | 351.5 | 273.5 | 1.65 |
| 2 range/ATR | 47 | 72.3 | 212.99 | 472.01 | 1.19 |
| 3 60m ADX | 28 | 78.6 | 331.49 | 304.51 | 1.58 |
| 4 Globex VWAP | 26 | 73.1 | 171.5 | 308.51 | 1.3 |
| 5 volume | 15 | 66.7 | -68.01 | 315.51 | 0.87 |

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
| 3 60m ADX | 50 | 32.0 | -71.41 | 73.83 | 0.27 |
| 4 Globex VWAP | 45 | 42.2 | -31.09 | 42.47 | 0.64 |
| 5 volume | 25 | 36.0 | -29.29 | 44.59 | 0.54 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 41.2 | -1.27 | 0.93 |
| Original | 17 | 23.5 | -27.1 | 0.07 |
| London | 16 | 43.8 | -12.21 | 0.48 |
| NY | 17 | 35.3 | -13.91 | 0.68 |

## GOLD: GOLD-USDC (gold perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 66 | 45.5 | -64.02 | 69.13 | 0.57 |
| 1 daily EMA | 33 | 45.5 | -31.06 | 38.83 | 0.53 |
| 2 range/ATR | 40 | 62.5 | -10.04 | 38.61 | 0.85 |
| 3 60m ADX | 51 | 47.1 | -55.81 | 63.81 | 0.55 |
| 4 Globex VWAP | 42 | 40.5 | -35.44 | 37.09 | 0.6 |
| 5 volume | 29 | 48.3 | -32.92 | 39.16 | 0.55 |

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 41.2 | -23.64 | 0.45 |
| Original | 17 | 52.9 | 3.05 | 1.17 |
| London | 16 | 31.2 | -37.2 | 0.2 |
| NY | 16 | 56.2 | -6.23 | 0.84 |

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

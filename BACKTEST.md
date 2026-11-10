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
| 5 volume | 17 | 58.8 | -155.5 | 201.0 | 0.47 |

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
| 4 Globex VWAP | 25 | 76.0 | 264.5 | 308.51 | 1.55 |
| 5 volume | 15 | 66.7 | -57.01 | 316.01 | 0.89 |

## XYZ100: XYZ100-USDC (Nasdaq-100 perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 55.9 | -40.35 | 77.53 | 0.76 |
| 1 daily EMA | 33 | 54.5 | -24.77 | 35.66 | 0.66 |
| 2 range/ATR | 38 | 81.6 | 16.21 | 24.52 | 1.28 |
| 3 60m ADX | 46 | 56.5 | -66.08 | 69.94 | 0.5 |
| 4 Globex VWAP | 51 | 60.8 | 1.4 | 36.36 | 1.01 |
| 5 volume | 22 | 45.5 | -19.41 | 44.86 | 0.73 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 70.6 | 45.43 | 1.35 |

Average stop distance 33.6 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | 12.28 | 1.45 |
| Original | 17 | 58.8 | -21.82 | 0.39 |
| London | 17 | 76.5 | 28.31 | 3.79 |
| NY | 17 | 29.4 | -59.12 | 0.37 |

## SP500: SP500-USDC (S&P 500 perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 36.8 | -48.75 | 60.37 | 0.57 |
| 1 daily EMA | 28 | 28.6 | -20.81 | 34.52 | 0.52 |
| 2 range/ATR | 38 | 50.0 | -26.54 | 35.27 | 0.52 |
| 3 60m ADX | 51 | 33.3 | -66.65 | 69.25 | 0.31 |
| 4 Globex VWAP | 46 | 43.5 | -26.66 | 38.3 | 0.69 |
| 5 volume | 26 | 38.5 | -26.07 | 41.65 | 0.58 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 72.1 | 38.88 | 1.57 |

Average stop distance 19.0 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 41.2 | -0.25 | 0.99 |
| Original | 17 | 23.5 | -26.08 | 0.08 |
| London | 17 | 47.1 | -9.48 | 0.59 |
| NY | 17 | 35.3 | -12.95 | 0.7 |

## GOLD: GOLD-USDC (gold perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 7.5 | -387.75 | 388.07 | 0.03 |
| 1 daily EMA | 34 | 2.9 | -197.27 | 197.27 | 0.02 |
| 2 range/ATR | 41 | 4.9 | -212.4 | 212.73 | 0.0 |
| 3 60m ADX | 52 | 9.6 | -307.57 | 307.88 | 0.03 |
| 4 Globex VWAP | 42 | 7.1 | -233.6 | 233.6 | 0.04 |
| 5 volume | 29 | 13.8 | -168.81 | 169.12 | 0.04 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 67 | 64.2 | 24.63 | 1.23 |

Average stop distance 23.9 bps of price (target is half of that). Assumed round-trip cost about 22.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 5.9 | -104.36 | 0.05 |
| Original | 17 | 5.9 | -78.54 | 0.01 |
| London | 17 | 0.0 | -124.38 | 0.0 |
| NY | 16 | 18.8 | -80.47 | 0.06 |

## WTIOIL: WTIOIL-USDC (WTI crude perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 58.8 | -74.04 | 102.68 | 0.72 |
| 1 daily EMA | 41 | 56.1 | -67.45 | 68.88 | 0.62 |
| 2 range/ATR | 45 | 68.9 | -23.36 | 60.91 | 0.88 |
| 3 60m ADX | 45 | 66.7 | -13.94 | 65.03 | 0.92 |
| 4 Globex VWAP | 54 | 59.3 | -74.07 | 83.25 | 0.68 |
| 5 volume | 14 | 57.1 | -17.77 | 46.53 | 0.7 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 60.3 | 17.16 | 1.08 |

Average stop distance 40.8 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -27.53 | 0.56 |
| Original | 17 | 52.9 | -35.89 | 0.48 |
| London | 17 | 70.6 | 32.55 | 1.92 |
| NY | 17 | 52.9 | -43.17 | 0.56 |

## BRENTOIL: BRENTOIL-USDC (Brent crude perp)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 57.4 | -63.3 | 87.42 | 0.75 |
| 1 daily EMA | 45 | 55.6 | -70.74 | 79.8 | 0.63 |
| 2 range/ATR | 44 | 65.9 | -26.81 | 58.79 | 0.86 |
| 3 60m ADX | 42 | 66.7 | -3.71 | 56.79 | 0.98 |
| 4 Globex VWAP | 51 | 58.8 | -62.57 | 71.32 | 0.69 |
| 5 volume | 19 | 63.2 | -8.03 | 30.93 | 0.89 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 60.3 | 27.3 | 1.13 |

Average stop distance 40.0 bps of price (target is half of that). Assumed round-trip cost about 5.8 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -8.65 | 0.82 |
| Original | 17 | 52.9 | -41.99 | 0.42 |
| London | 17 | 70.6 | 10.86 | 1.2 |
| NY | 17 | 47.1 | -23.51 | 0.69 |

## LT_US100: Lighter US100 (Nasdaq-100)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 58.8 | -72.16 | 102.35 | 0.64 |
| 1 daily EMA | 33 | 63.6 | -31.45 | 50.49 | 0.61 |
| 2 range/ATR | 40 | 67.5 | -32.81 | 54.98 | 0.69 |
| 3 60m ADX | 47 | 51.1 | -94.85 | 102.64 | 0.42 |
| 4 Globex VWAP | 48 | 58.3 | -22.67 | 50.97 | 0.83 |
| 5 volume | 24 | 58.3 | -22.34 | 35.26 | 0.68 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 66.2 | 6.36 | 1.04 |

Average stop distance 35.0 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 70.6 | 20.41 | 1.86 |
| Original | 17 | 58.8 | -37.96 | 0.25 |
| London | 17 | 64.7 | 0.89 | 1.03 |
| NY | 17 | 41.2 | -55.5 | 0.39 |

## LT_US500: Lighter US500 (S&P 500)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 67 | 38.8 | -43.41 | 63.16 | 0.62 |
| 1 daily EMA | 31 | 38.7 | -15.43 | 37.73 | 0.66 |
| 2 range/ATR | 31 | 54.8 | -37.22 | 45.55 | 0.44 |
| 3 60m ADX | 52 | 32.7 | -67.79 | 71.45 | 0.34 |
| 4 Globex VWAP | 50 | 44.0 | -15.97 | 39.46 | 0.81 |
| 5 volume | 30 | 33.3 | -17.61 | 28.99 | 0.69 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 67 | 64.2 | 38.47 | 1.6 |

Average stop distance 19.2 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 47.1 | -2.06 | 0.9 |
| Original | 17 | 17.6 | -29.82 | 0.09 |
| London | 16 | 37.5 | -19.88 | 0.37 |
| NY | 17 | 52.9 | 8.36 | 1.27 |

## LT_XAU: Lighter XAU (gold)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 54.4 | -26.88 | 67.11 | 0.81 |
| 1 daily EMA | 42 | 54.8 | -17.97 | 40.37 | 0.79 |
| 2 range/ATR | 44 | 68.2 | -10.12 | 54.23 | 0.88 |
| 3 60m ADX | 53 | 54.7 | -26.85 | 61.86 | 0.78 |
| 4 Globex VWAP | 45 | 53.3 | -2.58 | 46.31 | 0.97 |
| 5 volume | 26 | 53.8 | -5.85 | 26.23 | 0.9 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 67.6 | 54.84 | 1.56 |

Average stop distance 26.5 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 70.6 | 21.63 | 2.59 |
| Original | 17 | 52.9 | -14.7 | 0.59 |
| London | 17 | 41.2 | -29.37 | 0.39 |
| NY | 17 | 52.9 | -4.44 | 0.9 |

## LT_WTI: Lighter WTI (crude)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 61.8 | -85.86 | 106.7 | 0.68 |
| 1 daily EMA | 42 | 57.1 | -69.77 | 72.31 | 0.62 |
| 2 range/ATR | 44 | 68.2 | -27.04 | 58.53 | 0.86 |
| 3 60m ADX | 44 | 65.9 | -17.43 | 62.36 | 0.9 |
| 4 Globex VWAP | 55 | 61.8 | -94.62 | 105.94 | 0.61 |
| 5 volume | 15 | 46.7 | -75.49 | 77.28 | 0.31 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 63.2 | -5.43 | 0.98 |

Average stop distance 40.8 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -26.13 | 0.56 |
| Original | 17 | 58.8 | -19.67 | 0.65 |
| London | 17 | 82.4 | 29.22 | 1.72 |
| NY | 17 | 47.1 | -69.28 | 0.39 |

## LT_BRENT: Lighter BRENTOIL (Brent)

2026-10-24 to 2026-11-10

| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |
|---|---|---|---|---|---|
| 0 none | 68 | 66.2 | -5.49 | 64.06 | 0.97 |
| 1 daily EMA | 41 | 63.4 | -5.3 | 41.13 | 0.96 |
| 2 range/ATR | 44 | 72.7 | 19.92 | 37.7 | 1.13 |
| 3 60m ADX | 46 | 69.6 | 3.03 | 52.59 | 1.02 |
| 4 Globex VWAP | 50 | 70.0 | -4.85 | 38.05 | 0.97 |
| 5 volume | 26 | 73.1 | 27.19 | 27.41 | 1.5 |

Cost check (no filter): same trades with zero fees and zero slippage:

| Trades | Win % | Net $ | Profit factor |
|---|---|---|---|
| 68 | 67.6 | 73.94 | 1.44 |

Average stop distance 39.1 bps of price (target is half of that). Assumed round-trip cost about 6.0 bps.

Per session, no filter:

| Session | Trades | Win % | Net $ | Profit factor |
|---|---|---|---|---|
| Asia | 17 | 58.8 | -20.02 | 0.62 |
| Original | 17 | 64.7 | -14.61 | 0.71 |
| London | 17 | 76.5 | 30.49 | 1.77 |
| NY | 17 | 64.7 | -1.35 | 0.98 |

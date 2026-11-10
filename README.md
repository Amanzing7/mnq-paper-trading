# Multi-market paper trader on GitHub (free, no PC needed)
Same 15-minute range-breakout strategy (0.5R target, stop on the other side of the range).
* Futures (MNQ, MES, MYM, M2K, MCL, MGC via Yahoo): one range a day, 1:00-1:15am New York.
* Hyperliquid perps (XYZ100, SP500, WTIOIL, BRENTOIL): 24/7, so the same rules repeat at several session opens
  (Asia 19:00, Original 01:00, London 03:00, NY 09:30 New York time). Change with the PERP_SESSIONS repo variable,
  format `Name:HHMM-HHMM,...` (range start - close time).
Results: RESULTS.md. Backtest: BACKTEST.md. Edit instruments.py to add or remove markets.

# Data check: do the perp candles line up with the futures?

If the perp's clock is right, the best time shift is 0 and 5-minute returns are highly correlated with the matching futures (over 0.5 on US index pairs). A best shift other than 0 means perp timestamps are off and every session would be wrong.

| Perp | Futures | Overlapping bars | Median price ratio (perp / futures) | Best shift (hours) | Correlation at 0 | Correlation at best | Busiest hours, perp (NY) | Busiest hours, futures (NY) |
|---|---|---|---|---|---|---|---|---|
| XYZ100 | MNQ | 2993 | 0.9955 | 0 | 0.99 | 0.99 | 10:00, 18:00, 09:00 | 10:00, 09:00, 11:00 |
| SP500 | MES | 2992 | 0.9957 | 0 | 0.98 | 0.98 | 10:00, 09:00, 11:00 | 10:00, 09:00, 15:00 |
| WTIOIL | MCL | 3001 | 0.9996 | 0 | 0.97 | 0.97 | 11:00, 08:00, 10:00 | 09:00, 11:00, 08:00 |
| GOLD | MGC | 3003 | 0.9978 | 0 | 0.95 | 0.95 | 09:00, 11:00, 08:00 | 09:00, 10:00, 08:00 |

No timestamp shift detected where data was available.

"""The instruments the paper trader runs, and how each one is sized and costed.
Edit this file to add or remove markets. All use the same strategy rules and the same 1:00-1:15am New York range."""
from __future__ import annotations

import os
from dataclasses import dataclass, replace

import free_paper as fp


@dataclass(frozen=True)
class Instrument:
    symbol: str
    kind: str                     # "future" (Yahoo data) or "perp" (Hyperliquid data)
    label: str = ""
    yahoo: tuple = ()             # Yahoo tickers to try, in order
    hl_coins: tuple = ()          # Hyperliquid coin names to try, in order (HIP-3 'xyz' dex)
    lighter: tuple = ()           # Lighter symbols to try, in order (data comes from Lighter instead of Hyperliquid)
    fee_bps: float = 1.0          # perps: fee per side in bps (guide: HL growth mode 0.9, HL standard 9, Lighter Standard 0)
    slip_bps: float = 2.0         # perps: assumed slippage per side in bps (a guess; measure it live)
    tick: float = 0.25            # futures only
    pv: float = 1.0               # dollars per 1.0 price move per contract (futures only)


INSTRUMENTS = [
    Instrument("MNQ", "future", "Micro Nasdaq-100", yahoo=("MNQ=F",), tick=0.25, pv=2.0),
    Instrument("MES", "future", "Micro S&P 500", yahoo=("MES=F",), tick=0.25, pv=5.0),
    Instrument("MYM", "future", "Micro Dow", yahoo=("MYM=F",), tick=1.0, pv=0.5),
    Instrument("M2K", "future", "Micro Russell 2000", yahoo=("M2K=F",), tick=0.1, pv=5.0),
    Instrument("MCL", "future", "Micro WTI crude", yahoo=("MCL=F", "CL=F"), tick=0.01, pv=100.0),
    Instrument("MGC", "future", "Micro gold", yahoo=("MGC=F", "GC=F"), tick=0.1, pv=10.0),
    Instrument("XYZ100", "perp", "XYZ100-USDC (Nasdaq-100 perp)", hl_coins=("xyz:XYZ100",), fee_bps=0.9),
    Instrument("SP500", "perp", "SP500-USDC (S&P 500 perp)", hl_coins=("xyz:SP500",), fee_bps=0.9),
    Instrument("GOLD", "perp", "GOLD-USDC (gold perp)", hl_coins=("xyz:GOLD", "xyz:XAU"), fee_bps=9.0),
    Instrument("WTIOIL", "perp", "WTIOIL-USDC (WTI crude perp)", hl_coins=("xyz:WTIOIL", "xyz:CL"), fee_bps=0.9),
    Instrument("BRENTOIL", "perp", "BRENTOIL-USDC (Brent crude perp)", hl_coins=("xyz:BRENTOIL",), fee_bps=0.9),
]
# Lighter (lighter.xyz) perps. Standard account: 0 fee, but taker orders wait 300 ms, so slippage is assumed higher (3 bps).
INSTRUMENTS += [
    Instrument("LT_US100", "perp", "Lighter US100 (Nasdaq-100)", lighter=("US100",), fee_bps=0.0, slip_bps=3.0),
    Instrument("LT_US500", "perp", "Lighter US500 (S&P 500)", lighter=("US500",), fee_bps=0.0, slip_bps=3.0),
    Instrument("LT_XAU", "perp", "Lighter XAU (gold)", lighter=("XAU",), fee_bps=0.0, slip_bps=3.0),
    Instrument("LT_WTI", "perp", "Lighter WTI (crude)", lighter=("WTI",), fee_bps=0.0, slip_bps=3.0),
    Instrument("LT_BRENT", "perp", "Lighter BRENTOIL (Brent)", lighter=("BRENTOIL",), fee_bps=0.0, slip_bps=3.0),
]
BY_SYMBOL = {i.symbol: i for i in INSTRUMENTS}


def selected() -> list[Instrument]:
    raw = os.environ.get("INSTRUMENTS", "").replace(" ", "")
    if not raw:
        return list(INSTRUMENTS)
    return [BY_SYMBOL[s.upper()] for s in raw.split(",") if s.upper() in BY_SYMBOL]


def selected_filters() -> list[int]:
    raw = os.environ.get("FILTERS", "0,2").replace(" ", "")
    return [int(x) for x in raw.split(",") if x.isdigit() and 0 <= int(x) <= 5] or [0]


def params_for(inst: Instrument, fmode: int) -> fp.Params:
    env = os.environ.get
    if inst.kind == "perp":
        return fp.Params(fmode=fmode, kind="perp", symbol=inst.symbol, pv=1.0,
                         slip_bps=float(env("PERP_SLIP_BPS") or inst.slip_bps), fee_bps=float(env("PERP_FEE_BPS") or inst.fee_bps),
                         risk_usd=float(env("RISK_USD") or 20.0), max_notional=float(env("MAX_NOTIONAL") or 3000.0))
    return fp.Params(fmode=fmode, kind="future", symbol=inst.symbol, tick=inst.tick, pv=inst.pv, qty=1,
                     max_risk_usd=float(env("MAX_RISK") or 150.0))


# Trading sessions (New York clock). Futures keep the original single 1:00-1:15am range.
# Perps trade 24/7, so they repeat the same rules at several session opens. Format "Name:HHMM-HHMM" where the first time
# is when the 15-minute range starts and the second is when open trades are closed. Sessions are tracked independently.
DEFAULT_PERP_SESSIONS = "Asia:1900-2300,Original:0100-0900,London:0300-0700,NY:0930-1330"


def _hhmm(x: str) -> int:
    return int(x[:2]) * 60 + int(x[2:])


def sessions_for(inst: Instrument) -> list[tuple[str, int, int]]:
    if inst.kind != "perp":
        return [("Original", 60, 9 * 60)]
    raw = (os.environ.get("PERP_SESSIONS") or DEFAULT_PERP_SESSIONS).replace(" ", "")
    out = []
    for part in raw.split(","):
        name, span = part.split(":")
        a, b = span.split("-")
        out.append((name, _hhmm(a), _hhmm(b)))
    return out


def session_params(inst: Instrument, fmode: int) -> list[fp.Params]:
    base = params_for(inst, fmode)
    return [replace(base, session=n, range_start_min=a, cutoff_min=b) for n, a, b in sessions_for(inst)]

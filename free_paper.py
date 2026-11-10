#!/usr/bin/env python3
"""Free backtest + paper trading for the MNQ 1am range breakout. No TradingView, no paid anything.

Data: free Yahoo Finance via the `yfinance` package (symbol MNQ=F, 5-minute bars).
  * Yahoo keeps only ~60 days of 5m history, so backtests are SHORT (about 40 trading days).
  * Futures data on Yahoo can be delayed by 10-15 minutes. Paper results are approximate.

Usage:
  python free_paper.py backtest                 # compares no-filter and filters 1-5
  python free_paper.py live --filter 0          # paper trade today's signal, polling every 60s
Trades are saved to data/paper_trades.csv.
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")


@dataclass
class Params:
    fmode: int = 0               # regime filter 0-5
    rr: float = 0.5              # target in R
    cutoff_min: int = 9 * 60     # flatten / stop looking at 09:00 NY
    qty: int = 1
    slip_ticks: float = 1.0      # per side, applied to market-style fills (entry, stop, time exit)
    comm_side: float = 0.75
    max_risk_usd: float = 150.0  # skip trades whose stop risk is bigger (0 = off)
    futures_hours: bool = True   # perps: skip bars when the underlying futures market is closed (Fri 17:00 ET - Sun 18:00 ET, 17:00-18:00 daily)
    max_stop_bps: float = 0.0    # skip trades whose stop is wider than this many bps of price (0 = off)
    tick: float = 0.25
    pv: float = 2.0              # $ per point, MNQ
    f1_len: int = 50
    f2_min: float = 0.04
    f2_max: float = 0.25
    f3_min: float = 20.0
    f5_mult: float = 1.5
    # instrument kind: "future" = fixed contracts, $ commission; "perp" = risk-based fractional size, bps costs
    range_start_min: int = 60    # the 15-minute range starts here (minutes after midnight New York time); 60 = 01:00
    session: str = ""
    kind: str = "future"
    symbol: str = ""
    slip_bps: float = 2.0        # perp: slippage per side in basis points of price
    fee_bps: float = 1.0         # perp: taker fee per side in basis points of notional
    risk_usd: float = 20.0       # perp: size each trade so a stop-out loses about this much
    max_notional: float = 15000.0 # perp: cap on position value (about 3x a $1,000 account)


# ───────────────────────── data ─────────────────────────
def _clean(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    df.index = pd.to_datetime(df.index)
    df.index = df.index.tz_localize("UTC") if df.index.tz is None else df.index
    df.index = df.index.tz_convert(NY)
    return df


def fetch_5m(period: str = "60d") -> pd.DataFrame:
    import yfinance as yf
    df = _clean(yf.download("MNQ=F", period=period, interval="5m", progress=False, auto_adjust=False))
    # drop the bar that is still forming (bar start + 5 min is in the future)
    now = pd.Timestamp.now(tz=NY)
    return df[df.index + pd.Timedelta(minutes=5) <= now]


def fetch_daily() -> pd.DataFrame:
    import yfinance as yf
    df = yf.download("MNQ=F", period="1y", interval="1d", progress=False, auto_adjust=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close"]].dropna()
    df.index = pd.to_datetime(df.index).tz_localize(None)
    return df


# ───────────────────────── indicators ─────────────────────────
def adx(df: pd.DataFrame, n: int = 14) -> pd.Series:
    up, dn = df["High"].diff(), -df["Low"].diff()
    plus = np.where((up > dn) & (up > 0), up, 0.0)
    minus = np.where((dn > up) & (dn > 0), dn, 0.0)
    pc = df["Close"].shift()
    tr = pd.concat([df["High"] - df["Low"], (df["High"] - pc).abs(), (df["Low"] - pc).abs()], axis=1).max(axis=1)
    a = 1.0 / n
    atr = tr.ewm(alpha=a, adjust=False).mean()
    pdi = 100 * pd.Series(plus, index=df.index).ewm(alpha=a, adjust=False).mean() / atr
    mdi = 100 * pd.Series(minus, index=df.index).ewm(alpha=a, adjust=False).mean() / atr
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi).replace(0, np.nan)
    return dx.ewm(alpha=a, adjust=False).mean()


def prepare(df5: pd.DataFrame) -> pd.DataFrame:
    """Add per-bar features used by the regime filters (all use only completed data)."""
    d = df5.copy()
    # F4: VWAP anchored at 18:00 NY (Globex open)
    sess = (d.index - pd.Timedelta(hours=18)).date
    pv = (d[["High", "Low", "Close"]].mean(axis=1)) * d["Volume"]
    d["vwap"] = pv.groupby(sess).cumsum() / d["Volume"].groupby(sess).cumsum().replace(0, np.nan)
    # F5: average volume of the previous 20 bars
    d["volavg"] = d["Volume"].rolling(20).mean().shift(1)
    # F3: 60m ADX, using only completed 60m bars
    h = d.resample("60min").agg({"High": "max", "Low": "min", "Close": "last"}).dropna()
    h["adx"] = adx(h)
    d["adx60"] = h["adx"].shift(1).reindex(d.index, method="ffill")
    return d


def daily_context(daily: pd.DataFrame, p: Params) -> pd.DataFrame:
    c = pd.DataFrame(index=daily.index)
    c["ema"] = daily["Close"].ewm(span=p.f1_len, adjust=False).mean()
    pc = daily["Close"].shift()
    tr = pd.concat([daily["High"] - daily["Low"], (daily["High"] - pc).abs(), (daily["Low"] - pc).abs()], axis=1).max(axis=1)
    c["atr"] = tr.ewm(alpha=1 / 14, adjust=False).mean()
    return c


def _prev_daily(ctx: pd.DataFrame, day) -> pd.Series | None:
    prior = ctx[ctx.index < pd.Timestamp(day)]
    return prior.iloc[-1] if len(prior) else None


def closed_mask(index) -> np.ndarray:
    """True for bars when index/commodity futures (and so trade.xyz / Lighter external pricing) are closed, New York clock."""
    dow, m = np.asarray(index.dayofweek), np.asarray(index.hour * 60 + index.minute)
    return (dow == 5) | ((dow == 4) & (m >= 1020)) | ((dow == 6) & (m < 1080)) | ((dow <= 3) & (m >= 1020) & (m < 1080))


# ───────────────────────── strategy ─────────────────────────
def simulate_day(bars: pd.DataFrame, day, dctx: pd.DataFrame | None, p: Params) -> dict | None:
    """bars: prepared 5m bars (NY tz) for the calendar day `day`. Returns a trade dict or None.
    status is 'closed' or 'open' (still running because data ends before it resolves)."""
    if p.kind == "perp" and p.futures_hours:
        bars = bars[~closed_mask(bars.index)]
    mins = bars.index.hour * 60 + bars.index.minute
    rs = p.range_start_min
    rng = bars[(mins >= rs) & (mins < rs + 15)]
    if len(rng) < 3:
        return None
    rH, rL = rng["High"].max(), rng["Low"].min()
    post_idx = np.where((mins >= rs + 15) & (mins < p.cutoff_min))[0]

    for k in post_idx:
        b = bars.iloc[k]
        side = "long" if b["Close"] > rH else "short" if b["Close"] < rL else None
        if side is None:
            continue
        # first breakout of the day is the only one considered
        entry_sig = float(b["Close"])
        stop = float(rL if side == "long" else rH)
        risk = abs(entry_sig - stop)
        tgt = entry_sig + p.rr * risk if side == "long" else entry_sig - p.rr * risk
        qty = p.qty
        if p.max_stop_bps and risk / entry_sig * 1e4 > p.max_stop_bps:
            return None
        if p.kind == "perp":
            if risk <= 0:
                return None
            qty = min(p.risk_usd / risk, p.max_notional / entry_sig)
            qty = math.floor(qty * 10000) / 10000
            if qty <= 0:
                return None
        elif p.max_risk_usd and risk * p.pv * qty > p.max_risk_usd:
            return None
        if not _filter_ok(side, b, rH, rL, dctx, day, p):
            return None
        slip = entry_sig * p.slip_bps / 1e4 if p.kind == "perp" else p.slip_ticks * p.tick
        entry = entry_sig + slip if side == "long" else entry_sig - slip
        trade = dict(date=str(day), session=p.session, symbol=p.symbol, qty=qty, side=side, entry_time=str(bars.index[k]), entry=entry, stop=stop,
                     target=tgt, range_high=rH, range_low=rL, status="open", exit=None, reason="", pnl=None,
                     risk=risk * p.pv * qty)
        sign = 1 if side == "long" else -1
        for j in range(k + 1, len(bars)):
            x = bars.iloc[j]
            if mins[j] >= p.cutoff_min:
                break
            hit_stop = x["Low"] <= stop if side == "long" else x["High"] >= stop
            hit_tgt = x["High"] >= tgt if side == "long" else x["Low"] <= tgt
            if hit_stop:      # if both hit in one bar we assume the stop first (conservative)
                trade.update(exit=stop - sign * slip, reason="stop")
                break
            if hit_tgt:
                trade.update(exit=tgt, reason="target")
                break
        else:
            pass
        if trade["exit"] is None:
            after = np.where(mins >= p.cutoff_min)[0]
            if len(after):    # the day is over: flatten at the last bar before cutoff
                last = bars.iloc[[i for i in range(len(bars)) if mins[i] < p.cutoff_min][-1]]
                trade.update(exit=float(last["Close"]) - sign * slip, reason="time")
        if trade["exit"] is not None:
            pts = (trade["exit"] - entry) * sign
            gross = pts * p.pv * qty
            if p.kind == "perp":
                fees = p.fee_bps / 1e4 * (entry + trade["exit"]) * qty
            else:
                fees = 2 * p.comm_side * qty
            trade.update(status="closed", pnl=gross - fees)
        return trade
    return None


def _filter_ok(side, b, rH, rL, dctx, day, p: Params) -> bool:
    f = p.fmode
    if f == 0:
        return True
    if f in (1, 2):
        prev = _prev_daily(dctx, day) if dctx is not None else None
        if prev is None or pd.isna(prev["ema"]):
            return False
        if f == 1:
            return b["Close"] > prev["ema"] if side == "long" else b["Close"] < prev["ema"]
        pct = (rH - rL) / prev["atr"] if prev["atr"] > 0 else np.nan
        return bool(p.f2_min <= pct <= p.f2_max)
    if f == 3:
        return bool(pd.notna(b["adx60"]) and b["adx60"] >= p.f3_min)
    if f == 4:
        if pd.isna(b["vwap"]):
            return False
        return b["Close"] > b["vwap"] if side == "long" else b["Close"] < b["vwap"]
    if f == 5:
        return bool(pd.notna(b["volavg"]) and b["Volume"] >= p.f5_mult * b["volavg"])
    return True


def run_backtest(df_prepared: pd.DataFrame, dctx: pd.DataFrame | None, p: Params) -> list[dict]:
    out = []
    for day, bars in df_prepared.groupby(df_prepared.index.date):
        t = simulate_day(bars, day, dctx, p)
        if t:
            out.append(t)
    return out


def stats(trades: list[dict], capital: float = 1000.0) -> dict:
    closed = [t for t in trades if t["status"] == "closed"]
    pnl = np.array([t["pnl"] for t in closed], dtype=float)
    if not len(pnl):
        return dict(trades=0)
    eq = capital + np.cumsum(pnl)
    peak = np.maximum.accumulate(np.concatenate([[capital], eq]))[1:]
    gp, gl = pnl[pnl > 0].sum(), -pnl[pnl < 0].sum()
    rs_ = [t["pnl"] / t["risk"] for t in closed if t.get("risk")]
    extra = dict(avg_r=round(float(np.mean(rs_)), 3), net_r=round(float(np.sum(rs_)), 2)) if len(rs_) == len(closed) else {}
    return dict(**extra, trades=len(pnl), win_rate=round(100 * (pnl > 0).mean(), 1), net=round(pnl.sum(), 2),
                ret_pct=round(100 * pnl.sum() / capital, 1), max_dd=round(float((peak - eq).max()), 2),
                profit_factor=round(gp / gl, 2) if gl else float("inf"), avg_trade=round(pnl.mean(), 2))


# ───────────────────────── commands ─────────────────────────
def cmd_backtest(args):
    df5, daily = fetch_5m("60d"), fetch_daily()
    print(f"{len(df5)} five-minute bars, {df5.index[0].date()} to {df5.index[-1].date()}")
    prep = prepare(df5)
    names = {0: "none", 1: "daily EMA trend", 2: "range/ATR size", 3: "60m ADX", 4: "Globex VWAP bias", 5: "volume"}
    print(f"{'filter':<18}{'trades':>7}{'win%':>7}{'net$':>9}{'ret%':>7}{'maxDD$':>9}{'PF':>6}")
    for f in range(6):
        p = Params(fmode=f, qty=args.qty, max_risk_usd=args.max_risk)
        s = stats(run_backtest(prep, daily_context(daily, p), p), args.capital)
        if s["trades"] == 0:
            print(f"{f} {names[f]:<16}{'0':>7}")
        else:
            print(f"{f} {names[f]:<16}{s['trades']:>7}{s['win_rate']:>7}{s['net']:>9}{s['ret_pct']:>7}{s['max_dd']:>9}{s['profit_factor']:>6}")
    print("\nWith only ~40 trading days these numbers are noise-level. Treat them as a smoke test, not proof.")


FIELDS = ["date", "session", "symbol", "qty", "side", "entry_time", "entry", "stop", "target", "range_high", "range_low", "status", "exit", "reason", "pnl"]


def save_trade(t: dict, path="data/paper_trades.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rows = []
    if os.path.exists(path):
        rows = [r for r in csv.DictReader(open(path))
                if not (r["date"] == t["date"] and (r.get("session") or "") == (t.get("session") or ""))]
    rows.append({k: t.get(k) for k in FIELDS})
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def cmd_live(args):
    p = Params(fmode=args.filter, qty=args.qty, max_risk_usd=args.max_risk)
    daily = fetch_daily()
    dctx = daily_context(daily, p)
    last_msg = None
    print(f"Paper trading MNQ=F, filter {p.fmode}. Ctrl+C to stop. Data may be ~10-15 min delayed.")
    while True:
        try:
            now = datetime.now(NY)
            df5 = fetch_5m("5d")
            prep = prepare(df5)
            today = now.date()
            bars = prep[prep.index.date == today]
            t = simulate_day(bars, today, dctx, p) if len(bars) else None
            msg = "no trade yet" if t is None else (
                f"{t['side']} @ {t['entry']:.2f} stop {t['stop']:.2f} tgt {t['target']:.2f} "
                f"-> {t['status']}" + (f" {t['reason']} pnl ${t['pnl']:.2f}" if t["status"] == "closed" else ""))
            if t:
                save_trade(t)
            if msg != last_msg:
                print(f"[{now:%H:%M:%S}] {today}: {msg}")
                last_msg = msg
        except Exception as e:  # network hiccups should not kill the loop
            print("warning:", e)
        time.sleep(60)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("backtest", cmd_backtest), ("live", cmd_live)):
        s = sub.add_parser(name)
        s.add_argument("--filter", type=int, default=0, choices=range(6))
        s.add_argument("--qty", type=int, default=1)
        s.add_argument("--max-risk", type=float, default=150.0)
        s.add_argument("--capital", type=float, default=1000.0)
        s.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

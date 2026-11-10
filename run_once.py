#!/usr/bin/env python3
"""Multi-instrument paper trader, meant to run on a schedule on GitHub Actions (free, no PC needed).
  python run_once.py             -> check today's signals for every instrument, update data/*.csv and RESULTS.md
  python run_once.py --backtest  -> write BACKTEST.md (every instrument x every filter, recent history)
Every (instrument, filter) pair is its own fake $1,000 account.
Settings (environment variables / GitHub repo variables): INSTRUMENTS, FILTERS, MAX_RISK, RISK_USD, MAX_NOTIONAL."""
from __future__ import annotations

import csv
import glob
import os
import sys
from dataclasses import replace
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

import free_paper as fp
import datasources as ds
import instruments as inst_mod

CAPITAL = float(os.environ.get("CAPITAL", 1000))
NAMES = {0: "none", 1: "daily EMA", 2: "range/ATR", 3: "60m ADX", 4: "Globex VWAP", 5: "volume"}


def describe(t) -> str:
    if t is None:
        return "no trade yet"
    s = f"{t['side']} {t['entry']:.4g}, stop {t['stop']:.4g}, target {t['target']:.4g}: {t['status']}"
    if t["status"] == "closed":
        s += f" ({t['reason']}) ${t['pnl']:.2f}"
    return s


def write_if_changed(path: str, text: str):
    if os.path.exists(path) and open(path).read() == text:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(text)


def load_accounts(data_dir: str) -> dict:
    """{(symbol, filter): [trade rows]} from the saved CSVs."""
    acc = {}
    for path in glob.glob(os.path.join(data_dir, "*_f*.csv")):
        sym, f = os.path.basename(path)[:-4].rsplit("_f", 1)
        acc[(sym, int(f))] = list(csv.DictReader(open(path)))
    return acc


def results_md(accounts: dict, status: dict, errors: dict) -> str:
    out = ["# Paper trading: 1:00-1:15am New York range breakout (fake money)", "",
           f"Each row is a separate fake ${CAPITAL:,.0f} account. Same rules on every market; 0.5R target, stop on the other side of the range.", "",
           "| Market | Filter | Closed trades | Wins | P/L $ | Balance $ | Today |", "|---|---|---|---|---|---|---|"]
    grand = 0.0
    keys = sorted(set(accounts) | set(status))
    order = {i.symbol: n for n, i in enumerate(inst_mod.INSTRUMENTS)}
    keys.sort(key=lambda k: (order.get(k[0], 99), k[1]))
    for k in keys:
        rows = accounts.get(k, [])
        closed = [r for r in rows if r["status"] == "closed" and r["pnl"] not in ("", None)]
        pnl = sum(float(r["pnl"]) for r in closed)
        grand += pnl
        wins = sum(1 for r in closed if float(r["pnl"]) > 0)
        out.append(f"| {k[0]} | {k[1]} {NAMES.get(k[1], '')} | {len(closed)} | {wins} | {pnl:,.2f} | {CAPITAL + pnl:,.2f} | {status.get(k, '')} |")
    out += ["", f"**Total P/L across all accounts: ${grand:,.2f}**", ""]
    if errors:
        out += ["## Data problems", ""] + [f"- **{s}**: {e}" for s, e in sorted(errors.items())] + [""]
    recent = sorted(((r["date"], k, r) for k, rows in accounts.items() for r in rows), key=lambda x: x[0], reverse=True)[:60]
    if recent:
        out += ["## Recent trades", "", "| Date | Market | Filter | Session | Side | Size | Entry | Stop | Target | Exit | Result | P/L $ |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for d, k, r in recent:
            ex = f"{float(r['exit']):.4g}" if r["exit"] not in ("", None) else "open"
            pl = f"{float(r['pnl']):.2f}" if r["pnl"] not in ("", None) else ""
            out.append(f"| {d} | {k[0]} | {k[1]} | {r.get('session') or ''} | {r['side']} | {r.get('qty') or ''} | {float(r['entry']):.4g} | {float(r['stop']):.4g} | {float(r['target']):.4g} | {ex} | {r['reason'] or r['status']} | {pl} |")
    out += ["", "_Free data can be late and fills are idealised, so treat this as a rough test. Not financial advice._", ""]
    return "\n".join(out)


def run_live(today=None, data_dir="data", root=".", bars_fn=None, daily_fn=None):
    bars_fn = bars_fn or (lambda i: ds.fetch_bars(i, 5))
    daily_fn = daily_fn or ds.fetch_daily
    today = today or datetime.now(fp.NY).date()
    status, errors = {}, {}
    filters = inst_mod.selected_filters()
    for inst in inst_mod.selected():
        try:
            prep = fp.prepare(bars_fn(inst))
        except Exception as e:
            errors[inst.symbol] = f"price data failed: {e}"
            continue
        try:
            daily = daily_fn(inst)
        except Exception as e:
            daily = None
            errors[inst.symbol] = f"daily data failed (filters 1 and 2 skipped): {e}"
        for f in filters:
            dctx = None
            notes = []
            for p in inst_mod.session_params(inst, f):
                dctx = fp.daily_context(daily, p) if daily is not None else None
                for day in (today - timedelta(days=1), today):   # yesterday too, so late sessions are settled
                    bars = prep[prep.index.date == day]
                    t = fp.simulate_day(bars, day, dctx, p) if len(bars) else None
                    if t:
                        fp.save_trade(t, os.path.join(data_dir, f"{inst.symbol}_f{f}.csv"))
                        if day == today:
                            notes.append(f"{p.session}: {describe(t)}")
            status[(inst.symbol, f)] = "; ".join(notes) if notes else "no trade yet"
    md = results_md(load_accounts(data_dir), status, errors)
    write_if_changed(os.path.join(root, "RESULTS.md"), md)
    print(md)


def run_backtest(root=".", bars_fn=None, daily_fn=None):
    bars_fn = bars_fn or (lambda i: ds.fetch_bars(i, 60 if i.kind == "future" else 17))
    daily_fn = daily_fn or ds.fetch_daily
    lines = ["# Backtest on recent history", "",
             f"Each filter row is its own ${CAPITAL:,.0f} account. Futures use ~60 days of Yahoo data; Hyperliquid perps only have ~17 days of 5-minute history. "
             "These samples are tiny: a smoke test, not proof.", ""]
    for inst in inst_mod.selected():
        lines += [f"## {inst.symbol}: {inst.label}", ""]
        try:
            df5 = bars_fn(inst)
            prep = fp.prepare(df5)
        except Exception as e:
            lines += [f"Data failed: {e}", ""]
            continue
        daily_err = None
        try:
            daily = daily_fn(inst)
        except Exception as e:
            daily, daily_err = None, e
        lines += [f"{df5.index[0].date()} to {df5.index[-1].date()}", ""]
        if daily_err:
            lines += [f"**Daily data failed, so filters 1 and 2 could not run:** {daily_err}", ""]
        lines += [
                  "| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |", "|---|---|---|---|---|---|"]
        for f in range(6):
            trades = []
            for p in inst_mod.session_params(inst, f):
                dctx = fp.daily_context(daily, p) if daily is not None else None
                trades += fp.run_backtest(prep, dctx, p)
            s = fp.stats(trades, CAPITAL)
            lines.append(f"| {f} {NAMES[f]} | {s['trades']} | {s.get('win_rate', '')} | {s.get('net', '')} | {s.get('max_dd', '')} | {s.get('profit_factor', '')} |")
        lines.append("")
        if inst.kind == "perp":   # are costs eating the edge? same trades with zero fees and slippage
            free = []
            for p in inst_mod.session_params(inst, 0):
                free += fp.run_backtest(prep, None, replace(p, slip_bps=0.0, fee_bps=0.0))
            sf = fp.stats(free, CAPITAL)
            base_tr = []
            for p in inst_mod.session_params(inst, 0):
                base_tr += fp.run_backtest(prep, None, p)
            dist = [abs(t["entry"] - t["stop"]) / t["entry"] * 1e4 for t in base_tr] or [float("nan")]
            p0 = inst_mod.params_for(inst, 0)
            lines += ["Cost check (no filter): same trades with zero fees and zero slippage:", "",
                      "| Trades | Win % | Net $ | Profit factor |", "|---|---|---|---|",
                      f"| {sf['trades']} | {sf.get('win_rate', '')} | {sf.get('net', '')} | {sf.get('profit_factor', '')} |", "",
                      f"Average stop distance {np.nanmean(dist):.1f} bps of price (target is half of that). "
                      f"Assumed round-trip cost about {2 * (p0.slip_bps + p0.fee_bps):.1f} bps.", ""]
        # Stop-width cap test (no filter): does skipping wide-stop days explain the futures results?
        caps = [("$150 cap (as now)", 150.0), ("no cap", 0.0)] if inst.kind == "future" else \
               [("no cap", 0.0), ("40 bps", 40.0), ("30 bps", 30.0), ("25 bps", 25.0), ("20 bps", 20.0)]
        lines += ["Stop-width cap test (no filter):", "", "| Cap | Trades | Win % | Net $ | Profit factor |", "|---|---|---|---|---|"]
        for label, cap in caps:
            tr = []
            for p in inst_mod.session_params(inst, 0):
                q = replace(p, max_risk_usd=cap) if inst.kind == "future" else replace(p, max_stop_bps=cap)
                tr += fp.run_backtest(prep, None, q)
            s_ = fp.stats(tr, CAPITAL)
            lines.append(f"| {label} | {s_['trades']} | {s_.get('win_rate', '')} | {s_.get('net', '')} | {s_.get('profit_factor', '')} |")
        lines.append("")
        if inst.kind == "perp":   # which session works best (no filter)?
            lines += ["Per session, no filter:", "", "| Session | Trades | Win % | Net $ | Profit factor |", "|---|---|---|---|---|"]
            for p in inst_mod.session_params(inst, 0):
                s = fp.stats(fp.run_backtest(prep, None, p), CAPITAL)
                lines.append(f"| {p.session} | {s['trades']} | {s.get('win_rate', '')} | {s.get('net', '')} | {s.get('profit_factor', '')} |")
            lines.append("")
    write_if_changed(os.path.join(root, "BACKTEST.md"), "\n".join(lines))
    print("\n".join(lines))


# ───────────── data check: are the Hyperliquid candles sane? ─────────────
CHECK_PAIRS = [("XYZ100", "MNQ"), ("SP500", "MES"), ("WTIOIL", "MCL"), ("GOLD", "MGC")]


def _best_shift(perp: pd.DataFrame, fut: pd.DataFrame) -> dict:
    """Correlation of 5-minute returns when the perp's timestamps are shifted by k hours (0 = clocks agree)."""
    rf = fut["Close"].pct_change().rename("f")
    out = {}
    for k in range(-3, 4):
        rp = perp["Close"].pct_change().rename("p")
        rp.index = rp.index + pd.Timedelta(hours=k)
        j = pd.concat([rp, rf], axis=1, join="inner").replace([np.inf, -np.inf], np.nan).dropna()
        out[k] = float(j["p"].corr(j["f"])) if len(j) > 50 else float("nan")
    return out


def _top_hours(df: pd.DataFrame, n=3) -> str:
    v = df["Volume"].groupby(df.index.hour).mean().sort_values(ascending=False).head(n)
    return ", ".join(f"{h:02d}:00" for h in v.index)


def run_check(root=".", bars_fn=None):
    bars_fn = bars_fn or (lambda i: ds.fetch_bars(i, 15))
    lines = ["# Data check: do the perp candles line up with the futures?", "",
             "If the perp's clock is right, the best time shift is 0 and 5-minute returns are highly correlated with the matching futures "
             "(over 0.5 on US index pairs). A best shift other than 0 means perp timestamps are off and every session would be wrong.", "",
             "| Perp | Futures | Overlapping bars | Median price ratio (perp / futures) | Best shift (hours) | Correlation at 0 | Correlation at best | Busiest hours, perp (NY) | Busiest hours, futures (NY) |",
             "|---|---|---|---|---|---|---|---|---|"]
    notes = []
    for ps, fs in CHECK_PAIRS:
        try:
            pb, fb = bars_fn(inst_mod.BY_SYMBOL[ps]), bars_fn(inst_mod.BY_SYMBOL[fs])
            both = pd.concat([pb["Close"].rename("p"), fb["Close"].rename("f")], axis=1, join="inner").dropna()
            ratio = float((both["p"] / both["f"]).median()) if len(both) else float("nan")
            sh = _best_shift(pb, fb)
            best = max((k for k in sh if not np.isnan(sh[k])), key=lambda k: sh[k], default=None)
            lines.append(f"| {ps} | {fs} | {len(both)} | {ratio:.4f} | {best} | {sh.get(0, float('nan')):.2f} | "
                         f"{(sh[best] if best is not None else float('nan')):.2f} | {_top_hours(pb)} | {_top_hours(fb)} |")
            if best not in (None, 0):
                notes.append(f"- **{ps}**: timestamps look shifted by {best} hour(s). Tell Claude and it will be corrected.")
        except Exception as e:
            lines.append(f"| {ps} | {fs} | failed: {e} | | | | | | |")
    lines += [""] + (notes or ["No timestamp shift detected where data was available."]) + [""]
    write_if_changed(os.path.join(root, "DATACHECK.md"), "\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    if "--check" in sys.argv:
        run_check()
    elif "--backtest" in sys.argv:
        run_backtest()
    else:
        run_live()

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
from datetime import datetime, timedelta

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
        try:
            daily = daily_fn(inst)
        except Exception:
            daily = None
        lines += [f"{df5.index[0].date()} to {df5.index[-1].date()}", "",
                  "| Filter | Trades | Win % | Net $ | Max drawdown $ | Profit factor |", "|---|---|---|---|---|---|"]
        for f in range(6):
            trades = []
            for p in inst_mod.session_params(inst, f):
                dctx = fp.daily_context(daily, p) if daily is not None else None
                trades += fp.run_backtest(prep, dctx, p)
            s = fp.stats(trades, CAPITAL)
            lines.append(f"| {f} {NAMES[f]} | {s['trades']} | {s.get('win_rate', '')} | {s.get('net', '')} | {s.get('max_dd', '')} | {s.get('profit_factor', '')} |")
        lines.append("")
        if inst.kind == "perp":   # which session works best (no filter)?
            lines += ["Per session, no filter:", "", "| Session | Trades | Win % | Net $ | Profit factor |", "|---|---|---|---|---|"]
            for p in inst_mod.session_params(inst, 0):
                s = fp.stats(fp.run_backtest(prep, None, p), CAPITAL)
                lines.append(f"| {p.session} | {s['trades']} | {s.get('win_rate', '')} | {s.get('net', '')} | {s.get('profit_factor', '')} |")
            lines.append("")
    write_if_changed(os.path.join(root, "BACKTEST.md"), "\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    run_backtest() if "--backtest" in sys.argv else run_live()

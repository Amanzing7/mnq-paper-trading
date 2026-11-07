#!/usr/bin/env python3
"""One paper-trading check, meant to be run on a schedule by GitHub Actions (free, no PC needed).
  python run_once.py             -> check today's signal, update data/paper_trades.csv and RESULTS.md
  python run_once.py --backtest  -> write BACKTEST.md comparing all filters (last ~60 days)
Settings come from environment variables: FILTER (0-5), QTY, MAX_RISK, CAPITAL."""
from __future__ import annotations

import csv
import os
import sys
from datetime import datetime

import free_paper as fp

CAPITAL = float(os.environ.get("CAPITAL", 1000))
NAMES = {0: "No filter (baseline)", 1: "1 Daily EMA trend", 2: "2 Range size vs daily ATR",
         3: "3 60m ADX trend strength", 4: "4 Globex VWAP bias", 5: "5 Breakout volume"}


def params() -> fp.Params:
    return fp.Params(fmode=int(os.environ.get("FILTER", 0) or 0), qty=int(os.environ.get("QTY", 1) or 1),
                     max_risk_usd=float(os.environ.get("MAX_RISK", 150) or 150))


def describe(t) -> str:
    if t is None:
        return "No trade today (no breakout yet, or the filter blocked it)."
    s = (f"{t['side'].upper()} entered at {t['entry']:.2f}, stop {t['stop']:.2f}, target {t['target']:.2f}: "
         f"{t['status']}")
    if t["status"] == "closed":
        s += f" ({t['reason']}), P/L ${t['pnl']:.2f}"
    return s


def write_if_changed(path: str, text: str):
    if os.path.exists(path) and open(path).read() == text:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(text)


def results_md(rows: list[dict], status: str, p: fp.Params) -> str:
    closed = [r for r in rows if r["status"] == "closed" and r["pnl"] not in ("", None)]
    total = sum(float(r["pnl"]) for r in closed)
    wins = sum(1 for r in closed if float(r["pnl"]) > 0)
    out = ["# MNQ 1am Range Breakout: paper trading (fake money)", "",
           f"**Balance: ${CAPITAL + total:,.2f}**  (started ${CAPITAL:,.0f}, total P/L ${total:,.2f})  ",
           f"Closed trades: {len(closed)}, winners: {wins}  ",
           f"Filter: {NAMES[p.fmode]}, contracts: {p.qty}", "",
           f"**Latest status:** {status}", "",
           "| Date | Side | Entry | Stop | Target | Exit | Result | P/L $ |", "|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["date"], reverse=True):
        ex = f"{float(r['exit']):.2f}" if r["exit"] not in ("", None) else "open"
        pl = f"{float(r['pnl']):.2f}" if r["pnl"] not in ("", None) else ""
        out.append(f"| {r['date']} | {r['side']} | {float(r['entry']):.2f} | {float(r['stop']):.2f} | "
                   f"{float(r['target']):.2f} | {ex} | {r['reason'] or r['status']} | {pl} |")
    out += ["", "_Free Yahoo data can be 10-15 minutes late, fills are idealised. Not financial advice._", ""]
    return "\n".join(out)


def run_live(today=None, data_dir="data", root="."):
    p = params()
    today = today or datetime.now(fp.NY).date()
    dctx = fp.daily_context(fp.fetch_daily(), p)
    prep = fp.prepare(fp.fetch_5m("5d"))
    bars = prep[prep.index.date == today]
    t = fp.simulate_day(bars, today, dctx, p) if len(bars) else None
    path = os.path.join(data_dir, "paper_trades.csv")
    if t:
        fp.save_trade(t, path)
    rows = list(csv.DictReader(open(path))) if os.path.exists(path) else []
    write_if_changed(os.path.join(root, "RESULTS.md"), results_md(rows, describe(t), p))
    print(describe(t))


def run_backtest(root="."):
    p0 = params()
    df5, daily = fp.fetch_5m("60d"), fp.fetch_daily()
    prep = fp.prepare(df5)
    lines = ["# Backtest on recent history (about 60 days of free 5-minute data)", "",
             f"Data: {df5.index[0].date()} to {df5.index[-1].date()}, ${CAPITAL:,.0f} account, {p0.qty} contract(s).", "",
             "| Filter | Trades | Win % | Net $ | Return % | Max drawdown $ | Profit factor |", "|---|---|---|---|---|---|---|"]
    for f in range(6):
        p = fp.Params(fmode=f, qty=p0.qty, max_risk_usd=p0.max_risk_usd)
        s = fp.stats(fp.run_backtest(prep, fp.daily_context(daily, p), p), CAPITAL)
        if s["trades"]:
            lines.append(f"| {NAMES[f]} | {s['trades']} | {s['win_rate']} | {s['net']} | {s['ret_pct']} | {s['max_dd']} | {s['profit_factor']} |")
        else:
            lines.append(f"| {NAMES[f]} | 0 | | | | | |")
    lines += ["", "With only ~40 trading days this is a smoke test, not proof.", ""]
    write_if_changed(os.path.join(root, "BACKTEST.md"), "\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    run_backtest() if "--backtest" in sys.argv else run_live()

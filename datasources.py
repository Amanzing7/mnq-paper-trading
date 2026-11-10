"""Free market data: Yahoo Finance (futures) and the public Hyperliquid info API (perps). No keys needed."""
from __future__ import annotations

import time

import pandas as pd
import requests

import free_paper as fp
from instruments import Instrument

HL_URL = "https://api.hyperliquid.xyz/info"
HL_DEX = "xyz"
FIVE_MIN_MS = 5 * 60 * 1000


# ───────────── Yahoo (futures) ─────────────
def _yahoo_5m(tickers, period):
    import yfinance as yf
    last = None
    for tk in tickers:
        try:
            df = fp._clean(yf.download(tk, period=period, interval="5m", progress=False, auto_adjust=False))
            if len(df):
                return df
        except Exception as e:  # try the next ticker
            last = e
    raise RuntimeError(f"no Yahoo 5m data for {tickers}" + (f": {last}" if last else ""))


def _yahoo_daily(tickers):
    import yfinance as yf
    for tk in tickers:
        df = yf.download(tk, period="1y", interval="1d", progress=False, auto_adjust=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df[["Open", "High", "Low", "Close"]].dropna()
        if len(df):
            df.index = pd.to_datetime(df.index).tz_localize(None)
            return df
    raise RuntimeError(f"no Yahoo daily data for {tickers}")


# ───────────── Hyperliquid (perps) ─────────────
def _hl_post(payload: dict):
    r = requests.post(HL_URL, json=payload, timeout=25)
    r.raise_for_status()
    return r.json()


def hl_resolve(coins) -> str:
    """Pick the first candidate coin name that exists on the xyz dex (names can differ, e.g. CL vs WTIOIL)."""
    meta = _hl_post({"type": "meta", "dex": HL_DEX})
    names = [u["name"] for u in meta["universe"]]
    for c in coins:
        if c in names:
            return c
    short = {n.split(":")[-1].upper(): n for n in names}
    for c in coins:
        if c.split(":")[-1].upper() in short:
            return short[c.split(":")[-1].upper()]
    raise LookupError(f"none of {list(coins)} found on Hyperliquid dex '{HL_DEX}'. Available: {names[:60]}")


def _hl_candles(coin: str, interval: str, start_ms: int, end_ms: int) -> pd.DataFrame:
    rows, cur = [], start_ms
    while True:  # page forward: the API returns at most 5000 candles per call
        chunk = _hl_post({"type": "candleSnapshot", "req": {"coin": coin, "interval": interval,
                                                            "startTime": cur, "endTime": end_ms}})
        if not chunk:
            break
        rows += chunk
        if len(chunk) < 5000:
            break
        cur = int(chunk[-1]["t"]) + 1
    if not rows:
        raise RuntimeError(f"Hyperliquid returned no {interval} candles for {coin}")
    df = pd.DataFrame(rows).drop_duplicates("t")
    df.index = pd.to_datetime(df["t"].astype("int64"), unit="ms", utc=True)
    df = df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"})
    return df[["Open", "High", "Low", "Close", "Volume"]].astype(float).sort_index()


# ───────────── public API ─────────────
def fetch_bars(inst: Instrument, days: int = 5) -> pd.DataFrame:
    """Completed 5-minute bars, New York time. Hyperliquid keeps only ~17 days of 5m history."""
    now = pd.Timestamp.now(tz=fp.NY)
    if inst.kind == "future":
        df = _yahoo_5m(inst.yahoo, f"{max(days, 1)}d")
    else:
        coin = hl_resolve(inst.hl_coins)
        end = int(time.time() * 1000)
        df = _hl_candles(coin, "5m", end - days * 86_400_000, end)
        df.index = df.index.tz_convert(fp.NY)
    return df[df.index + pd.Timedelta(minutes=5) <= now]


def fetch_daily(inst: Instrument) -> pd.DataFrame:
    if inst.kind == "future":
        return _yahoo_daily(inst.yahoo)
    coin = hl_resolve(inst.hl_coins)
    end = int(time.time() * 1000)
    df = _hl_candles(coin, "1d", end - 400 * 86_400_000, end)
    df.index = df.index.tz_convert("UTC").tz_localize(None).normalize()
    return df[["Open", "High", "Low", "Close"]]

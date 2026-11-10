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


# ───────────── Lighter (perps) ─────────────
LT_URL = "https://mainnet.zklighter.elliot.ai"
_LT_IDS: dict = {}


def _lt_get(path: str, **params):
    r = requests.get(LT_URL + path, params=params, timeout=25)
    r.raise_for_status()
    return r.json()


def _walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from _walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from _walk(v)


def lt_resolve(symbols) -> int:
    """Market id for the first Lighter symbol that exists (response shape not verified, so parse it loosely)."""
    if not _LT_IDS:
        for d in _walk(_lt_get("/api/v1/orderBooks")):
            if "symbol" in d and "market_id" in d:
                _LT_IDS[str(d["symbol"]).upper()] = int(d["market_id"])
    for s in symbols:
        if s.upper() in _LT_IDS:
            return _LT_IDS[s.upper()]
    raise LookupError(f"none of {list(symbols)} found on Lighter. Available: {sorted(_LT_IDS)[:80]}")


def _lt_candles(market_id: int, resolution: str, start_ms: int, end_ms: int) -> pd.DataFrame:
    step = {"5m": 300_000, "1d": 86_400_000}[resolution]
    rows, cur = [], start_ms
    while cur < end_ms:  # at most 500 candles per call, so walk forward in windows
        stop = min(end_ms, cur + 499 * step)
        js = _lt_get("/api/v1/candles", market_id=market_id, resolution=resolution,
                     start_timestamp=cur, end_timestamp=stop, count_back=500)
        rows += js.get("c") or []
        cur = stop + step
    if not rows:
        raise RuntimeError(f"Lighter returned no {resolution} candles for market {market_id}")
    df = pd.DataFrame(rows).drop_duplicates("t")
    df.index = pd.to_datetime(df["t"].astype("int64"), unit="ms", utc=True)
    if "v" not in df:
        df["v"] = 0.0
    df = df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"})
    return df[["Open", "High", "Low", "Close", "Volume"]].fillna(0).astype(float).sort_index()


# ───────────── public API ─────────────
def fetch_bars(inst: Instrument, days: int = 5) -> pd.DataFrame:
    """Completed 5-minute bars, New York time. Hyperliquid keeps only ~17 days of 5m history."""
    now = pd.Timestamp.now(tz=fp.NY)
    if inst.kind == "future":
        df = _yahoo_5m(inst.yahoo, f"{max(days, 1)}d")
    elif inst.lighter:
        end = int(time.time() * 1000)
        df = _lt_candles(lt_resolve(inst.lighter), "5m", end - days * 86_400_000, end)
        df.index = df.index.tz_convert(fp.NY)
    else:
        coin = hl_resolve(inst.hl_coins)
        end = int(time.time() * 1000)
        df = _hl_candles(coin, "5m", end - days * 86_400_000, end)
        df.index = df.index.tz_convert(fp.NY)
    return df[df.index + pd.Timedelta(minutes=5) <= now]


def fetch_daily(inst: Instrument) -> pd.DataFrame:
    if inst.kind == "future":
        return _yahoo_daily(inst.yahoo)
    end = int(time.time() * 1000)
    if inst.lighter:
        df = _lt_candles(lt_resolve(inst.lighter), "1d", end - 400 * 86_400_000, end)
    else:
        df = _hl_candles(hl_resolve(inst.hl_coins), "1d", end - 400 * 86_400_000, end)
    df.index = df.index.tz_convert("UTC").tz_localize(None).normalize()
    return df[["Open", "High", "Low", "Close"]]

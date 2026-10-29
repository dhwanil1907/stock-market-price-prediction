"""Download and cache daily price bars for a single stock (MSFT).

Responsibility: return one clean DataFrame of daily bars and nothing else.
No feature logic here.
"""
from pathlib import Path

import pandas as pd

# Why MSFT: liquid, full history, calmer than NVDA/TSLA, and different from the AAPL used in
# the KPI Anomaly Detection project. It is a hindsight pick and a known winner, so buy-and-hold
# looks strong. State this survivorship bias in the README.
TICKER = "MSFT"
START = "2010-01-01"  # ~4,000 trading days. One series means every extra year helps.
DATA_DIR = Path("data")


def fetch_prices(ticker: str = TICKER, start: str = START) -> pd.DataFrame:
    """Return daily OHLCV indexed by date, with columns: open, high, low, close, volume.

    Steps:
    1. If data/msft.parquet exists, read it and return it (the cache makes reruns offline).
    2. Otherwise download with yfinance. Use adjusted prices (splits and dividends) and say so
       in a comment, because unadjusted closes create fake -50% days.
    3. yfinance may return MultiIndex columns even for one ticker. Flatten them.
    4. Sort by date and drop duplicate dates.
    5. Check for missing days, NaNs, and zero volume. Decide what to do (drop or ffill)
       and write the decision down in a comment.
    6. Write to parquet and return.
    """
    raise NotImplementedError

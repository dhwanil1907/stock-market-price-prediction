"""Feature engineering for one stock.

The one rule: a feature on row t may only use information available at the close of day t.
The target is about day t+1. Any `shift(-n)` belongs to the target and nowhere else.
"""
import pandas as pd

# With ~4,000 rows and a target that is mostly noise, keep the feature set SMALL
# (roughly 8 to 12 features). More features means more overfitting.
# Feature ideas:
# - lagged returns: 1, 2, 5, 10, 21 days
# - rolling volatility of returns: 5, 21, 63 days
# - RSI(14)
# - volume z-score vs a trailing 21-day window
# - distance from the 50-day and 200-day moving average
# - optional: SPY return as a market regime feature. It's a second download, so skip it
#   unless time allows, and note that it's shared across days.


def build_features(prices: pd.DataFrame) -> pd.DataFrame:
    """Return one row per date with features plus `target` and `next_return` columns.

    Steps:
    1. Compute daily returns from the adjusted close.
    2. Build each feature from rolling or shifted data (past only).
    3. Define `target` = 1 if the next day's return is > 0, else 0.
       The last row has no next day, so it must be dropped.
    4. Drop warm-up rows where the longest window (200 days) has not filled yet.
    5. Keep a `next_return` column for the backtest (strategy returns need the actual size,
       not just the direction). Keep it out of the model inputs and note why in a comment.
    6. Return a frame indexed by date.

    Test to write first (tests/test_features.py): perturb prices after day t and assert
    features on rows <= t are identical.
    """
    raise NotImplementedError

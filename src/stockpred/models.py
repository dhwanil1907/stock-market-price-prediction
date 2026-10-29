"""Model definitions behind one interface.

Every model, including the baselines and the LSTM, exposes fit() and predict_proba(), so
backtest.py can treat them the same. That makes the comparison fair.
"""
from typing import Protocol

import pandas as pd


class DirectionModel(Protocol):
    def fit(self, features: pd.DataFrame, target: pd.Series) -> "DirectionModel": ...

    def predict_proba(self, features: pd.DataFrame) -> pd.Series:
        """Return P(next-day return > 0) per row, aligned to the input index."""
        ...


# Baselines (a model has to beat these to count):
# - AlwaysUp: predicts the training-set up-fraction every time. MSFT rises on ~53% of days,
#   so the "accuracy" of an always-up model is already above 50%.
# - PrevDay: predicts the same direction as the prior day's return.
# - Buy-and-hold is a strategy, not a model, so it lives in backtest.py.
#
# Models (small data, so keep them simple and regularised):
# - Logistic regression: wrap with a scaler in a sklearn Pipeline so the scaler is fit
#   on the training window only.
# - XGBoost: keep it shallow with strong regularisation (max_depth 2 or 3, small learning
#   rate, few trees, early stopping on a validation slice taken from the END of the
#   training window).
# - LSTM (Day 2): input is a window of the last N days of features. Roughly 4,000 rows is
#   thin for a neural net, so expect it to be unstable. Seed everything, keep it tiny, and
#   report it honestly even if it loses.


def get_models() -> dict[str, DirectionModel]:
    """Return {name: model} for every model evaluated under the same protocol.

    Return fresh, unfitted instances on each call. A model reused across folds would leak.
    """
    raise NotImplementedError

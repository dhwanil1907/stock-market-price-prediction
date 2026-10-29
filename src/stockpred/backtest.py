"""Expanding-window walk-forward backtest with transaction costs, for one stock.

Writes outputs/metrics.csv. That file is the only source for numbers on the resume.
"""
import pandas as pd

COST_BPS = 5  # cost per position change, in basis points. Mention it in the README.


def walk_forward(features: pd.DataFrame, n_splits: int = 8) -> pd.DataFrame:
    """Return one row per (model, fold) with metrics, plus aggregate rows.

    Steps:
    1. Split by DATE. Hold out an initial training period of about 3 years, then divide the
       rest into n_splits consecutive test blocks (~6 months each). Fold k trains on all
       dates before its test block. The training window expands, and every test block is
       strictly after its training data.
    2. Leave a gap of a few days between train and test so overlapping windows don't leak.
    3. For each model from models.get_models(): fit on the train block, predict_proba on
       the test block.
    4. Direction metrics: AUC and accuracy on each test block. Compare against the baselines.
       A single fold has ~125 rows, so per-fold AUC is very noisy. Judge on the pooled
       out-of-sample predictions and report fold spread, not just one number.
    5. Strategy: go long when proba > 0.5, otherwise stay flat. Daily return = position *
       next_return - cost on every position change (COST_BPS / 10_000).
    6. Report net Sharpe (annualised with sqrt(252)) and max drawdown of the equity curve.
    7. Add a buy-and-hold row under the same cost model.
    8. Stitch the out-of-sample predictions from all folds into one series so there is a
       single equity curve per model for the dashboard.
    9. Consider a bootstrap confidence interval on the pooled AUC and Sharpe. With one
       stock, "better than baseline" claims need an error bar.

    Watch for: a position decided on day t is earned on day t+1. That is already in the
    `next_return` column, so do not shift it a second time.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # 1. fetch_prices -> build_features -> walk_forward
    # 2. write the metrics to outputs/metrics.csv
    # 3. fit the best model on all data and save it to outputs/model.joblib for the API
    # 4. print a short summary table
    raise NotImplementedError

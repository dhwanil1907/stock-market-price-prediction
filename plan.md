# Plan

Deadline: Friday, Oct 30, 2026. Resume-ready after Day 1; Day 2 is add-ons.
Stock: MSFT only, daily bars from 2010.
Rule: every resume figure comes from `outputs/metrics.csv`. Nothing is claimed that the output does not show.

## Day 1 (Wed night / Thu): core (A)
- [ ] Notebook `01_eda_baselines.ipynb`: data, features, leakage check, baselines, prototype walk-forward
- [ ] `data.py`: fetch MSFT from 2010, cache to parquet
- [ ] `features.py`: lagged returns, rolling volatility, RSI, volume z-score, next-day target (8 to 12 features)
- [ ] `models.py`: always-up, previous-day, logistic regression, XGBoost
- [ ] `backtest.py`: expanding-window walk-forward, 5 bps costs, long/flat strategy, buy-and-hold, writes `outputs/metrics.csv`
- [ ] `api.py`: `GET /predict` backed by a saved model
- [ ] ~12 pytest tests (leakage, split ordering, costs, API) and green CI
- [ ] README results table filled from `metrics.csv`

## Day 2 (Fri): add-ons (B, C)
- [ ] B: small LSTM under the same walk-forward protocol (cut first if it runs long)
- [ ] C: Streamlit dashboard (model comparison, equity curves, fold AUC, SHAP)
- [ ] Bootstrap confidence intervals on pooled AUC and Sharpe
- [ ] Final README pass, resume bullets drafted from verified metrics only

## Cut order if time runs short
LSTM, then SHAP in the dashboard, then the dashboard. Never cut tests, CI, or the cost-adjusted backtest.

## Done means
- `pytest` and CI green
- `metrics.csv` reproduces from one command
- README numbers match `metrics.csv`
- Repo public

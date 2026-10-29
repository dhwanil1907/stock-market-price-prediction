# Architecture

Single stock: MSFT, daily adjusted bars from 2010 (~4,000 rows).

## Data flow
yfinance -> `data.py` (parquet cache) -> `features.py` -> `backtest.py` (walk-forward over `models.py`)
-> `outputs/metrics.csv` + saved model -> `api.py` and `app.py`

## Modules
| Module | Purpose | Depends on |
|---|---|---|
| `data.py` | Fetch and cache MSFT daily OHLCV | yfinance |
| `features.py` | Build features and the next-day direction target | data |
| `models.py` | Baselines, logistic regression, XGBoost, LSTM behind one interface | features |
| `backtest.py` | Expanding-window walk-forward, costs, metrics | features, models |
| `api.py` | FastAPI `/health`, `/predict` | saved model |
| `app.py` | Streamlit dashboard | `outputs/` |

## Leakage controls
- Every feature at row t uses data up to the close of day t only. The target is the sign of the day t+1 return.
- Scalers and models are fit on the training window only.
- Splits are chronological and expanding, with a small gap. There is no shuffling and no random k-fold.
- Tests assert that changing future prices leaves earlier features unchanged.

## Evaluation
- Initial training period of about 3 years, then 8 consecutive test blocks of ~6 months.
- Metrics: AUC and accuracy for direction, pooled across folds. Net Sharpe and max drawdown for a long/flat strategy.
- Costs: 5 bps per position change.
- Baselines: always-up, previous-day direction, buy-and-hold. A model has to beat these to count.
- Small-sample caution: one fold has ~125 rows, so judge on pooled predictions and add bootstrap confidence intervals.
- All models run through the same walk-forward function.

## Interfaces
- Model: `fit(features, target)` and `predict_proba(features)`.
- API: `GET /predict` returns the up-probability for the latest day, with its date and the model name.

## Non-goals
Real-time scoring, live trading, intraday data, multi-stock universes, and any "deployed" claim.
This is batch scoring from localhost.

## Known limitations
Single stock chosen with hindsight (survivorship bias), one cost assumption, daily bars only, one market regime.

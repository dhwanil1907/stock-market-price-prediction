# MSFT Next-Day Direction Prediction

Walk-forward evaluation of next-day direction models on Microsoft (MSFT) daily bars, 2010 to now.
Baselines, logistic regression, XGBoost, and LSTM are compared under one protocol, after
transaction costs.

Results: _fill from `outputs/metrics.csv` only._

Limitations: a single stock picked with hindsight (survivorship bias), one 5 bps cost
assumption, daily bars only, and a small sample (~4,000 days).

## Run
    pip install -r requirements.txt
    python -m stockpred.backtest        # writes outputs/metrics.csv
    uvicorn stockpred.api:app           # scoring API
    streamlit run app.py                # dashboard
    pytest

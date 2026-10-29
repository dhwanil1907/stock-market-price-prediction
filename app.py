"""Streamlit dashboard for MSFT (Day 2, item C).

Reads only from outputs/. It never retrains and never downloads.
"""
import streamlit as st

st.title("MSFT Next-Day Direction Models")

# Sections to build:
# 1. Headline table from outputs/metrics.csv (pooled AUC, net Sharpe, max drawdown per model,
#    plus buy-and-hold). Show the baselines first so the reader sees what is being beaten.
# 2. Equity curves per model after costs (Plotly line chart, one line per model, with
#    buy-and-hold as the reference).
# 3. Fold-by-fold AUC, to show whether the edge is stable or only appears in one period.
# 4. SHAP summary for XGBoost. Precompute and save it in the backtest step, so the
#    dashboard only loads it.
# 5. A caveats box: single stock chosen with hindsight (survivorship bias), 5 bps cost
#    assumption, small sample, not investment advice.

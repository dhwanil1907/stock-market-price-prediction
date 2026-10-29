"""Backtest tests.

- Every test date is strictly after every train date in the same fold.
- Training windows expand across folds.
- With a model that always predicts up, the strategy equals buy-and-hold minus one entry cost.
- Costs: more position changes means lower net return, with identical predictions otherwise.
- A model given the true next-day direction (an oracle) scores AUC = 1, as a sanity check.
- A shuffled-target model scores AUC close to 0.5 (guards against hidden leakage).
"""

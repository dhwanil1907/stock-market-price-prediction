"""Leakage tests. Write these before the feature code.

- Features on rows <= t are unchanged when prices after t are altered.
- target at row t equals the sign of the day t+1 return.
- The last row is dropped.
- No NaNs remain after warm-up rows are dropped.
- The output index is unique and sorted by date.
"""

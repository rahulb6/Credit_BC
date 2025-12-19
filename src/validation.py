"""Validation checks (data quality + join sanity)."""

from __future__ import annotations
import pandas as pd

def assert_no_nulls(df: pd.DataFrame, cols: list[str]) -> None:
    missing = {c: int(df[c].isna().sum()) for c in cols if c in df.columns}
    bad = {c: n for c, n in missing.items() if n > 0}
    if bad:
        raise AssertionError(f"Nulls found in columns: {bad}")

def key_uniqueness_report(df: pd.DataFrame, key_cols: list[str]) -> pd.DataFrame:
    """Returns counts of duplicates for the provided key."""
    dup_mask = df.duplicated(subset=key_cols, keep=False)
    out = df.loc[dup_mask, key_cols].value_counts().reset_index(name="dup_count")
    return out

def compare_counts(before: pd.DataFrame, after: pd.DataFrame, label_before: str="before", label_after: str="after") -> pd.DataFrame:
    return pd.DataFrame({
        "stage": [label_before, label_after],
        "rows": [len(before), len(after)],
        "distinct_rows": [before.drop_duplicates().shape[0], after.drop_duplicates().shape[0]],
    })

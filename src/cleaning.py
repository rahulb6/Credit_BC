"""Data cleaning utilities.

Goal: make join keys stable and remove obvious data quality issues.
"""

from __future__ import annotations
import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    return df

def trim_strings(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for c in cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()
    return df

def coerce_int(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
    return df

def drop_duplicate_keys(df: pd.DataFrame, key_cols: list[str], keep: str = "first") -> pd.DataFrame:
    """Generic deduplication for one-to-one enforcement."""
    return df.drop_duplicates(subset=key_cols, keep=keep)

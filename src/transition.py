"""Transition matrix construction (counts + percentages)."""

from __future__ import annotations
import pandas as pd

def transition_matrix(
    df: pd.DataFrame,
    from_col: str,
    to_col: str,
    id_col: str,
    include_no_change: bool = True,
    categories: list[int] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build transition matrices: counts and row-normalized percentages.

    Args:
        df: input with from/to cluster columns and id_col
        from_col: origin cluster column (rows)
        to_col: destination cluster column (columns)
        id_col: account/customer identifier to count
        include_no_change: include cases where from == to
        categories: explicit ordering of cluster values (e.g., 1..19)

    Returns:
        counts_matrix, pct_matrix
    """
    base = df[[id_col, from_col, to_col]].dropna()
    base = base.drop_duplicates([id_col, from_col, to_col])

    if not include_no_change:
        base = base[base[from_col] != base[to_col]]

    if categories is not None:
        base[from_col] = pd.Categorical(base[from_col], categories=categories, ordered=True)
        base[to_col] = pd.Categorical(base[to_col], categories=categories, ordered=True)

    counts = pd.pivot_table(
        base,
        index=from_col,
        columns=to_col,
        values=id_col,
        aggfunc=lambda x: x.nunique(),
        fill_value=0,
        dropna=False,
    )

    pct = counts.div(counts.sum(axis=1).replace(0, pd.NA), axis=0) * 100
    return counts, pct

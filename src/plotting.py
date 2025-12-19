"""Plot helpers (keep visuals consistent across notebooks)."""

from __future__ import annotations
import pandas as pd
import matplotlib.pyplot as plt

def plot_transition_heatmap(matrix: pd.DataFrame, title: str):
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(matrix.values)
    ax.set_title(title)
    ax.set_xlabel(matrix.columns.name or "To")
    ax.set_ylabel(matrix.index.name or "From")
    ax.set_xticks(range(len(matrix.columns)))
    ax.set_xticklabels(matrix.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(matrix.index)))
    ax.set_yticklabels(matrix.index)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    return fig, ax

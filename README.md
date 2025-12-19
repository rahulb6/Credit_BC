# Bureau Cluster Analysis

This repository is a **starter template** for a credit-risk analytics project focused on **Bureau Cluster (BC) movement and stability**.
It is organized for clean project management and reproducible analysis with:
- separate notebooks for cleaning, data checks, and analysis
- lightweight Python modules for reusable logic
- room for documentation, figures, and tests

## Repository structure

```
bureau_cluster_analysis/
├─ data/
│  ├─ raw/          # original extracts (do not edit)
│  ├─ interim/      # cleaned / staged outputs
│  └─ processed/    # final outputs (summaries, transition matrices, CSVs)
├─ notebooks/
│  ├─ 01_data_cleaning.ipynb
│  ├─ 02_data_quality_checks.ipynb
│  └─ 03_transition_analysis.ipynb
├─ src/
│  ├─ config.py
│  ├─ io.py
│  ├─ cleaning.py
│  ├─ validation.py
│  ├─ transition.py
│  └─ plotting.py
├─ reports/
│  └─ figures/
├─ tests/
└─ README.md
```

## Quick start

1) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
# .venv\Scripts\activate  # windows
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Input files into `data/raw/` (CSV / parquet extracts).

4) Run notebooks in order:
- `01_data_cleaning.ipynb` → produces `data/interim/*`
- `02_data_quality_checks.ipynb` → validates counts, keys, and joins
- `03_transition_analysis.ipynb` → builds transition matrix and movement %s

## Notes on Git / PM workflow

- Use Git commits for each meaningful change (cleaning logic, validation rule, analysis step).
- Keep notebooks readable and stable; move reusable code into `src/`.
- Track tasks and progress using a GitHub Project Board (Backlog → In Progress → Validation/Analysis → Completed).

## Outputs

Typical outputs saved to `data/processed/`:
- `bc_summary.csv`
- `transition_matrix_counts.csv`
- `transition_matrix_pct.csv`
- `movement_patterns_top.csv`


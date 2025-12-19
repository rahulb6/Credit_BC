"""Project configuration.

Update paths and key column names here to avoid hardcoding across notebooks/scripts.
"""

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class Paths:
    raw: Path = ROOT / "data" / "raw"
    interim: Path = ROOT / "data" / "interim"
    processed: Path = ROOT / "data" / "processed"
    figures: Path = ROOT / "reports" / "figures"

PATHS = Paths()

@dataclass(frozen=True)
class Columns:
    # Update these to match your extracts
    account_id: str = "current_account_nbr"
    customer_id: str = "customer_id"
    month_code: str = "month_code"
    bc: str = "bureau_cluster"

COLS = Columns()

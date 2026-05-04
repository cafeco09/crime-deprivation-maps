"""
Inspect packaged CSV data.

Run:
    python scripts/inspect_data.py
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
for csv_path in sorted((ROOT / "data").glob("*.csv")):
    print(f"\n## {csv_path.name}")
    print(pd.read_csv(csv_path).to_string(index=False))

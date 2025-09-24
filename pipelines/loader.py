import pandas as pd
import json
from pathlib import Path


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def load_json(filename: str) -> pd.DataFrame:
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / filename
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

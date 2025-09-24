import pandas as pd
import json
from pathlib import Path


def save_scrapped_html(response, name_for_html_file: str):
    with open(f"{name_for_html_file}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Created html file - {name_for_html_file}.html")


def save_fetched_json(data: list[dict], save_path: str, save_json: bool = True, save_csv: bool = False):
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    saved_to_csv = False
    saved_to_json = False

    if save_csv:
        df = pd.DataFrame(data)
        df.to_csv(f"{save_path}.csv", index=False)
        saved_to_csv = True

    if save_json:
        with open(f"{save_path}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        saved_to_json = True

    print(f"Saved CSV to {save_path}.csv: {saved_to_csv}\nJSON to {save_path}.json: {saved_to_json}")

import pandas as pd
import json

from pipelines.loader import load_json


unknown_suspect_keywords_after_2019 = [
    "gunman unknown",
    "gunman unkown",
    "gunman unidentified",
    "gunmen unidentified",
    "suspect unidentified",
    "gunmen unknown",
    "gunmen unkown",
    "gunman: unidentified",
    "gunmen: unidentified",
]

unknown_suspect_keywords_before_2020 = [
    "unknown",
    "unkown",
    "two unknown",
    "unidentified",
    "suspect unidentified",
]

identifying_suspect_keywords = ["suspect", "suspects", "gunman", "gunmen"]


def classify_offender(entry: str, year: int) -> tuple[str, str]:
    """
    2013 -> 194 "unknown" -> 1 "Suspect unidentified" -> 2 "Unidentified" = 197 total unknown
    2014 -> 211 "unknown" -> 8 entries with "Unkown" -> 1 entry of "Two Unknown" = 220 total unknown
    2015 -> 289 "unknown" -> 4 "unidentified" = 293 total unknown
    2016 -> 316 "unknown" = 316 total unknown
    2017 -> 331 "unknown" -> 2 "unkown" -> 1 "unidentified" = 334 total unknown
    2018 -> 286 "unknown" -> 3 "unkown" -> 5 "unidentified" = 294 total unknown
    2019 -> 331 "unknown" -> 7 "unkown" -> 25 "unidentified" = 363 total unknown
    ----------------------- Naming Conventions Change past 2019 -----------------------------------------------------
    2020 -> gunman unidentified: 10, gunman: unidentified: 9, gunman unknown: 500, gunmen unknown: 16, gunman unkown: 1
            = 536 total unknown
    2021 -> gunman unknown: 457, gunmen unknown: 39, gunman: unidentified: 15, gunman unidentified: 23,
            gunmen: unidentified: 3, gunman unkown: 1 = 538 total unknown
    2022 -> gunman unknown: 450, gunman unidentified: 21, gunmen unknown: 29, gunman: unidentified: 17
            gunman unkown: 3, gunmen: unidentified: 2 = 522 total unknown
    2023 -> gunman unknown: 423, gunman: unidentified: 15, gunmen unknown: 22, gunman unidentified: 7
            suspect unidentified: 3, gunmen: unidentified: 1 = 471 total unknown
    2024 -> gunman unknown: 292, gunmen unknown: 8, gunman: unidentified: 4, gunman unidentified: 4
            suspect unidentified: 3 = 311 total unknown
    """

    entry = entry.lower()

    if year > 2019:
        for keyword in unknown_suspect_keywords_after_2019:
            if keyword in entry:
                return "Suspect Unknown", keyword
        for keyword in identifying_suspect_keywords:
            if keyword in entry:
                return "Suspect Identified", keyword

        return "No Suspect Information", "no keyword"
    else:
        for keyword in unknown_suspect_keywords_before_2020:
            if entry.startswith(keyword):
                return "Suspect Unknown", keyword

        return "Suspect Identified", "no keyword"


def clean_col_types(df: pd.DataFrame) -> pd.DataFrame:
    df["killed"] = pd.to_numeric(df["killed"], errors="coerce").fillna(0).astype(int)
    df["wounded"] = pd.to_numeric(df["wounded"], errors="coerce").fillna(0).astype(int)
    df["names"] = df["names"].apply(
        lambda x: ", ".join(x) if isinstance(x, list) else (str(x) if pd.notna(x) else "")
    )
    df["sources"] = df["sources"].apply(
        lambda x: json.dumps(x) if isinstance(x, list) else str(x)
    )

    return df


def clean_names_col(df: pd.DataFrame, year: int, show_debugging: bool = False) -> pd.DataFrame:
    """
    2013-2015 shooters col named 'names' will have just the shooters names and Unknown if else

    2016 - 2025 'names'(shooters) col can have shooters name, description, and victims info

    2013 - 2019 -> 'Unknown' if gunman is not known
    2020 - 2024 -> 'Gunman unknown' or 'Gunman unidentified'

    column titles with value examples:
    "date": "2013-01-01T00:00:00.000Z",
    "killed": "1",
    "wounded": "4",
    "city": "Lorain",
    "state": "OH",
    "names": [""],
    "sources": [
    "http://www.wkyc.com/news/article/276177/3/Lorain-Arrest-made-in-gas-station-shooting"
    ]
    """
    results = df["names"].apply(lambda x: classify_offender(entry=x, year=year))

    df["suspect_status"] = results.apply(lambda x: x[0])
    df["suspect_keyword"] = results.apply(lambda x: x[1])

    if show_debugging:
        unknown_keywords = {}
        suspect_found_keywords = {}
        no_info_keywords = {}

        for _, word in results:
            if word in unknown_suspect_keywords_before_2020 or word in unknown_suspect_keywords_after_2019:
                if word not in unknown_keywords:
                    unknown_keywords[word] = 1
                else:
                    unknown_keywords[word] += 1
            elif word in identifying_suspect_keywords:
                if word not in suspect_found_keywords:
                    suspect_found_keywords[word] = 1
                else:
                    suspect_found_keywords[word] += 1
            else:
                if word not in no_info_keywords:
                    no_info_keywords[word] = 1
                else:
                    no_info_keywords[word] += 1

        print("Clean Names Col Debug")

        print("-----")
        print("Unknown Suspect Keywords")

        unknown_keywords_sum = 0
        for key, val in unknown_keywords.items():
            unknown_keywords_sum += val
            print(f"{key}: {val}")

        print(f"Total Unknown Suspect Keywords: {unknown_keywords_sum}")

        print("-----")
        print("Suspect found keywords")

        suspect_found_keywords_sum = 0
        for key, val in suspect_found_keywords.items():
            suspect_found_keywords_sum += val
            print(f"{key}: {val}")

        print(f"Total Suspect Found Keywords: {suspect_found_keywords_sum}")

        print("-------")
        print("No Suspect Info Keywords")

        no_info_keywords_sum = 0
        for key, val in no_info_keywords.items():
            no_info_keywords_sum += val
            print(f"{key}: {val}")

        print(f"Total No Suspect Info Keywords: {no_info_keywords_sum}")

        print("-----------")
        total_keyword_sum = unknown_keywords_sum + suspect_found_keywords_sum + no_info_keywords_sum
        print(f"Total Entries via keyword sums: {total_keyword_sum}")
        print(f"Total Entries via len(df): {len(df)}")

        print("")
        print(df.head())

        print(f"Total keyword sum == len(df): {total_keyword_sum == len(df)}")

    return df


def clean_date_col(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df["date"] = df["date"].apply(lambda x: x.to_pydatetime() if pd.notna(x) else None)
    df["year"] = df["date"].dt.year.astype("int64")
    df["month"] = df["date"].dt.month.astype("int64")
    df["day"] = df["date"].dt.day.astype("int64")

    return df


def clean_all_entries_by_year(year: int) -> pd.DataFrame:
    name_of_file = f"{year}-data.json"
    df = load_json(filename=name_of_file)
    df = clean_col_types(df=df)
    df = clean_names_col(df=df, year=year)
    df = clean_date_col(df=df)
    # print(df.tail())
    # print(df.columns)

    return df


if __name__ == '__main__':
    year_start = 2013
    clean_all_entries_by_year(year=year_start)

    # Single year info for clean name col
    # desired_year = 2020
    # clean_names_col(year=desired_year, show_debugging=True)

    # Check all keywords match len(df) for every year of data via clean name col function
    # results = {}
    # for i in range(2013, 2025):
    #     keywords_equal_df_len = clean_names_col(year=i, show_debugging=True)
    #     results[i] = keywords_equal_df_len
    #
    # for key, val in results.items():
    #     print(f"{key}: {val}")


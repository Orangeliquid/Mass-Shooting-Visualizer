import time

from pipelines.scraper import fetch_json
from pipelines.saver import save_fetched_json
from pipelines.cleaner import clean_all_entries_by_year
from app.database import init_db
from app.crud.database import create_incident_entries, get_entries_by_year
from app.utils.transformers import to_dataframe


def scrape_and_save(url_to_scrape: str, file_path: str):
    """
    save_fetched_json defaults to only saving a .json file of data but save_csv and save_json bool params can be passed
    to save both or None
    """
    get_page_response = fetch_json(url=url_to_scrape)
    save_fetched_json(data=get_page_response, save_path=file_path)


def clean_and_save_entries(year_start: int, year_end: int):
    for year in range(year_start, year_end + 1):
        # clean data for each year
        df = clean_all_entries_by_year(year)

        print(f"Sample of cleaned data for {year}")
        sample = df.iloc[0]
        for col, val in sample.items():
            print(f"{col}: {val} | type = {type(val)}")

        # save to db
        create_incident_entries(df=df)


if __name__ == '__main__':
    pass
    # -------- Fetching and Saving -------------------
    # Url has data from 2013-2025
    # date_requested = "2025"
    # url_to_pass = f"https://mass-shooting-tracker-data.s3.us-east-2.amazonaws.com/{date_requested}-data.json"
    # desired_file_path = f"data/{date_requested}-data"
    # scrape_and_save(url_to_scrape=url_to_pass, file_path=desired_file_path)

    # for i in range(2015, 2024):
    #     date_requested = str(i)
    #     url_to_pass = f"https://mass-shooting-tracker-data.s3.us-east-2.amazonaws.com/{date_requested}-data.json"
    #     desired_file_path = f"data/{date_requested}-data"
    #     scrape_and_save(url_to_scrape=url_to_pass, file_path=desired_file_path)
    #     time.sleep(10)
    # ---------------------------------------------------

    # ------------- Cleaning and Saving ---------------------- #
    # init_db()  # Call once when starting db entry
    # start, stop = 2013, 2024
    # clean_and_save_entries(year_start=start, year_end=stop)

    # --------------- Reading Entries by Year -----------------------#
    # year_requested = 2013
    # year_entries = get_entries_by_year(year=year_requested)
    # df = to_dataframe(entries=year_entries)
    # print(df.head())
    # print(df.columns)
    # print(len(df))
    # ----------------------------------------------------------------- #




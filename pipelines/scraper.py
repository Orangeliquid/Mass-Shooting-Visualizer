from curl_cffi import requests as cureq


def fetch_page(url: str) -> str:
    response = cureq.get(url, impersonate="chrome136")
    print(f"RESPONSE: {response}")

    if not response.ok:
        raise Exception(f"Failed to fetch page: {response.status_code} - {response.reason}")

    return response


def fetch_json(url: str) -> list[dict]:
    response = cureq.get(url)
    if not response.ok:
        raise Exception(f"Failed to fetch: {response.status_code}")

    return response.json()


if __name__ == '__main__':
    # Url has data from 2013-2025
    date_requested = "2024"
    # url_to_pass = f"https://massshootingtracker.site/data/?year={date_requested}"
    # fetch_page(url=url_to_pass)

    json_url = f"https://mass-shooting-tracker-data.s3.us-east-2.amazonaws.com/{date_requested}-data.json"
    fetch_json(url=json_url)


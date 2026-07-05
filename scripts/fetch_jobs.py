import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

CITIES = ["Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai"]
QUERY = "data analyst"
PAGES_PER_CITY = 5       # 5 pages x 50 results = up to 250 postings per city
RESULTS_PER_PAGE = 50
DELAY_SECONDS = 1        # be polite to the API

def fetch_page(city, page):
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": QUERY,
        "where": city,
        "results_per_page": RESULTS_PER_PAGE,
        "content-type": "application/json",
    }
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    return response.json()

def main():
    os.makedirs("data/raw", exist_ok=True)
    for city in CITIES:
        print(f"Fetching: {city}")
        for page in range(1, PAGES_PER_CITY + 1):
            try:
                data = fetch_page(city, page)
            except requests.HTTPError as e:
                print(f"  Page {page} failed: {e}")
                break

            results = data.get("results", [])
            if not results:
                print(f"  No more results at page {page}, stopping for {city}")
                break

            filename = f"data/raw/{city.lower()}_page{page}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

            print(f"  Page {page}: {len(results)} postings saved to {filename}")
            time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    main()
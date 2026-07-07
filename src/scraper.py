import pandas as pd
import requests
from bs4 import BeautifulSoup

from src.config import PAKWHEELS_URL, RAW_DATA_PATH, RAW_DIR


def scrape_pakwheels() -> pd.DataFrame:
    """Scrape used car listings from PakWheels and return a DataFrame."""
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(PAKWHEELS_URL, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    listing_divs = soup.find_all("div", class_="ad-container")

    records = []

    for div in listing_divs:
        title_tag = div.find("h3")
        price_tag = div.find("div", class_="price-details")
        location_list = div.find("ul", class_="search-vehicle-info")
        specs_list = div.find("ul", class_="search-vehicle-info-2")

        location_tag = location_list.find("li") if location_list else None
        specs = specs_list.find_all("li") if specs_list else []

        records.append(
            {
                "Title": title_tag.get_text(strip=True) if title_tag else None,
                "Price": price_tag.get_text(strip=True) if price_tag else None,
                "Year": specs[0].get_text(strip=True) if len(specs) > 0 else None,
                "Mileage": specs[1].get_text(strip=True) if len(specs) > 1 else None,
                "Fuel": specs[2].get_text(strip=True) if len(specs) > 2 else None,
                "Engine": specs[3].get_text(strip=True) if len(specs) > 3 else None,
                "Transmission": specs[4].get_text(strip=True) if len(specs) > 4 else None,
                "Location": location_tag.get_text(strip=True) if location_tag else None,
            }
        )

    return pd.DataFrame(records)


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = scrape_pakwheels()
    df.to_csv(RAW_DATA_PATH, index=False)

    print(f"Scraping completed. {len(df)} records saved to {RAW_DATA_PATH}")


if __name__ == "__main__":
    main()

import re

import numpy as np
import pandas as pd

from src.config import CLEANED_DATA_PATH, CLEANED_DIR, RAW_DATA_PATH


def clean_price(value):
    """Convert PakWheels price text into approximate PKR numeric value."""
    if pd.isna(value):
        return np.nan

    text = str(value).lower().replace("pkr", "").replace(",", "").strip()

    if "call" in text or text in {"", "n/a", "none"}:
        return np.nan

    numbers = re.findall(r"\d+(?:\.\d+)?", text)
    if not numbers:
        return np.nan

    amount = float(numbers[0])

    if "crore" in text:
        return amount * 10000000
    if "lac" in text or "lakh" in text:
        return amount * 100000

    return amount


def clean_mileage(value):
    """Convert mileage text into numeric kilometers."""
    if pd.isna(value):
        return np.nan

    text = str(value).lower().replace(",", "")
    numbers = re.findall(r"\d+", text)

    return float(numbers[0]) if numbers else np.nan


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw PakWheels data."""
    cleaned = df.copy()

    cleaned["Price"] = cleaned["Price"].apply(clean_price)
    cleaned["Year"] = pd.to_numeric(cleaned["Year"], errors="coerce")
    cleaned["Mileage"] = cleaned["Mileage"].apply(clean_mileage)

    cleaned["Price"] = cleaned["Price"].fillna(cleaned["Price"].median())
    cleaned["Year"] = cleaned["Year"].fillna(cleaned["Year"].median())
    cleaned["Mileage"] = cleaned["Mileage"].fillna(cleaned["Mileage"].median())

    cleaned = cleaned.drop_duplicates()
    cleaned["Brand"] = cleaned["Title"].astype(str).str.split().str[0]

    cleaned = cleaned[cleaned["Price"] > 500000]
    cleaned = cleaned.sort_values(by="Year", ascending=False)

    return cleaned


def main() -> None:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw dataset not found: {RAW_DATA_PATH}. Run scraper first.")

    CLEANED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_DATA_PATH)
    cleaned = clean_data(df)
    cleaned.to_csv(CLEANED_DATA_PATH, index=False)

    print(f"Cleaned data saved to {CLEANED_DATA_PATH}")
    print(cleaned.head())


if __name__ == "__main__":
    main()

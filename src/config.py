from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"
PLOT_DIR = BASE_DIR / "plot_images"

RAW_DATA_PATH = RAW_DIR / "pakwheels_cars.csv"
CLEANED_DATA_PATH = CLEANED_DIR / "pakwheels_cleaned.csv"

PAKWHEELS_URL = "https://www.pakwheels.com/used-cars/search/-/"

SQL_SERVER = "."
SQL_DATABASE = "PakWheelsDB"
SQL_TABLE = "Cars"

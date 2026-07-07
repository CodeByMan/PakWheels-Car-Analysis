import matplotlib.pyplot as plt
import pandas as pd

from src.config import CLEANED_DATA_PATH, PLOT_DIR


def main() -> None:
    if not CLEANED_DATA_PATH.exists():
        raise FileNotFoundError(f"Cleaned dataset not found: {CLEANED_DATA_PATH}. Run cleaner first.")

    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(CLEANED_DATA_PATH)

    brand_counts = df["Brand"].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    brand_counts.plot(kind="bar")
    plt.title("Top 10 Car Brands by Number of Listings")
    plt.ylabel("Number of Listings")
    plt.xlabel("Brand")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(PLOT_DIR / "top_10_brands.png", dpi=300)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.hist(df["Price"], bins=20, edgecolor="black")
    plt.title("Distribution of Car Prices")
    plt.xlabel("Price (PKR)")
    plt.ylabel("Number of Cars")
    plt.tight_layout()
    plt.savefig(PLOT_DIR / "price_distribution.png", dpi=300)
    plt.close()

    avg_price = df.groupby("Brand")["Price"].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    avg_price.plot(kind="bar")
    plt.title("Average Price per Brand (Top 10)")
    plt.ylabel("Average Price (PKR)")
    plt.xlabel("Brand")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(PLOT_DIR / "average_price_per_brand.png", dpi=300)
    plt.close()

    year_counts = df["Year"].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    year_counts.plot(kind="line", marker="o")
    plt.title("Number of Cars by Year")
    plt.ylabel("Number of Cars")
    plt.xlabel("Year")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOT_DIR / "cars_by_year.png", dpi=300)
    plt.close()

    print(f"Visualizations saved to {PLOT_DIR}")


if __name__ == "__main__":
    main()

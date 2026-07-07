# 🚗 PakWheels Car Analysis

## 📌 Project Overview

This project collects used car listing data from **PakWheels**, cleans
and transforms the dataset, generates visual insights, optionally loads
the cleaned data into SQL Server, and provides an interactive Streamlit
dashboard.

## 🖼️ Visualization Preview

### Top 10 Car Brands

`<img src="plot_images/top_10_brands.png" width="900"/>`{=html}

### Price Distribution

`<img src="plot_images/price_distribution.png" width="900"/>`{=html}

### Average Price per Brand

`<img src="plot_images/average_price_per_brand.png" width="900"/>`{=html}

### Cars by Year

`<img src="plot_images/cars_by_year.png" width="900"/>`{=html}

## 🚀 How to Run

``` bash
git clone https://github.com/CodeByMan/PakWheels-Car-Analysis.git
cd PakWheels-Car-Analysis
conda env create -f environment.yml
conda activate pakwheels_env
python -m src.scraper
python -m src.cleaner
python -m src.visualization
streamlit run src/dashboard.py
```

## 👤 Author

**Muhammad Ali Nawaz**\
Cloud Data Engineer

<div align="center">

<h1>🚗 PakWheels Car Analysis</h1>

<p>
<b>Enterprise-style data pipeline for scraping, cleaning, analyzing, storing, and visualizing PakWheels used car listings.</b>
</p>

<p>
<img src="https://img.shields.io/badge/Python-Data%20Pipeline-blue">
<img src="https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green">
<img src="https://img.shields.io/badge/Pandas-Data%20Cleaning-orange">
<img src="https://img.shields.io/badge/SQL%20Server-Database-red">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-purple">
</p>

</div>

---

<img src="pakwheels.png" alt="PakWheels Banner" width="900"/>

## 📌 Project Overview

This project collects used car listing data from **PakWheels**, cleans and transforms the dataset, generates visual insights, optionally loads the cleaned data into SQL Server, and provides an interactive Streamlit dashboard.

The project is structured like a small production data project with separate modules for scraping, cleaning, visualization, database loading, dashboarding, and shared configuration.

---

## 🎯 Objectives

- Scrape used car listing data from PakWheels
- Extract title, price, year, mileage, fuel type, engine, transmission, and location
- Clean raw text fields into analysis-ready numeric columns
- Derive car brand from listing title
- Generate visualizations for brand counts, prices, and yearly trends
- Load cleaned data into SQL Server
- Build an interactive Streamlit dashboard

---

## 🔄 Pipeline Workflow

```text
PakWheels Website
      │
      ▼
Web Scraper
      │
      ▼
data/raw/pakwheels_cars.csv
      │
      ▼
Cleaning & Transformation
      │
      ▼
data/cleaned/pakwheels_cleaned.csv
      │
      ├──► plot_images/
      ├──► SQL Server Table: Cars
      └──► Streamlit Dashboard
```

---

## 📁 Project Structure

```text
PakWheels-Car-Analysis/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── scraper.py
│   ├── cleaner.py
│   ├── visualization.py
│   ├── database.py
│   └── dashboard.py
│
├── data/
│   ├── raw/
│   │   └── pakwheels_cars.csv
│   └── cleaned/
│       └── pakwheels_cleaned.csv
│
├── plot_images/
│   ├── top_10_brands.png
│   ├── price_distribution.png
│   ├── average_price_per_brand.png
│   └── cars_by_year.png
│
├── README.md
├── requirements.txt
├── environment.yml
├── LICENSE
└── .gitignore
```

---

## 🖼️ Visualization Preview

### Top 10 Car Brands

<img src="plot_images/top_10_brands.png" alt="Top 10 Car Brands" width="900"/>

### Price Distribution

<img src="plot_images/price_distribution.png" alt="Price Distribution" width="900"/>

### Average Price per Brand

<img src="plot_images/average_price_per_brand.png" alt="Average Price per Brand" width="900"/>

### Cars by Year

<img src="plot_images/cars_by_year.png" alt="Cars by Year" width="900"/>

---

## 📊 Data Fields

| Column | Description |
|---|---|
| `Title` | Car listing title |
| `Price` | Cleaned numeric car price in PKR |
| `Year` | Car model year |
| `Mileage` | Cleaned numeric mileage |
| `Fuel` | Fuel type |
| `Engine` | Engine capacity |
| `Transmission` | Transmission type |
| `Location` | Listing city/location |
| `Brand` | Derived brand from listing title |

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/CodeByMan/PakWheels-Car-Analysis.git
cd PakWheels-Car-Analysis
```

### 2. Install dependencies

Using pip:

```bash
pip install -r requirements.txt
```

Or using Conda:

```bash
conda env create -f environment.yml
conda activate pakwheels_env
```

### 3. Run scraper

```bash
python -m src.scraper
```

### 4. Clean data

```bash
python -m src.cleaner
```

### 5. Generate visualizations

```bash
python -m src.visualization
```

### 6. Run dashboard

```bash
streamlit run src/dashboard.py
```

### 7. Optional: Load into SQL Server

```bash
python -m src.database
```

> SQL Server, ODBC Driver 17, and the `PakWheelsDB` database must exist before running the database loading script.

---

## 🖼️ Visualizations

Generated plots are saved inside:

```text
plot_images/
```

Visualizations include:

- Top 10 car brands by number of listings
- Car price distribution
- Average price per brand
- Number of cars by year

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | HTTP requests |
| BeautifulSoup | Web scraping |
| Pandas | Data cleaning and analysis |
| NumPy | Numeric processing |
| Matplotlib | Visualization |
| SQLAlchemy | Database connection |
| PyODBC | SQL Server driver |
| SQL Server | Database storage |
| Streamlit | Interactive dashboard |

---

## 👤 Author

**Muhammad Ali Nawaz**  
Data Analyst

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
<b>⭐ If you found this project useful, consider giving it a star!</b>
</p>

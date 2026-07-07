import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from src.config import CLEANED_DATA_PATH

st.set_page_config(page_title="PakWheels Car Analysis", layout="wide")
st.title("🚗 PakWheels Car Analysis Dashboard")

if not CLEANED_DATA_PATH.exists():
    st.error("Cleaned dataset not found. Run `python -m src.cleaner` first.")
    st.stop()

df = pd.read_csv(CLEANED_DATA_PATH)

st.sidebar.header("Filter Options")

brands = sorted(df["Brand"].dropna().unique())
selected_brands = st.sidebar.multiselect("Select Brand(s):", brands, default=brands)

years = sorted(df["Year"].dropna().astype(int).unique())
selected_years = st.sidebar.slider(
    "Select Year Range:",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(int(min(years)), int(max(years))),
)

min_price = int(df["Price"].min())
max_price = int(df["Price"].max())
selected_price = st.sidebar.slider(
    "Select Price Range (PKR):",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),
)

filtered_df = df[
    (df["Brand"].isin(selected_brands))
    & (df["Year"] >= selected_years[0])
    & (df["Year"] <= selected_years[1])
    & (df["Price"] >= selected_price[0])
    & (df["Price"] <= selected_price[1])
]

st.subheader("Filtered Cars")

if filtered_df.empty:
    st.warning("No cars match your filter criteria.")
else:
    st.dataframe(
        filtered_df[["Title", "Brand", "Year", "Price", "Mileage", "Transmission", "Location"]]
        .sort_values(by="Year", ascending=False),
        use_container_width=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 10 Brands by Listings")
        st.bar_chart(filtered_df["Brand"].value_counts().head(10))

    with col2:
        st.subheader("Cars by Year")
        st.line_chart(filtered_df["Year"].value_counts().sort_index())

    st.subheader("Price Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(filtered_df["Price"], bins=20, edgecolor="black")
    ax.set_xlabel("Price (PKR)")
    ax.set_ylabel("Number of Cars")
    st.pyplot(fig)

import numpy as np
import pandas as pd
from pathlib import Path


# =========================================================
# Reproducibility
# =========================================================
np.random.seed(42)


# =========================================================
# Configuration
# =========================================================
DAYS = 90

# Current project reporting period:
# May 20, 2026 → August 17, 2026
START_DATE = "2026-05-20"
END_DATE = "2026-08-17"


# =========================================================
# Project root directory
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# =========================================================
# Output directory
# =========================================================
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "ecommerce_data.csv"


# =========================================================
# Generate dates
# =========================================================
dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

# Safety validation
if len(dates) != DAYS:
    raise ValueError(
        f"Expected {DAYS} dates, but generated {len(dates)} dates."
    )

day_number = np.arange(DAYS)


# =========================================================
# Weekly pattern
# Weekends generally receive more traffic.
# =========================================================
weekly_pattern = np.where(
    dates.dayofweek >= 5,
    1.10,
    0.95
)


# =========================================================
# Gradual business growth over time
# =========================================================
growth_factor = 1 + (day_number / DAYS) * 0.18


# =========================================================
# Website traffic
# =========================================================
base_traffic = 4200

traffic_noise = np.random.normal(
    loc=0,
    scale=280,
    size=DAYS
)

website_traffic = (
    base_traffic
    * weekly_pattern
    * growth_factor
    + traffic_noise
)

website_traffic = np.maximum(
    np.round(website_traffic),
    1000
).astype(int)


# =========================================================
# Marketing spend
# =========================================================
marketing_spend = (
    website_traffic * 0.18
    + np.random.normal(0, 45, DAYS)
)

marketing_spend = np.maximum(
    np.round(marketing_spend, 2),
    300
)


# =========================================================
# Conversion rate
# =========================================================
base_conversion = 0.032

conversion_variation = np.random.normal(
    0,
    0.0035,
    DAYS
)

conversion_rate_raw = (
    base_conversion
    + conversion_variation
    + (day_number / DAYS) * 0.004
)

conversion_rate_raw = np.clip(
    conversion_rate_raw,
    0.018,
    0.055
)


# =========================================================
# Orders
# =========================================================
orders = (
    website_traffic * conversion_rate_raw
    + np.random.normal(0, 5, DAYS)
)

orders = np.maximum(
    np.round(orders),
    1
).astype(int)


# =========================================================
# Customers
# =========================================================
new_customer_ratio = np.random.uniform(
    0.58,
    0.68,
    DAYS
)

new_customers = (
    orders * new_customer_ratio
).round().astype(int)

new_customers = np.maximum(
    new_customers,
    1
)

returning_customers = (
    orders - new_customers
)

returning_customers = np.maximum(
    returning_customers,
    0
)


# =========================================================
# Average Order Value and Revenue
# =========================================================
average_order_value = (
    72
    + (day_number / DAYS) * 8
    + np.random.normal(0, 5, DAYS)
)

average_order_value = np.clip(
    average_order_value,
    55,
    95
)

revenue = (
    orders * average_order_value
)

revenue = np.maximum(
    np.round(revenue, 2),
    50
)


# =========================================================
# Engagement rate
# =========================================================
engagement_rate = (
    0.42
    + np.random.normal(0, 0.025, DAYS)
    + (day_number / DAYS) * 0.025
)

engagement_rate = np.clip(
    engagement_rate,
    0.30,
    0.55
)

engagement_rate = np.round(
    engagement_rate * 100,
    2
)


# =========================================================
# Build dataset
# =========================================================
df = pd.DataFrame({
    "date": dates,
    "revenue": revenue,
    "orders": orders,
    "website_traffic": website_traffic,
    "marketing_spend": marketing_spend,
    "new_customers": new_customers,
    "returning_customers": returning_customers,
    "engagement_rate": engagement_rate
})


# =========================================================
# Derived metrics
# =========================================================

# Conversion Rate = Orders / Website Traffic × 100
df["conversion_rate"] = (
    df["orders"] / df["website_traffic"] * 100
).round(2)


# Average Order Value = Revenue / Orders
df["average_order_value"] = (
    df["revenue"] / df["orders"]
).round(2)


# Revenue Growth
df["revenue_growth"] = (
    df["revenue"].pct_change() * 100
).fillna(0).round(2)


# Traffic Growth
df["traffic_growth"] = (
    df["website_traffic"].pct_change() * 100
).fillna(0).round(2)


# Customer Growth
total_customers = (
    df["new_customers"]
    + df["returning_customers"]
)

df["customer_growth"] = (
    total_customers.pct_change() * 100
).fillna(0).round(2)


# =========================================================
# Final formatting
# =========================================================
df["date"] = df["date"].dt.strftime("%Y-%m-%d")


# =========================================================
# Save dataset
# =========================================================
df.to_csv(
    OUTPUT_FILE,
    index=False
)


# =========================================================
# Validation output
# =========================================================
print("=" * 60)
print("E-COMMERCE DATASET GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Output: {OUTPUT_FILE}")

print(f"\nReporting Period:")
print(f"Start Date: {df['date'].min()}")
print(f"End Date:   {df['date'].max()}")

print("\nColumns:")
for column in df.columns:
    print(f"- {column}")

print("\nFirst 5 rows:")
print(df.head().to_string(index=False))

print("\nLast 5 rows:")
print(df.tail().to_string(index=False))

print("\nDataset statistics:")
print(df.describe().round(2).to_string())

print("\nMissing values:")
print(df.isnull().sum())

print("\n" + "=" * 60)
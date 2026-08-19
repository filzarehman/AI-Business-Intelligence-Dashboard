import pandas as pd
from pathlib import Path


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "ecommerce_data.csv"


# ---------------------------------------------------------
# Load dataset
# ---------------------------------------------------------
def load_data():
    """Load the raw e-commerce dataset."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    return df


# ---------------------------------------------------------
# Clean and validate dataset
# ---------------------------------------------------------
def process_data(df):
    """Clean, validate, and calculate business metrics."""

    df = df.copy()

    # -----------------------------------------------------
    # Convert date column
    # -----------------------------------------------------
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    if df["date"].isna().any():
        raise ValueError(
            "Invalid date values detected."
        )

    # -----------------------------------------------------
    # Remove duplicate rows
    # -----------------------------------------------------
    df = df.drop_duplicates().reset_index(drop=True)

    # -----------------------------------------------------
    # Check required columns
    # -----------------------------------------------------
    required_columns = [
        "date",
        "revenue",
        "orders",
        "website_traffic",
        "marketing_spend",
        "new_customers",
        "returning_customers",
        "engagement_rate"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # -----------------------------------------------------
    # Check missing values
    # -----------------------------------------------------
    if df.isnull().any().any():
        missing_values = df.isnull().sum()
        missing_values = missing_values[
            missing_values > 0
        ]

        raise ValueError(
            f"Missing values detected:\n{missing_values}"
        )

    # -----------------------------------------------------
    # Validate numerical ranges
    # -----------------------------------------------------
    if (df["revenue"] < 0).any():
        raise ValueError(
            "Revenue cannot be negative."
        )

    if (df["orders"] < 0).any():
        raise ValueError(
            "Orders cannot be negative."
        )

    if (df["website_traffic"] < 0).any():
        raise ValueError(
            "Website traffic cannot be negative."
        )

    if (df["marketing_spend"] < 0).any():
        raise ValueError(
            "Marketing spend cannot be negative."
        )

    if (df["new_customers"] < 0).any():
        raise ValueError(
            "New customers cannot be negative."
        )

    if (df["returning_customers"] < 0).any():
        raise ValueError(
            "Returning customers cannot be negative."
        )

    if not df["engagement_rate"].between(0, 100).all():
        raise ValueError(
            "Engagement rate must be between 0 and 100."
        )

    # -----------------------------------------------------
    # Sort by date
    # -----------------------------------------------------
    df = df.sort_values("date").reset_index(drop=True)

    # -----------------------------------------------------
    # Calculate total customers
    # -----------------------------------------------------
    df["total_customers"] = (
        df["new_customers"]
        + df["returning_customers"]
    )

    # -----------------------------------------------------
    # Recalculate conversion rate
    # -----------------------------------------------------
    df["conversion_rate"] = (
        df["orders"]
        / df["website_traffic"]
        * 100
    ).round(2)

    # -----------------------------------------------------
    # Recalculate average order value
    # -----------------------------------------------------
    df["average_order_value"] = (
        df["revenue"]
        / df["orders"]
    ).round(2)

    # -----------------------------------------------------
    # Recalculate growth metrics
    # -----------------------------------------------------
    df["revenue_growth"] = (
        df["revenue"]
        .pct_change()
        .mul(100)
        .fillna(0)
        .round(2)
    )

    df["traffic_growth"] = (
        df["website_traffic"]
        .pct_change()
        .mul(100)
        .fillna(0)
        .round(2)
    )

    df["customer_growth"] = (
        df["total_customers"]
        .pct_change()
        .mul(100)
        .fillna(0)
        .round(2)
    )

    # -----------------------------------------------------
    # Validate calculated metrics
    # -----------------------------------------------------
    expected_conversion = (
        df["orders"]
        / df["website_traffic"]
        * 100
    ).round(2)

    if not df["conversion_rate"].equals(
        expected_conversion
    ):
        raise ValueError(
            "Conversion rate validation failed."
        )

    expected_aov = (
        df["revenue"]
        / df["orders"]
    ).round(2)

    if not df["average_order_value"].equals(
        expected_aov
    ):
        raise ValueError(
            "Average order value validation failed."
        )

    return df
# ---------------------------------------------------------
# KPI calculations
# ---------------------------------------------------------
def calculate_kpis(df):
    """Calculate the main business KPIs."""

    if df.empty:
        raise ValueError(
            "Cannot calculate KPIs from an empty dataset."
        )

    total_revenue = df["revenue"].sum()
    total_orders = df["orders"].sum()
    total_customers = df["total_customers"].sum()
    total_traffic = df["website_traffic"].sum()
    total_marketing_spend = df["marketing_spend"].sum()

    conversion_rate = (
        total_orders / total_traffic * 100
        if total_traffic > 0
        else 0
    )

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": int(total_orders),
        "total_customers": int(total_customers),
        "conversion_rate": round(conversion_rate, 2),
        "average_order_value": round(
            average_order_value,
            2
        ),
        "website_traffic": int(total_traffic),
        "marketing_spend": round(
            total_marketing_spend,
            2
        ),
    }


# ---------------------------------------------------------
# Period-over-period KPI changes
# ---------------------------------------------------------
def calculate_period_changes(df):
    """Calculate changes between the first and second
    half of the selected period."""

    if len(df) < 2:
        return {}

    midpoint = len(df) // 2

    previous_period = df.iloc[:midpoint]
    current_period = df.iloc[midpoint:]

    def percentage_change(current, previous):
        if previous == 0:
            return 0

        return round(
            ((current - previous) / previous) * 100,
            2
        )

    previous_revenue = previous_period["revenue"].sum()
    current_revenue = current_period["revenue"].sum()

    previous_orders = previous_period["orders"].sum()
    current_orders = current_period["orders"].sum()

    previous_customers = (
        previous_period["total_customers"].sum()
    )

    current_customers = (
        current_period["total_customers"].sum()
    )

    previous_traffic = (
        previous_period["website_traffic"].sum()
    )

    current_traffic = (
        current_period["website_traffic"].sum()
    )

    previous_marketing = (
        previous_period["marketing_spend"].sum()
    )

    current_marketing = (
        current_period["marketing_spend"].sum()
    )

    return {
        "revenue_change": percentage_change(
            current_revenue,
            previous_revenue
        ),
        "orders_change": percentage_change(
            current_orders,
            previous_orders
        ),
        "customers_change": percentage_change(
            current_customers,
            previous_customers
        ),
        "traffic_change": percentage_change(
            current_traffic,
            previous_traffic
        ),
        "marketing_spend_change": percentage_change(
            current_marketing,
            previous_marketing
        ),
    }

# ---------------------------------------------------------
# Main test
# ---------------------------------------------------------
if __name__ == "__main__":

    print("=" * 60)
    print("KPI ENGINE TEST")
    print("=" * 60)

    raw_df = load_data()
    clean_df = process_data(raw_df)

    kpis = calculate_kpis(clean_df)
    changes = calculate_period_changes(clean_df)

    print("\nMAIN KPIs")
    print("-" * 40)

    for name, value in kpis.items():
        print(f"{name}: {value}")

    print("\nPERIOD CHANGES")
    print("-" * 40)

    for name, value in changes.items():
        print(f"{name}: {value}%")

    print("\n" + "=" * 60)
    print("KPI ENGINE PASSED SUCCESSFULLY")
    print("=" * 60)
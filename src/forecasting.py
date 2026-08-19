import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


def create_revenue_forecast(
    df,
    forecast_days=30
):
    """
    Create a revenue forecast using
    Linear Regression.

    Parameters
    ----------
    df : pandas.DataFrame
        Historical ecommerce data.
        Must contain 'date' and 'revenue'.

    forecast_days : int
        Number of future days to predict.

    Returns
    -------
    historical_df : pandas.DataFrame
        Historical revenue data.

    forecast_df : pandas.DataFrame
        Future dates with predicted revenue.

    model : LinearRegression
        Trained regression model.
    """

    # -----------------------------------------------------
    # Prepare data
    # -----------------------------------------------------

    data = df[
        ["date", "revenue"]
    ].copy()

    data = data.sort_values("date")

    data = data.dropna(
        subset=[
            "date",
            "revenue"
        ]
    )

    # -----------------------------------------------------
    # Convert dates to numeric values
    # -----------------------------------------------------

    data["date_numeric"] = (
        data["date"]
        - data["date"].min()
    ).dt.days

    # -----------------------------------------------------
    # Features and target
    # -----------------------------------------------------

    X = data[
        ["date_numeric"]
    ]

    y = data[
        "revenue"
    ]

    # -----------------------------------------------------
    # Train model
    # -----------------------------------------------------

    model = LinearRegression()

    model.fit(
        X,
        y
    )

    # -----------------------------------------------------
    # Create future dates
    # -----------------------------------------------------

    last_date = data["date"].max()

    future_dates = pd.date_range(
        start=last_date + pd.Timedelta(days=1),
        periods=forecast_days,
        freq="D",
    )

    # -----------------------------------------------------
    # Convert future dates to numeric
    # -----------------------------------------------------

    future_numeric = (
        future_dates
        - data["date"].min()
    ).days

    future_numeric = np.array(
        future_numeric
    ).reshape(-1, 1)

    # -----------------------------------------------------
    # Predict revenue
    # -----------------------------------------------------

    predictions = model.predict(
        future_numeric
    )

    # Prevent negative revenue predictions
    predictions = np.maximum(
        predictions,
        0
    )

    # -----------------------------------------------------
    # Create forecast dataframe
    # -----------------------------------------------------

    forecast_df = pd.DataFrame(
        {
            "date": future_dates,
            "predicted_revenue": predictions,
        }
    )

    # -----------------------------------------------------
    # Historical dataframe
    # -----------------------------------------------------

    historical_df = data[
        [
            "date",
            "revenue"
        ]
    ].copy()

    return (
        historical_df,
        forecast_df,
        model
    )
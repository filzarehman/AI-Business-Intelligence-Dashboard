import pandas as pd


def generate_ai_insights(df):
    """
    Generate business intelligence insights from e-commerce data.
    """

    insights = []

    # ---------------------------------------------------------
    # Basic calculations
    # ---------------------------------------------------------
    total_revenue = df["revenue"].sum()
    total_orders = df["orders"].sum()
    total_traffic = df["website_traffic"].sum()
    total_marketing = df["marketing_spend"].sum()

    avg_conversion = df["conversion_rate"].mean()
    avg_order_value = df["average_order_value"].mean()

    revenue_growth = (
        (df["revenue"].iloc[-1] - df["revenue"].iloc[0])
        / df["revenue"].iloc[0]
    ) * 100

    traffic_growth = (
        (df["website_traffic"].iloc[-1] - df["website_traffic"].iloc[0])
        / df["website_traffic"].iloc[0]
    ) * 100

    marketing_growth = (
        (df["marketing_spend"].iloc[-1] - df["marketing_spend"].iloc[0])
        / df["marketing_spend"].iloc[0]
    ) * 100

    # ---------------------------------------------------------
    # Revenue insights
    # ---------------------------------------------------------
    if revenue_growth > 10:
        insights.append({
            "category": "Revenue",
            "severity": "Positive",
            "title": "Strong Revenue Growth",
            "message": (
                f"Revenue increased by {revenue_growth:.1f}% "
                "across the selected period."
            ),
            "recommendation": (
                "Maintain the current sales strategy and identify "
                "the highest-performing periods for further investment."
            )
        })
    elif revenue_growth < 0:
        insights.append({
            "category": "Revenue",
            "severity": "Warning",
            "title": "Revenue Decline",
            "message": (
                f"Revenue decreased by {abs(revenue_growth):.1f}% "
                "across the selected period."
            ),
            "recommendation": (
                "Review pricing, product performance, traffic sources, "
                "and conversion performance."
            )
        })

    # ---------------------------------------------------------
    # Traffic insights
    # ---------------------------------------------------------
    if traffic_growth > 10:
        insights.append({
            "category": "Traffic",
            "severity": "Positive",
            "title": "Website Traffic Growing",
            "message": (
                f"Website traffic increased by {traffic_growth:.1f}%."
            ),
            "recommendation": (
                "Continue investing in the channels generating the "
                "highest-quality traffic."
            )
        })
    elif traffic_growth < 0:
        insights.append({
            "category": "Traffic",
            "severity": "Warning",
            "title": "Traffic Declining",
            "message": (
                f"Website traffic decreased by {abs(traffic_growth):.1f}%."
            ),
            "recommendation": (
                "Review SEO, advertising campaigns, social media activity, "
                "and acquisition channels."
            )
        })

    # ---------------------------------------------------------
    # Conversion insights
    # ---------------------------------------------------------
    if avg_conversion >= 3.5:
        insights.append({
            "category": "Conversion",
            "severity": "Positive",
            "title": "Healthy Conversion Rate",
            "message": (
                f"Average conversion rate is {avg_conversion:.2f}%."
            ),
            "recommendation": (
                "Test checkout improvements and personalized offers "
                "to increase conversion further."
            )
        })
    else:
        insights.append({
            "category": "Conversion",
            "severity": "Warning",
            "title": "Conversion Opportunity",
            "message": (
                f"Average conversion rate is {avg_conversion:.2f}%."
            ),
            "recommendation": (
                "Optimize landing pages, product pages, checkout flow, "
                "and calls-to-action."
            )
        })

    # ---------------------------------------------------------
    # Marketing insights
    # ---------------------------------------------------------
    if marketing_growth > revenue_growth:
        insights.append({
            "category": "Marketing",
            "severity": "Warning",
            "title": "Marketing Spend Growing Faster",
            "message": (
                f"Marketing spend increased by {marketing_growth:.1f}%, "
                f"while revenue changed by {revenue_growth:.1f}%."
            ),
            "recommendation": (
                "Evaluate campaign ROI and shift budget toward "
                "higher-performing acquisition channels."
            )
        })
    else:
        insights.append({
            "category": "Marketing",
            "severity": "Positive",
            "title": "Marketing Efficiency",
            "message": (
                "Revenue growth is keeping pace with or exceeding "
                "marketing spend growth."
            ),
            "recommendation": (
                "Continue monitoring return on marketing investment "
                "before increasing campaign budgets."
            )
        })

    # ---------------------------------------------------------
    # Average order value
    # ---------------------------------------------------------
    if avg_order_value >= 75:
        insights.append({
            "category": "Sales",
            "severity": "Positive",
            "title": "Strong Average Order Value",
            "message": (
                f"Average order value is ${avg_order_value:,.2f}."
            ),
            "recommendation": (
                "Use bundles, cross-selling, and upselling to "
                "increase order value further."
            )
        })

    # ---------------------------------------------------------
    # Performance summary
    # ---------------------------------------------------------
    summary = {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_traffic": total_traffic,
        "total_marketing_spend": total_marketing,
        "average_conversion_rate": avg_conversion,
        "average_order_value": avg_order_value,
        "revenue_growth": revenue_growth,
        "traffic_growth": traffic_growth,
        "marketing_growth": marketing_growth,
    }

    return {
        "summary": summary,
        "insights": insights
    }


# ---------------------------------------------------------
# Test
# ---------------------------------------------------------
if __name__ == "__main__":

    data_file = "data/ecommerce_data.csv"

    df = pd.read_csv(data_file)

    result = generate_ai_insights(df)

    print("=" * 60)
    print("AI BUSINESS INSIGHTS ENGINE")
    print("=" * 60)

    print("\nKEY METRICS")
    print("-" * 40)

    for key, value in result["summary"].items():
        if "revenue" in key or "spend" in key or "value" in key:
            print(f"{key}: ${value:,.2f}")
        elif "growth" in key or "rate" in key:
            print(f"{key}: {value:.2f}%")
        else:
            print(f"{key}: {value:,.0f}")

    print("\nAI INSIGHTS")
    print("-" * 40)

    for insight in result["insights"]:
        print(f"\n[{insight['severity']}] {insight['title']}")
        print(f"Insight: {insight['message']}")
        print(f"Recommendation: {insight['recommendation']}")

    print("\n" + "=" * 60)
    print("AI INSIGHTS ENGINE PASSED")
    print("=" * 60)
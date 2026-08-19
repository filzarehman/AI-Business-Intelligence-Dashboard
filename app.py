import streamlit as st
import plotly.express as px
import pandas as pd

from src.data_processing import (
    load_data,
    process_data,
    calculate_kpis,
    calculate_period_changes,
)

from src.forecasting import create_revenue_forecast

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Business Intelligence Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# BLACK + BLUE THEME
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL APPLICATION
    ===================================================== */

    .stApp {
        background-color: #030712;
        color: #e5e7eb;
    }

    .main {
        background-color: #030712;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .stApp p,
    .stApp span,
    .stApp label {
        color: #cbd5e1;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
    }


    /* =====================================================
       STREAMLIT TOP HEADER / DEPLOY BAR
    ===================================================== */

    header[data-testid="stHeader"] {
        background-color: #020617 !important;
        border-bottom: 1px solid #172554 !important;
    }

    header[data-testid="stHeader"] > div {
        background-color: #020617 !important;
    }

    header[data-testid="stHeader"] [data-testid="stToolbar"] {
        background-color: #020617 !important;
    }

    /* Deploy button */
    header[data-testid="stHeader"] button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px !important;
    }

    header[data-testid="stHeader"] button:hover {
        background-color: #1d4ed8 !important;
        border-color: #60a5fa !important;
        color: #ffffff !important;
    }

    /* Three-dot menu */
    header[data-testid="stHeader"] [data-testid="stToolbar"] button {
        color: #60a5fa !important;
    }

    header[data-testid="stHeader"] [data-testid="stToolbar"] button:hover {
        background-color: #172554 !important;
        color: #93c5fd !important;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #172554 !important;
    }

    section[data-testid="stSidebar"] > div {
        background-color: #020617 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #dbeafe !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: #172554 !important;
    }


    /* =====================================================
       DATE PICKER / INPUTS
    ===================================================== */

    div[data-baseweb="input"],
    div[data-baseweb="select"],
    div[data-baseweb="popover"] {
        background-color: #0a1020 !important;
        border-color: #1e3a8a !important;
    }

    div[data-testid="stDateInput"] {
        color: #e5e7eb !important;
    }

    div[data-testid="stDateInput"] > div {
        background-color: #0a1020 !important;
        border-color: #1e3a8a !important;
        border-radius: 10px !important;
    }

    div[data-testid="stDateInput"] input {
        background-color: #0a1020 !important;
        color: #f8fafc !important;
        border-color: #1e3a8a !important;
    }

    div[data-testid="stDateInput"] input::placeholder {
        color: #64748b !important;
    }

    div[data-baseweb="calendar"] {
        background-color: #0a1020 !important;
        color: #f8fafc !important;
    }

    div[data-baseweb="calendar"] * {
        color: #e5e7eb !important;
    }

    div[data-baseweb="calendar"] button {
        background-color: #0a1020 !important;
        color: #e5e7eb !important;
    }

    div[data-baseweb="calendar"] button:hover {
        background-color: #1e3a8a !important;
        color: white !important;
    }

    div[data-baseweb="calendar"] [aria-selected="true"] {
        background-color: #2563eb !important;
        color: white !important;
    }


    /* =====================================================
       KPI CARDS
    ===================================================== */

    div[data-testid="stMetric"] {
        background-color: #080d18 !important;
        border: 1px solid #172554 !important;
        border-radius: 16px !important;
        padding: 1rem !important;
        min-height: 120px;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.45);
    }

    div[data-testid="stMetric"]:hover {
        border-color: #2563eb !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    div[data-testid="stMetricDelta"] {
        color: #60a5fa !important;
    }


    /* =====================================================
       TABS
    ===================================================== */

    div[data-baseweb="tab-list"] {
        background-color: #050a14 !important;
        border: 1px solid #172554 !important;
        border-radius: 12px !important;
        padding: 5px !important;
        gap: 4px !important;
    }

    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #64748b !important;
        border-radius: 8px !important;
        font-weight: 650 !important;
    }

    button[data-baseweb="tab"]:hover {
        background-color: #0f172a !important;
        color: #93c5fd !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #172554 !important;
        color: #60a5fa !important;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #2563eb !important;
    }


    /* =====================================================
       PLOTLY CHART CONTAINERS
    ===================================================== */

    div[data-testid="stPlotlyChart"] {
        background-color: #080d18 !important;
        border: 1px solid #172554 !important;
        border-radius: 16px !important;
        padding: 0.4rem !important;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.35);
    }


    /* =====================================================
       EXPANDERS
    ===================================================== */

    div[data-testid="stExpander"] {
        background-color: #080d18 !important;
        border: 1px solid #172554 !important;
        border-radius: 14px !important;
    }

    div[data-testid="stExpander"] summary {
        background-color: #080d18 !important;
        color: #dbeafe !important;
    }


    /* =====================================================
       DATAFRAME
    ===================================================== */

    div[data-testid="stDataFrame"] {
        background-color: #080d18 !important;
        border: 1px solid #172554 !important;
        border-radius: 12px !important;
        overflow: hidden;
    }


    /* =====================================================
       BUTTONS
    ===================================================== */

    .stButton > button {
        background-color: #1d4ed8 !important;
        color: white !important;
        border: 1px solid #2563eb !important;
        border-radius: 9px !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        background-color: #2563eb !important;
        border-color: #60a5fa !important;
    }


    /* =====================================================
       INFO / SUCCESS / WARNING BOXES
    ===================================================== */

    div[data-testid="stAlert"] {
        background-color: #080d18 !important;
        border: 1px solid #1e3a8a !important;
        color: #dbeafe !important;
        border-radius: 12px !important;
    }


    /* =====================================================
       SELECTBOX / OTHER WIDGETS
    ===================================================== */

    div[data-baseweb="select"] > div {
        background-color: #0a1020 !important;
        border-color: #1e3a8a !important;
        color: #f8fafc !important;
    }


    /* =====================================================
       DIVIDERS
    ===================================================== */

    hr {
        border-color: #172554 !important;
    }


    /* =====================================================
       CAPTIONS
    ===================================================== */

    .stCaption {
        color: #64748b !important;
    }


    /* =====================================================
       SCROLLBAR
    ===================================================== */

    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #030712;
    }

    ::-webkit-scrollbar-thumb {
        background: #1e3a8a;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #2563eb;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# LOAD DATA
# =========================================================

raw_df = load_data()
df = process_data(raw_df)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🤖 AI Dashboard")

st.sidebar.caption(
    "Intelligent E-commerce Analytics"
)

st.sidebar.divider()

st.sidebar.subheader("🎛️ Controls")

st.sidebar.write(
    "Use the controls below to analyze business performance."
)


# =========================================================
# DATE FILTER
# =========================================================

min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "📅 Analysis Period",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)


if isinstance(selected_dates, tuple):

    if len(selected_dates) == 2:
        start_date = selected_dates[0]
        end_date = selected_dates[1]

    else:
        start_date = selected_dates[0]
        end_date = selected_dates[0]

else:

    start_date = selected_dates
    end_date = selected_dates


# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df[
    (df["date"].dt.date >= start_date)
    & (df["date"].dt.date <= end_date)
].copy()


# =========================================================
# SIDEBAR STATUS
# =========================================================

st.sidebar.divider()

st.sidebar.subheader("📌 Dataset Status")

st.sidebar.metric(
    "Days Analyzed",
    len(filtered_df),
)

st.sidebar.caption(
    f"{min_date} → {max_date}"
)

st.sidebar.caption(
    "E-commerce analytics dataset"
)


# =========================================================
# KPI CALCULATIONS
# =========================================================

kpis = calculate_kpis(filtered_df)

changes = calculate_period_changes(filtered_df)


# =========================================================
# MAIN HEADER
# =========================================================

st.title("🤖 AI Business Intelligence Dashboard")

st.subheader(
    "Intelligent E-commerce Analytics"
)

st.caption(
    f"Analysis period: {start_date} → {end_date} "
    f"• {len(filtered_df)} days analyzed"
)

st.divider()


# =========================================================
# TABS
# =========================================================

dashboard_tab, revenue_tab, sales_tab, marketing_tab, insights_tab, forecast_tab, data_tab = st.tabs(
    [
        "🏠 Dashboard",
        "💰 Revenue",
        "🛒 Sales",
        "📢 Marketing",
        "🤖 AI Insights",
        "🔮 Forecast",
        "📋 Data",
    ]
)


# =========================================================
# DASHBOARD TAB
# =========================================================

with dashboard_tab:

    st.header("Executive Overview")

    st.caption(
        "High-level indicators of business performance."
    )

    row1 = st.columns(4)

    with row1[0]:

        revenue_change = changes.get(
            "revenue_change",
            0
        )

        st.metric(
            "Total Revenue",
            f"${kpis['total_revenue']:,.2f}",
            f"{revenue_change:.2f}%",
        )

    with row1[1]:

        orders_change = changes.get(
            "orders_change",
            0
        )

        st.metric(
            "Total Orders",
            f"{kpis['total_orders']:,}",
            f"{orders_change:.2f}%",
        )

    with row1[2]:

        customers_change = changes.get(
            "customers_change",
            0
        )

        st.metric(
            "Total Customers",
            f"{kpis['total_customers']:,}",
            f"{customers_change:.2f}%",
        )

    with row1[3]:

        st.metric(
            "Conversion Rate",
            f"{kpis['conversion_rate']:.2f}%",
        )

    st.write("")

    row2 = st.columns(3)

    with row2[0]:

        st.metric(
            "Average Order Value",
            f"${kpis['average_order_value']:,.2f}",
        )

    with row2[1]:

        traffic_change = changes.get(
            "traffic_change",
            0
        )

        st.metric(
            "Website Traffic",
            f"{kpis['website_traffic']:,}",
            f"{traffic_change:.2f}%",
        )

    with row2[2]:

        marketing_change = changes.get(
            "marketing_spend_change",
            0
        )

        st.metric(
            "Marketing Spend",
            f"${kpis['marketing_spend']:,.2f}",
            f"{marketing_change:.2f}%",
        )

    st.divider()

    st.header("Revenue Trend")

    revenue_chart = px.line(
        filtered_df,
        x="date",
        y="revenue",
        markers=True,
    )

    revenue_chart.update_traces(
        line=dict(
            width=3,
            color="#3b82f6",
        ),
        marker=dict(
            color="#60a5fa",
        ),
    )

    revenue_chart.update_layout(
        height=450,
        plot_bgcolor="#080d18",
        paper_bgcolor="#080d18",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            gridcolor="#172554",
            title=None,
        ),
        yaxis=dict(
            gridcolor="#172554",
            title="Revenue ($)",
        ),
    )

    st.plotly_chart(
        revenue_chart,
        use_container_width=True,
    )


# =========================================================
# REVENUE TAB
# =========================================================

with revenue_tab:

    st.header("💰 Revenue Analytics")

    st.caption(
        "Analyze revenue performance across the selected period."
    )

    revenue_chart = px.line(
        filtered_df,
        x="date",
        y="revenue",
        markers=True,
    )

    revenue_chart.update_traces(
        line=dict(
            width=3,
            color="#3b82f6",
        ),
        marker=dict(
            color="#60a5fa",
        ),
    )

    revenue_chart.update_layout(
        height=500,
        plot_bgcolor="#080d18",
        paper_bgcolor="#080d18",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            gridcolor="#172554"
        ),
        yaxis=dict(
            gridcolor="#172554",
            title="Revenue ($)",
        ),
    )

    st.plotly_chart(
        revenue_chart,
        use_container_width=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Revenue",
        f"${kpis['total_revenue']:,.2f}",
    )

    c2.metric(
        "Average Daily Revenue",
        f"${filtered_df['revenue'].mean():,.2f}",
    )

    c3.metric(
        "Highest Daily Revenue",
        f"${filtered_df['revenue'].max():,.2f}",
    )


# =========================================================
# SALES TAB
# =========================================================

with sales_tab:

    st.header("🛒 Sales Analytics")

    st.caption(
        "Monitor orders, traffic, customers, and conversion."
    )

    col1, col2 = st.columns(2)

    with col1:

        orders_chart = px.line(
            filtered_df,
            x="date",
            y="orders",
            markers=True,
        )

        orders_chart.update_traces(
            line=dict(
                width=2.5,
                color="#3b82f6",
            ),
            marker=dict(
                color="#60a5fa"
            ),
        )

        orders_chart.update_layout(
            height=420,
            plot_bgcolor="#080d18",
            paper_bgcolor="#080d18",
            font=dict(color="#cbd5e1"),
            xaxis=dict(
                gridcolor="#172554"
            ),
            yaxis=dict(
                gridcolor="#172554",
                title="Orders",
            ),
        )

        st.plotly_chart(
            orders_chart,
            use_container_width=True,
        )

    with col2:

        traffic_chart = px.line(
            filtered_df,
            x="date",
            y="website_traffic",
            markers=True,
        )

        traffic_chart.update_traces(
            line=dict(
                width=2.5,
                color="#2563eb",
            ),
            marker=dict(
                color="#60a5fa"
            ),
        )

        traffic_chart.update_layout(
            height=420,
            plot_bgcolor="#080d18",
            paper_bgcolor="#080d18",
            font=dict(color="#cbd5e1"),
            xaxis=dict(
                gridcolor="#172554"
            ),
            yaxis=dict(
                gridcolor="#172554",
                title="Website Traffic",
            ),
        )

        st.plotly_chart(
            traffic_chart,
            use_container_width=True,
        )

    st.header("Conversion Rate")

    conversion_chart = px.line(
        filtered_df,
        x="date",
        y="conversion_rate",
        markers=True,
    )

    conversion_chart.update_traces(
        line=dict(
            width=2.5,
            color="#38bdf8",
        ),
        marker=dict(
            color="#7dd3fc"
        ),
    )

    conversion_chart.update_layout(
        height=420,
        plot_bgcolor="#080d18",
        paper_bgcolor="#080d18",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            gridcolor="#172554"
        ),
        yaxis=dict(
            gridcolor="#172554",
            title="Conversion Rate (%)",
        ),
    )

    st.plotly_chart(
        conversion_chart,
        use_container_width=True,
    )


# =========================================================
# MARKETING TAB
# =========================================================

with marketing_tab:

    st.header("📢 Marketing Analytics")

    st.caption(
        "Monitor marketing investment and efficiency."
    )

    marketing_chart = px.bar(
        filtered_df,
        x="date",
        y="marketing_spend",
    )

    marketing_chart.update_traces(
        marker_color="#2563eb"
    )

    marketing_chart.update_layout(
        height=500,
        plot_bgcolor="#080d18",
        paper_bgcolor="#080d18",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            gridcolor="#172554"
        ),
        yaxis=dict(
            gridcolor="#172554",
            title="Marketing Spend ($)",
        ),
    )

    st.plotly_chart(
        marketing_chart,
        use_container_width=True,
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Total Marketing Spend",
            f"${kpis['marketing_spend']:,.2f}",
        )

    with c2:

        efficiency = (
            kpis["total_revenue"]
            / kpis["marketing_spend"]
            if kpis["marketing_spend"] > 0
            else 0
        )

        st.metric(
            "Revenue per Marketing $",
            f"${efficiency:.2f}",
        )


# =========================================================
# AI INSIGHTS TAB
# =========================================================

with insights_tab:

    st.header("🤖 AI Business Insights")

    st.caption(
        "Automated analysis of business performance."
    )

    st.info(
        "AI Insight Engine: analyzing the selected business data..."
    )

    revenue_change = changes.get(
        "revenue_change",
        0
    )

    orders_change = changes.get(
        "orders_change",
        0
    )

    traffic_change = changes.get(
        "traffic_change",
        0
    )

    if revenue_change > 10:

        st.success(
            f"📈 Revenue is growing strongly. "
            f"Revenue increased by {revenue_change:.2f}% "
            f"compared with the previous period."
        )

    elif revenue_change < -10:

        st.error(
            f"⚠️ Revenue declined by "
            f"{abs(revenue_change):.2f}%. "
            f"Review traffic, conversion, and marketing performance."
        )

    else:

        st.info(
            f"📊 Revenue changed by "
            f"{revenue_change:.2f}%. "
            f"Overall revenue performance is relatively stable."
        )

    if traffic_change > orders_change:

        st.warning(
            "🔎 Traffic is growing faster than orders. "
            "This may indicate an opportunity to improve website "
            "conversion performance."
        )

    else:

        st.success(
            "✅ Order growth is keeping pace with website traffic."
        )

    if kpis["conversion_rate"] >= 3:

        st.success(
            f"🎯 Conversion rate is "
            f"{kpis['conversion_rate']:.2f}%, "
            "indicating healthy visitor-to-order performance."
        )

    else:

        st.warning(
            f"⚠️ Conversion rate is "
            f"{kpis['conversion_rate']:.2f}%. "
            "Improving the customer journey could increase orders."
        )

    st.subheader("💡 Recommended Action")

    st.write(
        "Monitor revenue, traffic, conversion rate, customer growth, "
        "and marketing efficiency together. Focus on the metrics "
        "that show the strongest change during the selected period."
    )

    st.caption(
        "MVP: Insights are generated by an automated "
        "rule-based intelligence engine. No external LLM is used."
    )


# =========================================================
# FORECAST TAB
# =========================================================

with forecast_tab:

    st.header("🔮 Revenue Forecast")

    st.caption(
        "AI-powered revenue prediction based on historical "
        "e-commerce performance."
    )

    # -----------------------------------------------------
    # GENERATE FORECAST
    # -----------------------------------------------------

    historical_df, forecast_df, forecast_model = (
        create_revenue_forecast(
            filtered_df,
            forecast_days=30
        )
    )

    # -----------------------------------------------------
    # FORECAST METRICS
    # -----------------------------------------------------

    total_forecast_revenue = (
        forecast_df["predicted_revenue"].sum()
    )

    average_forecast_revenue = (
        forecast_df["predicted_revenue"].mean()
    )

    highest_forecast_revenue = (
        forecast_df["predicted_revenue"].max()
    )

    lowest_forecast_revenue = (
        forecast_df["predicted_revenue"].min()
    )

    historical_average = (
        historical_df["revenue"].mean()
    )

    # Forecast growth compared with historical average
    if historical_average != 0:

        forecast_growth = (
            (
                average_forecast_revenue
                - historical_average
            )
            / historical_average
        ) * 100

    else:

        forecast_growth = 0


    # =====================================================
    # FORECAST KPI CARDS
    # =====================================================

    st.subheader("📊 Forecast Overview")

    forecast_col1, forecast_col2, forecast_col3, forecast_col4 = (
        st.columns(4)
    )

    with forecast_col1:

        st.metric(
            "Expected 30-Day Revenue",
            f"${total_forecast_revenue:,.2f}",
        )

    with forecast_col2:

        st.metric(
            "Average Daily Forecast",
            f"${average_forecast_revenue:,.2f}",
        )

    with forecast_col3:

        st.metric(
            "Forecast Growth",
            f"{forecast_growth:+.2f}%",
        )

    with forecast_col4:

        st.metric(
            "Forecast Horizon",
            "30 Days",
        )


    st.write("")


    # =====================================================
    # HISTORICAL VS FORECAST CHART
    # =====================================================

    st.subheader("📈 Historical vs Forecast Revenue")

    historical_plot = historical_df[
        ["date", "revenue"]
    ].copy()

    historical_plot["type"] = "Historical"


    forecast_plot = forecast_df[
        ["date", "predicted_revenue"]
    ].copy()

    forecast_plot = forecast_plot.rename(
        columns={
            "predicted_revenue": "revenue"
        }
    )

    forecast_plot["type"] = "Forecast"


    combined_df = pd.concat(
        [
            historical_plot,
            forecast_plot,
        ],
        ignore_index=True,
    )


    forecast_chart = px.line(
        combined_df,
        x="date",
        y="revenue",
        color="type",
        markers=True,
    )


    forecast_chart.update_traces(
        line=dict(
            width=3
        ),
        marker=dict(
            size=5
        ),
    )


    forecast_chart.update_layout(
        height=500,

        plot_bgcolor="#080d18",

        paper_bgcolor="#080d18",

        font=dict(
            color="#cbd5e1"
        ),

        xaxis=dict(
            gridcolor="#172554",
            title=None,
        ),

        yaxis=dict(
            gridcolor="#172554",
            title="Revenue ($)",
        ),

        legend=dict(
            title=None,
            bgcolor="#080d18",
            font=dict(
                color="#cbd5e1"
            ),
        ),

        hovermode="x unified",
    )


    st.plotly_chart(
        forecast_chart,
        use_container_width=True,
    )


    # =====================================================
    # FORECAST DETAILS
    # =====================================================

    st.subheader("📌 Forecast Range")

    range_col1, range_col2 = st.columns(2)

    with range_col1:

        st.metric(
            "Highest Predicted Daily Revenue",
            f"${highest_forecast_revenue:,.2f}",
        )

    with range_col2:

        st.metric(
            "Lowest Predicted Daily Revenue",
            f"${lowest_forecast_revenue:,.2f}",
        )


    # =====================================================
    # AI FORECAST INTERPRETATION
    # =====================================================

    st.divider()

    st.subheader("🤖 AI Forecast Interpretation")


    if forecast_growth > 5:

        st.success(
            f"📈 Positive revenue trend detected. "
            f"The model forecasts average daily revenue to be "
            f"{forecast_growth:.2f}% higher than the historical "
            f"average."
        )

        st.write(
            "💡 Recommended action: maintain the current growth "
            "strategy while monitoring traffic, conversion rate, "
            "customer demand, and marketing efficiency."
        )


    elif forecast_growth < -5:

        st.warning(
            f"⚠️ Potential revenue decline detected. "
            f"The model forecasts average daily revenue to be "
            f"{abs(forecast_growth):.2f}% lower than the historical "
            f"average."
        )

        st.write(
            "💡 Recommended action: review customer acquisition, "
            "conversion performance, product demand, and "
            "marketing efficiency."
        )


    else:

        st.info(
            f"📊 Revenue is expected to remain relatively stable. "
            f"The forecast differs from the historical average "
            f"by {forecast_growth:+.2f}%."
        )

        st.write(
            "💡 Recommended action: maintain current operations "
            "and continue monitoring the major business KPIs."
        )


    # =====================================================
    # AI FORECAST SUMMARY
    # =====================================================

    st.subheader("🧠 AI Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)


    with summary_col1:

        st.markdown(
            f"""
            **Historical Average**

            ${historical_average:,.2f}

            Average daily revenue from the selected
            historical period.
            """
        )


    with summary_col2:

        st.markdown(
            f"""
            **Predicted Average**

            ${average_forecast_revenue:,.2f}

            Expected average daily revenue for the
            next 30 days.
            """
        )


    with summary_col3:

        trend_status = (
            "Positive 📈"
            if forecast_growth > 5
            else
            "Negative 📉"
            if forecast_growth < -5
            else
            "Stable 📊"
        )

        st.markdown(
            f"""
            **Predicted Trend**

            {trend_status}

            Based on the linear regression forecast.
            """
        )


    # =====================================================
    # FORECAST MODEL
    # =====================================================

    st.divider()

    st.subheader("⚙️ Forecast Model")


    model_col1, model_col2, model_col3 = st.columns(3)


    with model_col1:

        st.markdown(
            """
            **Model**

            Linear Regression
            """
        )


    with model_col2:

        st.markdown(
            f"""
            **Training Data**

            {len(historical_df)} historical records
            """
        )


    with model_col3:

        st.markdown(
            """
            **Forecast Horizon**

            30 days
            """
        )


    st.caption(
        "MVP predictive model. Forecast accuracy depends on "
        "historical data quality, data volume, and the underlying "
        "revenue patterns."
    )

# =========================================================
# DATA TAB
# =========================================================

with data_tab:

    st.header("📋 Data Explorer")

    st.caption(
        "Inspect the underlying data used by the AI dashboard."
    )

    st.write(
        f"Showing {len(filtered_df)} records "
        f"from {start_date} to {end_date}."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🤖 AI Business Intelligence Dashboard • "
    "E-commerce Intelligence MVP • "
    "Automated Data-Driven Insights"
)
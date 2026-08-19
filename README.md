
# 🤖 AI Business Intelligence Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-business-intelligence-dashboard-dq7pd8yxpbusnzkrrsvx9y.streamlit.app/)
<<<<<<< HEAD

🔗 **Live Demo:** [AI Business Intelligence Dashboard](https://ai-business-intelligence-dashboard-dq7pd8yxpbusnzkrrsvx9y.streamlit.app/)
=======
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
>>>>>>> 20e772b (docs: sync updated README)

An intelligent analytics and forecasting platform designed for small-to-medium e-commerce businesses to transform fragmented operational data into automated executive summaries, interactive visuals, and predictive demand modeling.

🔗 **Live Production App:** [Launch AI Business Intelligence Dashboard](https://ai-business-intelligence-dashboard-dq7pd8yxpbusnzkrrsvx9y.streamlit.app/)

---

## 📌 Problem Statement

Small and medium-sized business (SMB) owners and e-commerce operators frequently manage sales, marketing, and traffic data scattered across disjointed spreadsheets and platforms. Without a dedicated data analyst, extracting clear performance signals, calculating marketing efficiency (ROAS), and forecasting near-term revenue trends is time-consuming and error-prone.

---

## 💡 Solution Overview

The **AI Business Intelligence Dashboard** consolidates critical commercial KPIs into a single unified dark-mode interface. It combines dynamic date filtering, automated rule-based AI diagnostic insights, predictive linear modeling, and one-click executive PDF report generation.

---

## 🎯 Target Audience & Commercial Viability

* **Target Customers:** E-commerce store operators, digital marketing agencies, DTC brands, and small retail chains.
* **Target Markets:** USA, Canada, UK, UAE, Saudi Arabia, Qatar, Bahrain, Kuwait, Australia, and wider Europe.
* **Commercialization & Service Models:**
  * **Monthly Reporting Retainer:** $50 – $200 / month for automated tracking, forecasting, and periodic executive summaries.
  * **Turnkey Custom Deployment:** $200 – $600 one-time setup and data warehouse integration fee for bespoke client pipelines.

---

## 🚀 Key Features

* **Executive Business Dashboard:** Live KPI cards tracking Total Revenue, Orders, Customer Counts, and Conversion Rates with period-over-period delta indicators.
* **Granular Analytical Drill-Downs:** Interactive Plotly charts for Revenue Trends, Traffic-to-Order Conversion ratios, and Marketing Spend attribution.
* **Predictive Demand Forecasting:** Time-series linear regression engine projecting expected daily and aggregate revenue over a 30-day forward horizon.
* **Automated AI Insight Engine:** Dynamic diagnostics providing plain-English performance evaluations and strategic action items.
* **Exportable PDF Reports:** Native server-side compilation (`fpdf2`) generating downloadable executive summaries with one click.
* **Self-Contained Data Explorer:** Embedded table preview with full date-range slicing capabilities.

---

## 🧠 AI & Analytics Architecture

* **KPI & Period-over-Period Engine:** Automated delta calculation evaluating current vs. previous performance metrics.
* **Rule-Based Business Insight Engine:** Heuristic evaluation layer translating numerical variations into actionable executive takeaways.
* **30-Day Revenue Forecasting:** Supervised machine learning (Linear Regression) modeling trendlines and forward-looking demand.
* **Marketing Efficiency Analysis:** Automated Return on Ad Spend (ROAS) and revenue-per-marketing-dollar tracking.

> **Note on AI Engine:** The current MVP utilizes an internal automated rule-based diagnostic intelligence engine for deterministic business insights without requiring third-party LLM API keys.

---

## 🛠️ Technology Stack

* **Core Language:** Python 3.9+
* **Web & UI Framework:** Streamlit
* **Data Processing & Manipulation:** Pandas, NumPy
* **Interactive Visualizations:** Plotly Express
* **Machine Learning & Modeling:** Scikit-learn
* **PDF Report Generation:** FPDF2
* **Cloud Hosting:** Streamlit Community Cloud

---

## 📂 Project Structure

```text
AI-Business-Intelligence-Dashboard/
│
├── .streamlit/
│   └── config.toml             # Theme styling and visual configuration
│
├── data/
│   └── ecommerce_data.csv      # E-commerce transaction and operational dataset
│
├── src/
│   ├── __init__.py
│   ├── ai_insights.py          # Rule-based diagnostic heuristics
│   ├── data_processing.py      # KPI calculations and data transformations
│   ├── forecasting.py          # Linear Regression predictive model
│   └── generate_data.py        # Synthetic data generation pipeline
│
<<<<<<< HEAD
├── screenshots/
│
├── assets/
│
└── src/
    ├── ai_insights.py
    ├── data_processing.py
    ├── forecasting.py
    └── generate_data.py
▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run the application
python -m streamlit run app.py

The dashboard will open in your browser.

🔮 Forecasting

The forecasting module uses Linear Regression to estimate revenue for the next 30 days based on historical revenue patterns.

The forecast section provides:

Expected 30-day revenue
Average daily forecast
Highest forecast value
Lowest forecast value
Historical vs forecast visualization
Automated forecast interpretation
Forecast model information
📊 Dashboard Sections
🏠 Dashboard

Provides an executive overview of key business KPIs and revenue trends.

💰 Revenue Analytics

Analyzes revenue performance, average daily revenue, and highest daily revenue.

🛒 Sales Analytics

Tracks orders, website traffic, and conversion rate.

📢 Marketing Analytics

Analyzes marketing spending and revenue generated per marketing dollar.

🤖 AI Business Insights

Generates automated business recommendations based on revenue, traffic, orders, and conversion performance.

🔮 Forecast

Uses Linear Regression to predict revenue for the next 30 days.

📋 Data Explorer

Allows users to inspect the underlying e-commerce dataset.

⚠️ Disclaimer

This project is an MVP business intelligence and predictive analytics system.

The dataset is used for demonstration purposes, and forecast accuracy depends on the quality, quantity, and historical patterns of the available data.

The forecasting model should not be considered a guarantee of future business performance.

👩‍💻 Author

Filza Rehman

AI / Machine Learning Student
=======
├── app.py                      # Main Streamlit dashboard application
├── requirements.txt            # Application dependencies
└── README.md                   # Complete system documentation

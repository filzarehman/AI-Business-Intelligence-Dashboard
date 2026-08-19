# 🤖 AI Business Intelligence Dashboard


An AI-powered e-commerce analytics dashboard built with **Python, Streamlit, Pandas, Plotly, and Scikit-learn**.


## 📌 Overview


This project provides an interactive business intelligence platform for analyzing e-commerce performance.


The dashboard combines historical data analysis, KPI monitoring, automated rule-based business insights, and predictive revenue forecasting.


## 🚀 Features


- 📊 Executive business dashboard
- 💰 Revenue analytics
- 🛒 Sales analytics
- 📢 Marketing analytics
- 🤖 Automated business insights
- 🔮 30-day revenue forecasting
- 📋 Interactive data explorer
- 📅 Custom date-range analysis
- 📈 Interactive Plotly visualizations
- 🌑 Professional black and blue UI
- 📌 KPI and period-over-period analysis


## 🧠 AI & Analytics


The project includes:


- KPI analysis
- Period-over-period performance comparison
- Rule-based business insight generation
- Linear Regression revenue forecasting
- Historical vs forecast revenue analysis
- Automated recommendations based on business metrics


> The current MVP uses a rule-based intelligence engine for business insights and does not use an external LLM API.


## 🛠️ Technologies


- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- ReportLab


## 📂 Project Structure


```text
Ai Business Intelligence Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── ecommerce_data.csv
│
├── reports/
│
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

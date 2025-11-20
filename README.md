🚀 AI-Powered Sales Intelligence Dashboard:
End-to-End Data Analytics + Visualization + AI Insights + Forecasting

📌 Project Overview
1.This project delivers a complete Sales Intelligence System using:
2.Python for cleaning & EDA
3.Tableau for interactive dashboarding
4.AI (Julius AI) for auto-generated insights
5.Prophet for future sales forecasting
6.The goal is to help businesses understand performance across categories, regions, segments, and predict future trends.

🧩 Tech Stack
🐍 Python (Pandas, NumPy, Prophet)
📊 Tableau (or Power BI)
🤖 AI APIs: OpenAI / Gemini
🗄 CSV Dataset: Sample Superstore
🔧 GitHub Version Control

📁 Project Structure:
  📂 data/
  📄 SampleSuperstore_cleaned.csv (final cleaned dataset)
📂 notebooks/
  📘 01_Data_Cleaning.ipynb
  📘 02_EDA_and_Grouping.ipynb
  📘 03_Sales_Forecasting_Prophet.ipynb
📂 dashboard/
  📊 AI_Sales_Dashboard.twbx (Tableau packaged workbook)
  🖼 Dashboard.png (preview image for GitHub)
📂 ai/
  🤖 Sales_AI_Insights.py (AI insights script)
📂 scripts/
  🧹 data_cleaning.py
 🔍 eda_analysis.py
 🔮 forecast_sales.py
📄 README.md

🧹 1. Data Cleaning (Python)

Performed complete preprocessing using Pandas:
✔ Handled missing values
✔ Removed duplicates
✔ Fixed improper data types
✔ Converted Postal Code → String
✔ Converted Order/Ship Dates → datetime
✔ Checked & handled outliers
✔ Exported cleaned dataset for dashboarding

📊 2. Exploratory Data Analysis (EDA)
Generated insights using Python:
Sales & profit distribution
Category-wise statistics
Region-wise performance
Segment-based patterns
Discount vs Profit analysis
Trend exploration

📈 3. Interactive Dashboard (Tableau)
Dashboard contains:
Category-Level Insights
Sales by Category
Profit by Category
Sub-Category Insights
Sales by Sub-Category
Profit by Sub-Category
Regional & Segment Insights
Sales by Region
Profit by Region
Sales by Segment
AI Insights Summary (Text Box)
👉 LIVE Dashboard Link: https://public.tableau.com/views/AIpoweredSalesIntelligenceDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

🤖 4. AI-Generated Insights
Used ChatGPT/Gemini to create:
Top insights summary
Best & worst performing categories
Key reasons for profit/loss patterns
Customer behavior findings
Region-based improvements
5–7 recommendations for management

Example Prompt Used:

You are a business analyst. Based on this sales dataset, 
generate 10 insights, category performance analysis, 
regional insights, loss-causing areas, and 5 business recommendations.

🔮 5. Sales Forecasting (Prophet)
Used Prophet to forecast future 30 days of sales.
Simple Forecasting Code:

import pandas as pd
from prophet import Prophet

df = pd.read_csv("SampleSuperstore_cleaned.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

daily = df.groupby("Order Date")["Sales"].sum().reset_index()
daily = daily.rename(columns={"Order Date": "ds", "Sales": "y"})

model = Prophet()
model.fit(daily)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

print(forecast[["ds", "yhat"]].tail())

Outputs:
ds → Date
yhat → Predicted Sales
This helps businesses plan inventory, marketing, and budgeting.
🧠 What This Project Demonstrates
Data Cleaning skills
Exploratory Data Analysis
Dashboard Development (Tableau)
AI-integrated insights
Forecasting using ML models
Business decision support
Practical, real-world analytics workflow
⚡ How to Run This Project
 Install Python dependencies


pip install pandas prophet matplotlib numpy
 Run Forecasting Script


python Sales_Forecasting_Prophet.py
 Open Tableau Dashboard
Open dashboard/Tableau_Dashboard.twbx
Run AI insights
Use ChatGPT/Gemini with dataset sample.


🏁 Conclusion
This project combines Analytics + Visualization + AI + Forecasting
to produce a complete business intelligence solution.
Perfect for:
Data Analyst Roles
BI Analyst Roles
AI Analyst Roles
Junior Data Scientist Roles


📧 Contact
Akash Yadav
Aspiring Data Analyst
Tools: Python • SQL • Tableau • Power BI • AI Tools

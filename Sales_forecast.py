import pandas as pd
from prophet import Prophet

df = pd.read_csv("archive/Sample - Superstore.csv", encoding='latin-1')

# Converted “Order Date” to datetime format.
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Prophet needs two columns:

# ds → date

# y → value to predict (sales)
# So I grouped sales by day.

daily = df.groupby("Order Date")["Sales"].sum().reset_index()
daily = daily.rename(columns={"Order Date": "ds", "Sales": "y"})

model = Prophet()
model.fit(daily)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

print(forecast[["ds", "yhat"]].tail())

# note

# “I built a simple time-series forecasting model using Prophet, where I cleaned the sales data, prepared day-wise totals, trained the model, and forecasted the next 30 days of sales.”

# “Prophet automatically handles seasonality, trends, and missing values.
# It’s easy to use and works well for business forecasts.”


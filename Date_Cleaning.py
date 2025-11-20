# # step -0
# from sqlite3 import Date
import pandas as pd

df = pd.read_csv("archive/Sample - Superstore.csv", encoding='latin-1')
print(df.head())

# # step - 01 : shows columns

print(df.columns)

# # step - 02 : Handling Date Columns
# # : Convert data columns into proper date format 
# # Reason --> order date and ship date are currently in string , so string --> datetime

df["Order Date"] =pd.to_datetime(df["Order Date"])
df["Ship Date"] =pd.to_datetime(df["Ship Date"])

df[["Order Date","Ship Date"]].dtypes

# step - 03 : Handling missing values
print(df.isnull().sum().sort_values(ascending=False))

# step - 04 : Checking Duplicates# Check duplicates
print("Duplicate rows:", df.duplicated().sum())

# step - 05 : clean the datatypes
print(df.dtypes)

# issues: postal code : is int64( obejct(string ) )

df["Postal Code"] = df["Postal Code"].astype(str)
print(df["Postal Code"].dtype)

# step - 06: Basic Data Cleaning Summary
print("\n---- FINAL CLEANED DATA SUMMARY ----")
print(df.info())


# STEP 07: Simple Outlier Check (IQR)

numeric_cols = ["Sales", "Quantity", "Discount", "Profit"]

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(col, " → Outliers:", outliers.shape[0])
    
# Step - 08 : Export the Cleaned Dataset
df.to_csv("archive/Sample - Superstore.csv",index=False)
print("File saved sucessfully")

import os
print(os.listdir())

print(os.listdir("archive"))

import os
print(os.path.abspath("archive/Sample - Superstore.csv"))

import os

print("Root Folder:", os.listdir())
print("Archive Folder:", os.listdir("archive"))


import pandas as pd

clean_df = pd.read_csv("archive/Sample - Superstore.csv")

print(clean_df.head())
print(clean_df.info())

# Step-10: EDA(Exploratory Data Analysis) --> Process of exploring the dataset into to undertstand patterns,detect errors, find relationship 
# and summarize key insights before doing visluization or modelling 

# 📌 Part 1 — Basic Sales Insights
print("------ BASIC SALES METRICS ------")
# Total Sales
print("Total Sales =", df["Sales"].sum())
# Total Profit
print("Total Profit =", df["Profit"].sum())
# Total Quantity Sold
print("Total Quantity Sold =", df["Quantity"].sum())
# Average Discount
print("Average Discount =", df["Discount"].mean())

#  NOte:
# grouping the rows based on the columns and then calculate something

# 📌 Part 2 — Category Level Insights
print("\n------ PART 2 : CATEGORY LEVEL INSIGHTS ------")


# 1. Sales by Category
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

# 2. Profit by Category
print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum())

# 3. Sales by Sub-Category
print("\nSales by Sub-Category:")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))

# 4. Profit by Sub-Category
print("\nProfit by Sub-Category:")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))

# 📌 Part 3 — Customer Level Insights

# print("\n------ PART 3 : Customer Level Insights ------")

#  Insights 01 : Top 10 customers by Sales
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(top_customers)
# --> Who brings the the most money to the customer

#  Insights 02: Average Profit per Customer :
profit_per_customer = df.groupby("Customer Name")["Profit"].mean().sort_values(ascending=False).head(10)
print(profit_per_customer)
# --> whhich customer are the most preticible profitabele


# Insights 03: Total Orders per Customer
order_per_customer = df.groupby("Customer Name")["Profit"].count().sort_values(ascending=False).head(10)
print(order_per_customer)

# --> who orders the most frequent 


#  Insights 04: Customer Insights
segment_sales = df.groupby("Segment")["Sales"].sum()
print(segment_sales)

segment_profit = df.groupby("Segment")["Profit"].sum()
print(segment_profit)

# --> whoch segement performs the best :: whether it is coperate , home office, consumer

# 📌 Part 4 — Region/ Geographical Insights :

print("\n------ PART 4 :Region/ Geographical Insights : ------")

#  Insight 1: Sales by Region

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

# --> Which region brings the highest revenue.

# Insight 2: Profit by Region

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print(region_profit)

# Shows which region is losing money or giving profit.

#  Insight 3: Sales by State

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
print(state_sales)

# --> Top 10 best performing states.

#  Insight 4: Profit by State

state_profit = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(10)
print(state_profit)
#  Shows which states are profitable.

#  Insight 5: Loss-Making States
# Sometimes profit is negative.

loss_states = df.groupby("State")["Profit"].sum()
loss_states = loss_states[loss_states < 0]
print(loss_states)

# Which states are causing losses.

# Insight 6: Sales by City

city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)
print(city_sales)

# --> top 10 city via sales 

# 📌 Part 5 — Product level  Insights :
print("\n------ PART 5 :Product level  Insights : ------")


# Insight 1: Sales by products :
print("Top 10 Products by Sales:\n")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

# Insight 2: profit by sales :
print("\nTop 10 Products by Profit:\n")
print(df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10))

# Insight 3: loss :
print("\nProducts with Negative Profit:\n")
prod_loss = df.groupby("Product Name")["Profit"].sum()
print(prod_loss[prod_loss < 0].sort_values().head(10))


print(df.info())


print(df.head())

import pandas as pd
from prophet import Prophet

df = pd.read_csv("archive/Sample - Superstore.csv", encoding='latin-1')
df["Order Date"] = pd.to_datetime(df["Order Date"])

daily = df.groupby("Order Date")["Sales"].sum().reset_index()
daily = daily.rename(columns={"Order Date": "ds", "Sales": "y"})

model = Prophet()
model.fit(daily)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

print(forecast[["ds", "yhat"]].tail())

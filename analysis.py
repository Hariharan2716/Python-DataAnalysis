import pandas as pd

# Load data from csv file
df = pd.read_csv("sales_data.csv")

# Step 1 it is to clean the data so
# Convert date column
# df['Order_Data'] = pd.to_datetime(df['Order_Date'])
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# Removing the missing values
# df = df.dropna()
df = df.dropna(subset=['Order_Date'])
# Remove missing values. See the User Guide <missing_data> for more on which values are considered missing, and how to work with missing data.

# Extract month name
print(df.dtypes)
df['Month'] = df['Order_Date'].dt.month_name()
# Analysis
# Sales by Product
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)

# Monthly Sales Trend, Region-wise Sales
monthly_sales = df.groupby('Month')['Sales'].sum()
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
top_orders = df.sort_values(by='Sales', ascending=False).head(3)

# OUTPUT

print("\n=== Sales by Product ===")
print(product_sales)

print("\n=== Monthly Sales ===")
print(monthly_sales)

print("\n=== Region Sales ===")
print(region_sales)

print("\n=== Top 3 High Value Orders ===")
print(top_orders)

# Average order value per product
avg_sales = df.groupby('Product')['Sales'].mean()
print("\n=== Average Sales per Product ===")
print(avg_sales)
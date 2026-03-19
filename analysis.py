import pandas as pd

# Load data from csv file
df = pd.read_csv("sales_data.csv")

# Step 1 it is to clean the data so
# Convert date column
df['Order_Data'] = pd.to_datetime(df['Order_Date'])

# Removing the missing values
df = df.dropna()
# Remove missing values. See the User Guide <missing_data> for more on which values are considered missing, and how to work with missing data.

import pandas as pd
import numpy as np

# -----------------------------
# 1. Sample Data Lists
# -----------------------------
customers = ["CUST001", "CUST002", "CUST003", "CUST004", "CUST005"]
customer_names = ["Amit Sharma", "Priya Singh", "John Doe", "Sara Khan", "Michael Lee"]
cities = ["New York", "Chicago", "Houston", "San Francisco", "Boston"]

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor"]
categories = ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]
unit_prices = [900, 600, 80, 40, 200]

# -----------------------------
# 2. Generate Dataset
# -----------------------------
np.random.seed(42)

rows = 100

data = {
    "Order_ID": [f"ORD{1000+i}" for i in range(rows)],
    "Customer_ID": np.random.choice(customers, rows),
    "Customer_Name": np.random.choice(customer_names, rows),
    "City": np.random.choice(cities, rows),
    "Product": np.random.choice(products, rows),
    "Category": np.random.choice(categories, rows),
    "Quantity": np.random.randint(1, 10, rows),
    "Unit_Price": np.random.choice(unit_prices, rows),
    "Discount": np.round(np.random.uniform(0, 0.30, rows), 2),
    "Order_Date": pd.date_range(start="2023-01-01", periods=rows, freq="D")
}

df = pd.DataFrame(data)

# -----------------------------
# 3. Calculate Total Sales
# -----------------------------
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])

# -----------------------------
# 4. Show Output
# -----------------------------
print(df.head())
print(df.describe())
print(df)
print(df.info())
print(df.columns)
print(df.groupby('Quantity')['Total_Sales'].sum())
"""
Pandas Basics — Phase 0 / Python for ML
========================================
Run: python pandas_basics.py
"""

import pandas as pd
import numpy as np

print("=" * 50)
print("SECTION 1: Creating a DataFrame")
print("=" * 50)

df = pd.DataFrame({
    "size"     : [600, 800, 1000, 1200, 1500],
    "price"    : [150, 200,  250,  300,  375],
    "bedrooms" : [1, 2, 2, 3, 3],
    "garage"   : [0, 0, 1, 1, 1]
})

print(df)
print("\nShape  :", df.shape)       # (rows, cols)
print("Columns:", df.columns.tolist())
print("dtypes :\n", df.dtypes)

# ── PRACTICE: Add a "garden" column (all 0s for now) using df["garden"] = 0 ──


print("\n" + "=" * 50)
print("SECTION 2: Exploring Data")
print("=" * 50)

print("First 3 rows:\n", df.head(3))
print("\nDescribe:\n", df.describe())
print("\nNull counts:\n", df.isnull().sum())

# Access single column
print("\nPrices:", df["price"].values)

# Access single row by index
print("Row 0 :", df.iloc[0].to_dict())

# ── PRACTICE: Print only the "size" and "price" columns together ──


print("\n" + "=" * 50)
print("SECTION 3: Filtering Rows")
print("=" * 50)

# Single condition
print("Bedrooms > 1:\n", df[df["bedrooms"] > 1])

# Multiple conditions
print("\nLarge houses with garage:\n",
      df[(df["size"] >= 1000) & (df["garage"] == 1)])

# ── PRACTICE: Filter houses with price < 250 ──


print("\n" + "=" * 50)
print("SECTION 4: Derived Columns & Transformations")
print("=" * 50)

df["price_per_sqft"] = (df["price"] / df["size"] * 1000).round(2)
df["is_large"]       = df["size"] >= 1000    # Boolean column

print(df)

# Apply a function to a column
df["price_log"] = df["price"].apply(lambda x: round(np.log(x), 3))
print("\nWith log price:\n", df[["price", "price_log"]])

# ── PRACTICE: Add a column "total_rooms" = bedrooms + garage ──


print("\n" + "=" * 50)
print("SECTION 5: GroupBy & Aggregation")
print("=" * 50)

# Average price per bedroom count
grouped = df.groupby("bedrooms")["price"].mean()
print("Avg price by bedrooms:\n", grouped)

# Multiple aggregations
summary = df.groupby("bedrooms").agg(
    avg_price=("price", "mean"),
    avg_size =("size",  "mean"),
    count    =("price", "count")
)
print("\nSummary by bedrooms:\n", summary)

# ── PRACTICE: Group by "garage" and find the average price ──


print("\n" + "=" * 50)
print("SECTION 6: Extracting NumPy Arrays for Models")
print("=" * 50)

# In ML: Pandas for prep, NumPy arrays fed to the model
X = df[["size", "bedrooms"]].values   # numpy array
y = df["price"].values

print(f"Feature matrix X (shape {X.shape}):\n{X}")
print(f"Target vector y (shape {y.shape}): {y}")

# ── PRACTICE: Add "garage" as a third feature in X ──

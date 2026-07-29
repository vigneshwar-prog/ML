"""
Module 0.1 — Python for ML: NumPy, Pandas, Matplotlib
======================================================
Phase  : 0 — Prerequisites
Topic  : Core Python libraries for ML
Run    : python module_0_1_numpy_pandas_matplotlib.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("SECTION 1: NumPy Basics")
print("=" * 50)

# Sample data — house sizes (sq ft) and prices ($1000s)
sizes  = np.array([600, 800, 1000, 1200, 1500])
prices = np.array([150, 200,  250,  300,  375])

print(f"Sizes  : {sizes}")
print(f"Prices : {prices}")
print(f"Mean size    : {np.mean(sizes)}")
print(f"Std deviation: {np.std(sizes):.2f}")
print(f"Dot product  : {np.dot(sizes, prices)}")

# Vectorized normalization — no loops needed
normalized = (sizes - np.mean(sizes)) / np.std(sizes)
print(f"Normalized sizes: {normalized.round(2)}")

# ── PRACTICE: Try changing the sizes array and re-run ──


print("\n" + "=" * 50)
print("SECTION 2: Pandas Basics")
print("=" * 50)

df = pd.DataFrame({
    "size"     : sizes,
    "price"    : prices,
    "bedrooms" : [1, 2, 2, 3, 3]
})

print("\nDataFrame:\n", df)
print("\nDescribe:\n", df.describe())
print("\nFilter (bedrooms > 1):\n", df[df["bedrooms"] > 1])

# Add a derived column
df["price_per_sqft"] = (df["price"] / df["size"] * 1000).round(2)
print("\nWith price_per_sqft:\n", df)

# ── PRACTICE: Try adding a "garage" column (0 or 1) and filter by it ──


print("\n" + "=" * 50)
print("SECTION 3: Matplotlib — Scatter Plot")
print("=" * 50)

plt.figure(figsize=(7, 4))
plt.scatter(df["size"], df["price"], color="steelblue", s=100, zorder=3)

# Annotate each point with its bedroom count
for _, row in df.iterrows():
    plt.annotate(
        f"{int(row['bedrooms'])}BR",
        (row["size"], row["price"]),
        textcoords="offset points",
        xytext=(6, 4),
        fontsize=8,
        color="gray"
    )

plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("House Size vs Price")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plot_0_1_scatter.png", dpi=120)
print("Plot saved to plot_0_1_scatter.png")
plt.show()

# ── PRACTICE: Try plotting size vs price_per_sqft instead ──


print("\n" + "=" * 50)
print("SECTION 4: Putting It Together — Mini Pipeline")
print("=" * 50)

# Step 1: Load data (simulated from DataFrame)
X = df[["size", "bedrooms"]].values   # NumPy array — model input
y = df["price"].values                 # NumPy array — target

print(f"Feature matrix X (shape {X.shape}):\n{X}")
print(f"Target vector y (shape {y.shape}):\n{y}")

# Step 2: Normalize features (zero mean, unit variance)
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
print(f"\nNormalized X:\n{X_norm.round(3)}")

# ── PRACTICE: What does axis=0 mean? Try axis=1 and observe the difference ──

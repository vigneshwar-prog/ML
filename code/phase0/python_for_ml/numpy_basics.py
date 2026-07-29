"""
NumPy Basics — Phase 0 / Python for ML
=======================================
Run: python numpy_basics.py
"""

import numpy as np

# %%
print("=" * 50)
print("SECTION 1: Creating Arrays")
print("=" * 50)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("a:", a)
print("b:", b)
print("dtype:", a.dtype)
print("shape:", a.shape)

# Useful constructors
print("\nzeros(5)  :", np.zeros(5))
print("ones(5)   :", np.ones(5))
print("arange    :", np.arange(0, 10, 2))   # 0,2,4,6,8
print("linspace  :", np.linspace(0, 1, 5))  # 5 evenly spaced points

# ── PRACTICE: Create an array of 10 values from 0 to 100 using linspace ──
print("linspace  :", np.linspace(0, 100, 10))  # 10 evenly spaced points from 0 to 100

# %%
print("\n" + "=" * 50)
print("SECTION 2: Vectorized Math (no loops)")
print("=" * 50)

print("a + b  :", a + b)
print("a * 2  :", a * 2)
print("a ** 2 :", a ** 2)
print("sqrt(a):", np.sqrt(a).round(3))

# ── PRACTICE: Compute a + b, a - b, a * b without any loop ──
print("a - b  :", a - b)
print("a * b  :", a * b)
print("a / b  :", a / b)

# %%
print("\n" + "=" * 50)
print("SECTION 3: Aggregations")
print("=" * 50)

data = np.array([600, 800, 1000, 1200, 1500])  # house sizes

print("Mean      :", np.mean(data))
print("Median    :", np.median(data))
print("Std Dev   :", np.std(data).round(2))
print("Variance  :", np.var(data))
print("Min / Max :", np.min(data), "/", np.max(data))
print("Sum       :", np.sum(data))

# ── PRACTICE: Find the index of the minimum and maximum value (hint: argmin/argmax) ──
print("Index of Min:", np.argmin(data))
print("Index of Max:", np.argmax(data))


# %%
print("\n" + "=" * 50)
print("SECTION 4: Dot Product & Matrix Ops")
print("=" * 50)

# Dot product — used in EVERY linear model: y = w · x
weights = np.array([0.5, 0.3, 0.2])
features = np.array([1.0, 2.0, 3.0])
prediction = np.dot(weights, features)
print(f"w · x = {prediction}")   # 0.5*1 + 0.3*2 + 0.2*3 = 1.7

# 2D matrix multiply
W = np.array([[1, 2], [3, 4]])
X = np.array([[5, 6], [7, 8]])
print("W @ X =\n", W @ X)        # matrix multiplication (same as np.matmul)

# ── PRACTICE: Create a 3x3 identity matrix using np.eye(3) ──
W = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("W @ X =\n", W @ X)        # matrix multiplication (same as np.matmul)


# %%
print("\n" + "=" * 50)
print("SECTION 5: Normalization (Feature Scaling)")
print("=" * 50)

# ML models train better when features are on the same scale
raw = np.array([600, 800, 1000, 1200, 1500], dtype=float)

# Min-Max scaling → [0, 1]
min_max = (raw - raw.min()) / (raw.max() - raw.min())
print("Min-Max scaled:", min_max.round(3))

# Z-score standardization → mean=0, std=1
z_score = (raw - raw.mean()) / raw.std()
print("Z-score scaled:", z_score.round(3))

# ── PRACTICE: Apply z-score normalization to np.array([10, 20, 30, 40, 50]) ──

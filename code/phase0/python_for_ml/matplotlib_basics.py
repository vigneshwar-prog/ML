"""
Matplotlib Basics — Phase 0 / Python for ML
=============================================
Run: python matplotlib_basics.py
Plots are saved as PNG files in the same folder.
"""

import numpy as np
import matplotlib.pyplot as plt

sizes  = np.array([600, 800, 1000, 1200, 1500])
prices = np.array([150, 200,  250,  300,  375])
labels = ["1BR", "2BR", "2BR", "3BR", "3BR"]

print("=" * 50)
print("SECTION 1: Scatter Plot")
print("=" * 50)

plt.figure(figsize=(7, 4))
plt.scatter(sizes, prices, color="steelblue", s=100, zorder=3)

for i, label in enumerate(labels):
    plt.annotate(label, (sizes[i], prices[i]),
                 textcoords="offset points", xytext=(6, 4), fontsize=8, color="gray")

plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("House Size vs Price")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter_size_vs_price.png", dpi=120)
plt.close()
print("Saved: scatter_size_vs_price.png")

# ── PRACTICE: Change the color to "tomato" and marker size to 200 ──


print("\n" + "=" * 50)
print("SECTION 2: Line Plot (Loss Curve)")
print("=" * 50)

# Simulate a training loss curve
epochs = np.arange(1, 21)
loss   = 10 / epochs + np.random.uniform(-0.1, 0.1, len(epochs))  # noisy decay

plt.figure(figsize=(7, 4))
plt.plot(epochs, loss, marker="o", color="coral", linewidth=2, markersize=5)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("line_loss_curve.png", dpi=120)
plt.close()
print("Saved: line_loss_curve.png")

# ── PRACTICE: Plot both a training loss and a validation loss on the same chart ──


print("\n" + "=" * 50)
print("SECTION 3: Histogram — Distribution of Values")
print("=" * 50)

np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=200)  # 200 people, mean 170cm

plt.figure(figsize=(7, 4))
plt.hist(heights, bins=20, color="mediumpurple", edgecolor="white", alpha=0.8)
plt.axvline(np.mean(heights), color="red", linestyle="--", label=f"Mean={np.mean(heights):.1f}")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.title("Distribution of Heights")
plt.legend()
plt.tight_layout()
plt.savefig("hist_heights.png", dpi=120)
plt.close()
print("Saved: hist_heights.png")

# ── PRACTICE: Change loc=170 to 160 and std=10 to 5 and observe the shift ──


print("\n" + "=" * 50)
print("SECTION 4: Bar Chart — Comparing Categories")
print("=" * 50)

algorithms = ["Linear\nRegression", "Decision\nTree", "Random\nForest", "SVM"]
accuracies = [82, 78, 91, 88]
colors = ["steelblue", "coral", "mediumseagreen", "mediumpurple"]

plt.figure(figsize=(7, 4))
bars = plt.bar(algorithms, accuracies, color=colors, edgecolor="white", width=0.5)

for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f"{acc}%", ha="center", fontsize=10)

plt.ylim(70, 100)
plt.ylabel("Accuracy (%)")
plt.title("Algorithm Comparison")
plt.tight_layout()
plt.savefig("bar_algorithm_comparison.png", dpi=120)
plt.close()
print("Saved: bar_algorithm_comparison.png")

# ── PRACTICE: Add a 5th algorithm "KNN" with accuracy 85 ──


print("\n" + "=" * 50)
print("SECTION 5: Subplots — Multiple Charts at Once")
print("=" * 50)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: scatter
axes[0].scatter(sizes, prices, color="steelblue", s=80)
axes[0].set_title("Size vs Price")
axes[0].set_xlabel("Size (sq ft)")
axes[0].set_ylabel("Price ($1000s)")
axes[0].grid(True, alpha=0.3)

# Right: bar
axes[1].bar(["600", "800", "1000", "1200", "1500"], prices, color="coral")
axes[1].set_title("Price by House Size")
axes[1].set_xlabel("Size (sq ft)")
axes[1].set_ylabel("Price ($1000s)")

plt.tight_layout()
plt.savefig("subplots_overview.png", dpi=120)
plt.close()
print("Saved: subplots_overview.png")

# ── PRACTICE: Add a third subplot with the loss curve from SECTION 2 ──

print("\nAll plots saved. Open the PNG files to view them.")

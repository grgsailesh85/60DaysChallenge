import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 1. THE DATASET (Using Pandas)
# ==========================================
# Creating a 12-month business dataset representing income and baseline expenses
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
income_curve = [50, 75, 45, 90, 110, 65, 80, 55, 40, 95, 120, 85]
expense_curve = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]

df = pd.DataFrame({
    'Month': months,
    'Income': income_curve,
    'Expenses': expense_curve
})

# ==========================================
# 2. THE VISUALIZATION SETUP
# ==========================================
fig, ax = plt.subplots(figsize=(11, 6))

# Plot standard tracking lines
ax.plot(df['Month'], df['Income'], color="darkblue", label="Monthly Income", lw=2)
ax.plot(df['Month'], df['Expenses'], color="crimson", label="Fixed Expenses Baseline", lw=2, linestyle=":")

# ==========================================
# 3. FILL_BETWEEN WITH ALL ATTRIBUTES USED
# ==========================================
ax.fill_between(
    x=df['Month'],               # Horizontal X-coordinates
    y1=df['Income'],             # Top boundary array
    y2=df['Expenses'],           # Bottom boundary array
    
    # Logic & Clipping Controls
    where=(df['Income'] > df['Expenses']),  # Conditional Mask: Only fill when profitable
    interpolate=True,            # Calculates exact geometric cross-over points
    step=None,                   # Can be 'pre', 'post', or 'mid' for step/staircase plots
    
    # Core Color & Transparency 
    facecolor="lightgreen",      # Inside fill color
    edgecolor="darkgreen",       # Border stroke color
    alpha=0.4,                   # Transparency level (0.0 transparent to 1.0 opaque)
    
    # Advanced Geometry/Styling (Passed down from PolyCollection)
    linewidth=2.5,               # Outer border thickness
    linestyle="--",              # Outer border style ('-', '--', '-.', ':', etc.)
    hatch="//",                  # Visual pattern texture inside the shape
    zorder=2,                    # Canvas layer level (higher = drawn on top)
    
    # Metadata
    label="Profitable Months Zone" # Label linked directly to the legend
)

# ==========================================
# 4. CLEANUP & PRESENTATION
# ==========================================
ax.set_title("Fully Featured fill_between Implementation Blueprint", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Timeline (2026 Fiscal Year)", fontsize=11)
ax.set_ylabel("Revenue / Costs ($ in Thousands)", fontsize=11)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper left")

# Display the final layout
plt.tight_layout()
plt.show()
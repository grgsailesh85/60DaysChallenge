import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
sns.set_style("darkgrid")
sns.set_context("notebook", font_scale = 1.0)
tips = sns.load_dataset("tips")


# Plot Histogram and KDE
plt.figure(figsize = (8,3))
sns.histplot(tips["total_bill"], kde = True)
plt.title("Histogram and KDE Plot od Total Bill")
plt.show()


# Scatter Plot with HUe and Size
plt.figure(figsize = (10, 5))
print(tips)
sns.scatterplot(
    data = tips,
    x = "total_bill",
    y = "tip",
    hue = "day",
    size = "size",
    sizes = (20, 240)
)
plt.title("Total-Bill Vs Tip (hue = Day, Size = Order Size)")
plt.show()

# Box + Swaarm Plot
plt.figure(figsize = (10, 5))
sns.boxplot(
    data = tips,
    x = "day",
    y = "total_bill"
)
sns.swarmplot(
    data = tips,
    x = "day",
    y = "total_bill",
    color = "k",
    alpha = 0.4
)
plt.title("BoxPlot with swarm overlay")
plt.show()
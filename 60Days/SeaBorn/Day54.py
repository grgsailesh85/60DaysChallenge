import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")


sns.pointplot(
    data = tips, 
    x = "day", 
    y = "total_bill", 
    hue = "sex", 
    dodge = 0.3,
    markers = ["x", "s"],
    capsize = 0.04
    
)
plt.title("Plot of averga total_bill by days")
plt.show()

corr = tips.corr(numeric_only = True)
print(corr)

x = flights.pivot_table(
    index = "date",
    columns = "month",
    values = "passengers"
)
sns.heatmap(
    x,
    fmt = ".0f",
    annot = True
)
plt.title("Heatmap of Passengers of month and year")
plt.show()
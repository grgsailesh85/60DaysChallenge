import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set_style("whitegrid")   #plt.style.use(---) => Matplotlib
sns.set_context("notebook", font_scale = 1.0)
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")
print(tips)
#----------------
#1 --> Histogram + KDE
#---------------- 
plt.figure(figsize = (8, 3))
sns.histplot(tips["total_bill"], kde = True)
plt.title("Histogram + KDE from tips -> total bill")
plt.show()
#------------------------------------
#2 --> Scatter plot with hue and size
#---------------- -------------------
plt.figure(figsize = (8, 3))
sns.scatterplot(
    data = tips, 
    x = "total_bill", 
    y = "tip",
    hue = "day",
    size = "size",
    sizes = (20, 200)
)
plt.title("Tip Vs Total_Bill")
plt.show()
#--------------------------
#3 --> Box + Swarm combined
#--------------------------
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
    alpha = 0.6
)
plt.title("Boxplot with Swarm overlay")
plt.show()
#--------------------------------------------
#4 --> Regression per smocker status (lmplot)
#--------------------------------------------
sns.lmplot(
    data = tips, 
    x = "total_bill",
    y = "tip",
    hue = "smoker",
    height = 4,
    aspect = 1.3
)
plt.title("Linear Regression By Smoker Status")
plt.show()
#--------------------------
#5 --> Correlation Heat Map
#--------------------------
corr = tips.select_dtypes(include = [np.number]).corr()
sns.heatmap(
    corr,
    annot = True,
    cmap = "coolwarm"
)
plt.title("Correlation Heat_map")
plt.show()
#--------------------------------------------------
#6 --> FaceGrid Scatter Plot by Time (lunch/Dinner)
#--------------------------------------------------
g = sns.FacetGrid(
    tips,
    col = "time",
    height = 4
)
g.map(
    sns.scatterplot,
    "total_bill",
    "tip"
)
g.add_legend()
plt.show()
#-----------------
#6 --> Violin PLot
#-----------------
plt.figure(figsize = (10, 5))
sns.violinplot(
    data = tips,
    x = "day",
    y = "total_bill",
    hue = "sex",
    split = True
)
plt.title("Violine Plot of total_bill by day and gender")
#---------------
#8 --> Pair plot
#---------------
sns.pairplot(
    iris,
    hue = "species",
    diag_kind = "hist"
)
plt.suptitle("Pairplot of Iris dataset", y = 1.02)
plt.show()
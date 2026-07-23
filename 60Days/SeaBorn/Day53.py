import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale = 1.0)
tips = sns.load_dataset("tips")
print(tips)

# Violin Plot
plt.figure(figsize = (8,5))
sns.violinplot(
    data = tips,
    x = "day",
    y = "total_bill",
    hue = "sex"
)
plt.title("Violin Plot of total_bill and sex")
plt.show()

# Count Plot
plt.figure(figsize = (7, 4))
sns.countplot(data = tips, x = "day", hue = "sex")
plt.title("Count Plot of records by day and sex")
plt.show()

# Facet Grid
g = sns.FacetGrid(tips, row = "time", col = "sex")
g.map(sns.histplot, "total_bill", bins = 10)
plt.show()

# Lmplot or regression plot
sns.lmplot(data = tips, x = "total_bill", y = "tip", )
plt.title("Linera Regression of total_bill and tip")
plt.show()
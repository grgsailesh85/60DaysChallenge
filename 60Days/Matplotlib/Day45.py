import pandas as pd
import matplotlib.pyplot as plt  # from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

data = pd.read_csv("testdataset.csv.csv")

view_count = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(view_count, likes)

plt.title("Trending YouTube Video")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()
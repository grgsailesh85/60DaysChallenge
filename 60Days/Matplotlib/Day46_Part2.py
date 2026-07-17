import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")
ages = [18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32]

plt.hist(ages, bins = 10, color = "lightgreen", edgecolor = "black")

plt.xlabel("Age Range")
plt.ylabel("Number of Students")

plt.title("Age Distribution of students")

plt.grid(True)
plt.tight_layout()
plt.show()


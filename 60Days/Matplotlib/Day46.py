import matplotlib.pyplot as plt # from matplotlib import pyplot as plt

# plt.style.use("fivethirtyeight")

department = ["Computer Science", "Electrical", "Civil", "Mechnical", "Aerospace", "BE Computer", "AI/ML", "Physic", "Econonmics"]

no_of_students = [120, 60, 90, 80, 40, 50, 30, 60, 5]

# plt.bar(
#     department, 
#     no_of_students, 
#     color = "skyblue", 
#     edgecolor = "black"
# )

# for horizontal
plt.barh(
    department, 
    no_of_students, 
    color = "skyblue", 
    edgecolor = "black"
)

for i, value in enumerate(no_of_students):
    plt.text(i, value + 1, str(value), ha = "center")

plt.xlabel("Deparments")
plt.ylabel("Number of Students")
plt.title("Number of students in each department of a college")

plt.show()
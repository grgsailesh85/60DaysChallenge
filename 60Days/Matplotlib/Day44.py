import matplotlib.pyplot as plt # from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use("fivethirtyeight")

# labels = ["JavaScript", "HTML/CSS", "SQL", "Python", "Java"]

# slices = [59219, 55466, 47544, 36443, 32917]
# explode = [0, 0, 0, 0.1, 0]

# plt.pie(
#         slices, 
#         labels = labels, 
#         explode = explode, 
#         shadow = True , 
#         autopct ="%1.1f%%",
#         startangle = 120
#     )

# plt.title("Pie Chart")
# plt.tight_layout()
# plt.show()

# Ages between to 55
ages_x = [
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55
]

py_dev_y = [
    32000, 34500, 33800, 37200, 40100, 39500, 43800, 45500, 48200, 47500,
    52800, 54600, 53900, 58400, 61200, 63800, 62500, 68300, 71500, 74200,
    73500, 78100, 81600, 80900, 85400, 88700, 91200, 90500, 94800, 98600,
    101500, 100800, 105400, 108900, 107600, 111800, 115600, 118500
]
js_dev_y = [
    30000, 32200, 31800, 35100, 37900, 38800, 41500, 44200, 46800, 45900,
    50100, 52300, 51800, 56200, 58900, 61500, 60800, 65400, 68100, 70900,
    70100, 74800, 77500, 76800, 81200, 83900, 86400, 85700, 90100, 92800,
    95400, 94700, 99200, 101800, 100600, 104500, 107900, 110800
]
dev_y = [
    34000, 36600, 35900, 39800, 42800, 42100, 46800, 49500, 52800, 51900,
    57200, 59800, 59100, 64500, 67800, 70600, 69900, 75600, 78800, 82100,
    81300, 86800, 90300, 89500, 94800, 98600, 101500, 100600, 105800, 109600,
    113400, 112700, 117500, 121800, 120900, 125600, 129800, 133500
]


plt.plot(ages_x, py_dev_y, linewidth=1 ,label = "Python")
plt.plot(ages_x, js_dev_y, linewidth=2 ,label = "JavaScript Developer")
plt.plot(ages_x, dev_y, linestyle="--", linewidth=3 , label = "Full Stack Developer")


plt.xlabel("Ages")
plt.ylabel("Meadian Salary in USD")
plt.title("Meadian Salary of Developer by Age in USD")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

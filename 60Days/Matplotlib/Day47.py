import matplotlib.pyplot as plt                      # Import Matplotlib library

# X-axis values
x = [1, 2, 3, 4, 5, 6, 7]

# First line values (Upper line)
python_salary = [25, 35, 45, 40, 55, 60, 70]

# Second line values (Lower line)
java_salary = [20, 30, 38, 45, 48, 52, 65]

# Create a figure with width=10 inches and height=6 inches
plt.figure(figsize=(10, 6))

# Plot the first line
plt.plot(
    x,
    python_salary,
    color="blue",                 # Line color
    linewidth=2,                  # Thickness of line
    marker="o",                   # Circle marker
    markersize=8,                 # Marker size
    label="Python Developer"      # Legend label
)

# Plot the second line
plt.plot(
    x,
    java_salary,
    color="red",
    linewidth=2,
    marker="s",                   # Square marker
    markersize=8,
    label="Java Developer"
)

# Fill the area between the two lines
plt.fill_between(
    x,                            # X-axis values
    python_salary,                # Upper curve
    java_salary,                  # Lower curve

    where=(                       # Fill only where Python salary is greater
        [p > j for p, j in zip(python_salary, java_salary)]
    ),

    interpolate=True,             # Smooth filling at intersection points

    step=None,                    # Step style (None, "pre", "post", "mid")

    color="green",                # Fill color

    alpha=0.35,                   # Transparency (0-1)

    facecolor="lightgreen",       # Interior fill color

    edgecolor="black",            # Border color

    linewidth=2,                  # Border thickness

    hatch="//",                   # Pattern inside fill

    label="Python > Java",        # Legend label

    zorder=1                      # Draw order
)

# Draw grid
plt.grid(True)

# Set title
plt.title("Python Salary vs Java Salary")

# X-axis label
plt.xlabel("Experience (Years)")

# Y-axis label
plt.ylabel("Salary (Thousands)")

# Set X-axis tick values
plt.xticks(x)

# Set Y-axis range
plt.ylim(10, 80)

# Set X-axis range
plt.xlim(1, 7)

# Show legend
plt.legend()

# Adjust spacing automatically
plt.tight_layout()

# Display the graph
plt.show()
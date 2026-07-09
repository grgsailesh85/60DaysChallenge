import pandas as pd

# Read the CSV file and store it in the DataFrame 'df'
df = pd.read_csv('outlier_dataset.csv')


# Function to calculate the lower and upper limits using the IQR method
def iqr_bounds(data, column):

    # Find the 25th percentile (First Quartile)
    Q1 = data[column].quantile(0.25)

    # Find the 75th percentile (Third Quartile)
    Q3 = data[column].quantile(0.75)

    # Calculate the Interquartile Range
    IQR = Q3 - Q1

    # Calculate the minimum acceptable value
    lower = Q1 - 1.5 * IQR

    # Calculate the maximum acceptable value
    upper = Q3 + 1.5 * IQR

    # Display the calculated limits
    print(f"Upper = {upper} \nLower = {lower}")

    # Return both limits to the calling function
    return lower, upper


# Function to remove outliers from a specific column
def remove_outliers(data, column):

    # Call iqr_bounds() to get the lower and upper limits
    lower, upper = iqr_bounds(data, column)

    # Create a Boolean filter:
    # True  -> Keep the row
    # False -> Remove the row (outlier)
    filt = ((data[column] >= lower) & (data[column] <= upper))

    # Return only the rows where the filter is True
    return data[filt]


# Functional pipeline
# The DataFrame is passed to remove_outliers() using .pipe()

df_cleaned = (
    df

    # Remove outliers from the Salary column first
    .pipe(remove_outliers, column="Salary")

    # Then remove outliers from the Age column
    .pipe(remove_outliers, column="Age")
)

# Display the original dataset
print("Original Dataset:\n", df)

# Display the dataset after removing outliers
print("\nCleaned Dataset:\n", df_cleaned)

# Save the DataFrame into a new CSV file
# index=False means do not save row numbers
df.to_csv("clean_data.csv", index=False)
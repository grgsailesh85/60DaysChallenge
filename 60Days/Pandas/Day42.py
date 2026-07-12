import pandas as pd

# Path of the raw dataset
file_path = "raw_dataset.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# ==================================================
# 1. STANDARDIZE THE DATA
# ==================================================

# Remove extra spaces, capitalize the first letter,
# and convert "Male" -> "M" and "Female" -> "F"
df["Gender"] = df["Gender"].str.strip().str.capitalize().replace({
    "Male" : "M",
    "Female" : "F"
})

# Remove extra spaces and make the first letter uppercase
# Example: " alice " -> "Alice"
df["Name"] = df["Name"].str.strip().str.capitalize()

# Remove extra spaces, capitalize text,
# then convert "It" -> "IT" and "Hr" -> "HR"
df["Department"] = df["Department"].str.strip().str.capitalize().replace({
    "It" : "IT",
    "Hr" : "HR"
})

# ==================================================
# 2. HANDLE MISSING VALUES
# ==================================================

# Calculate 50% of the total number of rows.
# This is used as a threshold for removing columns.
thres = len(df) * 0.5

# Remove columns having more than 50% missing values.
# axis=1 means remove columns.
df = df.dropna(thresh = thres, axis = 1)

# Loop through every column in the DataFrame
for col in df.columns:

    # If the column contains numeric data
    if df[col].dtype in ["float64", "int64"]:

        # Replace missing values with the median
        df[col] = df[col].fillna(df[col].median())

    # If the column contains text data
    else:

        # Replace missing values with the most frequent value (mode)
        df[col] = df[col].fillna(df[col].mode()[0])

# ==================================================
# 3. CONVERT DATE COLUMN
# ==================================================

# Convert Joining_Date column into datetime format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# Fill missing dates with the most common date
df["Joining_Date"] = df["Joining_Date"].fillna(df["Joining_Date"].mode()[0])

# ==================================================
# 4. ENSURE CORRECT DATA TYPES
# ==================================================

# Convert Age column into integer type
df["Age"] = df["Age"].astype(int)

# Convert Salary column into integer type
df["Salary"] = df["Salary"].astype(int)

# Convert Performance Score column into integer type
df["Performance_Score"] = df["Performance_Score"].astype(int)

# ==================================================
# 5. REMOVE OUTLIERS USING IQR METHOD
# ==================================================

# Function to remove outliers from a selected column
def remove_outliers_IQR(data, column):

    # Find the 25th percentile (Q1)
    Q1 = data[column].quantile(0.25)

    # Find the 75th percentile (Q3)
    Q3 = data[column].quantile(0.75)

    # Calculate the Interquartile Range (IQR)
    IQR = Q3 - Q1

    # Calculate the lower limit
    lower_bound = Q1 - 1.5 * IQR

    # Calculate the upper limit
    upper_bound = Q3 + 1.5 * IQR

    # Keep only the values inside the lower and upper limits
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Apply the outlier removal function one column at a time
df = (
    df

    # Remove outliers from Age
    .pipe(remove_outliers_IQR, column = "Age")

    # Remove outliers from Salary
    .pipe(remove_outliers_IQR, column = "Salary")

    # Remove outliers from Performance Score
    .pipe(remove_outliers_IQR, column = "Performance_Score")
)

# ==================================================
# 6. REMOVE DUPLICATE ROWS
# ==================================================

# Remove duplicate records from the DataFrame
df = df.drop_duplicates()

# ==================================================
# 7. SAVE THE CLEANED DATASET
# ==================================================

# File name for the cleaned dataset
clean_path = "Clean_dataset_Day42.csv"

# Save the cleaned DataFrame as a CSV file
# index=False means row numbers will not be saved
df.to_csv(clean_path, index = False)
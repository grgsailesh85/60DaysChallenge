# import pandas as pd
# df = pd.read_csv("sample_dirty_dataset.csv")
# # Remove outliers
# def remove_outliers_IQR(data, column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
# df_clean = (
#     df
#     .pipe(remove_outliers_IQR, column = "Age")
#     .pipe(remove_outliers_IQR, column = "Salary")
# )
# # Fill the unknown values -> strings
# df_clean["Department"] = df_clean["Department"].fillna("unknown")
# # Remove duplicates
# df_clean.drop_duplicates(inplace = True)
# # Making Data consistent
# df_clean["Gender"] = df["Gender"].replace({
#     "Male" : "M",
#     "Female" : "F"
# })
# df_clean.to_csv("Cleaned_data.csv", index = False)






import pandas as pd
df = pd.read_csv("sample_dirty_dataset.csv") 
print(df)
df["Age"].fillna(df["Age"].median(), inplace = True)
df["Salary"].fillna(df["Salary"].median(), inplace = True)
df["Department"].fillna("Unknown", inplace = True)
print(df)

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
df = pd.read_csv("House Price Prediction Dataset.csv")
df.sample(10)
df["Age"] = 2026 - df["YearBuilt"]
df.drop("YearBuilt", axis = 1, inplace = True)
df.sample(10)
condition_encoder = OrdinalEncoder(
    categories = [[
        "Poor", "Fair", "Good", "Excellent"
    ]]
)
df[["Condition"]] = condition_encoder.fit_transform(df[["Condition"]])
ohe = OneHotEncoder(
    drop = None,
    sparse_output = False,
)
garage_encoded = ohe.fit_transform(df[["Garage"]])

garage_cols = ohe.get_feature_names_out(["Garage"])
garage_df = pd.DataFrame(
    garage_encoded,
    columns = garage_cols,
    index = df.index
)
df.drop("Garage", axis = 1, inplace = True)
df = pd.concat([df, garage_df], axis = 1)
ohe = OneHotEncoder(
    drop = None,
    sparse_output = False,
)
location_encoded = ohe.fit_transform(df[["Location"]])

location_cols = ohe.get_feature_names_out(["Location"])
location_df = pd.DataFrame(
    location_encoded,
    columns = location_cols,
    index = df.index
)
df.drop("Location", axis = 1, inplace = True)
df = pd.concat([df, location_df], axis = 1)
price_col = df.pop("Price")
df["Price"] = price_col
df.to_csv("PreProcessed_Data.csv", index = False)
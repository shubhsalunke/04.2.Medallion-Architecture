import pandas as pd

df = pd.read_csv("bronze/sales_raw.csv")

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing amount
df["amount"] = df["amount"].fillna(0)

# Standardize city name
df["city"] = df["city"].str.upper()

df.to_csv("silver/sales_clean.csv", index=False)

print("Bronze to Silver completed")

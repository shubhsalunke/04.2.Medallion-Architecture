import pandas as pd

df = pd.read_csv("silver/sales_clean.csv")

gold = df.groupby("city")["amount"].sum().reset_index()

gold.columns = ["city", "total_sales"]

gold.to_csv("gold/city_sales_report.csv", index=False)

print("Silver to Gold completed")

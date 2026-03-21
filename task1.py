import pandas as pd

# Load all 3 CSV files from GitHub (correct way)
df1 = pd.read_csv("https://raw.githubusercontent.com/Samradyni/quantium-starter-repo/main/data/daily_sales_data_0.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/Samradyni/quantium-starter-repo/main/data/daily_sales_data_1.csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/Samradyni/quantium-starter-repo/main/data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Create Sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save output file
df.to_csv("formatted_sales_data.csv", index=False)

print("Task completed! File saved as formatted_sales_data.csv")
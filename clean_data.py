import pandas as pd

# 1️⃣ Load the raw CSV as strings
df = pd.read_csv("ebay_tech_deals.csv", dtype=str)

# 2️⃣ Clean the price and original_price columns
df["price"] = df["price"].str.replace("US $","").str.replace(",","").str.strip()
df["original_price"] = df["original_price"].str.replace("US $","").str.replace(",","").str.strip()

# 3️⃣ Fill missing original_price with price
df["original_price"] = df["original_price"].replace(["N/A",""], None)
df["original_price"] = df["original_price"].fillna(df["price"])

# 4️⃣ Clean shipping column
df["shipping"] = df["shipping"].replace(["N/A","", " "], "Shipping info unavailable")

# 5️⃣ Convert price columns to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["original_price"] = pd.to_numeric(df["original_price"], errors="coerce")

# 6️⃣ Calculate discount percentage
df["discount_percentage"] = ((df["original_price"] - df["price"]) / df["original_price"]) * 100
df["discount_percentage"] = df["discount_percentage"].round(2)

# 7️⃣ Save cleaned CSV
df.to_csv("cleaned_ebay_deals.csv", index=False)

print("Cleaned CSV saved!")
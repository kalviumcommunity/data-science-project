import pandas as pd

# Creating a mock dataset for our SmartStock inventory project
data = {
    "Item_ID": [101, 102, 103, 104, 105, 106],
    "Product_Name": ["Milk", "Bread", "Eggs", "Apples", "Coffee", "Rice"],
    "Category": ["Dairy", "Bakery", "Dairy", "Produce", "Beverage", "Pantry"],
    "Price": [4.99, 2.49, 3.99, 1.99, 12.99, 5.49],
    "Stock_Quantity": [45, 12, 8, 100, 30, 50],
    "Daily_Sales": [15, 20, 10, 25, 5, 8]
}

# Loading the data into a Pandas DataFrame (Think of this as an Excel spreadsheet in Python)
df = pd.DataFrame(data)


print("--- 1. df.head() : VISUAL PREVIEW ---")
# head() shows the first 5 rows by default. It's used to visually confirm the data loaded correctly.
print(df.head())


print("\n--- 2. df.info() : STRUCTURE & HEALTH CHECK ---")
# info() tells us the data types, number of rows/columns, and if any data is missing (nulls).
# Note: info() automatically prints to the console, so we don't need a print() statement around it.
df.info()


print("\n--- 3. df.describe() : NUMERICAL SUMMARY ---")
# describe() calculates statistics (mean, min, max, percentiles) for all numerical columns.
# It is heavily used to spot crazy outliers (e.g., if max 'Price' was $10,000 for groceries).
print(df.describe())
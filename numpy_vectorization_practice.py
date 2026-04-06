import numpy as np

# Sample Data: Quantities of 5 different products and their respective prices
quantities = np.array([10, 50, 8, 120, 5])
prices = np.array([3.00, 1.50, 4.00, 0.50, 5.00])

print("--- 1. THE OLD WAY: LOOP-BASED MATH ---")
# If we want to calculate the total value of each product (Quantity * Price), 
# a standard Python loop requires creating an empty list and iterating line by line:
loop_results = []
for i in range(len(quantities)):
    value = quantities[i] * prices[i]
    loop_results.append(value)

print("Loop Results:", loop_results)


print("\n--- 2. THE DATA SCIENCE WAY: VECTORIZATION ---")
# NumPy vectorization applies the operation to the entire array instantly, under the hood.
# No empty lists, no 'for' keywords, no index tracking.
vectorized_results = quantities * prices

print("Vectorized Results:", vectorized_results)
# Notice how the code went from 4 lines to exactly 1 line, and is much easier to read!


print("\n--- 3. VECTORIZED COMPARISONS & CONDITIONS ---")
# We can also apply logic and conditions without loops.
# Let's say our restock threshold is 15 units.
# The Old Way would require a loop with an 'if' statement. 
# The Vectorized Way checks the entire array at once!

low_stock_mask = quantities < 15

print("Low Stock Check (Quantities < 15):")
print(low_stock_mask)
# This returns an array of Booleans (True/False). 
# True means the condition was met (stock is less than 15).
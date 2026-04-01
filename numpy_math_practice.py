import numpy as np

print("--- 1. ELEMENT-WISE ARRAY OPERATIONS ---")
# Data: Units of Milk, Bread, and Eggs sold
last_week_sales = np.array([40, 50, 20])
this_week_sales = np.array([45, 48, 25])

# Addition: Total sales over two weeks
total_sales = last_week_sales + this_week_sales
print("Total Sales (Last + This week):", total_sales)

# Subtraction: Did we sell more this week? (Positive means growth)
sales_growth = this_week_sales - last_week_sales
print("Sales Growth (This week - Last week):", sales_growth)


print("\n--- 2. SCALAR OPERATIONS ON ARRAYS ---")
# A scalar is just a single number. 
# Let's say we want to forecast next week by assuming a flat 10-unit increase across all items
forecasted_sales = this_week_sales + 10
print("Forecasted Sales (+10 to all):", forecasted_sales)

# Let's calculate total revenue. Assume every item costs $3.00 (Scalar Multiplication)
item_price = 3.00
revenue = this_week_sales * item_price
print(f"Revenue for this week at $3 each: ${revenue}")


print("\n--- 3. THE PITFALL: PYTHON LISTS VS NUMPY ARRAYS ---")
# If we tried to add two standard Python lists together...
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("Python List Addition (list_a + list_b):")
print(list_a + list_b)  
# It glues them together! [1, 2, 3, 4, 5, 6]

print("\nNumPy Array Addition (array_a + array_b):")
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print(array_a + array_b) 
# It actually does the math! [5, 7, 9]
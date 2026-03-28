import numpy as np

print("--- 1. CREATING ARRAYS FROM LISTS ---")
# Standard Python List (representing 5 days of Milk sales)
sales_list = [15, 22, 18, 25, 20]
print("Standard Python List:", sales_list)

# Converting the list to a 1D NumPy Array
sales_array = np.array(sales_list)
print("1D NumPy Array:", sales_array)


print("\n--- 2. MULTI-DIMENSIONAL ARRAYS ---")
# Nested list (Sales of Milk and Bread over 3 days)
nested_sales = [
    [15, 22, 18],  # Milk
    [5, 9, 7]      # Bread
]
sales_matrix = np.array(nested_sales)
print("2D NumPy Array (Matrix):\n", sales_matrix)


print("\n--- 3. INSPECTING ARRAY PROPERTIES ---")
# Checking the structure of our 2D array
print("Shape (Rows, Columns):", sales_matrix.shape)
print("Dimensions:", sales_matrix.ndim)
print("Data Type:", sales_matrix.dtype)


print("\n--- 4. BASIC OPERATIONS: LISTS vs. ARRAYS ---")
# Let's say we want to forecast what happens if sales double.
print("List Math (sales_list * 2):")
print(sales_list * 2)  
# Notice how multiplying a list just duplicates the elements!

print("\nNumPy Math (sales_array * 2):")
print(sales_array * 2) 
# NumPy performs 'element-wise' math, actually doubling the values!
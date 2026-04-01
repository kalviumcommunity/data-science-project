import numpy as np

print("--- 1. 1D ARRAYS: SHAPE & DIMENSIONS ---")
# A 1D array representing daily sales of Milk (Mon-Fri)
milk_sales_1d = np.array([12, 15, 14, 20, 18])
print("1D Array:", milk_sales_1d)

# Shape tells us how many items are in each dimension
print("Shape:", milk_sales_1d.shape)  # Output will be (5,) meaning 1 dimension with 5 elements
print("Dimensions (ndim):", milk_sales_1d.ndim)


print("\n--- 2. 1D ARRAYS: INDEXING ---")
# Python uses ZERO-BASED indexing. The first item is at index 0.
print("Monday's Sales (Index 0):", milk_sales_1d[0])
print("Friday's Sales (Index 4):", milk_sales_1d[4])


print("\n--- 3. 2D ARRAYS: SHAPE & DIMENSIONS ---")
# A 2D array representing sales of 3 items (Milk, Bread, Eggs) over 4 days
# Think of this as a spreadsheet: Rows are items, Columns are days
inventory_matrix_2d = np.array([
    [12, 15, 14, 20],  # Row 0: Milk
    [30, 28, 35, 40],  # Row 1: Bread
    [10, 8, 12, 15]    # Row 2: Eggs
])
print("2D Array (Matrix):\n", inventory_matrix_2d)

# Shape for 2D arrays is always (Rows, Columns)
print("Shape (Rows, Columns):", inventory_matrix_2d.shape) 
print("Dimensions (ndim):", inventory_matrix_2d.ndim)


print("\n--- 4. 2D ARRAYS: INDEXING ---")
# To find a specific value in a 2D array, use: array[row_index, column_index]
# Let's find how much Bread (Row 1) we sold on the second day (Column 1)
bread_day_2 = inventory_matrix_2d[1, 1]
print("Bread sales on Day 2 (Row 1, Col 1):", bread_day_2)

# We can also grab an entire row at once (e.g., all Egg sales)
all_egg_sales = inventory_matrix_2d[2]
print("All sales for Eggs (Row 2):", all_egg_sales)
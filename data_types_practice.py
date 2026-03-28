print("--- 1. NUMERIC DATA TYPES ---")
# Integers (whole numbers) and Floats (decimals)
stock_quantity = 50          # int
item_price = 4.99            # float

# Basic arithmetic
total_inventory_value = stock_quantity * item_price
print(f"Total value of stock: ${total_inventory_value}")
# Notice how Python handles the math: an int multiplied by a float results in a float!

print("\n--- 2. STRING DATA TYPES ---")
# Strings (text)
product_name = "Organic Apples"
category = "Produce"

# String concatenation (combining text)
product_label = product_name + " - Category: " + category
print("Generated Label:", product_label)

print("\n--- 3. MIXING TYPES SAFELY ---")
# Mixing numbers and strings directly causes an error!
# BAD: print("We have " + stock_quantity + " items.") -> TypeError

# GOOD: Explicitly converting the integer to a string using str()
restock_message = "We currently have " + str(stock_quantity) + " units of " + product_name + "."
print(restock_message)

print("\n--- 4. INSPECTING DATA TYPES ---")
# Using the type() function to verify what kind of data we are working with
print("Type of stock_quantity:", type(stock_quantity))
print("Type of item_price:", type(item_price))
print("Type of product_name:", type(product_name))
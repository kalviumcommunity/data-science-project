print("--- 1. PYTHON LISTS (Mutable & Ordered) ---")
# Use Case: A dynamic list of items sold today. Lists can grow, shrink, and change.
recent_sales = ["Milk", "Bread", "Eggs"]
print("Initial sales:", recent_sales)

recent_sales.append("Apples")         # Adding an element to the end
recent_sales[1] = "Sourdough Bread"   # Modifying an element using its index (position 1)
print("Updated sales:", recent_sales)


print("\n--- 2. PYTHON TUPLES (Immutable & Ordered) ---")
# Use Case: Fixed data that should NEVER change accidentally, like GPS coordinates or tax rates.
store_coordinates = (40.7128, -74.0060)
print("Store Coordinates (Lat, Lon):", store_coordinates)
print("Latitude:", store_coordinates[0])

# Uncommenting the line below would cause a TypeError because Tuples are immutable!
# store_coordinates[0] = 41.0000 


print("\n--- 3. PYTHON DICTIONARIES (Key-Value Pairs) ---")
# Use Case: Storing structured information about a specific entity (like one product's details).
product_info = {
    "item_name": "Organic Milk",
    "price": 4.99,
    "quantity": 25
}
print("Initial Product Info:", product_info)

# Accessing data using keys instead of numerical indexes
print(f"The price of {product_info['item_name']} is ${product_info['price']}")

# Modifying and adding new key-value pairs
product_info["quantity"] = 20                 # Updating existing value
product_info["supplier"] = "Local Farms Inc." # Adding a completely new key
print("Updated Product Info:", product_info)
# inventory_report.py

# 1. Sample Data (Simulating a small local business inventory)
inventory = {
    "Milk": 45,
    "Bread": 12,
    "Eggs": 8,
    "Rice": 100,
    "Apples": 5
}

# 2. Threshold for "Low Stock"
LOW_STOCK_THRESHOLD = 15

print("--- DAILY INVENTORY CHECK ---")

# 3. Logic: Loop through inventory and flag items to restock
items_to_reorder = []

for item, quantity in inventory.items():
    if quantity < LOW_STOCK_THRESHOLD:
        print(f"⚠️ ALERT: {item} is low! Current stock: {quantity}")
        items_to_reorder.append(item)
    else:
        print(f"✅ {item} is healthy. Current stock: {quantity}")

# 4. Final Summary
print("\n--- SUMMARY ---")
if items_to_reorder:
    print(f"Items to add to restock list: {', '.join(items_to_reorder)}")
else:
    print("All inventory levels are sufficient.")
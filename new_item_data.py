#for test run analysis acting as a comparism to item data to test code
import json

with open("products.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

items = raw_data.get("items", [])


useful_item_data = []
for item in items:
    useful_item_data.append({
        "name": item.get("name"),
        "sku": item.get("sku"),
        "rate": item.get("rate")
    })


with open("products_old.json", "w", encoding="utf-8") as f:
    json.dump(useful_item_data, f, indent=4)

print("✅ Extracted product name, SKU, and rate from products.json")
print("📁 Saved to products_new.json")

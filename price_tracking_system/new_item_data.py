import json

# 📂 Load raw inventory data from fetch_erp_data.py
with open("products.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

items = raw_data.get("items", [])

# 🎯 Extract only the useful fields
filtered_items = []
for item in items:
    filtered_items.append({
        "name": item.get("name"),
        "sku": item.get("sku"),
        "rate": item.get("rate")
    })

# 💾 Save to products_new.json for further use
with open("products_new.json", "w", encoding="utf-8") as f:
    json.dump(filtered_items, f, indent=4)

print("✅ Extracted product name, SKU, and rate from products.json")
print("📁 Saved to products_new.json")

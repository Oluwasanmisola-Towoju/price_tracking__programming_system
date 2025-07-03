# iterates through the product data, extracting relevant information such as product name, SKU, and rate.
import json


def extract_important_data():
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
    print("📁 Saved to products_old.json")


# Optionally, allow running standalone
if __name__ == "__main__":
    extract_important_data()

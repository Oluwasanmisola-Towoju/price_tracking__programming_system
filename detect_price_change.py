from json import load, dump
import tkinter as tk
from tkinter import messagebox 

def detect_price_change(threshold=30):
    price_anomaly_threshold = threshold

    with open("products_old.json", "r", encoding= "utf-8") as old_item_data:
        old_data = load(old_item_data)

    with open("products_new.json", "r", encoding="utf-8") as new_item_data:
        new_data = load(new_item_data)

    old_prices = {item["name"]: item["rate"] for item in old_data}

    price_changes = []
    price_anomaly_noticed = []

    for item in new_data:
        sku = item["sku"]
        name = item["name"]
        new_rate = item["rate"]
        old_rate = old_prices.get(name)

        if old_rate is None:
            continue

        if old_rate != new_rate:
            change = new_rate - old_rate
            percentage_change = change / old_rate * 100

            price_changes.append({
                "sku": sku,
                "name": name,
                "old_rate": old_rate,
                "new_rate": new_rate,
                "percent_change": round(percentage_change, 2)
            })

            if abs(percentage_change) > price_anomaly_threshold:
                price_anomaly_noticed.append(f"{name} : {round(percentage_change, 2)}% change")

    with open("price_changes.json", "w", encoding="utf-8") as output:
        dump(price_changes, output, indent=4)

    print(f"Tracked {len(price_changes)} price changes.")
    print(f"🚨 Found {len(price_anomaly_noticed)} anomalies.")

    if price_anomaly_noticed:
        root = tk.Tk()
        root.withdraw()
        alert_message = "⚠️ Price Anomalies Detected:\\n\\n" + "\\n".join(price_anomaly_noticed)
        messagebox.showwarning("ERP Price Change Alert!", alert_message)

    return price_changes

if __name__ == "__main__":
    detect_price_change()

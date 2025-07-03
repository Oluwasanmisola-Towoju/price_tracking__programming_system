#Fetches product inventory data from Zoho Inventory API.
#retrieves product details such as SKU, name, and rate, and saves the data
#to a respective json for further processing and analysis.

import requests
import json
from configurations import HEADERS


url = "https://www.zohoapis.com/inventory/v1/items"

print("🔄 Sending request to Zoho Inventory...\n")
response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    print("Fetching full product inventory...\n")
    data = response.json()

    
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Your Full product inventory saved to products.json")

else:
    print("Failed to fetch products:", response.status_code, response.text)





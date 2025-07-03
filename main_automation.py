import fetch_product_data
import item_data  
import detect_price_change
import generate_pptx_file
import supervisor_private_copy
import time


def main():
    print("Fetching latest product data from Zoho Inventory API...\n")
    fetch_product_data.fetch_products()

    time.sleep(4)  

    print("Extracting product name, SKU and rate...\n")
    item_data.extract_important_data()

    time.sleep(4)

    print("Detecting price changes, anomalies and saving reports...\n")
    changes_found = detect_price_change.detect_price_change()

    time.sleep(4)

    print("Generating public Powerpoint price list...\n")
    generate_pptx_file.generate_pptx()

    time.sleep(4)

    print("Generating private PowerPoint dashboard for supervisor...\n")
    supervisor_private_copy.create_pptx()

    print("✅ Program completed successfully.")

if __name__ == "__main__":
    main()

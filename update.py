import sqlite3

def search_product(cursor, identifier):
    cursor.execute('''
        SELECT * FROM products WHERE barcode = ? OR name = ?
    ''', (identifier, identifier))
    products = cursor.fetchall()

    if len(products) == 0:
        print("No product found with the given identifier.")
        return None
    else:
        print("Product found with the given identifier:")
        for product in products:
            print(product)
        return products[0]

def update_stock_info(cursor, barcode, new_price, new_expiry_date, new_stock_shipment, new_stock_remaining):
    cursor.execute('''
        UPDATE products
        SET price = ?,
            expiry_date = ?,
            stock_shipment = ?,
            stock_remaining = ?
        WHERE barcode = ?
    ''', (new_price, new_expiry_date, new_stock_shipment, new_stock_remaining, barcode))

    if cursor.rowcount > 0:
        print("Stock information updated successfully!")
    else:
        print("No product found with the given barcode.")

def update_product_info(cursor, barcode, new_name, new_price, new_expiry_date, new_size, new_weight, new_stock_shipment, new_stock_remaining, new_category):
    cursor.execute('''
        UPDATE products
        SET name = ?,
            price = ?,
            expiry_date = ?,
            size = ?,
            weight = ?,
            stock_shipment = ?,
            stock_remaining = ?,
            category = ?
        WHERE barcode = ?
    ''', (new_name, new_price, new_expiry_date, new_size, new_weight, new_stock_shipment, new_stock_remaining, new_category, barcode))

    if cursor.rowcount > 0:
        print("Product information updated successfully!")
    else:
        print("No product found with the given barcode.")

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Prompt user to enter identifier (barcode or name) of the product to update
identifier = input("Enter the barcode or name of the product to update: ")

# Search for the product based on the identifier
product = search_product(cursor, identifier)

if product:
    update_choice = input("Do you want to update stock information only? (yes/no): ").lower()

    if update_choice == "yes":
        new_price = int(input("Enter new product price: "))
        new_expiry_date = input("Enter new expiry date (YYYY-MM-DD): ")
        new_stock_shipment = int(input("Enter new stock shipment quantity: "))
        new_stock_remaining = int(input("Enter new stock remaining quantity: "))

        # Update stock information
        update_stock_info(cursor, product[0], new_price, new_expiry_date, new_stock_shipment, new_stock_remaining)
    else:
        new_name = input("Enter new product name: ")
        new_price = int(input("Enter new product price: "))
        new_expiry_date = input("Enter new expiry date (YYYY-MM-DD): ")
        new_size = input("Enter new product size: ")
        new_weight = float(input("Enter new product weight: "))
        new_stock_shipment = int(input("Enter new stock shipment quantity: "))
        new_stock_remaining = int(input("Enter new stock remaining quantity: "))
        new_category = input("Enter new product category: ")

        # Update product information
        update_product_info(cursor, product[0], new_name, new_price, new_expiry_date, new_size, new_weight, new_stock_shipment, new_stock_remaining, new_category)

# Commit the transaction to save changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

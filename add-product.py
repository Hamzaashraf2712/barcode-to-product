import sqlite3

def add_product(cursor):
    barcode = input("Enter product barcode: ")
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
    size = input("Enter product size: ")
    weight = float(input("Enter product weight: "))
    stock_shipment = int(input("Enter stock shipment quantity: "))
    stock_remaining = int(input("Enter stock remaining quantity: "))
    
    cursor.execute('''
        INSERT INTO products (barcode, name, price, expiry_date, size, weight, stock_shipment, stock_remaining)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (barcode, name, price, expiry_date, size, weight, stock_shipment, stock_remaining))

    print("Product added successfully!")

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Prompt user to add a product
add_product(cursor)

# Commit the transaction to save changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

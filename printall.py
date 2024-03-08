import sqlite3

def print_all_products(cursor):
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    if len(products) == 0:
        print("No products found.")
    else:
        for product in products:
            print(product)

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Print all entries in the products table
print_all_products(cursor)

# Close the cursor and connection
cursor.close()
conn.close()

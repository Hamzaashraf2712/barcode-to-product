import sqlite3

def search_product_by_name(cursor, name):
    cursor.execute('''
        SELECT * FROM products WHERE name LIKE ?
    ''', ('%' + name + '%',))
    products = cursor.fetchall()
    if len(products) == 0:
        print("No products found with the name '{}'.".format(name))
    else:
        print("Products found with the name '{}':".format(name))
        for product in products:
            print(product)

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Prompt user to enter the name to search
name_to_search = input("Enter the name of the product to search: ")

# Search for products by name and print matching entries
search_product_by_name(cursor, name_to_search)

# Close the cursor and connection
cursor.close()
conn.close()

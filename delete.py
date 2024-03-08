import sqlite3

def delete_product(cursor, name):
    cursor.execute('''
        SELECT * FROM products WHERE name = ?
    ''', (name,))
    products = cursor.fetchall()

    if len(products) == 0:
        print("No product found with the name '{}'.".format(name))
    else:
        print("Products found with the name '{}':".format(name))
        for product in products:
            print(product)

        confirmation = input("Are you sure you want to delete these products? (yes/no): ").lower()
        if confirmation == "yes":
            cursor.execute('''
                DELETE FROM products
                WHERE name = ?
            ''', (name,))
            print("Products '{}' deleted successfully!".format(name))
        else:
            print("Deletion canceled.")

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Prompt user to enter the name of the product to delete
name_to_delete = input("Enter the name of the product to delete: ")

# Delete the product from the database
delete_product(cursor, name_to_delete)

# Commit the transaction to save changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

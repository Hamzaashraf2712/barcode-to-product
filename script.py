import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Add category column to the products table
cursor.execute('''
    ALTER TABLE products
    ALTER COLUMN price DROP NOT NULL,
    ALTER COLUMN expiry_date DROP NOT NULL,
    ALTER COLUMN size DROP NOT NULL,
    ALTER COLUMN weight DROP NOT NULL,
    ALTER COLUMN stock_shipment DROP NOT NULL,
    ALTER COLUMN stock_remaining DROP NOT NULL,
    ALTER COLUMN category DROP NOT NULL
''')

# Commit the transaction to save changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Category column added successfully!")

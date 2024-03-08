import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Add category column to the products table
cursor.execute('''
    ALTER TABLE products
    ADD COLUMN category TEXT
''')

# Commit the transaction to save changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Category column added successfully!")

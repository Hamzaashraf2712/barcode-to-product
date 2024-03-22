import tkinter as tk
from tkhtmlview import HTMLLabel
import sqlite3

class BarcodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Barcode Scanner App")

        # Create HTML labels for item name and price
        self.item_name_html = "<h1>Item Name</h1>"
        self.item_name_label = HTMLLabel(master, html=self.item_name_html)
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.price_html = "<h1>Price</h1>"
        self.price_label = HTMLLabel(master, html=self.price_html)
        self.price_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Entry field for user input
        self.entry_label = tk.Label(master, text="Enter Barcode or Item Name:")
        self.entry_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry = tk.Entry(master)
        self.entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Set focus on the entry field
        self.entry.focus_set()

        # Connect to SQLite database
        self.conn = sqlite3.connect('../test.db')
        self.cursor = self.conn.cursor()

        # Bind Enter key to trigger search
        self.entry.bind('<Return>', self.search)

    def search_product(self, search_input):
        # Check if the input is a barcode or a name
        if search_input.isdigit():  # Assuming barcodes are numeric
            self.cursor.execute('''
                SELECT name, price FROM products WHERE barcode = ?
            ''', (search_input,))
        else:
            self.cursor.execute('''
                SELECT name, price FROM products WHERE name LIKE ?
            ''', ('%' + search_input + '%',))

        return self.cursor.fetchall()

    def update_labels(self, item_name, price):
        self.item_name_html = f"<h1>{item_name}</h1>"
        self.item_name_label.set_html(self.item_name_html)

        self.price_html = f"<h1>{price}</h1>"
        self.price_label.set_html(self.price_html)

    def search(self, event):
        # Get user input from the entry field
        search_input = self.entry.get()

        # Search for product
        products = self.search_product(search_input)

        if len(products) == 0:
            print("No products found with the input '{}'.".format(search_input))
        else:
            for product in products:
                name, price = product
                print("Name: {}, Price: {}".format(name, price))
                # Update labels with product information
                self.update_labels(name, price)

        # Clear the entry field
        self.entry.delete(0, tk.END)

    def mainloop(self):
        self.master.mainloop()

def main():
    root = tk.Tk()
    app = BarcodeApp(root)
    app.mainloop()

if __name__ == "__main__":
    main()

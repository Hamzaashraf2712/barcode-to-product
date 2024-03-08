import tkinter as tk
from tkhtmlview import HTMLLabel

class BarcodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Barcode Scanner App")

        # Create HTML labels for item name and price
        item_name_html = "<h1>Item Name</h1>"
        self.item_name_label = HTMLLabel(master, html=item_name_html)
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        price_html = "<h1>Price</h1>"
        self.price_label = HTMLLabel(master, html=price_html)
        self.price_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def update_labels(self, item_name, price):
        item_name_html = f"<h1>{item_name}</h1>"
        self.item_name_label.set_html(item_name_html)

        price_html = f"<h1>{price}</h1>"
        self.price_label.set_html(price_html)

def main():
    root = tk.Tk()
    app = BarcodeApp(root)

    # Simulate reading a barcode and updating labels
    # Replace this with actual barcode reading logic
    item_name = "Scan Item"
    price = "00.00"
    app.update_labels(item_name, price)

    root.mainloop()

if __name__ == "__main__":
    main()

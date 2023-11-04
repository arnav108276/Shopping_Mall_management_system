import tkinter as tk
from datetime import datetime

class Item:
    def _init_(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def _init_(self):
        self.items = []
         def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["item"].price * item["quantity"]
        return total

class ShoppingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Shopping Mall Management System")

        self.cart = ShoppingCart()
        self.sales = 0
        self.purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items = [
            Item(1, "Item A", 10.0, 50),
            Item(2, "Item B", 5.0, 30)
        ]

import tkinter as tk
from datetime import datetime

class Item:
    def _init_(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["item"].price * item["quantity"]
        return total

class ShoppingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Shopping Mall Management System")

        self.cart = ShoppingCart()
        self.sales = 0
        self.purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items = [
            Item(1, "Item A", 10.0, 50),
            Item(2, "Item B", 5.0, 30)
        ]

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Select Item:").pack()
        self.item_var = tk.StringVar()
        self.item_var.set(self.items[0].name)
        item_options = [item.name for item in self.items]
        item_dropdown = tk.OptionMenu(self.root, self.item_var, *item_options)
        item_dropdown.pack()

        tk.Label(self.root, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack()

        calculate_sales_button = tk.Button(self.root, text="Calculate Sales", command=self.calculate_sales)
        calculate_sales_button.pack()

        self.invoice_text = tk.Text(self.root, height=10, width=40)
        self.invoice_text.pack()



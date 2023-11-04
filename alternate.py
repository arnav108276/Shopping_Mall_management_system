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


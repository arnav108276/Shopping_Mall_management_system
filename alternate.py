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

class Trader:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_item(self, item, price):
        self.inventory[item] = price

    def show_inventory(self):
        for item, price in self.inventory.items():
            print(f"{item}: {price} gold")

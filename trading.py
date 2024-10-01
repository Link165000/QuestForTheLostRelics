class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Trader:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def trade(self, player, item_name):
        item = next((item for item in self.inventory if item.name == item_name), None)
        if item:
            player.inventory.append(item)
            print(f"{player.name} traded for {item.name}!")
            self.inventory.remove(item)
        else:
            print("Item not found!")

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(f"- {item.name}")

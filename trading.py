class NPC:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def trade(self, item):
        if item in self.inventory:
            return f"Traded for {item}"
        else:
            return f"{self.name} does not have {item}."

# Example Usage
if __name__ == "__main__":
    npc = NPC("Merchant", ["Potion", "Sword", "Shield"])
    print(npc.trade("Potion"))  # Example trade

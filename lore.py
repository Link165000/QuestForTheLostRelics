class Lore:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"{self.title}\n{self.content}")

# Example lore entries
def create_lore_entries():
    lore_entries = [
        Lore("The Legend of the Ancients", "Long ago, powerful beings shaped the world."),
        Lore("The Rise of Corruption", "A dark force now threatens to consume everything."),
    ]
    return lore_entries

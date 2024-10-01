class Lore:
    def __init__(self):
        self.backstory = "The Elemental Cataclysm fractured the world; now a dark force seeks to corrupt the elemental energies."

    def get_backstory(self):
        return self.backstory

# Example usage
if __name__ == "__main__":
    lore = Lore()
    print(lore.get_backstory())

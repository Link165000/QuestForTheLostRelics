class Lore:
    def __init__(self):
        self.stories = self.create_lore()

    def create_lore(self):
        return {
            "origin": "In the beginning, the world was created by ancient elemental forces...",
            "heroes": "Legends speak of heroes who harnessed the power of the elements...",
            "dangers": "But dark forces lurk in the shadows, waiting to unleash chaos..."
        }

# Example Usage
if __name__ == "__main__":
    lore = Lore()
    for key, value in lore.stories.items():
        print(f"{key}: {value}")

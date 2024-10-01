import random

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.generate_map()

    def generate_map(self):
        return [[self.create_tile() for _ in range(self.width)] for _ in range(self.height)]

    def create_tile(self):
        terrain_types = ["forest", "mountain", "ice", "desert"]
        return {"type": random.choice(terrain_types), "enemies": self.generate_enemies()}

    def generate_enemies(self):
        return random.sample(["wolf", "goblin", "ice elemental", "dragon"], k=2)

    def display_map(self):
        for row in self.map:
            print(" | ".join([tile['type'] for tile in row]))

# Example Usage
if __name__ == "__main__":
    my_map = GameMap(10, 10)
    my_map.display_map()

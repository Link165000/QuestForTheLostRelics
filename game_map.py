import random

class GameMap:
    def __init__(self, size):
        self.size = size
        self.map_data = self.generate_map()

    def generate_map(self):
        # Generating a simple map with different terrain types
        terrains = ['grassland', 'forest', 'mountain', 'desert', 'ice']
        return [[random.choice(terrains) for _ in range(self.size)] for _ in range(self.size)]

    def display_map(self):
        for row in self.map_data:
            print(" ".join(row))

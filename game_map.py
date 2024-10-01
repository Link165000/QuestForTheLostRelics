import random

class Terrain:
    def __init__(self, name, element, mobs):
        self.name = name
        self.element = element
        self.mobs = mobs

class Chunk:
    def __init__(self, terrain):
        self.terrain = terrain
        self.fog_of_war = True  # Start with fog of war enabled
        self.mobs_present = self.generate_mobs()

    def generate_mobs(self):
        # Randomly select mobs based on terrain
        return random.sample(self.terrain.mobs, k=random.randint(1, 3))

class GameMap:
    def __init__(self, size):
        self.size = size
        self.chunks = self.generate_map(size)

    def generate_map(self, size):
        terrains = [
            Terrain("Ice Field", "ice", ["Ice Elemental", "Snow Wolf"]),
            Terrain("Fire Land", "fire", ["Fire Spirit", "Fire Elemental"]),
            Terrain("Forest", "nature", ["Woodland Creature", "Forest Spirit"]),
        ]
        return [[Chunk(random.choice(terrains)) for _ in range(size)] for _ in range(size)]

    def reveal_chunk(self, x, y):
        # Reveal fog of war for a specific chunk
        if 0 <= x < self.size and 0 <= y < self.size:
            self.chunks[x][y].fog_of_war = False

    def display_map(self):
        for row in self.chunks:
            for chunk in row:
                if chunk.fog_of_war:
                    print("🌫️", end=" ")
                else:
                    print(chunk.terrain.name[0], end=" ")
            print()

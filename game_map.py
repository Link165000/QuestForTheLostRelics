class GameMap:
    def __init__(self, size=(1000, 1000)):
        self.size = size
        self.map_data = self.generate_map()

    def generate_map(self):
        # Procedural generation logic for terrain
        return [['grass' for _ in range(self.size[1])] for _ in range(self.size[0])]

    def display_map(self):
        for row in self.map_data:
            print(" ".join(row))

# Example usage
if __name__ == "__main__":
    game_map = GameMap()
    game_map.display_map()

import random

def generate_map(size):
    game_map = [['.' for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            if random.random() < 0.1:
                game_map[y][x] = 'F'  # Forest
            elif random.random() < 0.1:
                game_map[y][x] = 'I'  # Ice
            elif random.random() < 0.1:
                game_map[y][x] = 'W'  # Water
            elif random.random() < 0.05:
                game_map[y][x] = 'E'  # Enemy

    return game_map

def get_terrain_type(game_map, x, y):
    terrain_types = {
        '.': 'Plain',
        'F': 'Forest',
        'I': 'Ice',
        'W': 'Water',
        'E': 'Enemy',
    }
    return terrain_types.get(game_map[y][x], 'Unknown')

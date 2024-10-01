def generate_map(size):
    game_map = [['.' for _ in range(size)] for _ in range(size)]
    
    # Add biomes
    for y in range(size):
        for x in range(size):
            if random.random() < 0.1:  # 10% chance to place a forest
                game_map[y][x] = 'F'  # Forest
            elif random.random() < 0.1:  # 10% chance to place ice
                game_map[y][x] = 'I'  # Ice
            elif random.random() < 0.1:  # 10% chance to place water
                game_map[y][x] = 'W'  # Water
            elif random.random() < 0.05:  # 5% chance for an enemy
                game_map[y][x] = 'E'  # Enemy
    
    return game_map

def get_terrain_type(x, y):
    # Return the type of terrain at (x, y)
    terrain_types = {
        '.': 'Plain',
        'F': 'Forest',
        'I': 'Ice',
        'W': 'Water',
        'E': 'Enemy',
    }
    return terrain_types.get(game_map[y][x], 'Unknown')

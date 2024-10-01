import random

def generate_map(size):
    game_map = [['.' for _ in range(size)] for _ in range(size)]
    
    # Add different terrain types
    for _ in range(size // 2):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        game_map[y][x] = 'E'  # Example Enemy
        # You can add more terrain types here

    return game_map

def get_terrain_type(x, y):
    # Return the type of terrain at (x, y)
    # You can define your terrain logic here
    return '.'

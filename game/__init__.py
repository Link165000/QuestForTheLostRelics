#this file exists to define what packages will be imported when you import the file
#example use

# import importlib

# submodules = [
#     'Town', 
#     'Character',   
#     'Weapons',
#     'movement_client',
#     'movement_server'
# ]

# for module in submodules:
#     try:
#         globals()[module] = importlib.import_module(f'.{module}', __name__)
#     except ImportError as e:
#         print(f"Failed to import {module}: {e}")

if __name__ == "__main__":
    from game.movement_client import  display_map, receive_map, client
    from game.movement_server import  game_map, update_map, players, display_size, update_map, display_map, broadcast_map, handle_client, start_server
    from game.Town import square, visit_blacksmith, visit_potions, Healer, create_magic_school, load_player, Fight, Magic, Inventory, Help, buy_blacksmith_item, buy_potion_item, Blacksmith, Potions
    from game.Weapons import starter_bow, starter_sword, intermediate_bow, intermediate_sword, scythe, katana



# #
# #
# #

__all__ = [
    "square", 
    "visit_blacksmith", 
    "visit_potions", 
    "Healer", 
    "create_magic_school", 
    "load_player", 
    "Fight", 
    "Magic", 
    "Inventory", 
    "Help", 
    "buy_blacksmith_item", 
    "Blacksmith", 
    "buy_potion_item", 
    "Potions",
    "display_map",
    "receive_map",
    "client",
    "game_map",
    "update_map",
    "players",
    "display_size",
    "update_map",
    "broadcast_map",
    "handle_client",
    "start_server",
    "starter_bow",
    "starter_sword",
    "intermediate_bow",
    "intermediate_sword",
    "scythe",
    "katana"
    ]







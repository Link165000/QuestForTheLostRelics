#this file exists to define what packages will be imported when you import the file
#example use

import importlib
import pkgutil

submodules = [
    'Town', 
    'Character',   
    'Weapons',
    'movement_client',
    'movement_server'
]


for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    try:
        globals()[module_name] = importlib.import_module(f'.{module_name}', __name__)
    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")



if __name__ == "__main__":
    from . import (
    Town,
    Character,
    Weapons,
    movement_client,
    movement_server
)
    from game.movement_client import  display_map, receive_map, client
    from game.movement_server import  game_map, update_map, players, display_size, update_map, display_map, broadcast_map, handle_client, start_server
    from game.Town import square, visit_blacksmith, visit_potions, Healer, create_magic_school, load_player, Fight, Magic, Inventory, Help, buy_blacksmith_item, buy_potion_item, Blacksmith, Potions
    from game.Status_effect import StatusEffect, Poison, Bleed, Frostbite
    # from game.Weapons import Weapon, Bows, MeleeWeapon, starter_bow, starter_sword, intermediate_bow, intermediate_sword, scythe, katana
    # Importing Classes and Instances
    from game.Weaponsv2 import (
        Weapon,
        Shield,
        MagicStaff,
        MeleeWeapon,
        Bows,
        starter_sword,
        starter_bow,
        intermediate_sword,
        intermediate_bow,
        battle_axe,
        dagger,
        mace,
        throwing_knives,
        repeating_bow,
        starter_staff,
        ice_wand,
        rapier,
        scythe,
        warhammer,
        longbow,
        nature_staff,
        fire_staff,
        flail,
        katana,
        crossbow,
        lightning_rod,
        greatsword,
        superior_sword,
        superior_bow,
        superior_staff,
        superior_dagger,
        phoenix_blade,
        darkmatter_bow,
        crystal_staff,
        shadowfang_dagger,
        soulreaper_staff,
        void_spear,
        void_reaver
    )


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
    "katana",
    "Weapon",
    "Bows",
    "MeleeWeapon",
    "Shield",
    "MagicStaff",
    "battle_axe",
    "dagger",
    "mace",
    "throwing_knives",
    "repeating_bow",
    "starter_staff",
    "ice_wand",
    "rapier",
    "longbow",
    "nature_staff",
    "fire_staff",
    "flail",
    "crossbow",
    "warhammer",
    "lightning_rod",
    "greatsword",
    "superior_sword",
    "superior_bow",
    "superior_staff",
    "superior_dagger",
    "phoenix_blade",
    "darkmatter_bow",
    "crystal_staff",
    "shadowfang_dagger",
    "soulreaper_staff",
    "void_spear",
    "void_reaver",
    "StatusEffect",
    "Poison",
    "Bleed",
    "Frostbite"

    ]







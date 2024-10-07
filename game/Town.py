### Town

import time
import random

gold = 100
inventory = ['basic armour']
health = 50
max_health = 100


blacksmith_inventory = {
    'iron sword': {'rarity': 'F', 'price': 50, 'damage': 10},
    'wooden shield': {'rarity': 'F', 'price': 15, 'defense': 5},
    'steel shield': {'rarity': 'E', 'price': 75, 'defense': 15},
    'wooden bow': {'rarity': 'F', 'price': 50, 'range': 15},
    'wooden arrow': {'rarity': 'F', 'price': 5, 'damage': 5},
}

potion_inventory = {
    'health potion': {'rarity': 'F', 'price': 30, 'heal': 10},
    'big health potion': {'rarity': 'E', 'price': 40, 'heal': 20}
}

def Inventory(player):
    print("Inventory:", player['inventory'])
    print("Gold:", player['gold'])


def Help():
    print("Help information goes here!")


def square(player):
    while True:
        print("Where would you like to go?")
        SquarePlaces = input('Potions and Lotions (P), Healer (H), Blacksmith (B), and Leave (L): ')
        if SquarePlaces == "P":
            visit_potions(player)
        elif SquarePlaces == "H":
            Healer(player)
        elif SquarePlaces == "B":
            visit_blacksmith(player)
        elif SquarePlaces == "L":
            break


def Blacksmith():
    items = "Welcome to the Blacksmith! Here are the available items:\n"
    for item, details in blacksmith_inventory.items():
        if 'damage' in details:
            stat_type = 'damage'
            stat_value = details['damage']
        elif 'defense' in details:
            stat_type = 'defense'
            stat_value = details['defense']
        elif 'range' in details:
            stat_type = 'range'
            stat_value = details['range']
        items += f"{item}: {details['price']} gold - {stat_type.capitalize()}: {stat_value}\n"
    return items

def buy_blacksmith_item(player, item_name):
    if item_name in blacksmith_inventory:
        item = blacksmith_inventory[item_name]
        if player['gold'] >= item['price']:
            player['gold'] -= item['price']
            player['inventory'].append(item_name)
            return f"You bought {item_name} for {item['price']} gold!"
        else:
            return "You don't have enough gold!"
    else:
        return "Item not found."

def visit_blacksmith(player):
    while True:
        print(Blacksmith())
        item = input("Enter the item you want to buy or (L) to leave: ")
        if item != "L":
            result = buy_blacksmith_item(player, item)
            print(result)
        else:
            break


def Potions():
    items = "Welcome to Potions and Lotions! Here are the available items:\n"
    for item, details in potion_inventory.items():
        stat_type = 'heal'
        stat_value = details['heal']
        items += f"{item}: {details['price']} gold - {stat_type.capitalize()}: {stat_value}\n"
    return items

def buy_potion_item(player, item_name):
    if item_name in potion_inventory:
        item = potion_inventory[item_name]
        if player['gold'] >= item['price']:
            player['gold'] -= item['price']
            player['inventory'].append(item_name)
            return f"You bought {item_name} for {item['price']} gold!"
        else:
            return "You don't have enough gold!"
    else:
        return "Item not found."

def visit_potions(player):
    while True:
        print(Potions())
        item = input("Enter the item you want to buy or (L) to leave: ")
        if item != "L":
            result = buy_potion_item(player, item)
            print(result)
        else:
            break


def Healer(player):
    while True:
        if player['health'] < player['max_health']:
            print("Pay 10 gold to have your health go up by 10:")
            heal_choice = input("Y/N: ")
            if heal_choice.upper() == "Y" and player['gold'] >= 10:
                player['health'] += 10
                if player['health'] > player['max_health']:
                    player['health'] = player['max_health']
                player['gold'] -= 10
                print("Your new health is", player['health'])
                print("Your remaining gold is", player['gold'])
            elif player['gold'] < 10:
                print("You don't have enough gold!")
                break
            else:
                break
        else:
            print("Your health is maxed")
            break


def load_player(name, gold, inventory):
    return {
        'name': name,
        'health': health,
        'max_health': max_health,
        'gold': gold,
        'inventory': [inventory]
    }

def Fight(player):
    enemy_health = 30
    enemy_damage = 5
    print("A wild enemy appears!")

    while enemy_health > 0:
        print(f"Enemy Health: {enemy_health}")
        print(f"Your Health: {player['health']}")
        
        action = input("Choose your action: Attack (A), Heal (H): ").upper()
        if action == "A":
            damage_dealt = random.randint(5, 15)  
            enemy_health -= damage_dealt
            print(f"You dealt {damage_dealt} damage to the enemy.")
        elif action == "H":
            if player['gold'] >= 10:
                player['health'] += 10
                player['gold'] -= 10
                print("You healed yourself for 10 health!")
            else:
                print("You don't have enough gold to heal.")
        else:
            print("Invalid action. Please choose again.")

        
        if enemy_health > 0:
            player['health'] -= enemy_damage
            print(f"The enemy dealt {enemy_damage} damage to you.")

        if player['health'] <= 0:
            print("You have been defeated!")
            break

    if enemy_health <= 0:
        print("You defeated the enemy!")
        player['gold'] += 20  
        print("You gained 20 gold!")


def Magic(player):
    magic_inventory = {
        'fireball': {'price': 30, 'damage': 20},
        'heal': {'price': 25, 'heal': 15}
    }
    
    while True:
        print("Welcome to the Magic School! Here are your spells:")
        for spell, details in magic_inventory.items():
            if 'damage' in details:
                print(f"{spell}: {details['price']} gold - Damage: {details['damage']}")
            elif 'heal' in details:
                print(f"{spell}: {details['price']} gold - Heal: {details['heal']}")
        
        action = input("Choose a spell to cast or (L) to leave: ").lower()
        if action in magic_inventory:
            spell = magic_inventory[action]
            if player['gold'] >= spell['price']:
                player['gold'] -= spell['price']
                if 'damage' in spell:
                    print(f"You cast {action} and dealt {spell['damage']} damage to the enemy!")
                elif 'heal' in spell:
                    player['health'] += spell['heal']
                    if player['health'] > player['max_health']:
                        player['health'] = player['max_health']
                    print(f"You cast {action} and healed yourself for {spell['heal']} health!")
            else:
                print("You don't have enough gold!")
        elif action == "l":
            break
        else:
            print("Invalid spell choice.")




def load_player(name, gold, inventory):
    return {
        'name': name,
        'health': health,
        'max_health': max_health,
        'gold': gold, 
        'inventory': [inventory]
    }


if __name__ == '__main__':
    
    player = load_player("Hero", gold, inventory)

    
while True:
    print("Town Square (T)', 'Fighting arena (F)', 'Magic School (M), ")
    Places = str(input('Leave(L) and Help(H): '))
    if Places == "T":
        square(player)
    elif Places == "'F'":
        Fight(player)
    elif Places == "M":
        Magic(player)
    elif Places == "L":
        print("Goodbye")
        break
    elif Places == "H":
        Help(player)
    elif Places == "I":
        Inventory(player)





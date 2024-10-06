### Town

import time

gold = 100
inventory = 'basic armour'
health = 50
max_health = 100

# Inventory for blacksmith
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
    print(player['inventory'], "and", player['gold'], "gold")


def Help():
    print("you idiot")


def square():
    while True:
        print("Where would you like to go?")
        SquarePlaces = str(input('Potions and Lotions (P), Healer (H), Blacksmith (B) and Leave(L)'))
        if SquarePlaces == "P":
            visit_potions(player)
        elif SquarePlaces == "H":
            Healer(player)
        elif SquarePlaces == "B":
            visit_blacksmith(player)
        elif SquarePlaces == "L":
            break


# -----------
# Shops in square
# -----------

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
        else:
            stat_type = 'unknown'
            stat_value = 'N/A'

        items += f"{item}: {details['price']} gold - {stat_type.capitalize()}: {stat_value}\n"
    return items


# Function to buy an item from the blacksmith
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


# Function to interact with the blacksmith
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
    items = "Welcome to the Blacksmith! Here are the available items:\n"
    for item, details in potion_inventory.items():
        if 'heal' in details:
            stat_type = 'heal'
            stat_value = details['heal']
        elif 'defense' in details:
            stat_type = 'defense'
            stat_value = details['defense']
        elif 'move' in details:
            stat_type = 'move'
            stat_value = details['move']
        else:
            stat_type = 'unknown'
            stat_value = 'N/A'
        items += f"{item}: {details['price']} gold - {stat_type.capitalize()}: {stat_value}\n"
    return items


# Function to buy an item from the blacksmith
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


# Function to interact with the blacksmith
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
            healchoice = input("Y/N: ")
            if healchoice.upper() == "Y" and player['gold'] >= 10:
                player['health'] += 10
                if player['health'] > player['max_health']:
                    player['health'] = player['max_health']  # Make sure it doesn't exceed max health
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
    print("Thank you for visiting the healer")




def load_player(name, gold, inventory):
    return {
        'name': name,
        'health': health,
        'max_health': max_health,
        'gold': gold,  # You can change this value to test purchases
        'inventory': [inventory]
    }


if __name__ == '__main__':
    # Create a player for testing
    player = load_player("Hero", gold, inventory)

    # Places in town
while True:
    print("Town Square (T)', 'Fighting arena (F)', 'Magic School (M), ")
    Places = str(input('Leave(L) and Help(H): '))
    if Places == "T":
        square()
    elif Places == "'F'":
        Fight()
    elif Places == "M":
        Magic()
    elif Places == "L":
        print("Goodbye")
        break
    elif Places == "H":
        Help()
    elif Places == "I":
        Inventory(player)





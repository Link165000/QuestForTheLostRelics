import random
import os

defending = False

class Character:
    def __init__(self, name, level, stats, runes, status):
        self.name = name
        self.level = level
        self.stats = stats  # Dictionary for stats like vigor, mind, endurance, etc.
        self.runes = runes
        self.status = status  # Dictionary for health, fp, stamina

    def level_up(self):
        if self.runes >= 20:
            print("What do you want to level up?")
            print(f"""
XP: {self.runes}

Level {self.level}
Max Health: {self.stats['Max Health']}
Max Maic: {self.stats['Max Magic']}
Max Stamina: {self.stats['Max Stamina']}
Strength: {self.stats['Strength']}
Logic: {self.stats['Logic']}
Belief: {self.stats['Belief']}""")
            choice = input("> ").lower()
            if choice in self.stats:
                self.stats[choice] += 10
                self.level += 1
                self.runes -= 20
                print(f"{choice.capitalize()} increased to {self.stats[choice]}")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("You don't have enough runes")

    def rest(self):
        # Restore health, fp, and stamina to their corresponding maximum values
        print("You sat near the fire.")
        print("Its warmth rejuvenated you.")
        self.status["health"] = self.stats["Max Health"]
        self.status["magic"] = self.stats["Max Magic"]
        self.status["stamina"] = self.stats["Max Stamina"]
        print("Health, Magic, and Stamina restored.")
        # Add enemy respawn system here

    def fight(self, enemy_health, enemy_damage):
        defending = False
        while enemy_health > 0 or player.status["health"] > 0:
            print(player.status["health"])
            print(enemy_health)
            print("Fight, Defend, Item, Run")
            choice = input("> ")
            if choice.lower() == "fight":
                if random.randint(0, 10) <= cool_sword.accuracy:
                    enemy_health -= cool_sword.damage
                    print(f"You did {cool_sword.damage} damage to the mean boi")
                else:
                    print("You missed the attack")
            elif choice.lower() == "defend":
                defending = True
            elif choice.lower() == "item":
                print("Heal health or magic?")
                potion = input("> ")
                if potion.lower() == "health" and player.status["healing potions"] > 0:
                    player.status["healing potions"] -= 1
                    self.status["health"] += 20
                    print("+20 health")
                elif potion.lower() == "magic" and player.status["magic potions"] > 0:
                    player.status["magic potions"] -= 1
                    self.status["magic"] += 20
                    print("+20 magic")
            else:
                print("You couldn't run away (u little bitch)")

            if enemy_health < 1:
                print("You slain the boi")
                break

            if defending:
                if cool_sword.defence > enemy_damage:
                    print("You blocked all damage")
                else:
                    player.status["health"] -= cool_sword.defence - enemy_damage
                    print(f"You took {cool_sword.defence - enemy_damage} damage")
                defending = False
            else:
                player.status["health"] -= enemy_damage
                print(f"You took {enemy_damage} damage")

            if player.status["health"] < 1:
                print("You died")
                print("Skill issue")
                quit()

    # Could help with monitoring individual players' money and items
    def buy(self, cost, item):
        print(f"{name} bought {item} for {cost}")
        self.runes -= cost
        # Add code for adding to inventory


# Probably won't add. Just stole stuff from Elden Ring
# Could maybe change the name to ally or something

class Weapon:
    def __init__(self, name, damage, stamina_use, range, accuracy, defence):
        self.name = name
        self.damage = damage
        self.stamina_use = stamina_use
        self.range = range
        self.accuracy = accuracy
        self.defence = defence


# Example character creation
if __name__ == "__main__":
    name = input("Enter your name: ")
    print("That's the dumbest name I've ever heard")

    stats = {
        "Max Health": 100,
        "Max Magic": 20,
        "Max Stamina": 69,
        "Strength": 50,
        "Logic": 2,
        "Belief": 30
    }

    status = {
        "health": 100,
        "magic": 20,
        "stamina": 69,
        "healing potions": 3,
        "magic potions": 2
    }

    player = Character(name, 1, stats, runes=100, status=status)

    cool_sword = Weapon("Cool Sword", 42069, 2, 3452, 10, 500)

#    Example of different ways to use the character class
#    player.level_up()
#    player.status["health"] -= 10
#    player.rest()
#    player.fight(10000, 10)

# combat.py

import random

class Character:
    def __init__(self, name, health, damage, mana):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        damage_dealt = random.randint(0, self.damage)
        target.health -= damage_dealt
        return damage_dealt

    def cast_spell(self, spell, target):
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            damage_dealt = spell.damage
            target.health -= damage_dealt
            return damage_dealt
        else:
            print(f"{self.name} does not have enough mana to cast {spell.name}!")
            return 0

class Spell:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_turn(self):
        action = input("Choose action (attack/cast): ").strip().lower()
        if action == "attack":
            damage = self.player.attack(self.enemy)
            print(f"{self.player.name} attacks {self.enemy.name} for {damage} damage!")
        elif action == "cast":
            spell_name = input("Choose a spell: Fireball (25 damage, 10 mana), Heal (15 damage, 5 mana): ").strip().lower()
            if spell_name == "fireball":
                spell = Spell("Fireball", damage=25, mana_cost=10)
            elif spell_name == "heal":
                spell = Spell("Heal", damage=15, mana_cost=5)
            else:
                print("Invalid spell!")
                return
            damage = self.player.cast_spell(spell, self.enemy)
            if damage > 0:
                print(f"{self.player.name} casts {spell.name} on {self.enemy.name} for {damage} damage!")

        print(f"{self.enemy.name}'s health is now {self.enemy.health}")

    def enemy_turn(self):
        damage = self.enemy.attack(self.player)
        print(f"{self.enemy.name} attacks {self.player.name} for {damage} damage!")
        print(f"{self.player.name}'s health is now {self.player.health}")

    def start_combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player_turn()
            if self.enemy.is_alive():
                self.enemy_turn()
        if self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
        else:
            print(f"{self.player.name} has been defeated by {self.enemy.name}!")

# Example usage
if __name__ == "__main__":
    player = Character(name="Hero", health=100, damage=20, mana=30)
    enemy = Character(name="Goblin", health=50, damage=15, mana=0)

    combat = Combat(player, enemy)
    combat.start_combat()

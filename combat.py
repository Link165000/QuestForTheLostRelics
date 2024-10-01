import random

class Character:
    def __init__(self, name, health, damage, mana, character_class):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.combos = {
            "Quick Strike": (2, 10),  # (number of hits, damage per hit)
            "Power Attack": (1, 25),   # A strong single hit
        }
        self.spells = {
            "Fireball": (30, 15),       # (damage, mana cost)
            "Heal": (-20, 10),          # Healing spell (negative damage)
        }
        self.skills = {
            "Shield Bash": (15, 5),     # (damage, mana cost)
            "Mana Surge": (0, 5),       # (restores mana, mana cost)
        }
        self.skill_levels = {
            "Shield Bash": 1,
            "Mana Surge": 1,
        }

    def attack(self, other):
        other.health -= self.damage
        return f"{self.name} attacks {other.name} for {self.damage} damage!"

    def perform_combo(self, combo_name, other):
        if combo_name in self.combos:
            hits, damage_per_hit = self.combos[combo_name]
            total_damage = hits * damage_per_hit
            other.health -= total_damage
            return f"{self.name} performs {combo_name} on {other.name} for {total_damage} damage!"
        else:
            return f"{combo_name} is not a valid combo!"

    def cast_spell(self, spell_name, other):
        if spell_name in self.spells:
            damage, mana_cost = self.spells[spell_name]
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                other.health -= damage
                return f"{self.name} casts {spell_name} on {other.name} for {damage} damage!"
            else:
                return f"Not enough mana to cast {spell_name}!"
        else:
            return f"{spell_name} is not a valid spell!"

    def use_skill(self, skill_name, other):
        if skill_name in self.skills:
            effect, mana_cost = self.skills[skill_name]
            if self.mana >= mana_cost:
                self.mana -= mana_cost
                if effect < 0:  # Healing effect
                    self.health -= effect  # Heal the character
                    return f"{self.name} uses {skill_name} and heals for {-effect} health!"
                else:  # Damage effect
                    other.health -= effect
                    return f"{self.name} uses {skill_name} on {other.name} for {effect} damage!"
            else:
                return f"Not enough mana to use {skill_name}!"
        else:
            return f"{skill_name} is not a valid skill!"

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= 100:  # Level up every 100 experience points
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= 100
        self.health += 10  # Increase health on level up
        self.mana += 5     # Increase mana on level up
        print(f"{self.name} leveled up to level {self.level}!")

    def level_up_skill(self, skill_name):
        if skill_name in self.skill_levels:
            self.skill_levels[skill_name] += 1
            damage_increase = random.randint(1, 5)  # Random increase in damage
            self.skills[skill_name] = (self.skills[skill_name][0] + damage_increase, self.skills[skill_name][1])
            print(f"{self.name} leveled up {skill_name} to level {self.skill_levels[skill_name]}!")

    def choose_action(self, other):
        print(f"\n{self.name}'s turn!")
        print("Choose an action:")
        print("1. Attack")
        print("2. Perform Combo")
        print("3. Cast Spell")
        print("4. Use Skill")
        action = input("Enter the number of your action: ")

        if action == "1":
            print(self.attack(other))
        elif action == "2":
            combo_name = input("Enter the combo name: ")
            print(self.perform_combo(combo_name, other))
        elif action == "3":
            spell_name = input("Enter the spell name: ")
            print(self.cast_spell(spell_name, other))
        elif action == "4":
            skill_name = input("Enter the skill name: ")
            print(self.use_skill(skill_name, other))
        else:
            print("Invalid action!")

# Example Usage
if __name__ == "__main__":
    hero = Character("Hero", 100, 10, 50, "Warrior")
    enemy = Character("Enemy", 100, 5, 30, "Mage")

    while hero.health > 0 and enemy.health > 0:
        hero.choose_action(enemy)
        if enemy.health > 0:
            enemy.choose_action(hero)

    if hero.health <= 0:
        print(f"{hero.name} has been defeated!")
    elif enemy.health <= 0:
        print(f"{enemy.name} has been defeated!")

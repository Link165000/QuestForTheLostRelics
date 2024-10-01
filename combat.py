import random

class Character:
    def __init__(self, name, max_health, mana, attack, defense):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.combos = []  # Combos currently known
        self.combo_book = {}  # Store discovered combos with reduced mana cost
        self.status_effects = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def cast_spell(self, spell):
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.effect(self)
        else:
            print(f"{self.name} does not have enough mana to cast {spell.name}!")

    def discover_combo(self, combo):
        if combo.name not in self.combo_book:
            # Add the combo to the combo book with reduced mana cost
            reduced_cost = combo.mana_cost // 2  # Reduce the cost by half
            self.combo_book[combo.name] = reduced_cost
            print(f"{self.name} has discovered the combo: {combo.name}!")

class Spell:
    def __init__(self, name, mana_cost, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.effect = effect

class Combat:
    def __init__(self):
        self.active_combos = []

    def add_combo(self, combo):
        self.active_combos.append(combo)

    def perform_combo(self, attacker, defender, combo):
        if all(skill in attacker.combos for skill in combo.skills):
            total_damage = sum(combo.damage)
            defender.take_damage(total_damage)
            print(f"{attacker.name} performed {combo.name} for {total_damage} damage!")
            attacker.discover_combo(combo)  # Discover the combo after performing it

class Combo:
    def __init__(self, name, skills, damage, mana_cost):
        self.name = name
        self.skills = skills
        self.damage = damage
        self.mana_cost = mana_cost

# Example spells
fireball = Spell("Fireball", 10, lambda caster: caster.attack * 2)
heal = Spell("Heal", 5, lambda caster: caster.heal(20))

# Example combos
fire_combo = Combo("Fire Combo", ["Fireball", "Basic Attack"], [20, 10], 15)
water_combo = Combo("Water Blast", ["Water Spell", "Basic Attack"], [25, 5], 20)

# Example characters
hero = Character("Hero", 100, 50, 15, 5)
monster = Character("Monster", 80, 30, 10, 3)

# Example usage
combat = Combat()
combat.add_combo(fire_combo)
combat.add_combo(water_combo)

hero.cast_spell(fireball)
combat.perform_combo(hero, monster, fire_combo)

# Check discovered combos and their reduced mana costs
print("Discovered Combos:")
for combo_name, cost in hero.combo_book.items():
    print(f"{combo_name}: {cost} mana cost")

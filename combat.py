class Character:
    def __init__(self, name, health, damage, mana):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
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

# Example Usage
if __name__ == "__main__":
    hero = Character("Hero", 100, 10, 50)
    enemy = Character("Enemy", 100, 5, 30)

    print(hero.attack(enemy))
    print(hero.perform_combo("Quick Strike", enemy))
    print(hero.cast_spell("Fireball", enemy))
    print(hero.use_skill("Shield Bash", enemy))
    print(hero.use_skill("Heal", hero))

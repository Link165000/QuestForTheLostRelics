import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self):
        base_damage = random.randint(10, 20)
        damage = self.apply_elemental_damage(base_damage)
        self.enemy['health'] -= damage

        print(f"{self.player['name']} attacked {self.enemy['name']} for {damage} damage!")

        if self.enemy['health'] <= 0:
            print(f"{self.enemy['name']} has been defeated!")

    def apply_elemental_damage(self, base_damage):
        if self.player['element'] == 'Fire' and self.enemy['element'] == 'Ice':
            return base_damage * 1.5
        elif self.player['element'] == 'Ice' and self.enemy['element'] == 'Fire':
            return base_damage * 0.5
        return base_damage

    def combo_attack(self):
        if random.random() < 0.3:
            damage = self.apply_elemental_damage(30)
            self.enemy['health'] -= damage
            print(f"{self.player['name']} performed a combo attack on {self.enemy['name']} for {damage} damage!")

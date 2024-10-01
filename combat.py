import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def choose_action(self):
        # Placeholder for action selection logic
        return random.choice(['attack', 'spell', 'combo'])

    def calculate_damage(self, attack_type):
        base_damage = self.player['attack']
        if attack_type == 'combo':
            base_damage *= 2  # Increase damage for combos
        return base_damage

    def battle(self):
        while self.player['hp'] > 0 and self.enemy['hp'] > 0:
            action = self.choose_action()
            damage = self.calculate_damage(action)
            self.enemy['hp'] -= damage
            print(f"{self.player['name']} dealt {damage} to {self.enemy['name']}.")

            if self.enemy['hp'] <= 0:
                print(f"{self.enemy['name']} has been defeated!")
                break
            
            # Enemy attacks back (basic AI)
            enemy_damage = self.enemy['attack']
            self.player['hp'] -= enemy_damage
            print(f"{self.enemy['name']} dealt {enemy_damage} to {self.player['name']}.")

            if self.player['hp'] <= 0:
                print(f"{self.player['name']} has been defeated!")

# Example usage
if __name__ == "__main__":
    player = {'name': 'Hero', 'hp': 100, 'attack': 10}
    enemy = {'name': 'Goblin', 'hp': 50, 'attack': 5}
    combat = Combat(player, enemy)
    combat.battle()

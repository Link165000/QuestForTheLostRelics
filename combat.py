class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other):
        other.health -= self.damage
        return f"{self.name} attacks {other.name} for {self.damage} damage!"

    def is_alive(self):
        return self.health > 0

# Example Usage
if __name__ == "__main__":
    player = Character("Hero", 100, 20)
    enemy = Character("Goblin", 50, 10)

    while player.is_alive() and enemy.is_alive():
        print(player.attack(enemy))
        print(f"{enemy.name} health: {enemy.health}")
        if enemy.is_alive():
            print(enemy.attack(player))
            print(f"{player.name} health: {player.health}")

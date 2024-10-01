import random

class Monster:
    def __init__(self, name, health, experience_value):
        self.name = name
        self.health = health
        self.experience_value = experience_value

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0


class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.level = 1
        self.experience = 0
        self.skill_points = 0
        self.stats = {
            'strength': 5,
            'intelligence': 5,
            'agility': 5,
            'mana': 5,
            'health': 100,
        }
        self.player_class = player_class
        self.skills = []
        self.level_up_threshold = 100  # Example threshold for leveling up

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience!")
        while self.experience >= self.level_up_threshold:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.level_up_threshold
        self.skill_points += 3  # Players receive 3 skill points per level
        self.level_up_threshold += 50  # Increase threshold for next level
        print(f"{self.name} leveled up to Level {self.level}!")

    def allocate_skill_points(self, stat=None, skill=None):
        if self.skill_points <= 0:
            print("No skill points available to allocate.")
            return

        if stat and stat in self.stats:
            self.stats[stat] += 1
            self.skill_points -= 1
            print(f"Allocated 1 point to {stat}. Total: {self.stats[stat]}")

        elif skill and skill not in self.skills:
            self.skills.append(skill)
            self.skill_points -= 1
            print(f"Unlocked skill: {skill}")

        else:
            print("Invalid allocation.")

    def show_status(self):
        print(f"Player Name: {self.name}")
        print(f"Level: {self.level} | Experience: {self.experience}/{self.level_up_threshold}")
        print(f"Skill Points Available: {self.skill_points}")
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")
        print("Skills:", ", ".join(self.skills) if self.skills else "None")

    def attack(self, monster):
        damage = self.stats['strength'] + random.randint(1, 5)  # Example damage calculation
        monster.take_damage(damage)
        if not monster.is_alive():
            print(f"{monster.name} has been defeated!")
            self.gain_experience(monster.experience_value)

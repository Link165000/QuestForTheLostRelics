class StatusEffect:
    def __init__(self, name, duration, effect_strength):
        self.name = name
        self.duration = duration
        self.effect_strength = effect_strength

    def apply_effect(self, target):
        pass

    def remove_effect(self, target):
        pass

class Poison(StatusEffect):
    def __init__(self, duration, effect_strength):
        super().__init__("Poison", duration, effect_strength)

    def apply_effect(self, target):
        target.health -= self.effect_strength
        print(f"{target.name} is poisoned! Health reduced by {self.effect_strength}.")

    def remove_effect(self, target):
        print(f"{target.name} is no longer poisoned.")

class Bleed(StatusEffect):
    def __init__(self, duration, effect_strength):
        super().__init__("Bleed", duration, effect_strength)

    def apply_effect(self, target):
        target.health -= self.effect_strength
        print(f"{target.name} is bleeding! Health reduced by {self.effect_strength}.")

    def remove_effect(self, target):
        print(f"{target.name} stopped bleeding.")

class Frostbite(StatusEffect):
    def __init__(self, duration, effect_strength):
        super().__init__("Frostbite", duration, effect_strength)

    def apply_effect(self, target):
        target.speed -= self.effect_strength
        print(f"{target.name} is frostbitten! Speed reduced by {self.effect_strength}.")

    def remove_effect(self, target):
        print(f"{target.name} is no longer frostbitten.")


class Character:
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed

if __name__ == "__main__":
    player = Character("Player", 100, 10)
    poison = Poison(duration=5, effect_strength=10)
    poison.apply_effect(player)
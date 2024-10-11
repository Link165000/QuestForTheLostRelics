# Basic layout for melee weapons:
#   damage_delt = obv
#   mastery_given = obv
#   health_regen = if the weapon heals you, basically life steal
#   spread = how many monsters damaged at a time

# Basic layout for range weapons:
#   damage_delt = obv
#   range_of = how far it shoots
#   mastery_given = obv
#   do we need this? the exp - shouldn't xp be from mobs?
#   health_regen = if the weapon heals you
#   spread = how many monsters damaged at a time


class Weapon():
    def __init__(self, damage_delt, mastery_given, health_regen, spread):
        self.damage_dealt = damage_delt
        self.mastery_given = mastery_given
        self.health_regen = health_regen
        self.spread = spread
        
    def attack(self):
        return f"dealt {self.damage_dealt} damage. spread to {self.spread} enemies"
    
    
class Sword(Weapon):
    def __init__(self, damage_delt, mastery_given, health_regen, spread):
        super().__init__(damage_delt, mastery_given, health_regen, spread)
        
class Bows(Weapon):
    def __init__(self, damage_delt, range_of, mastery_given, health_regen, spread):
        super().__init__(damage_delt, mastery_given, health_regen, spread)
        self.range_of = range_of
        
    def attack(self):
        return f"Dealt {self.damage_delt} damage at range {self.range_of}. Spread to {self.spread} enemies."
    
class Scythe(Weapon):
    def __init__(self, damage_delt, mastery_given, health_regen, spread):
        super().__init__(damage_delt, mastery_given, health_regen, spread)
        self.special_move = "spin attack"

class Katana(Weapon):
    def __init__(self, damage_delt, mastery_given, health_regen, spread):
        super().__init__(damage_delt, mastery_given, health_regen, spread)
        self.special_move = "quick slash"
    
    
    
starter_sword = Sword(damage_delt=1, mastery_given=0.5, health_regen=0, spread=1)
starter_bow = Bows(damage_delt=1, range_of=2, mastery_given=0.5, health_regen=0, spread=1)

intermediate_sword = Sword(damage_delt=3, mastery_given=2, health_regen=0, spread=1)
intermediate_bow = Bows(damage_delt=2, range_of=5, mastery_given=1.5, health_regen=0, spread=1)


scythe = Scythe(damage_delt=20, mastery_given=10, health_regen=10, spread=3)
katana = Katana(damage_delt=10, mastery_given=2, health_regen=15, spread=5)




# def starter_sword():
#     damage_delt = 1
#     mastery_given = 0.5
#     health_regen = 0
#     spread = 1

# def starter_bow():
#     damage_delt = 1
#     range_of = 2
#     mastery_given = 0.5
#     health_regen = 0
#     spread = 1
   
# def intermediate_sword():
#     damage_delt = 3
#     mastery_given = 2
#     health_regen = 0
#     spread = 1
    
# def intermediate_bow():
#     damage_delt = 2
#     range_of = 5
#     mastery_given = 1.5
#     health_regen = 0
#     spread = 1

# def scythe():
#     damage_delt = 20
#     mastery_given = 10
#     health_regen = 10
#     spread = 3

# def katana():
#     damage_delt = 10
#     mastery_given = 30
#     health_regen = 15
#     spread = 5



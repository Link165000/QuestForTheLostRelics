class Weapon:
    def __init__(self, damage_delt, mastery_given, health_regen, spread, rarity="F", special_ability=None):
        self.damage_dealt = damage_delt
        self.mastery_given = mastery_given
        self.health_regen = health_regen
        self.spread = spread
        self.rarity = rarity
        self.special_ability = special_ability

    def attack(self):
        attack_info = f"Dealt {self.damage_dealt} damage. Spread to {self.spread} enemies. Rarity: {self.rarity}"
        if self.special_ability:
            attack_info += f". Special ability: {self.special_ability}"
        return attack_info


class Shield:
    def __init__(self, defense_boost, health_regen, rarity="F"):
        self.defense_boost = defense_boost
        self.health_regen = health_regen
        self.rarity = rarity

    def defend(self):
        return f"Boosts defense by {self.defense_boost}. Health regeneration: {self.health_regen}. Rarity: {self.rarity}"


class MagicStaff(Weapon):
    def __init__(self, damage_delt, mana_boost, mastery_given, health_regen, spread, rarity="F", special_ability=None):
        super().__init__(damage_delt, mastery_given, health_regen, spread, rarity, special_ability)
        self.mana_boost = mana_boost

    def attack(self):
        attack_info = f"Dealt {self.damage_dealt} damage with {self.spread} spread and {self.mana_boost} mana boost. Rarity: {self.rarity}"
        if self.special_ability:
            attack_info += f". Special ability: {self.special_ability}"
        return attack_info


class MeleeWeapon(Weapon):
    pass


class Bows(Weapon):
    def __init__(self, damage_delt, range_of, mastery_given, health_regen, spread, rarity="F", special_ability=None):
        super().__init__(damage_delt, mastery_given, health_regen, spread, rarity, special_ability)
        self.range_of = range_of

    def attack(self):
        attack_info = f"Dealt {self.damage_dealt} damage at range {self.range_of}. Spread to {self.spread} enemies. Rarity: {self.rarity}"
        if self.special_ability:
            attack_info += f". Special ability: {self.special_ability}"
        return attack_info


# Starter Weapons
starter_sword = MeleeWeapon(damage_delt=1, mastery_given=0.5, health_regen=0, spread=1, rarity="Common")
starter_bow = Bows(damage_delt=1, range_of=3, mastery_given=0.5, health_regen=0, spread=1, rarity="Common")

# Intermediate Weapons
intermediate_sword = MeleeWeapon(damage_delt=4, mastery_given=2, health_regen=0, spread=2, rarity="Uncommon")
intermediate_bow = Bows(damage_delt=3, range_of=6, mastery_given=1.5, health_regen=0, spread=1, rarity="Uncommon")

# Common Weapons
battle_axe = MeleeWeapon(damage_delt=8, mastery_given=2, health_regen=0, spread=2, rarity="Uncommon")
dagger = MeleeWeapon(damage_delt=3, mastery_given=5, health_regen=2, spread=1, rarity="Common")
mace = MeleeWeapon(damage_delt=7, mastery_given=1, health_regen=0, spread=2, rarity="Uncommon")
throwing_knives = Bows(damage_delt=5, range_of=4, mastery_given=1.5, health_regen=0, spread=3, rarity="Uncommon")
repeating_bow = Bows(damage_delt=3, range_of=6, mastery_given=2, health_regen=0, spread=3, rarity="Uncommon")

# Uncommon Weapons
starter_staff = MagicStaff(damage_delt=2, mana_boost=5, mastery_given=1, health_regen=1, spread=2, rarity="Common")
ice_wand = MagicStaff(damage_delt=4, mana_boost=7, mastery_given=2, health_regen=2, spread=2, rarity="Uncommon")
rapier = MeleeWeapon(damage_delt=5, mastery_given=6, health_regen=1, spread=1, rarity="Uncommon")

# Rare Weapons
scythe = MeleeWeapon(damage_delt=15, mastery_given=8, health_regen=5, spread=2, rarity="Rare")
warhammer = MeleeWeapon(damage_delt=12, mastery_given=3, health_regen=0, spread=1, rarity="Rare")
longbow = Bows(damage_delt=4, range_of=10, mastery_given=2, health_regen=0, spread=3, rarity="Rare")
nature_staff = MagicStaff(damage_delt=3, mana_boost=5, mastery_given=1.5, health_regen=8, spread=1, rarity="Rare")
fire_staff = MagicStaff(damage_delt=6, mana_boost=10, mastery_given=3, health_regen=1, spread=3, rarity="Rare")
flail = MeleeWeapon(damage_delt=9, mastery_given=4, health_regen=0, spread=3, rarity="Rare")

# Epic Weapons
katana = MeleeWeapon(damage_delt=10, mastery_given=4, health_regen=7, spread=3, rarity="Epic")
crossbow = Bows(damage_delt=7, range_of=8, mastery_given=3, health_regen=0, spread=1, rarity="Epic")
lightning_rod = MagicStaff(damage_delt=10, mana_boost=12, mastery_given=5, health_regen=0, spread=4, rarity="Epic")
greatsword = MeleeWeapon(damage_delt=15, mastery_given=7, health_regen=0, spread=1, rarity="Epic")

# Superior Weapons
superior_sword = MeleeWeapon(damage_delt=18, mastery_given=8, health_regen=5, spread=3, special_ability="ATK Speed", rarity="Superior")
superior_bow = Bows(damage_delt=15, range_of=4, mastery_given=7, health_regen=0, spread=4, special_ability="AoE", rarity="Superior")
superior_staff = MagicStaff(damage_delt=12, mana_boost=6, mastery_given=6, health_regen=3, spread=2, special_ability="Shield 20% 10", rarity="Superior")
superior_dagger = MeleeWeapon(damage_delt=10, mastery_given=5, health_regen=2, spread=1, special_ability="Crit 20%", rarity="Superior")

# Legendary Weapons
phoenix_blade = MeleeWeapon(damage_delt=40, mastery_given=15, health_regen=10, spread=4, special_ability="Revives 25% on kill", rarity="Legendary")
darkmatter_bow = Bows(damage_delt=38, range_of=8, mastery_given=12, health_regen=5, spread=5, special_ability="Piercing", rarity="Legendary")
crystal_staff = MagicStaff(damage_delt=36, mana_boost=15, mastery_given=15, health_regen=12, spread=3, special_ability="Health 4 mana", rarity="Legendary")
shadowfang_dagger = MeleeWeapon(damage_delt=45, mastery_given=16, health_regen=6, spread=2, special_ability="Invis", rarity="Legendary")
soulreaper_staff = MagicStaff(damage_delt=40, mana_boost=15, mastery_given=15, health_regen=8, spread=3, special_ability="Damage buff", rarity="Legendary")
void_spear = Bows(damage_delt=50, range_of=15, mastery_given=17, health_regen=2, spread=1, special_ability="Piercing", rarity="Legendary")

# Display examples of each weapon
print(starter_sword.attack())
print(starter_bow.attack())
print(ice_wand.attack())
print(scythe.attack())
print(phoenix_blade.attack())
print(darkmatter_bow.attack())

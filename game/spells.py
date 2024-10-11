# spells.py

class Spell:
    def __init__(self, name, damage, mana_cost, description, rarity):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.description = description
        self.rarity = rarity

# Rarities
RARITIES = {
    "Common": 1,
    "Uncommon": 2,
    "Rare": 3,
    "Epic": 4,
    "Legendary": 5,
}

# List of spells
spells = [
    Spell("Fireball", damage=25, mana_cost=10, description="A fiery explosion that deals damage to a single target.", rarity=RARITIES["Rare"]),
    Spell("Ice Shard", damage=20, mana_cost=8, description="A shard of ice that pierces the enemy, dealing damage.", rarity=RARITIES["Uncommon"]),
    Spell("Lightning Bolt", damage=30, mana_cost=15, description="A bolt of lightning strikes the enemy, causing heavy damage.", rarity=RARITIES["Epic"]),
    Spell("Heal", damage=0, mana_cost=5, description="Restores a small amount of health to the caster.", rarity=RARITIES["Common"]),
    Spell("Poison Cloud", damage=15, mana_cost=12, description="Creates a cloud of poison that deals damage over time.", rarity=RARITIES["Rare"]),
    Spell("Arcane Missile", damage=10, mana_cost=6, description="A missile of arcane energy that seeks its target.", rarity=RARITIES["Common"]),
    Spell("Earthquake", damage=40, mana_cost=20, description="Shakes the ground, damaging all enemies in the vicinity.", rarity=RARITIES["Legendary"]),
    Spell("Water Surge", damage=15, mana_cost=7, description="A surge of water that knocks enemies back and deals damage.", rarity=RARITIES["Uncommon"]),
    Spell("Wind Slash", damage=20, mana_cost=10, description="A sharp gust of wind that slices through enemies.", rarity=RARITIES["Uncommon"]),
    Spell("Shadow Strike", damage=35, mana_cost=18, description="A sudden strike from the shadows, dealing massive damage.", rarity=RARITIES["Epic"]),
    Spell("Divine Light", damage=0, mana_cost=10, description="Channels divine energy to heal allies in an area.", rarity=RARITIES["Rare"]),
    Spell("Firestorm", damage=50, mana_cost=30, description="A storm of fire that engulfs the battlefield.", rarity=RARITIES["Legendary"]),
    Spell("Frostbite", damage=25, mana_cost=12, description="Chills the enemy to the core, dealing frost damage.", rarity=RARITIES["Rare"]),
    Spell("Mana Drain", damage=0, mana_cost=5, description="Drains mana from the target, restoring the caster's mana.", rarity=RARITIES["Uncommon"]),
    Spell("Summon Familiar", damage=0, mana_cost=15, description="Summons a familiar to aid the caster in battle.", rarity=RARITIES["Rare"]),
    Spell("Meteor Strike", damage=60, mana_cost=40, description="Calls down a meteor from the sky, causing massive damage.", rarity=RARITIES["Legendary"]),
    Spell("Chain Lightning", damage=35, mana_cost=20, description="Strikes one enemy and jumps to others, dealing damage.", rarity=RARITIES["Epic"]),
    Spell("Healing Rain", damage=0, mana_cost=25, description="Summons rain that heals allies in an area over time.", rarity=RARITIES["Epic"]),
    Spell("Vortex", damage=30, mana_cost=18, description="Creates a vortex that pulls enemies in and damages them.", rarity=RARITIES["Rare"]),
    Spell("Fire Wave", damage=20, mana_cost=10, description="A wave of fire that sweeps across the battlefield.", rarity=RARITIES["Uncommon"]),
    Spell("Barrier", damage=0, mana_cost=12, description="Creates a protective barrier around the caster.", rarity=RARITIES["Rare"]),
    Spell("Time Stop", damage=0, mana_cost=25, description="Stops time for a brief moment, allowing for extra actions.", rarity=RARITIES["Legendary"]),
    Spell("Confusion", damage=0, mana_cost=15, description="Confuses enemies, causing them to act unpredictably.", rarity=RARITIES["Rare"]),
    Spell("Soul Siphon", damage=20, mana_cost=15, description="Drains health from the enemy, healing the caster.", rarity=RARITIES["Epic"]),
    Spell("Light Beam", damage=30, mana_cost=12, description="A concentrated beam of light that damages a target.", rarity=RARITIES["Rare"]),
    Spell("Mind Control", damage=0, mana_cost=20, description="Temporarily takes control of an enemy for one turn.", rarity=RARITIES["Legendary"]),
    Spell("Fire Wall", damage=15, mana_cost=10, description="Creates a wall of fire that damages enemies who pass through.", rarity=RARITIES["Rare"]),
    Spell("Berserk", damage=0, mana_cost=10, description="Increases an ally's attack power for a short duration.", rarity=RARITIES["Uncommon"]),
    Spell("Teleport", damage=0, mana_cost=15, description="Teleports the caster to a nearby location.", rarity=RARITIES["Epic"]),
    Spell("Illusion", damage=0, mana_cost=8, description="Creates an illusion to distract enemies.", rarity=RARITIES["Uncommon"]),
    Spell("Stone Skin", damage=0, mana_cost=10, description="Hardens the caster's skin, reducing damage taken.", rarity=RARITIES["Rare"]),
    Spell("Thunder Clap", damage=25, mana_cost=12, description="A powerful clap of thunder that stuns enemies.", rarity=RARITIES["Rare"]),
    Spell("Haste", damage=0, mana_cost=10, description="Increases the speed of the caster for a limited time.", rarity=RARITIES["Uncommon"]),
    Spell("Fumble", damage=0, mana_cost=5, description="Causes enemies to drop their weapons for a turn.", rarity=RARITIES["Uncommon"]),
    Spell("Summon Elemental", damage=0, mana_cost=30, description="Summons an elemental to fight alongside the caster.", rarity=RARITIES["Legendary"]),
    Spell("Dust Cloud", damage=10, mana_cost=5, description="Creates a cloud of dust that obscures vision.", rarity=RARITIES["Common"]),
    Spell("Gust", damage=15, mana_cost=8, description="Creates a strong gust of wind that pushes enemies back.", rarity=RARITIES["Uncommon"]),
    Spell("Searing Light", damage=25, mana_cost=10, description="A beam of light that burns the target.", rarity=RARITIES["Rare"]),
    Spell("Shadow Bolt", damage=35, mana_cost=15, description="A bolt of shadow energy that strikes the enemy.", rarity=RARITIES["Epic"]),
    Spell("Frost Nova", damage=40, mana_cost=20, description="A chilling blast that freezes enemies in place.", rarity=RARITIES["Epic"]),
    Spell("Life Leech", damage=20, mana_cost=10, description="Drains life from the enemy and heals the caster.", rarity=RARITIES["Rare"]),
    Spell("Illumination", damage=15, mana_cost=5, description="Illuminates the area, revealing hidden enemies.", rarity=RARITIES["Common"]),
    Spell("Nightmare", damage=0, mana_cost=15, description="Induces a nightmare in the target, causing fear.", rarity=RARITIES["Uncommon"]),
    Spell("Flame Wave", damage=30, mana_cost=12, description="A wave of flames that sweeps across the battlefield.", rarity=RARITIES["Epic"]),
]

# Optional: Function to get spells by rarity
def get_spells_by_rarity(rarity_level):
    return [spell for spell in spells if spell.rarity == rarity_level]

# Basic layout for melee weapons:
#   damage_delt = obv
#   exp_given = obv
#   health_regen = if the weapon heals you, basically life steal
#   spread = how many monsters damaged at a time

# Basic layout for range weapons:
#   damage_delt = obv
#   range_of = how far it shoots
#   exp_given = obv
#   health_regen = if the weapon heals you
#   spread = how many monsters damaged at a time

def starter_sword():
    damage_delt = 1
    exp_given = 0.5
    health_regen = 0
    spread = 1

def starter_bow():
    damage_delt = 1
    range_of = 2
    exp_given = 0.5
    health_regen = 0
    spread = 1
   
def intermediate_sword():
    damage_delt = 5
    exp_given = 2
    health_regen = 0
    spread = 1
    
def intermediate_bow():
    damage_delt = 2
    range_of = 5
    exp_given = 1.5
    health_regen = 0
    spread = 1

def scyth():
    damage_delt = 20
    exp_given = 10
    health_regen = 20
    spread = 5

def katana():
    damage_delt = 50
    exp_given = 30
    health_regen = 15
    spread = 10
    
def pistol():
    damage_delt = 30
    range_of = 50
    exp_given = 25
    health_regen = 10
    spread = 1
    
def shotgun():
    damage_delt = 60
    range_of = 20
    exp_given = 30
    health_regen = 15
    spread = 5

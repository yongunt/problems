MAGES:tuple = ("W", "U", "B", "R", "G", "C")

def can_pay_cost(player_mana:str, mana_cost:str) -> bool:
    player_mages:dict = {}
    player_addiction:int = 0
    cost_mages:dict = {}
    cost_addiction:int = 0

    for mage in player_mana:
        if mage in MAGES: player_mages[mage] = player_mana.count(mage)    
        elif mage.isdigit(): player_addiction = int(mage)

    for mage in mana_cost:
        if mage in MAGES: cost_mages[mage] = mana_cost.count(mage)    
        elif mage.isdigit(): cost_addiction = int(mage)

    for mage in cost_mages:
        if mage not in player_mages: return False
        player_mages[mage] -= cost_mages[mage]
        if player_mages[mage] < 0: return False

    for mage in player_mages: player_addiction += player_mages[mage]

    if (player_addiction - cost_addiction) < 0: return False
    else: return True


print(can_pay_cost("WWGGR", "2WWG"))
print(can_pay_cost("WWGG", "2WWG"))
print(can_pay_cost("WGGGR", "2WWG"))
print(can_pay_cost("WUUUBC", "UUB"))


'''
can_pay_cost("WWGGR", "2WWG") ➞ True

can_pay_cost("WWGG", "2WWG") ➞ False
# Not enough total mana.

can_pay_cost("WGGGR", "2WWG") ➞ False
# Not enough W mana.

can_pay_cost("WUUUBC", "UUB") ➞ True
# Having extra mana is okay.
'''
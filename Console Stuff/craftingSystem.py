#this is just a crafting system I was messing around with, Feel free to copy or use it

crafting_table = {'Wooden Axe':{'stick':1, 'wood':1}, 'Iron Axe':{'Iron':2, 'Wooden Axe':1}}

class Item:
    def __init__(self, name, amount=1, consumedUponCraft=True):
        self.name = name
        self.amount = amount
        self.consumedUponCraft = consumedUponCraft
    
inventory = {'stick':Item('stick', 5), 'wood':Item('wood', 5), 'Iron':Item('Iron', 3)}

def craft(item_name, craft_amount=1):
    materials = crafting_table[item_name]
    costs = {}
    for material, material_amount in materials.items():
        if inventory[material].amount >= material_amount*craft_amount:
            if inventory[material].consumedUponCraft:
                costs[material] = material_amount*craft_amount
    
    if sum(costs.values()) == sum(materials.values())*craft_amount:
        inventory[item_name] = Item(item_name, craft_amount)
        for material, cost in costs.items():
            inventory[material].amount -= cost

craft('Wooden Axe')

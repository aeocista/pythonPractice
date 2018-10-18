#Items I need for my latest adventure
adventureInventory = {
             'rope': 1, 
             'torch': 6, 
             'gold coin': 42,
             'dagger': 1, 
             'arrow': 12, 
             'bow': 1
            }

#Create the display inventory function
def displayQuantity(item, quantity):
    itemQuantity = 0
    for k, v in items.quantities():
        itemQuantity = itemQuantity + v.get(quantity, 0)
    return itemQuantity

#Print the number of items in inventory
print('Number of items in inventory:')
print(' - Ropes      ' + str(displayInventory(adventureInventory, 'rope')))
print(' - Torches    ' + str(displayInventory(adventureInventory, 'torch')))
print(' - Gold Coins ' + str(displayInventory(adventureInventory, 'gold coin')))
print(' - Daggers    ' + str(displayInventory(adventureInventory, 'dagger')))
print(' - Arrows     ' + str(displayInventory(adventureInventory, 'arrow')))
print(' - Bows       ' + str(displayInventory(adventureInventory, 'bow')))

inventory = {
             'gold' : 500,
             'pouch' : ['flint', 'twine', 'gemstone'],
             'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
            }

#1.) Add a key inventory called 'pocket'. 
inventory['pocket'] = []
print(inventory,'\n')

#2.) Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory,'\n')

#3.) Sort()the items in the list stored under the 'backpack' key.
backpack = inventory['backpack']
backpack.sort()
print(inventory,'\n')

#4.) Then .remove('dagger') from the list of items stored under the 'backpack' key.
backpack.remove('dagger')
print(inventory,'\n')

#5.) Add 50 to the number stored under the 'gold' key.
inventory['gold'] =  inventory['gold']+ 50
print(inventory,'\n')
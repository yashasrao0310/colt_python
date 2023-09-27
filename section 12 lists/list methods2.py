# REMOVE ITEM METHODS

# clear() --> removes everything in list
list = [1,2,3,4,4,4]
list.clear()
print(list)

# pop() --> removes last eml 
# pop(idx) --> removes item at index
# RETURNS REMOVED ITEM TO USE/MANIPULATE
my_list = [1,2,3,4,5]
item = my_list.pop()
print(item)
print(my_list.pop(2))
# print(my_list.pop(4))  --> index error

# remove() --> does NOT return anything --> pass in value we want to remove(first occurance only)
names = ['rao','messi','ronaldo','zlatan','puffs']
names.remove('puffs')
print(names)

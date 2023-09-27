# ADD ITEM METHODS

list =[1,2,3,4]

# append() --> one item only to EOL
list.append(5)
print(len(list))
print(list)

list.append([6,7])
print(len(list))
print(list)

my_list = [1,2,3,4,5]
# extend() --> many items to EOL
my_list.extend([6,7])
print(len(my_list))
print(my_list)

# insert(idx,item) 
addList = [1,2,3,4]
addList.insert(2,'hi!')
print(addList)

addList.insert(-1,'last')
print(addList)

addList.insert(len(addList), 'LAST')
print(addList)


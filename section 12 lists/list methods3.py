# MORE LIST METHODS

# index(item,start,end)
list = [1,2,34,4,4,45,66,7,8,8,8,9]
print(list.index(2))
print(list.index(4,4))
# print(list.index(7))  gives error

print(list.count(2))
print(list.count(4))
print(list.count(41))

# in-place
forward = [1,2,3,4]
forward.reverse()
print(forward)

# sort() -> in-Place
num = [8,2,4,3,5,1]
num.sort()
print(num)

# string method that works on lists
words = [ "coding",'is','fun!']
print(' '.join(words))
print(words)



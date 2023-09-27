# reversed - return a reverse iterator 
# used when we want iterate over an obj

# list method inplace
nums =[1,2,3,4]
nums.reverse()
print(nums)

print(reversed(nums)) #gives list_reverseiterator object
print(list(reversed(nums))) #[1, 2, 3, 4]

for char in reversed('hello world'):
    print(char)
    
# using slice
print('hello'[::-1]) #olleh

print(list(reversed('hello'))) #['o', 'l', 'l', 'e', 'h']
print(''.join(list(reversed('hello')))) #olleh

#reversed iterator
for x in reversed(range(0,10)):
    print(x)
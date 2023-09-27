# 1.multiple assignments
n, m = 0, "abc"
print(n,m)
a, b, c = 0.125, "abc", True
print(a,b,c)

# 2.Increment/decrement
n = n+1 #good
n += 1 #good
# n++  #bad

# 3.None is null(absence of value)
n = 4
n = None
print("n=",n)

# 4.If statements don't require aprenthesis or curly braces
n=1
if n > 1:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# 5.Parenthesis needed for multiline conditions
# and = &&
# or = ||
n, m = 1,2
if((n > 2 and n != m) or n == m):
    n += 1

# 6.while loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

# 7.for loops
# ex1 = looping from i = 0 to i = 4
for i in range(5):
    print(i, end=" ")
    
# ex2 = looping from i = 2 to i = 5
for i in range(2,6):
    print(i)

# ex3 = looping from i = 5 to i = 2 and decrementing by 1(i.e,-1)
for i in range(5,1,-1):
    print(i, end=" ")

# 8.division is decimal by default
print(5/2)

# Double slash rounds down(like integer division)
print(5//2)

# CAREFUL:most languages round towards 0 by default so negative numbers will round down
print(-3//2)

# A workaround for rounding towards 0 is to use deciaml division and then convert to int.
print(int(-3/2))

# 9.Modding is similar to most langauges
print(10 % 3)

# Expect for negative values(we get unexpected results)
print(-10 % 3)  #2

# To be consistent twith other languages modulo(C based languages like - c++,java and JS)
import math
print(math.fmod(-10, 3))  #-1

# More math helpers
print(math.floor(3/2))  #rounddown
print(math.ceil(3/2))   #roundup
print(math.sqrt(2))     #sqrt
print(math.pow(2,3))    #power of a variable raised to another

# Max / Min int
print(float('inf'))  #positive infinity
print(float('-inf'))  #negative infinity

# Python numhers are infinite so they never overflow
print(math.pow(2,200))

# But still less than infinity
print(math.pow(2,200) < float("inf"))

# 10.Arrays (called lists in python) - dynamic by default
arr = [1,2,3] #declaring and intializing
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# unlike pushing or popping from an array inserting into middle
# of an array is a Big O(n) operation
arr.insert(1,7) #insert 7 at index 1 insert(idx, obj)
print(arr)

# const-time operation - indexing an rarray and then reading or writing into an array
arr[0] = 0
arr[3] = 0
print(arr)

# Initialize an array of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

#careful: -1 is not out of bounds, 
# it's the last value
arr = [1,2,3]
print(arr[-1])

# Indexing -2 is the second to the last value, etc
print(arr[-2])

# Sublists (aka slicing) - super useful feature
arr = [1,2,3,4]
print(arr[1:3]) #[1,2] excluding 3rd index

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# Unpacking (also super useful)
# - taking all the individual elements of an array and assigning them to variables
a, b, c = [1, 2, 3]
print(a, b, c)

# be acreful though - number of variables on LHS = RHS
# a, b = [1,2,3] #error

# 11.Loop through arrays
nums = [1,2,3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index 
for n in nums:
    print(n)

# with index and value 
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
# zip is a helper func that takes both the arrays an combines them into pairs and then unpack the values.
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    
# Reverse 
nums = [1,2,3,4]
nums.reverse()
print(nums)

# Sorting 
arr = [5,4,3,7,8,9]
arr.sort() #ascending by default
print(arr)

arr.sort(reverse=True) # descending
print(arr)

# sorting a string 
arr = ['bob','alice','jane','doe']
arr.sort()
print(arr)

# custom sort (by lenght of string)
arr.sort(key=lambda x:len(x))
print(arr)

# List comprehensions -  allows you to generate a new list by applying an expression 
# to each item in an existing iterable
arr = [i for i in range(5)]
print(arr)

arr = [i+i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]  #[0,0,0,0] * 4 , 4 from i in range(4)
print(arr)

# this won't work - all the rows are same and modifying any one will modify all.
# (not creating 4 unique rows here)
arr = [[0] * 4] * 4
print(arr)

# 12.Strings are similar to arrays
s = 'abc'# or s = "abc"
print(s[0:2])

# But they are immutable
# s[0] = "A"  - cannot re-assign at index 0 - Error
print(s)

# so this creates a new string - so anytime we update a String - bigO(n) operation
s += 'def'
print(s) #allowed

# Strings can e converted to integers and those integers can be added
# Valid numeric strings can be converted
print(int('123') + int('123'))  #246

# And numbers can be converted to strings
print(str(123) + str(123))  #123123 - appends those strings

# In rare cases you may need the ASCII value of a char
print(ord('a'))
print(ord('b'))

# Combine a list of strings (with an empty string delimitor i.e, "" - empty string literal)
strings = ['ab','cd','ef']
print("".join(strings))
print(" ".join(strings))

# 13.Queues (double ended queue) - by default
from collections import deque

queue = deque()
queue.append(1)  #to right end
queue.append(2)
print(queue)

# const time operation
queue.popleft()  # from left
print(queue)

queue.appendleft(1)  #added to left-side
print(queue)

queue.pop()  #popped from right-side
print(queue)

# 14.hashSets - useful as can search and insert values in const-time 
# Unlike a list there cannot be any duplicates in an hashSet 
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

# confirm presence of elem in set using  the "in" operator
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1,2,3]))

# Set comprehension
mySet = { i for i in range(5) }
print(mySet)

# 15.hashMap (aka dict - collection of key:pair values) - most commonly used data structure
#no duplicate keys allowed
myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77
print(myMap)
print(len(myMap))   #gives the number of keys

myMap['alice'] = 80
print(myMap['alice'])

# search if keys exists in hashmap - const time
print('alice' in myMap)
myMap.pop('alice')
print('alice' in myMap)

#initializing a hashmap
myMap = {'alice':90,'ramesh':69}
print(myMap)

# Dict comprehension
myMap = { i:i*2 for i in range(4) }
print(myMap)

# Looping through maps
myMap = {'alice':90,'bob':69}
# using keys
for key in myMap:
    print(key, myMap[key])

# using val
for val in myMap:
    print(val)

# unpacking - concise way of writing first method above
for key, val in myMap.items():
    print(key, val)
    
# 16.tuples are like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify
# tup[0] = 0  Error

# Can be used as key for hash map/set 
myMap = {(1,2): 3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print(mySet)
print((1,2) in mySet)

# Lists are not hashable and can't be used as keys to hahs Maps/sets
# myMap[[3,4]] = 5 TypeError: unhashable type: 'list'

# 17.heaps - commonly used to find the min and maximum value of a set
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# In python heaps are always min heaps by default
# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap)) #ascending as it is minHeap by default
    
# No max heaps by default,
# work aroud is to use min heap and multiply by -1 when push & pop 
# (to negate/confirm the values are stored and printed from max to min i.e, maxHeap) 
maxHeap = []
heapq.heappush(maxHeap, -3) 
heapq.heappush(maxHeap, -2) 
heapq.heappush(maxHeap, -4) 

# Max is already at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
    
# Build heap from initial values
arr = [2,1,8,4,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# 18.Functions
def myFunc(n,m):
    return n * m

print(myFunc(2,3))  #6
print(myFunc(3,4))  #12

# 19.Nested functions have access to outer variables
def outer(a,b):
    c = 'c'
    def inner():
        return a + b + c
    return inner()

print(outer('a','b'))
    
# Can modify objects but not reassign values unless using nonlocal keyword
def double(arr, val): #here array is an object but val is an value
    def helper():
        # Modifying array works(also modyfies original array)
        for i, n in enumerate(arr):
            arr[i] *= 2 
            
        # will only modify val in the helper scope
        # val *= 2
        
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)

# 20.class
class myClass:
    # Constructor -> always called  __init__
    def __init__(self,nums): # "self" is like "this" keyword in other languages 
        # Create member variables
        self.nums = nums
        self.size = len(nums)
        
    # self keyword required as param
    def getLenght(self):
        return self.size
    
    def getDoubleLenght(self):
        return 2 * self.getLenght()
    
    
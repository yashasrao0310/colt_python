# generator expression - easier syntax to create generators
# (like list comprehension are to lists)
# we use () instead of []

def nums():
    for num in range(1,10):
        yield num
        
g1 = nums()
print(g1) #<generator object nums at 0x00000206B8644190>

g2 = (num for num in range(1,10))
print(g2) #<generator object <genexpr> at 0x00000206B8645D20>

list1 = sum([num for num in range(1,10)])
print(list1) #45

gen1 = sum((num for num in range(1,10)))
print(gen1) #45

import time

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f'sum(n for n in range(10000000)) took: {gen_time}')
print(f'sum([n for n in range(10000000)]) took: {list_time}')


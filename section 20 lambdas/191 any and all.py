# all - return True if all elements of the iterable are truthy(or if the iterable is empty)
print(all([0,1,2,3]))  # false

print(all([char for char in 'eio' if char in 'aeiou']))  #True

print(all([num for num in [2,4,6,8,10] if num %2 == 0]))  #True

people = ['Charlie','Casey','Cody','Carly','Cristina']
print([name[0]=='C' for name in people]) #[True, True, True, True, True]
# check if all elemnts start with a 'C'
print(all([name[0]=='C' for name in people])) #true

people.append("Kristy")
print(all([name[0]=='C' for name in people])) # false

# check if all elemnts are even
nums = [2,6,28,18,21]
print(any([num %2 == 0 for num in nums])) #true
print(any([num %2 == 1 for num in nums])) #true
print(any([num %2 == 2 for num in nums])) #false

# any - returns True if any element in the iterale is truthy.
# If the iterable is empty, return False.

print(any([0,1,2,3]))  # true

print(any([val for val in [1,2,3] if val > 2]))  #True

print(any([val for val in [1,2,3] if val > 5]))  #false

#generator expressions - don't have to add [] brackets to makae things lighter - less space 
# use when u don't need to store it or use again. ex:passing into a func once like all and any
print((name[0]=='C' for name in people))  #<generator object <genexpr> at 0x0000023929965EB0>

# generator exp takes less memory than list comprehension in system memory
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print('To do the same thing, it takes...')
print(f'List comprehension: {list_comp} bytes')
print(f'Generator Expression: {gen_exp} bytes')


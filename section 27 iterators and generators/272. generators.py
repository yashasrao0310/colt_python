# generators - are a subset of iterators.
# (every generator is a iterator but viceversa is not true)
# NOTE: quick-short way of creating an iterator
# can be created in 2 ways:
    #1.using keyword "yield"
    #2.using generator expressions
    
# NOTE: quick-short way of creating an iterator
# generator function - uses "yield" instead of return
# can yield multiple times
# when invoked returns a generator which is an iterator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count     #pauses on hitting yield returns a generator-obj - waits for next() to be called - keeps record of the state of the variables
        count += 1

counter = count_up_to(5)
# print(counter()) #TypeError: 'generator' object is not callable
print(counter) #generator-obj
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) #StopIteration

# print(help(counter)) #gen-obj has next() and iter() builtin

counter1 = count_up_to(10)
print(next(counter1)) #1
print('\n')
#NOTE: for loop automatically catches StopIteration and stops looping 
for num in counter1: #2 to 10
    print(num) 
    
counter2 = count_up_to(10)
print(list(counter2))  #takes each obj all at once puts into list n returns the list


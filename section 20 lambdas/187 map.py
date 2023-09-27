# MAP - a standard function which accepts atleast two args: a function and an iterable
    # - get a map object in return - upgraded iterable
# Note:Map objects can be iterated only once

# ex1
nums = [2,3,4,5,6]
# doubles = map(lambda x:x*2,nums)
doubles = list(map(lambda x:x*2,nums))
print(doubles)  # returns map object

# iterating over map object
for num in doubles:
    print(num , end=" ")
    
# ex2
people = ["Yashas","ramesh",'suresh','kamlesh']
peeps = map(lambda name:name.upper(),people)
print(list(peeps))

# ex3
names = [
    {'first':'colt','last':'Steele'},
    {'first':'rusty','last':"steele"},
    {'first':'masty','last':'mamu'}
]

first_name = list(map(lambda x:x ['first'], names))
print(first_name) # ['colt', 'rusty', 'masty']

last_name = list(map(lambda x:x ['last'], names))
print(last_name)  # ['Steele', 'steele', 'mamu']

# ex4
def doubles(x): return x*2
print(list(map(doubles,nums)))


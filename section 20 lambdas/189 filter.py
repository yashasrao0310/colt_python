# FILTER: - there is a lambda for each value in the iterable.
    # -return filter object which can be converted into other iterables
    # -the object contains only values that return true to the lambda. 
# NOTE:lambda needs to have a boolean expression(similar to map but with an expression to filter)


# ex1 
l = [1,2,3,4,5,6]
evens = list(filter(lambda x:x%2 == 0,l))
print(evens) # printing out the evens

# ex2
names = ['anthony','austin','paul','bob','charlie','ashok']
a_names = filter(lambda x:x[0]=='a',names)
print(list(a_names)) # list of names that start with an "a"
print(a_names) # filter object

# ex3
users = [
    {'username':'samuel','tweets':['I love cake','i love cats']},
    {'username':'katie','tweets':['I love my cat']},
    {'username':'jeff','tweets':[]},
    {'username':'bob123','tweets':[]},
    {'username':'doggo_luvr','tweets':["dogs are the best"]},
    {'username':'guitar gal','tweets':[]}
]

# [] '' 0 - are inherently falsy 
# inactive_users = list(filter(lambda u: len(u['tweets'])==0 ,users))
# print(inactive_users)       

# OR negate true with "not"
# using filter:
inactive_users = list(filter(lambda u: not u['tweets'] ,users))
print(inactive_users)

# using list comprehension:
inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2) 

# active users
active_users = list(filter(lambda u: u['tweets'] ,users))
print(active_users)

# Combining filter and map 
# return a list with the string 'Your instructor is' + each value in
# the array but only if the value is less than 5 characters
names = ['Lassie','Colt','Rusty','Ram',"katey"]
result = list(map(lambda name:f"Your instructor is {name}",
                filter(lambda value: len(value) < 5, names)))
print(result) # ['Your instructor is Colt', 'Your instructor is Ram']

# List comprehension
# Same question as above
names = [f"Your instructor is {name}" for name in names if len(name) < 5]
print(names)

# or using list comprehension
inactive_users2 = [user['username'].upper() for user in users if not user['tweets']]
print(inactive_users2) 

# inactive users
usernames = list(map(lambda user:user['username'],filter(lambda u: not u['tweets'] ,users)))
print(usernames)




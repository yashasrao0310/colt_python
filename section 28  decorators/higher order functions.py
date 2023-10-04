# higher order function - a function which accepts a function as an arg or returns one or more functions 

# ex1 - passing func as an argument
def sum(n , func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x**3

print(sum(3, square))
print(sum(3, cube))

# ex2 - we can nest functions one inside another
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there! ','Go away ','I love you '))
        return msg
    
    result = get_mood() + person
    return result

print(greet('Toby'))

# ex3 - return func from another function
# def make_laugh():
#     def get_laugh():
#         l = choice(("Hahaha",'lol','tehehe'))
#         return l
    
#     return get_laugh

# laugh = make_laugh()  #returns a function
# print(laugh) #<function make_laugh.<locals>.get_laugh at 0x000001EDA9CB1CF0>
# print(laugh()) #correct one

# ex4 - Inner function can access outer function scope
def make_laugh_at(person):
    def get_laugh():
        laugh = choice(("Hahaha",'lol','tehehe'))
        return f'{laugh} {person}'
    
    return get_laugh

laugh_at = make_laugh_at("Raju")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())

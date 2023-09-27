# called anonymous functions in languages like javascript
# ex1 - normal - named function
def square(num): return num*num
print(square(9))

# ex2 - lambdas
square2 = lambda num :num*num
print(square2(9))

# ex3
add = lambda a,b:a+b
print(add(3,10))

#Note: __name__ is a special built-in variable which evaluates to the name of the current module
print(square.__name__)
print(square2.__name__)
print(add.__name__)
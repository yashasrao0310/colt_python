# ex1 - functions with different signatures

# most frequently the wrapper funcs that are decorator returns will accept an 
# unlimited number of arguments and keyword args
def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "lol"

print(greet("todd"))
# print(order("burger","fries"))
print(order(side="burger",main="fries"))
print(lol())





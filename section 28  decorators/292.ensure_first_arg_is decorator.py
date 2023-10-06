# implementing deacorator which accepts an argument - needs an extra intermediate layer
from functools import wraps

#we are constructing and returning a decorator(inner) 
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs) 
        return wrapper
    return inner
    
# we are constructing and returning a decorator(inner) 
# when wrapping a func with a decorator with an arg(val) using that val
@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)
    
print(fav_foods("burrito",'ice cream'))
print(fav_foods('ice cream',"burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10,2))
print(add_to_ten(2,10))

# NOT WORKING CODE!

# when we write
# @decorator
# def func(*args, **kwargs):
#     pass

# # we're really doing
# func = decorator(func)

# # when we write
# @decorator_with_args(arg)
# def func(*args, **kwargs):
#     pass

# # we're really doing
# func = decorator_with_args(arg)(func)
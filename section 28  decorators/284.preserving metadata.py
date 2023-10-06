from functools import wraps
#wraps preserves a functions metadata(name and docstring) which are trying to wrap or decorate
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM A WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    """ADDS TWO NUMBERS TOGETHER"""
    return x+y

# print(add(10,30)) #no problem

# problem - we get wrapper func not add - sepecially when other people wroking with our code.
print(add.__doc__)
print(add.__name__)
help(add) 

# ex2 - solve using module called functools
# from functools import wraps
#wraps preservs a function's metadata when it is decorated(here fn())

# def my_decorator(fn):
#     @wraps(fn)
#     def wrapper(*arhs,**kwargs):
#         pass
#     return wrapper

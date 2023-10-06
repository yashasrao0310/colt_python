# another comman usecase od decorators is to enforce certain restrictions on arguments
# ex: prevent a function 
# from being called with any numeraical args or with **kwargs 
from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")

# greet("Tony") 
greet(name="Tony")


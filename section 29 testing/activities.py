# UNIT TEST:(testing framework)
# test small parts of an application in isolation(eg: units)
# good candidates for unit testing: individual classes, modules or functions. 
# bad candidates for unit testing: an entire application, dependencies across several classes or modules

# pytohn comes with a builtin module called unittest
# you can write unit tests encapsulated as classes that inherit from unittest.TestCase
# This inheritamce gives you access to many assertion helpers that let you test the behaviour of the functions
# you can run your tests by calling unittest.main()
from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean!")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"

    
def nap(num_hours):
    if num_hours >+ 2:
        return f"Ugh I overslept. I didn't measn to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return choice(('lol','haha','tehehe'))
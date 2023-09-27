# use pre written modules/packages/code that other developers have written 
# why modules? - keep python files small(DRY) 
# - reuse code across multiple files by importing 
# - a module is just a python file.

# types of modules:
#   1.User-defined(Custom) modules: written by us, used in other files
#   2.Built-in modules: come with python by default, still manually import them to use them.
#   3.External modules: are downloaded from the internet.(on PyPI.org - Python Package Index)
# link to python doc: https://docs.python.org/3/py-modindex.html

# 1.import random 

# print(random.choice(['apple','mango','grapes','durian','berry']))
# print(random.randint(0,100))
# # print(random.shuffle(['apple','mango','grapes','durian','berry']))

# # 2.alias the module name - with "as" keyword
# import random as rand

# print(rand.choice(['apple','mango','grapes','durian','berry']))
# print(rand.randint(0,100))

# importing parts of a module - using "from" keyword
# Note: ROT - rule of thumb - only import what you need! 
# SYNTAX: from MODULE import * , * means everything

# 3.from random import choice, randint #choice , randint available individually now under there own name
# print(choice(['apple','mango','grapes','durian','berry']))
# print(randint(0,100))

# meth4
from random import choice as pick , randint as magic_number_chooser
print(pick(['apple','mango','grapes','durian','berry']))
print(magic_number_chooser(0,100))

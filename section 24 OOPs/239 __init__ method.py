# Classes in python can have a special __init__ method, 
# which gets called everytime you create an instance of a class(instantiate).

# self - refers to the current class instance(object) 
# - self must always be the first parameterto __init__ and
# any methods and properties on class instances.

# example
# class Vehicle:
#     def __init__(self, make , model, year):
#         self.make = make
#         self.made = made
#         self.year = year

class User:
    #called everytime and instance of a class is instantiated.
    def __init__(self, name, last, age):
        #attributes
        self.first = name
        self.last = last
        self.age = age

# self - way to refer to the current individual instances(object) of the class
# two instances of the User class 
user1 = User("Joe",'aesthetics', 35)
user2 = User("Blanca",'lopez', 43)
print(user1.first,user1.last)
print(user2.first,user2.last)



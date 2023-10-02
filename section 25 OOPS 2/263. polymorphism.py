# Polymorphism  - key principle of OOP is the idea of polymorphism 
# - an object can take on many(poly) forms(morph)

# 2 practical applications:
#   1.The same class method works in a similar way for different classes.
    # Cat.speak() #meow
    # Dog.speak() #woof
    # Human.speak() #yo
    
#   2.same opration works for different types of objects.
# sample_list = [1,2,3]
# sample_tuple = (1,2,3)
# sample_string = "awesome"

# print(len(sample_list))
# print(len(sample_tuple))
# print(len(sample_string))

# example 1.method overriding 
# - a common implementation of this is to have a method in a base(or parent) class 
# that is overriden by a subclass.
# - each method of the sublass will have a different implementation of the method.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")
# NOTE: NotImplementedError - builtin error used when we can to define a class and basically enforce that whatever
# the name of the method is (speak)should be implemented on anything that inherits from Animal  
class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())
# f = Fish()
# print(f.speak())

# Example 2.Special Methods - dunder methods- also called magic methods
# Same operation works for different types of objects.
print(8+2)
print('8'+'2')



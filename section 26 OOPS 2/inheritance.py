# In python, inheritance works by passing the parent class as an argument 
# to the definition of a child class. 

class Animal:
    # class attribute
    cool = True
    
    def make_sound(self, sound):
        print(f"this animal says {sound}")
    
class Cat(Animal):
    pass

# a = Animal()
# a.make_sound("chirp")
blue = Cat()
# blue.make_sound("meow!")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

# built-in function to find class of an obj 
# everything in python inherits from the base "object" class 
print(isinstance(blue, object))
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance([1,2,3,4], list))
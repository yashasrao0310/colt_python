import random

class Hat:
    # def __init__(self):
    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    
    @classmethod
    def sort(cls, name): #cls refers tothe class itself
        print(name, "is in", random.choice(cls.houses)) #access class variable not local variable that belongs to the method.

# hat = Hat()  #no need to instantiate a class
Hat.sort("Harry")  

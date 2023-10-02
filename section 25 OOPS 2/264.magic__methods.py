# Special/magic methods - dunders - control how python behaves with our objects of a 
# human defined class

# ex1
# class Human:
#     def __init__(self, height):
#         self.height = height
        
#     def __len__(self):
#         return self.height
    
# colt = Human(60)
# print(len(colt)) #60

# ex2
from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other): #self is first aperand and other is the other operand.
        if isinstance(other, Human):
            return Human(first = "Newborn", last = self.last, age=0)
        raise TypeError("You can't add that!")
    
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't multiply"

j = Human("Jenny","Larsen", 47)
k = Human("Kevin","jones", 46)

print(j)
print(len(j))

# triplets = j * 3 
# triplets[1].first = "jessica"
# print(triplets)
# print(2 * j) #error - so order definitely matters. 

# kevin and jessica having triplets!
triplets = (k + j) * 3
print(triplets)


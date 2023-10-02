class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0
            
    # def get_age(self):
    #     return self._age      
        
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0
    
    @property #turns method into property
    #useful as a getter
    def age(self):
        return self._age
    
    #setter
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be nagative")
        
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane","Godall", -34)
# print(jane.get_age()) v/s print(jane.age) is just "syntactic sugar" - easier to typeor access
# jane.set_age(45)
# print(jane.get_age())
print(jane.age) #34 
jane.age = 20
print(jane.age) #20
print(jane.full_name)
jane.full_name = "Yashas Rao"
print(jane.__dict__)


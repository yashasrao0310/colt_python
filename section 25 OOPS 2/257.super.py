class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
    def make_sound(self, sound):
        print(f"This animal says {sound}")
    
class Cat(Animal):
        def __init__(self, name, breed, toy):
            # Animal.__init__(self, name, species) or else we can write or use
            # super refers to the base or parent class of the current child class - no need to pass in "self"
            # here returns Animal and run __init__ and pass self as first argument.
            super().__init__(name, species="Cat")
            self.breed = breed
            self.toy = toy
            
        def play(self):
            print(f"{self.name} plays with {self.toy}")
    
blue = Cat("Blue", 'Scottish Fold',"String")
blue.play()
# print(blue.species)
# print(blue.breed)
# print(blue.toy)

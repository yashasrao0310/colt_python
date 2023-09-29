# creating validations - creating a list of permitted entries(ex:lions
# are not permitted to be made in class Pet)
# A class attribute is shared by all instances of the class(not need to define separately .ex: here allowed)
# Note: actual instances can still access class attributes (unique to python)
class Pet:
    allowed = ['cat','dog','fish','rat'] 
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!" )
        self.name = name
        self.species = species
        
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!" )
        self.species = species
        
cat = Pet('Blue','cat')
dog = Pet('Simba','dog')

# cat.allowed and dog.allowed POINT to the same allowed class attribute
# id() - gives memory id or address python has assigned to an object.
# Note: actual instances can still access class attributes (unique to python)
print(id(cat.allowed)) #1964717190400 #reference to Pet.allowed
print(id(dog.allowed)) # same as above #reference to Pet.allowed
print(id(Pet.allowed)) # same as above

# you can do self.allowed instead of Pet.allowed but only to access it(pointing to Pet.allowed anyway)
# but 
cat.allowed = ['tiger','bear'] #point to an instance attribute(disassociated from class attribute(Pet.allowed)) 
print(cat.allowed)
print(id(cat.allowed))

print(Pet.allowed)
print(id(Pet.allowed))
print(id(dog.allowed))

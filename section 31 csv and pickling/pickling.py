# PICKLING(just like pickling/storing something without spoiling it to be used later)

# Pickle is a Python module used for serializing(into a byte stream - binary code) and deserializing Python objects.
# It allows you to save Python objects to a file and later load them back into memory. 
# Pickling is often used for saving the state of a program or for transferring data between
# different Python processes

import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

# blue = Cat("Blue","Scottish Fold","String")

# serializing
# # need to write wb(writing binary) for binary stream conversion
# with open("pets.pickle",'wb') as file:
#     pickle.dump(blue, file)
    
# deserializing, rb - reading binary
with open("pets.pickle",'rb') as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())
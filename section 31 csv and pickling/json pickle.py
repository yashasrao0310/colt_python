# json - javascript object notation -  a data format(representation)

# initially created to represent javascript objects
# used to sent JS code from one computer to another over the web

#json.dumps() -  formats a python object as a String of JSON - and returns a STRING.
# import json 

# class Cat:
# 	def __init__(self, name, breed):
# 		self.name = name
# 		self.breed = breed
# c =Cat("Charles","Tabby")
# # j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  #no tuples in JSON
# j = json.dumps(c.__dict__)

# print(j)

# jsonpickle - is a Python library for serialization and deserialization of 
# complex Python objects to and from JSON

import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles","Tabby")

# with open("cat.json",'w') as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open("cat.json",'r') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)

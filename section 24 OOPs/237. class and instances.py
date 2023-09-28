# classes follow CamelCase by convention
# variables and functions - snake_case
class User:
    pass

user1 = User()
user2 = User()
user3 = User()
user4 = User()
print(type(user1)) #<class '__main__.User'>
print(type(user2)) #user1 and user2 are different(see memory location)

# an instance attribute and method are defined on each instance of a class 
# call attributes are defined directly on a class that are shared by all
# instances of a class and the class itself.(defined once and lives on the class itself)

# call attributes and methods are used far less often than instance attributes and methods

class User:
    active_users = 0
    def __init__(self, name, last, age):
        #attributes
        self.first = name
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out!'    
    
    #instance method  - self is passed as first parameter always
    def full_name(self):
        return f'{self.first} {self.last}' 
    
    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'

    # thing is individual instance 
    def likes(self, thing):
        return f'{self.first} likes {thing}'
    
    def is_senior(self):
        return self.age >= 65
        
    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th, {self.first}'
        

# print(user2.first,user2.last)
# print(user1.full_name())
# print(user2.full_name())
# print(user1.initials())
# print(user2.initials())
# print(user1.likes('Ice Cream'))
# print(user2.likes('Chips'))
# print(user1.is_senior())
# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# print(user2.birthday())

# class arttibute
print(User.active_users) #0
 
print(User.active_users) #2
print(user2.logout()) #Blanca has logged out!
print(User.active_users) #1

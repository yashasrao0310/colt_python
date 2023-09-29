# class methods - are methods (with the @classmethod decorator)
# that are not concerned with instances, but the class itself.

# ex 
# class Person:
#     #...
#     @classmethod # signifies next method is a class method
#     def from_csv(cls, filename):
#         return cls(*params)  #this is same as calling Person(*params)
    
# Person.from_csv(my_csv)

class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
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
    
user1 = User("Joe",'Aesthetics', 68)
user2 = User("Blanca",'Lopez', 43)
print(User.display_active_users())
user1 = User("Joe",'Aesthetics', 68)
user2 = User("Blanca",'Lopez', 43)
print(User.display_active_users())

# user1.display_active_users() # allowed but not prefered
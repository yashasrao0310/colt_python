# [].pop() method in an obj but print() is not aa method on an obj 
# instance method - every instance of a class as its own method 
class User:
    #called everytime and instance of a class is instantiated.
    def __init__(self, name, last, age):
        #attributes
        self.first = name
        self.last = last
        self.age = age
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
print(user1.first,user1.last)
print(user2.first,user2.last)
print(user1.full_name())
print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.likes('Ice Cream'))
print(user2.likes('Chips'))
print(user1.is_senior())
print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)
print(user2.birthday())

class User:
    active_users = 0
    # If data is coming into one format and you need to convert it to
    # another format before init is called
    @classmethod  #cls(className) is always passed in first
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first,last,int(age))      # cls = User
    
    def __init__(self, name, last, age):
        #attributes
        self.first = name
        self.last = last
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        return f"{self.first} is {self.age}"
    
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

#creating new user named Tom - using class method
tom = User.from_string("Tom,Jones,89")
# __repr__ - allows us to define a representation of an object(CUSTOM REPRESENTATION)
# - we can control what it looks like before printing it.
#<__main__.User object at 0x0000017A0596BBB0> is print(obj) before __repr__()
print(tom) 

j = User('judy','steele',18)
j = str(j)
print(j)

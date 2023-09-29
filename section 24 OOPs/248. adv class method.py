# Usually class methods are used while creating new instance of a class.  
# If data is coming into one format and you need to convert it to another format before init is called

# dict().fromkeys - class method - not capitalised as its built-in.
# {}.keys - instance(object) method

# ex1
# data = dict().fromkeys(['name','age','city'],'unknown')
# print(data)
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
print(tom.first)
print(tom.full_name())
print(tom.birthday())


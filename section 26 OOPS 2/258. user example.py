class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first,last,int(age))      # cls = User
    
    def __init__(self, first, last, age):
        #attributes
        self.first = first
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
# tom = User.from_string("Tom,Jones,89")

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
        
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active users"
        
    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

u1 = User("tom","Garcia", 35)
u2 = User("tom","Garcia", 35)
u3 = User("tom","Garcia", 35)
ramesh1 = Moderator("Ramesh", 'Ramraj', 78, "rambhakt")
ramesh2 = Moderator("Ramesh", 'Ramraj', 78, "rambhakt")

print(User.display_active_users())
print(Moderator.display_active_mods())


# print(ramesh.full_name())
# print(ramesh.community)

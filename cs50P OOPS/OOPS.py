class Student:
    def __init__(self, name, house):
        self.name = name  #goes via setter function
        self.house = house  #goes via setter function
        # self.patronus = patronus
        
    def __str__(self):
        return f'{self.name} from {self.house}'

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    #Getter
    # @property
    # def house(self):
    #     return self._house
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name
    
    # #Setter
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house
    
    
    
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "Neighh"
    #         case "Dog":
    #             return "WOff woff"
    #         case "Cat":
    #             return "meow!"
    #         case _:
    #             return "Evil laugh!!"

def main():
    student = Student.get()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw" #tuple is immutable , TypeError
    # if student['name'] == "Padma":
    #     student['house'] = "Ravenclaw"

    # print(f"{student.name} from {student.house}") #use single quotes to access dict() elements - better
    # print("Expecto Patronum!")
    # print(student.charm())
    
    # student.house = "Number four, Pivot Drive" #can't override due to getter and setters
    # student._house = "Number four, Pivot Drive"
    print(student)
    
# def get_student():
#     # name = input("Name: ")
#     # house = input("House: ")
#     # # return name, house # returning one tuple with two items(when commas are used)
#     # return [name, house]
    
#     # student = {} #dict is better than list and tuple in the sense that - we dont have to remember which index is name or house.
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return {'name':name, 'house':house} #dicts are mutable

#     name = input("Name: ")
#     house = input("House: ")
#     # patronus = input("Patronus: ")
#     return Student(name, house)
    
#conditional used to avoid accidentally running main when weare making a module /package
if __name__ == "__main__":
    main()


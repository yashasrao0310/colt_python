# there is no such thing as a private attribut or method 
# _name - convention by developers to say - its PRIVATE(for internal use only)method or property
# __name - name mangling - python changes/mangles the name of the attribute or method behind the scenes(SO can't be called)
# __name__ - dunder method (don't override)

# defining our own dunder methods ia a bad idea 
# - bcs it should be only used to reference or OVERRIDE THAT ALREADY EXISTS AND IS SPECIAL(magic methods) 

class Person:
    def __init__(self):
        self.name = 'Tony'
        self._secret = 'HI!'
        self.__msg = "I LIKE TURTLES" #purpose is to make this attribute specific to this person class
        self.__lol = "hahahhah"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         let them in
        
p = Person()

print(p.name)
print(p._secret)
# print(p.__msg) #name mangling - AttributeError: 'Person' object has no attribute '__msg'
print(dir(p)) #always mangled in this format - '_Person__msg' - "_ClassName__attributeUsed"
#so that no confusion during inheritance
print(p._Person__msg)
print(p._Person__lol)


# decorators are just functions that accept other functions, 
# they wrap them with some other functionality and then return that wrapper function 

# - are examples of higher order functions
# syntax: @decorator 

# ex1 - without @decator syntactic sugar
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# def greet():
#     print("My name is Colt")
    
# def rage():
#     print("I HATE YOU!")
    

# # we are decorating our function withpoliteness!
# greet = be_polite(greet)
# print(greet) #<function be_polite.<locals>.wrapper at 0x000001F3DB88B520>
# # () matters if want to access the contents 
# greet()

# polite_rage = be_polite(rage)
# polite_rage()

# ex2 - placing @function_name above the function it wants to be wrapped in(decorator syntax).
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite #be_polite wraps greet
def greet():
    print("My name is yashas.")

@be_polite #be_polite wraps rage
def rage():
    print("I HATE YOU!")
    
# we don't need to set
# greet = be_polite(greet)
greet()
rage()


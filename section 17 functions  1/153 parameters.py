def square(num):
    return num**2

print(square(4))
print(square(8))

def sing_happy_birthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print(f"Happy birthday to {name} dear!")
    print("Happy birthday to you!")
    
name = input("Name please: ")
sing_happy_birthday(name) #calling/invoking function.

def divide(num1,num2):
    return num1/num2

print(divide(2,5))
print(divide(5,2))
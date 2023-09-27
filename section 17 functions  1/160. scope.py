instructor1 = "marry"
def say_hello():
    instructor2 = "colt"
    return f"Hello {instructor2}"

say_hello()

print(instructor1)
# print(instructor2) #nameError not defined

# ex2
total = 0
def increment():
    global total
    total += 1
    return total

print(increment())

# ex3 - access a value - no change - works fine
name = "ramesh"
def greet():
    print(name)
    
greet()

# ex4 - nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())

# adding * to an argument unpacks the values in a collection like list or tuple - works with both tuples and list

def total_of_nums(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)
    
# nums = [1,2,3,4,5,6]
# total_of_nums(nums)
numbers = (1,2,3,4,5,6)
total_of_nums(*numbers)

# unpacking dictionaries - passing **kwargs as args
def display_name(first,second):
    print(f"{first} says hello to {second}")

names = {"first":"yashas","second":"rao"}

# display_name(names) #nope 
display_name(**names)
display_name(first="Colt",second="Sarah")

# ex2
def add_and_multiply_nums(a,b,c,**kwargs):
    print(a+b*c)
    print("Other stuff..")
    print(kwargs)
    
data = dict(a=1,b=2,c=3,d=55,cat="chad")
add_and_multiply_nums(**data,name="tony")
# add_and_multiply_nums(data) #Error
    
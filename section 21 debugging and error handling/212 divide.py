# Note:handling each error separately is recommended for specificity

# def divide(a,b):
#     try:
#         result =  a/b
#     except ZeroDivisionError:
#         print("dont' divide by zero please")
#     except TypeError as err:
#         print("a and b must be ints or floats")
#         print(err)
#     else:
#         print(f"{a} divided by {b} is {result}")

# another way - to combine the errors
def divide(a,b):
    try:
        result =  a/b
    except (ZeroDivisionError,TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

# print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))


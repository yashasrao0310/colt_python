# assert statement(NOT FUNCTION) - we can make simple assertions with the assert keyword.
# assert accepts an expression
# returns None if the statement id truthy
# returns an AssertionError if the expression is falsy 
# accepts an optional error message as a second argument 
# Note: not ideal as it can be overriden

# # ex1
# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# print(add_positive_numbers(1,1))
# print(add_positive_numbers(1,-1)) #AssertionError: Both numbers must be positive!

# ex2
def eat_junk(food):
    assert food in [
        'pizza',
        'ice cream',
        'candy'
    ], 'food must be junk food'
    return f"NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))
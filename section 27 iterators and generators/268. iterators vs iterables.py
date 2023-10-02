# iterator - an object that can be iterated upon.An object which returns data, 
# one element at a time when next() is called on it.

# iterable - An objet which will return an iterator when iter() is called on it.
# EX:"hello" ia an iterable, but is not an iterator.
# iter("hello") returns an iterator

# MECHANISM:
# the list is never directly looped over in a for loop
# the for loop calls iter, passes in the list and that returns on iterator
# that the loop will call next() on over an over till the end of list is reached

# iter(name) - takes in iterable returns an iterator.
# <str_iterator object at 0x000002929156AC20>

# name = "yashas"
# >>> next(name) -next() taeks in iterator - to go through each item in iterator until it raises a StopIterator error.
# TypeError: 'str' object is not an iterator


# len - return the lenght(the number of items) of an object.
# The argument may be a sequence (such as a string, tuple, list, or range) 
# or a collection(such as a dictionary,set)

print(len('awesome')) #7
print(len((1,2,3,4))) #4
print(len([1,2,3,4])) #4
print(len(range(0,10))) #10

print(len({1,2,3,4})) #4
print(len({'a':1,'b':2,'c':3})) #3

# dunder - double underscore method - we are not suppsed to call __len__() - JTK how it works
# len('hello') and 'hello'.__len__() are the same.
class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50

# round() - return digits rounded to ndigits precision after the deciaml point.
# If ndigits is omiited or None, it returns the nearest integer to its input. 
print(round(10.2)) #10
print(round(1.212121, 2)) #1.21 , 2 is number of decimal point it should round to
print(round(1.212121, 4))


# abs - return absolute value of a number i.e, magnitude of a real number without regard to its sign.
# The argument may be an integer or a floating number

print(abs(-5)) #5
print(abs(5)) #5

print(abs(-3.444)) #3.444
print(abs(3.444)) #3.444

print(abs(float('20'))) #20.0
# print(abs('20')) #error

# fabs - float abs() - everything as float first 
import math
print(math.fabs(4)) #4.0

# sum() - sums iterable item left to right , with optional start 

print(sum([1,2,3])) #6
print(sum([1,2,3],10)) #16
print(sum([1,2,3],-6)) #0
print(sum([1.2,2,3.8])) #7.0

print(sum({1,15,99})) #115



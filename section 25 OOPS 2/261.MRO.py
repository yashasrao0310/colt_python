# MRO - method resolution order i which is the order i which python will look for
# methods on instances of that class.

# you can programmatically reference the MRO three ways:
# 1.__mro__ attribute on the class 
# 2.use the mro() method of the class 
# 3.use the builtin help(cls) method - most used - better representation for humans

class A:
    def do_something(self):
        print("Method Defined in: A")
        
class B(A):
    def do_something(self):
        print("Method Defined in: B")
        
class C(A):
    def do_something(self):
        print("Method Defined in: C")
        
class D(B,C):
    def do_something(self):
        print("Method Defined in: D")
        super().do_something() #super refers to the next class in line.

# print(D.__mro__) #tuple
# print(D.mro()) #list
# help(D)

thing = D() 
thing.do_something()

    #     A
    #   /   \
    #  B     C
    #   \   /
    #     D
    # D,B,C,A,Object 
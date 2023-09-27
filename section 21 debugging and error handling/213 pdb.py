# pdb(python debugger is a python module) - tool to handle errors or bugs that don't break the code
# but give different o/p that we expect

# To set breakpoints in our code we can use pdb by inserting this line:
# import pdb;
# pdb.set_trace()

# Also commonly on one line 
# import pdb; pdb.set_trace()

# Common PDB Commands:
# # l(list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "third"
# result += third
# print(result)

# Note: be careful while using varaible names that are similar to pdb commands like c 
def add_numbers(a,b,c,d):
    import pdb;pdb.set_trace()

    return a+b+c+d
add_numbers(1,2,3,4)

# itr1
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
        
# # itr2
# def sum_all_nums(num1,*args):
#     print(num1)
#     total = 0
#     for num in args:
#         total += num
#     return total

# works with as many args as required
print(sum_all_nums(3,4,5,6,2))
print(sum_all_nums(3,4))

# ex2
def ensure_correct_info(*args):
    if "Yashas" in args and "rao" in args:
        return "Welcome back yashas"
    return "Not sure who you are"

print(ensure_correct_info(1,"True","Yashas","rao"))
print(ensure_correct_info("Yashas",False,67))
        

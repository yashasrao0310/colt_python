# SYNTAX: [ ___ for ___ in ___ ]
numbers = [1,2,3,4,5]
# convert to str
new_nums = [str(num) for num in numbers]
print(new_nums)

# ex2
# check if value is truthy or from django.utils.translation import ugettext_lazy as _
values = [0 ,'' , []]
check = [bool(value) for value in values]
print(check)

number = [ 12,34,45,67,]
print([num*10 for num in number])


# LC v/s looping
nums = [1,2,3,4,5]
double_nums = []
for num in nums:
    double_num = num*2
    double_nums.append(double_num)
    
print(double_nums)

# instead
nums = [5,6,7,8,9]
double = [num*2 for num in nums]
print(double)
    
friends = ['ramesh','suresh','tendulkar']
cap_friends = [friend[0].upper()+friend[1:] for friend in friends]
print(cap_friends)

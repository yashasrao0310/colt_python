def full_name(first,last):
    return f"Your name is {first} {last}"

print(full_name(last="rao",first="yashas"))
print(full_name(first="yashas",last="rao"))

def exponent(num,power=2): #default params
    return num**power

print(exponent(2,3))
print(exponent(power=3,num=2)) #keyword args
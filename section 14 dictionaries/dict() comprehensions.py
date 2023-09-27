# SYNTAX
# {___:__ for __ in ___}

numbers = dict(first=1,second=2,third=3)
squared = {key:value ** 2 for key,value in numbers.items()}
print(squared)

print({num:num*2 for num in range(1,5)})

str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

student ={"name":'yashas','city':'mysuru','color':'purple'}
caps = {k.upper():v.upper() for k,v in student.items()}
print(caps)

# conditional logic
cap2 = {(k.upper() if k is 'color' else k):v.upper() for k,v in student.items()}
print(cap2)

# parity check
numbers = [1,2,3,4,5]
check = {num:('even' if num%2 == 0 else "odd") for num in numbers}
print(check)

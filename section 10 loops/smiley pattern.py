# gross solution
# print('\U0001f600')
# n = int(input('enter number: '))
# for i in range(n):
#     for j in range(i+1):
#         print('\U0001f600', end='')
#     print('\n')


# with string multiplication
# for num in range(1,11):
#     print('\U0001f600' * num)

# times = 1
# while times < 11:
#     print('\U0001f600' * times)
#     times += 1

# without string multiplication
for num in range(1,11):
    count = 1
    smileys = ""
    while count <= num:
        count +=1
        smileys += '\U0001f600'
    print(smileys)    
    


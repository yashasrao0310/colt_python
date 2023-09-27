student = {
    'Name':'yashas',
    'owns_dog':'No',
    'num_of_courses':2,
    'favourite_language':'python',
    'is_hilarious':'True',
    69:'my_fav_num'
}

# getting keys
for key in student.keys():
    print(key)

# getting values
for value in student.values():
    print(value)

# getting keys and values
for key,value in student.items():
    print(f'key is {key} and value is {value}')

# check for presence of key or value i dict()
# checking for key only, by default  
print('Name' in student)
# or
if 'Name' in student:
    print("True")
print(4 in student)   #False
    
# check for values
if 'True' in student.values():
    print("True")
    
print(69 in student.values()) #False


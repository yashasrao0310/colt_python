# Tuple is a ordered collection like list but is IMMUTABLE
months = ('Jan','Feb','Mar',"April",'May','June','July','Aug','Sept','Oct','Nov','Dec')

for month in months:
    print(month)

i = len(months)-1
while i >= 0:
    print(months[i])
    i-= 1

print(months[2])
print(months[0])
# print(months[12]) index out of range

# Tuples can be taken as keys in dict()
location = {
    (2324.234,23.323):"Mysuru",
    (324.234,24.323):"Bnagalore",
    (231.234,25.323):"Mandya",
}
# a list used as a key would throw KeyError

# some dict() mwthods return list of tuple key:values
student = {
    'Name':'yashas',
    'owns_dog':'No',
    'num_of_courses':2,
    'favourite_language':'python',
    'is_hilarious':'True',
    69:'my_fav_num'
}
print(student.items())

# methods
numbers =(1,2,3,4,3,4)
print(numbers.count(2))
print(numbers.count(3))
print(numbers.count(5))  # no error thrown

print(numbers.index(3))
print(numbers.index(4))
print(numbers.index(5))   #error

# Note: can do SLICING and 2D matrixes just like with lists
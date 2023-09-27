student = {
    'Name':'yashas',
    'owns_dog':'No',
    'num_of_courses':2,
    'favourite_language':'python',
    'is_hilarious':'True',
    69:'my_fav_num'
}

# pop() --> removes given key:value pair and returns value -- takes atleast one arg
print(student.pop(69))
# keyError id key not present 
# print(student.pop("Names"))

# popitem() --> removes an item at random -- no args
d = dict(a=1,b=2,c=3,d=4)
print(d.popitem())

# update() add one dict to another
first = {'real_name':'ramesh','last_name':'ram_raj'}
second = {'player':'KL raju'}
second.update(first)
print(second)
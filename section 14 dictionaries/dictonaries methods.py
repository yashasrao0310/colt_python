student = {
    'Name':'yashas',
    'owns_dog':'No',
    'num_of_courses':2,
    'favourite_language':'python',
    'is_hilarious':'True',
    69:'my_fav_num'
}

# clear() --> returns empty dict()
student.clear()
print(student)

# fromkeys()  --> assigns values by taking an iterable object as key to each item of iterable object
names = ['yashas','sdgash','djfha','sfhad']
new_dict = {}.fromkeys(names,'initialise')
print(new_dict)

nums = {}.fromkeys(range(1,10),'might be the key')
print(nums)

# copy() --> gives a new copy of dict()
d= dict(a=1,b=2,c=3,d=4)
clone = d.copy()
print(clone == d)
print(clone is d)

# get() --> returns True or False instead of keyError if not present
print(d.get('a'))
print(d.get('shit'))

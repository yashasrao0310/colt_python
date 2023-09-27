
# set --> unordered set of data that's unique
s = set({1,22,3,4,5,4,5,6,7})
print(len(s))
print(s)

nums = {1,2,3,4,3,4}
print(nums)

print(1 in nums)
print(5 in nums)

numbers = {1,2,3,4}
for num in numbers:
    print(num)

print(list(set(nums)))

# METHODS
values = {1,2,3,4}
values.add(4)
print(values)
values.add(5)
print(values)

# remove()  --> gives error if not present while discard() does NOT
values.remove(4)
print(values)
values.remove(5)
print(values)

values.discard(3)
print(values)
values.discard(5)
print(values)

math_students = {'mathew','james','prasanth','helen','aparna'}
biology_students = {'mathew','james','charlotte','mesut','oliver','jane'}

# union | to generate a set with all my unique students
print(math_students | biology_students)
# intersection of students
print(math_students & biology_students)

# COMPREHENSIONS
set1 = {num**2 for num in range(5)}
print(set1)

print({char.upper() for char in 'hello'})

def are_vowels_in_strings(string):
    return len({char for char in string if char in 'aeiou'}) == 5
string = 'sequioa'
print(are_vowels_in_strings(string))

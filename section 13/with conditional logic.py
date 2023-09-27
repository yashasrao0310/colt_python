numbers = [1,2,3,4,5,6]
print([num for num in numbers if num%2 == 0])  #even numbers
print([num for num in numbers if num%2 != 0])  #odd numbers

# if lese syntax is different
test =[num*2 if num%2 == 0 else num/2 for num in numbers]
print(test)

with_vowels = "This is so much fun!"
test = [char for char in with_vowels if char not in "aeiou"]
print(test)
without_vowels = ' '.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)
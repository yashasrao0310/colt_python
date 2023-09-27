# max = return the largest item of an iterable or the largest of teo or more arguements. 
# min does the opposite of max
print(max(3,43,12)) #43
print(max('c','d','a')) #'d

print(max([2,3,4,2,5])) #5
print(max((2,3,4,2,5))) #5
print(max('awesome')) #'w - string is an iterable
print(max({1:'a',3:'c',2:'b'})) #3

nums = [2,4,6,4,1]
print(max(nums)) #6
print(min(nums)) #1

string = 'Hello world!'
print(max(string)) #'w'
print(min(string)) #" "

names = ["Arya",'Samson','Dora','Tim','Ollivander']
print(min(names)) #alphabetical order #Arya
print(max(names)) #Tim

# gen-exp 
print(min(len(name) for name in names))
print((len(name) for name in names)) #gen-obj
print([len(name) for name in names]) #list-obj #[4, 6, 4, 3, 10]

#longest name
print(max(names, key=lambda n:len(n))) #Ollivander
#shortest name
print(min(names, key=lambda n:len(n))) #Tim

songs = [
    {'title':'happy birthday','playcount':1},
    {'title':'Survive','playcount':13},
    {'title':'rara rakamma','playcount':11},
    {'title':'thalaivar','playcount':123},
]

print(min(songs, key=lambda s:s['playcount'])) #{'title': 'happy birthday', 'playcount': 1}
print(max(songs, key=lambda s:s['playcount'])) #{'title': 'thalaivar', 'playcount': 123}
# title of song with most playcount
print(max(songs, key=lambda s:s['playcount'])['title']) #thalaivar

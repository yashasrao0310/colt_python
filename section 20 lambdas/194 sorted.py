# sorted -returns a copy - does not change original (works on anything that is iterable)
more_nums = [2,5,34,2,7,6,9]
print(sorted(more_nums)) #[2, 2, 5, 6, 7, 9, 34]
print(more_nums) #[2, 5, 34, 2, 7, 6, 9]

# sort() - changes original iterable - Note: list specific methodv only
more_nums.sort()
print(more_nums) #[2, 2, 5, 6, 7, 9, 34]

print(sorted(more_nums, reverse=True)) #descending order
print(sorted((2,5,3,4,6))) #takes in tuple returns list

users = [
    {'username':'samuel','tweets':['I love cake','i love cats']},
    {'username':'katie','tweets':['I love my cat']},
    {'username':'jeff','tweets':[],'color':'purple'},
    {'username':'bob123','tweets':[],'num':10,'color':'teal'},
    {'username':'doggo_luvr','tweets':["dogs are the best"]},
    {'username':'guitar gal','tweets':[]}
]

# print(sorted(users,key=len))  #based on number of dict items
print(sorted(users,key=lambda user:user['username'])) #on username
# print(sorted(users,key=lambda user:len(user['tweets']))) #num of tweets
# print(sorted(users,key=lambda user:len(user['tweets']),reverse=True)) #num of tweets
print('\n')

songs = [
    {'title':'happy birthday','playcount':1},
    {'title':'Survive','playcount':13},
    {'title':'rara rakamma','playcount':11},
    {'title':'thalaivar','playcount':123},
]
print(sorted(songs,key=lambda song:song['playcount']))
print(sorted(songs,key=lambda song:song['playcount'],reverse=True))

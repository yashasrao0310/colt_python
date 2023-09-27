# zip - makes an iterator that aggregates elements from each of the iterables.
# - returns an iterator of tuples, where i-th tuple contains the the ith element from 
# each of the arguement sequence or iterables - goes from left to right
# - the iterator stops when the shortest input iterable is exhausted  

first_zip = zip([1,2,3],[4,5,6])
print(list(first_zip)) #[(1, 4), (2, 5), (3, 6)]

print(dict(first_zip)) #{}
print(dict(zip([1,2,3],[4,5,6]))) #{1: 4, 2: 5, 3: 6}
print(dict(zip([4,5,6],[1,2,3]))) #{4: 1, 5: 2, 6: 3}
print(first_zip) #zip object

nums1 = [1,2,3,4]
nums2 = [5,6,7,8,9] 
print(list(zip(nums2,nums1))) #[(5, 1), (6, 2), (7, 3), (8, 4)] - stops at shortest len of iterable

words = ['yo','ho','are','bol toh']
print(list(zip(words,nums1,nums2))) #[('yo', 1, 5), ('ho', 2, 6), ('are', 3, 7), ('bol toh', 4, 8)]

# using * operator to unpack a list of tuples
five_by_two = [(0,1),(1,2),(2,3),(3,4),(4,5)] 
print(list(zip(* five_by_two))) #[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# 204 next vid
midterms = [80,91,78]
finals = [89,78,99]
students = ['dan','ang','kate']

# required o/p: final_grades = {'dan': 89, 'ang': 91, 'kate': 99}

# final_grades = [pair for pair in zip(midterms, finals)]
# print(final_grades) #[(80, 89), (91, 78), (78, 99)]
# final_grades = [max(pair) for pair in zip(midterms, finals)]
# print(final_grades) #[89, 91, 99]

# using dict comprehension
final_grades = {t[0]:max(t[1],t[2]) for t in zip(students, midterms, finals)}
print(final_grades) #{'dan': 89, 'ang': 91, 'kate': 99}

# using map 
# final_grades = dict(
#         zip(
#         students,
#             map(
#             lambda pair:max(pair),
#             zip(midterms, finals)
#         )   
#     )
# )
# print(final_grades) #{'dan': 89, 'ang': 91, 'kate': 99}

avg_grades = dict(
        zip(
        students,
            map(
            lambda pair:((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )   
    )
)
print(avg_grades)











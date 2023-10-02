# NOTE: generators are always used for saving memory
# ex:instead of producing a list of 1to4 on repeat, storing and removing one item a time 
# - we can produce 1 o/p using gen exp without storing such a large lis of repeating numbers

# list of 1 to 4 over and over again 
# ex1 - using list - lot of memory used

# def current_beat():
#     max = 100
#     nums = (1,2,3,4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i=0
#         result.append(nums[i])
#         i += 1
#     return result 
    
# print(current_beat())

# ex2 - using generator functions
# infinite generator 
def beat_counter():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

counter = beat_counter()
print(next(counter))
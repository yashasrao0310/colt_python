#
# No, you cannot change the list item "ram" to 'rao' inside the tuple because tuples
# are immutable in Python. However, you can modify the list that is inside the tuple 
# because lists are mutable.

# Here's how you can modify the list inside the tuple to achieve your desired result:
tuple1 = (['yashas', 'ram'], 'ramesh')

# Access the list inside the tuple using index 0
inner_list = tuple1[0]

# Modify the list
inner_list[1] = 'rao'

# Print the modified tuple
print(tuple1) #(['yashas', 'rao'], 'ramesh')

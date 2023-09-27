nest_list = [[1,2,3],[4,5,6],[7,8,9]]
for val in nest_list:
    for x in val:
        print(x)

print('\n')

[[print(val) for val in x] for x in nest_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)
pattern = [['X' if num%2 == 0 else 'O' for num in range(1,4)] for val in range(1,4)]
print(pattern)

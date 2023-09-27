def generate_evens():
    list = []
    for i in range(1,50):
        if i%2==0:
            list.append(i)
    return list

result = generate_evens()
print(result)




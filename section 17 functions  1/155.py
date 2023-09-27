def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))

def check_odd(number):
    if number % 2!= 0:
        return True
    return False
print(check_odd(4))
print(check_odd(9))
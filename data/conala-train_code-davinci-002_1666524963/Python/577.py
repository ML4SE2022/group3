numbers = [1, 2, 3, 4, 5]

def squared(num):
    return num ** 2

squared_numbers = [squared(num) for num in numbers]

print(squared_numbers)
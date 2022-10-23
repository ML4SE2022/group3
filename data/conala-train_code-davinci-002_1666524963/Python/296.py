import random

def random_list(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(1,100))
    return my_list

print(random_list(10))
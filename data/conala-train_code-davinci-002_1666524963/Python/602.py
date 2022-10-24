# Python

# delete all elements from a list that do not satisfy a constraint

# create a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# delete all elements from a list that do not satisfy a constraint
my_list = [x for x in my_list if x % 2 == 0]

# print the list
print(my_list)
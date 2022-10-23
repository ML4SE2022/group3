a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 10]

c = [x for x in a if x not in b]
print(c)
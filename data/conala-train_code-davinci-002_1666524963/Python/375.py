a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

a.sort(key=lambda x: b[x-1])
print(a)
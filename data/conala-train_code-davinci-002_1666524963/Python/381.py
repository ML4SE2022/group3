list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])

print(list3)
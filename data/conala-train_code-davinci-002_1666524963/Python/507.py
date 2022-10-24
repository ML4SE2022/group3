list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5]

list3 = [x for x in list1 if x not in list2]
print(list3)
def find_non_common_elements(list1, list2):
    return list(set(list1) - set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(find_non_common_elements(list1, list2))
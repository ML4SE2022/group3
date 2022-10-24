def find_same_index(list1, list2):
    """
    Find the index of the same elements in two lists.
    """
    index_list = []
    for i in range(len(list1)):
        if list1[i] in list2:
            index_list.append(i)
    return index_list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 3, 5, 7, 9]

print(find_same_index(list1, list2))
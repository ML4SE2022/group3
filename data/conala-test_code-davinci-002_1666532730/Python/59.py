def find_n_largest_differences(list1, list2, n):
    """
    Finds the n largest differences between two lists.
    """
    # sort the lists
    list1.sort()
    list2.sort()
    # initialize the result list
    result = []
    # initialize the index of the first list
    i = 0
    # initialize the index of the second list
    j = 0
    # loop through the lists
    while i < len(list1) and j < len(list2):
        # if the first list's element is smaller than the second list's element
        if list1[i] < list2[j]:
            # add the difference to the result list
            result.append(list2[j] - list1[i])
            # increment the index of the first list
            i += 1
        # if the second list's element is smaller than the first list's element
        elif list2[j] < list1[i]:
            # add the difference to the result list
            result.append(list1[i] - list2[j])
            # increment the index of the second list
            j += 1
        # if the elements are equal
        else:
            # increment the index of the first list
            i += 1
            # increment the index of the second list
            j += 1
    # sort the result list
    result.sort()
    # return the n largest differences
    return result[-n:]

# test
print(find_n_largest_differences([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 3))
print(find_n_largest_differences([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5))
print(find_n_largest_differences([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 10))
print(find_n_largest_differences([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 15))
print(find_n_largest_differences([1
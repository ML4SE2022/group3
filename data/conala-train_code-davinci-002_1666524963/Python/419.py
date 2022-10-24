def remove_adjacent_duplicates(lst):
    """
    Remove adjacent duplicate elements from a list.
    """
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

print(remove_adjacent_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
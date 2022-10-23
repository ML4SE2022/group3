def sort_list(list_to_sort, index_1, index_2):
    return sorted(list_to_sort, key=lambda x: (x[index_1], x[index_2]))
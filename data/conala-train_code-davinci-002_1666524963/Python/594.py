def sort_list(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1] + x[2])
def sort_list_of_tuples(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: (x[0], x[1]))
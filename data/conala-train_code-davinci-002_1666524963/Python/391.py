def sort_by_key(list_of_tuples, key):
    return sorted(list_of_tuples, key=lambda x: x[key])
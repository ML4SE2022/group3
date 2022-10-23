def remove_duplicates(list_of_sets):
    return list(set(map(frozenset, list_of_sets)))
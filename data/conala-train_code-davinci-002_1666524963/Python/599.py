def sort_by_keys(lst, *keys):
    """
    Sort a multidimensional list by a variable number of keys.
    """
    if len(keys) == 1:
        return sorted(lst, key=lambda x: x[keys[0]])
    else:
        return sorted(lst, key=lambda x: [x[key] for key in keys])
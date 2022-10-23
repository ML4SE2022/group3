def contains_lists(lst):
    for item in lst:
        if isinstance(item, list):
            return True
    return False
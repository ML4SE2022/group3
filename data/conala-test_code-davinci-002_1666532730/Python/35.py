def sum_nested_list(nested_list):
    """
    Given a nested list of ints, return the sum of all the ints.
    """
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += sum_nested_list(item)
        else:
            total += item
    return total
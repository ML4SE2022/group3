def all_combinations(lists):
    """
    Returns all combinations of a list of lists.
    """
    if len(lists) == 0:
        return []
    elif len(lists) == 1:
        return lists[0]
    else:
        return [x + [y] for x in all_combinations(lists[:-1]) for y in lists[-1]]
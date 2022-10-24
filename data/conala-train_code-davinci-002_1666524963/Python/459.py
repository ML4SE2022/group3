def split_list(lst, field):
    """
    Split a list of tuples into sub-lists of the same tuple field.
    """
    return [list(g) for k, g in groupby(lst, lambda x: x[field])]
def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst
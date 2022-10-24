def adjacent_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1) if lst[i] == lst[i+1]]
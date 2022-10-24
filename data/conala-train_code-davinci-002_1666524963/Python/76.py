def combinate(set, n):
    if n == 0:
        return [[]]
    else:
        return [x + [y] for x in combinate(set, n - 1) for y in set if y not in x]
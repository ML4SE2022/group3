import itertools

def get_combinations(lst):
    return list(itertools.combinations(lst, 3))

print(get_combinations([10, 1, 2, 7, 6, 1, 5]))
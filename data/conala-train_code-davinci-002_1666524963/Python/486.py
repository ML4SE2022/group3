import itertools

def generate_pairs(n):
    return list(itertools.combinations(range(n), 2))
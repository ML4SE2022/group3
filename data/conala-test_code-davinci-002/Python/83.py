def find_largest_key(d):
    return max(k for k, v in d.items() if v)

d = {'a': 0, 'b': 1, 'c': 2, 'd': 0}
print(find_largest_key(d))
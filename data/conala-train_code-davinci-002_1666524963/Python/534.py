d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Remove all entries with value less than 3
d = {k: v for k, v in d.items() if v >= 3}

# Remove all entries with value less than 3
d = {k: v for k, v in d.items() if v < 3}
from itertools import chain

def split_dict_of_lists(d):
    return [dict(zip(d, t)) for t in zip(*d.values())]

d = {'a': [1, 2, 3], 'b': [4, 5, 6]}
split_dict_of_lists(d)
# [{'a': 1, 'b': 4}, {'a': 2, 'b': 5}, {'a': 3, 'b': 6}]
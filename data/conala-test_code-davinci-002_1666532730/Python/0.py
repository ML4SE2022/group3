def transpose_dict(d):
    return {k: [d[k] for d in d] for k in d[0]}

transpose_dict([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}])
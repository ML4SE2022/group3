from collections import defaultdict

def merge_dicts(dicts):
    result = defaultdict(list)
    for d in dicts:
        for k, v in d.items():
            result[k].append(v)
    return result
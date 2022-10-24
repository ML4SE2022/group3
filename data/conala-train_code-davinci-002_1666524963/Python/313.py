from collections import defaultdict

def group_similar_items(items):
    groups = defaultdict(list)
    for item in items:
        groups[item].append(item)
    return groups
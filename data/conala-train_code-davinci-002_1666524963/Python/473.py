def count_elements(d):
    if isinstance(d, dict):
        return sum(count_elements(v) for v in d.values())
    else:
        return 1
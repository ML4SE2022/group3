def diff(l):
    return [l[i] - l[i-1] for i in range(1, len(l))]
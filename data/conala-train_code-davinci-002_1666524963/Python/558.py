def coalesce(s):
    return ''.join(c for c, _ in itertools.groupby(s))
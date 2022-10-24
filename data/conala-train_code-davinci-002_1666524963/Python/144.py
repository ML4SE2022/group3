def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r

def remove_key_from_list(l, key):
    return [remove_key(d, key) for d in l]
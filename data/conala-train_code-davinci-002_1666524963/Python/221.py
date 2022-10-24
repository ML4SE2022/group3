from hashlib import sha256

def hash_dict(d):
    return sha256(str(sorted(d.items())).encode('utf-8')).hexdigest()

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

print(hash_dict(d1))
print(hash_dict(d2))
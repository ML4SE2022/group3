import json

def encode_tuple(t):
    return {'__tuple__': True, 'items': t}

def decode_tuple(d):
    if d.get('__tuple__'):
        return tuple(d['items'])
    return d

t = (1, 2, 3)

print(json.dumps(t, default=encode_tuple))
# {"__tuple__": true, "items": [1, 2, 3]}

print(json.loads('{"__tuple__": true, "items": [1, 2, 3]}', object_hook=decode_tuple))
# (1, 2, 3)
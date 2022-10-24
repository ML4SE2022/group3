from collections import defaultdict

keys = ['a', 'b', 'c', 'd', 'e', 'f']
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

d = defaultdict(list)
for k, v in zip(keys, values):
    d[k].append(v)

print(d)
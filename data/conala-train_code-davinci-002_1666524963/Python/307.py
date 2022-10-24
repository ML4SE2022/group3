from bisect import bisect_left

def insert(a, x):
    i = bisect_left(a, x)
    a.insert(i, x)

a = []
insert(a, [2, 3])
insert(a, [1, 2])
insert(a, [3, 4])
print(a)
a = [[1,2],[3,4],[1,3]]
a.sort(key=lambda x: (x[1], -x[0]))
print(a)
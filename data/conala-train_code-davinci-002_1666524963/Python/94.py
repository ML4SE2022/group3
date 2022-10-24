def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
print(closest(lst, K))
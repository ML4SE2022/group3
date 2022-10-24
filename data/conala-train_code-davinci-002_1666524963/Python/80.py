def find_closest(L, target):
    low = 0
    high = len(L) - 1
    while low < high:
        mid = (low + high) // 2
        if target < L[mid]:
            high = mid
        elif target > L[mid]:
            low = mid + 1
        else:
            return mid
    return low

L = [1, 2, 4, 5, 6, 7, 8, 9]
target = 3
print(find_closest(L, target))
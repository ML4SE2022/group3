def max_list(lst, length):
    if length == 0:
        return 0
    else:
        return max(lst[:length])

print(max_list([1,2,3,4,5], 3))
print(max_list([1,2,3,4,5], 0))
print(max_list([1,2,3,4,5], 5))
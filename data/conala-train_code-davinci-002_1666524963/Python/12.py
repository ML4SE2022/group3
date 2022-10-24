def get_all_combination(n):
    if n == 0:
        return []
    if n == 1:
        return [[0], [1]]
    else:
        result = []
        for i in get_all_combination(n-1):
            result.append(i + [0])
            result.append(i + [1])
        return result

print(get_all_combination(3))
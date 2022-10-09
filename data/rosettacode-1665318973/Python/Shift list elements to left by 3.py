def rotate(list, n):
    for _ in range(n):
        list.append(list.pop(0))

    return list

# or, supporting opposite direction rotations:

def rotate(list, n):
    k = (len(list) + n) % len(list)
    return list[k::] + list[:k:]


list = [1,2,3,4,5,6,7,8,9]
print(list, " => ", rotate(list, 3))
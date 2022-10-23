def greater_than(list, number):
    count = 0
    for i in list:
        if i > number:
            count += 1
    return count
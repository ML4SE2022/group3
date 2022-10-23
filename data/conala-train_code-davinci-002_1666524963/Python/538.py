def find_element(lst, elem):
    for i in range(len(lst)):
        if lst[i][0] == elem:
            return lst[i][1]
    return None
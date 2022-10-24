def replace_string(list_of_lists, old_string, new_string):
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if list_of_lists[i][j] == old_string:
                list_of_lists[i][j] = new_string
    return list_of_lists
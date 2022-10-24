def sum_list_of_lists(list_of_lists):
    return [sum(x) for x in zip(*list_of_lists)]

sum_list_of_lists([[1,2,3],[4,5,6],[7,8,9]])
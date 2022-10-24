def convert_list_of_lists_to_list_of_integers(list_of_lists):
    return [int(item) for sublist in list_of_lists for item in sublist]
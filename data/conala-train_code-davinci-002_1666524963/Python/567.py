from operator import itemgetter

def sort_list_of_dict(list_of_dict, order):
    return sorted(list_of_dict, key=itemgetter(*order))
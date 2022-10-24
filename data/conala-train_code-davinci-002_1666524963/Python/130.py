def search_list_in_dict(dict_to_search, list_to_search):
    for key, value in dict_to_search.items():
        if set(list_to_search).issubset(value):
            return key
    return None
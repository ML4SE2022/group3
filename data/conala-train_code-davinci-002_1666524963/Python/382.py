from collections import defaultdict

def transform_list_of_dicts_into_dict_of_dicts(list_of_dicts):
    dict_of_dicts = defaultdict(dict)
    for d in list_of_dicts:
        dict_of_dicts[d['key']].update(d)
    return dict_of_dicts
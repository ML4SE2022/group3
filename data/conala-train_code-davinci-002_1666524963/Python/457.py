def convert_to_tuple(string):
    return tuple(string.split(','))

def add_to_tuple(tuple, string):
    return tuple + convert_to_tuple(string)
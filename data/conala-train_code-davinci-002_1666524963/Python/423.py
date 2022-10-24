import ast

def string_to_dict(string):
    return ast.literal_eval(string)

string_to_dict('{"a": 1, "b": 2}')
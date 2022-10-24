def replace_empty_string_with_zero(string):
    return ','.join(str(int(x) if x else 0) for x in string.split(','))
def max_string_length(lst):
    max_len = 0
    for item in lst:
        if isinstance(item, list):
            max_len = max(max_len, max_string_length(item))
        else:
            max_len = max(max_len, len(item))
    return max_len
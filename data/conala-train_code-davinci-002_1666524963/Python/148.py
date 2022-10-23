def remove_substring(string_list, substring_list):
    return [string for string in string_list if not any(substring in string for substring in substring_list)]
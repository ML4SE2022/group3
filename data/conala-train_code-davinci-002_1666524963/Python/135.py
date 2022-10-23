import re

def sort_by_regex(lst, regex):
    return sorted(lst, key=lambda x: re.search(regex, x).group(0))
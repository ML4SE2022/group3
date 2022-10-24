import re

def remove_duplicate_chars(s):
    return re.sub(r'(.)\1+', r'\1', s)
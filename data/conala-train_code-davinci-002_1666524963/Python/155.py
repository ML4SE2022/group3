import re

def has_letters(input_string):
    return bool(re.search('[a-zA-Z]', input_string))
import re

def add_character(string, character):
    return re.sub(r'(.)', r'\1' + character, string)
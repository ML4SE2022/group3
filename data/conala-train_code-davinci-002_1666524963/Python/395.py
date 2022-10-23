import re

def is_valid(word):
    return re.match(r'^(?!.*[aeiou]{2})[a-z]+$', word)
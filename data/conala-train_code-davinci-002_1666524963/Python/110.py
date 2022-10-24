import re

def remove_parentheses(string):
    return re.sub(r'\(([^)]+)\)', r'\1', string)
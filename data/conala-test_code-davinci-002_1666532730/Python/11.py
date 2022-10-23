import re

def find_brackets(string):
    return re.findall(r'\[(.*?)\]', string)

find_brackets('[hello] [world]')
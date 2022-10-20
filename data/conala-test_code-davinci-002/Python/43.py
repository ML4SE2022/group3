import re

def split_string(string):
    return re.findall(r'[A-Z]{1}[^A-Z]*', string)

split_string('ABCD')
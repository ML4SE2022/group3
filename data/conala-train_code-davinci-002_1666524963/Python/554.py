import re

def match_all_but(string):
    return re.compile(r'^(?:(?!{}).)*$'.format(string))
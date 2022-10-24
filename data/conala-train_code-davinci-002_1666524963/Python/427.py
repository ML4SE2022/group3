import re

def strip_random_chars(url):
    return re.sub(r'[^a-zA-Z0-9]', '', url)
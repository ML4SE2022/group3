import re

def escape_quotes(s):
    return re.sub(r'(["\'])', r'\\\1', s)
import re

def replace_whitespace(string, replace_with):
    return re.sub(r'\s+', replace_with, string)

replace_whitespace('Hello World', '_')
# 'Hello_World'

replace_whitespace('Hello_World', ' ')
# 'Hello World'
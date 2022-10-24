import re

def replace_non_alphanumeric(string):
    return re.sub(r'\W+', '', string)

replace_non_alphanumeric('Hello, World!')
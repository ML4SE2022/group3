import re

def replace_word(text, word, replacement):
    regex = r"\b" + word + r"\b"
    return re.sub(regex, replacement, text)
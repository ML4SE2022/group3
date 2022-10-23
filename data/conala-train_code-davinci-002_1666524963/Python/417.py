import re

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub(r'[^\w\s]','',input_string)

print(remove_punctuation("Hello, I am a string!"))
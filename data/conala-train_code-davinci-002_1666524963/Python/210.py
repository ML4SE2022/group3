import re

def get_matchable_characters(regex_class):
    """
    Returns a list of characters that can be matched by the regex class.
    """
    if regex_class == '.':
        return [chr(i) for i in range(256)]
    elif regex_class == '\w':
        return [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
               [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
               [chr(i) for i in range(ord('0'), ord('9') + 1)] + \
               ['_']
    elif regex_class == '\W':
        return [chr(i) for i in range(256)] - \
               [chr(i) for i in range(ord('a'), ord('z') + 1)] - \
               [chr(i) for i in range(ord('A'), ord('Z') + 1)] - \
               [chr(i) for i in range(ord('0'), ord('9') + 1)] - \
               ['_']
    elif regex_class == '\d':
        return [chr(i) for i in range(ord('0'), ord('9') + 1)]
    elif regex_class == '\D':
        return [chr(i) for i in range(256)] - \
               [chr(i) for i in range(ord('0'), ord('9') + 1)]
    elif regex_class == '\s':
        return [' ', '\t', '\n', '\r', '\f', '\v']
    elif regex_class == '\S':
        return [chr(i) for i in range(256)] - \
               [' ', '\t', '\n', '\r', '\f', '\v']
    elif regex_class == '\b':
        return ['\b']
    elif regex_class == '\B':
        return [chr(i) for
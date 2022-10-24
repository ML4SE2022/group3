import re

def find_pattern(string):
    pattern = re.compile(r'(\w+)\1')
    match = pattern.search(string)
    if match:
        return match.group()
    else:
        return None

print(find_pattern('abcabcabc'))
print(find_pattern('abcabc'))
print(find_pattern('abc'))
print(find_pattern('ababab'))
print(find_pattern('abab'))
print(find_pattern('ab'))
print(find_pattern('a'))
print(find_pattern(''))
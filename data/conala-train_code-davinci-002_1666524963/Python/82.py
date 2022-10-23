import re

def extract_first_two_characters(string):
    return re.findall(r'^\w{2}', string)

print(extract_first_two_characters('Python'))
print(extract_first_two_characters('Py'))
print(extract_first_two_characters('Java'))
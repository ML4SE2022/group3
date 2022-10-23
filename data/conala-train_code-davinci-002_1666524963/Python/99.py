import re

with open('file.txt', 'r') as f:
    for line in f:
        if re.search(r'\r$', line):
            print('DOS line break found!')
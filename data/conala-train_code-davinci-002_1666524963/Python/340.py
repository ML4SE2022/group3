import re

with open('file.txt', 'r') as f:
    lines = f.readlines()

with open('file.txt', 'w') as f:
    for line in lines:
        f.write(re.sub('\r\n', '', line))
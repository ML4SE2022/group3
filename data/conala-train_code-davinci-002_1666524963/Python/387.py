import re

name = "John Smith"

if re.match("John", name):
    print("Match")
else:
    print("No match")
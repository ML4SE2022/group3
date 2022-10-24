import re

text = "This is a [test] of [bracket] matching"

re.findall(r'\[(.*?)\]', text)
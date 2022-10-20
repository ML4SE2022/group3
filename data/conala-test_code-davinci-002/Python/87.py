import re

text = "This is a [test] of the [emergency] broadcast system."

re.findall(r'[^\[\]]+', text)
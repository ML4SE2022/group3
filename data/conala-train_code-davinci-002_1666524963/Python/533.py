import re

def repl(m):
    return '{} {}'.format(m.group(1), m.group(2))

re.sub(r'(\w+) (\w+)', repl, 'hello world')
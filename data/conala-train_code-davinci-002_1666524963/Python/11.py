import re

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    l.sort(key=alphanum_key)

l = ['1', '2', '10', '11', '20', '21', '100', '101', '200', '201']
sort_nicely(l)
print(l)
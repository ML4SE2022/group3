import re

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = re.sub(i, j, text)
    return text

text = "My name is David. Hi David."
dic = {'David': 'Amy'}

print replace_all(text, dic)
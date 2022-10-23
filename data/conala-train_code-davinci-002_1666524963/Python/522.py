import re

def extract_float(string):
    return float(re.findall(r'[-+]?\d*\.\d+|\d+', string)[0])

extract_float('$123.45')
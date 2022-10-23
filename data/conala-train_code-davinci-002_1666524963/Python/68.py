import re

def is_valid_IP(strng):
    return bool(re.match(r'^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$', strng))
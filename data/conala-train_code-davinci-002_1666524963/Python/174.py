import re

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_ascii_re(s):
    return bool(re.match('^[\x00-\x7F]+$', s))

def is_ascii_re2(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re3(s):
    return bool(re.match('^[\x00-\x7F]{0,}$', s))

def is_ascii_re4(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re5(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re6(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re7(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re8(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re9(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re10(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re11(s):
    return bool(re.match('^[\x00-\x7F]*$', s))

def is_ascii_re12(s):
    return bool(re.match('^[\x00-\x7F]*$', s))
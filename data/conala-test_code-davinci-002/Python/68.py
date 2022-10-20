def string_to_pairs(s):
    return list(zip(s, s[1:]))

string_to_pairs('abcd')
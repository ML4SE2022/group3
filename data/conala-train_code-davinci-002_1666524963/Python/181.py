def decode_string(s):
    """
    Decode a string from utf8 or latin1.
    """
    try:
        return s.decode('utf8')
    except UnicodeDecodeError:
        return s.decode('latin1')

def encode_string(s):
    """
    Encode a string to utf8 or latin1.
    """
    try:
        return s.encode('utf8')
    except UnicodeEncodeError:
        return s.encode('latin1')
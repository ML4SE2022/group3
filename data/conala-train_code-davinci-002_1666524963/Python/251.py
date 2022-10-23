from bs4 import UnicodeDammit

def decode_html(html_string):
    converted = UnicodeDammit(html_string, is_html=True)
    if not converted.unicode_markup:
        raise UnicodeDecodeError(
            "Failed to detect encoding, tried [%s]",
            ', '.join(converted.tried_encodings))
    return converted.unicode_markup
import unicodedata

unicodedata.normalize('NFKD', unicode_text).encode('ascii','ignore')
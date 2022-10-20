import re

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_regex( s, first, last ):
    try:
        start = re.search( first, s ).end()
        end = re.search( last, s ).start()
        return s[start:end]
    except AttributeError:
        return ""

s = "This is a string"
print find_between( s, "is", "a" )
print find_between_r( s, "is", "a" )
print find_between_regex( s, "is", "a" )
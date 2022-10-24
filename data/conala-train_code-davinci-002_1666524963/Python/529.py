def switch_chars(string):
    """
    >>> switch_chars('abcd')
    'badc'
    >>> switch_chars('a')
    'a'
    >>> switch_chars('')
    ''
    """
    if len(string) < 2:
        return string
    else:
        return string[1] + string[0] + switch_chars(string[2:])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
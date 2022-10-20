def remove_special_characters(string):
    """
    Remove all special characters, punctuation and spaces from string
    """
    regex = re.compile('[^a-zA-Z\d]')
    return regex.sub('', string)

remove_special_characters("The quick brown fox!")
def delete_letters(string, letters):
    for letter in letters:
        string = string.replace(letter, '')
    return string
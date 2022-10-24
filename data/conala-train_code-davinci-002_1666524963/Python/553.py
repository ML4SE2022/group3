def remove_duplicates(string):
    return ''.join(set(string))

print(remove_duplicates('abcdabcd'))
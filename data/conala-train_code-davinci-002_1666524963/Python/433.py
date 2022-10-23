def remove_final_characters(string, n):
    if n == 0:
        return string
    else:
        return remove_final_characters(string[:-1], n-1)
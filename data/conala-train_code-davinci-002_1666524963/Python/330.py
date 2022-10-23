def count_end_char(string, char):
    count = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            count += 1
        else:
            break
    return count
def most_frequent(string):
    return max(string, key=string.count)

most_frequent('abca')
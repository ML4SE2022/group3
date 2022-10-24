def remove_substring(string, substring):
    if string.endswith(substring):
        return string[:-len(substring)]
    return string
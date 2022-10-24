def longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

print(longest_word(['cat', 'dog', 'elephant']))
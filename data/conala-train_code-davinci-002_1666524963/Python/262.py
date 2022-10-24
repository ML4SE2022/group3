def find_consecutive_consonants(word):
    """
    Finds the longest consecutive consonants in a word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = []
    for letter in word:
        if letter not in vowels:
            consonants.append(letter)
    return ''.join(consonants)

print(find_consecutive_consonants('strengths'))
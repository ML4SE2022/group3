sentence = "The quick brown fox jumps over the lazy dog"

# Method 1
print(len(sentence.split()))

# Method 2
print(len(sentence.split(' ')))

# Method 3
print(len(sentence.split(' ')) - 1)

# Method 4
print(sentence.count(' ') + 1)

# Method 5
print(sentence.count(' '))

# Method 6
print(sentence.count(' ') + sentence.count('\n'))

# Method 7
print(sentence.count(' ') + sentence.count('\n') + 1)

# Method 8
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t'))

# Method 9
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + 1)

# Method 10
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r'))

# Method 11
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r') + 1)

# Method 12
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r') + sentence.count('\f'))

# Method 13
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r') + sentence.count('\f') + 1)

# Method 14
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r') + sentence.count('\f') + sentence.count('\v'))

# Method 15
print(sentence.count(' ') + sentence.count('\n') + sentence.count('\t') + sentence.count('\r') + sentence.
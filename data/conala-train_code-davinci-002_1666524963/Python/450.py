def generate_all_strings(tokens, length):
    if length == 0:
        return ['']
    else:
        return [token + suffix for token in tokens for suffix in generate_all_strings(tokens, length - 1)]

print(generate_all_strings(['a', 'b'], 3))
def find_max_in_nested_dict(d):
    """
    Find the maximum value in a nested dictionary.
    """
    max_value = -float('inf')
    for k, v in d.items():
        if isinstance(v, dict):
            max_value = max(max_value, find_max_in_nested_dict(v))
        else:
            max_value = max(max_value, v)
    return max_value

d = {'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {'t': {'u': {'v': {'w': {'x': {'y': {'z': {'A': {'B': {'C': {'D': {'E': {'F': {'G': {'H': {'I': {'J': {'K': {'L': {'M': {'N': {'O': {'P': {'Q': {'R': {'S': {'T': {'U': {'V': {'W': {'X': {'Y': {'Z': {'1': {'2': {'3': {'4': {'5': {'6': {'7': {'8': {'9': {'0': {'!': {'@': {'#': {'$': {'%': {'^': {'&': {'*': {'(': {')': {'-': {'_': {'=': {'+': {'[': {']': {'{': {'}': {'\\': {'|': {';': {':': {'\'': {'"': {',': {'<': {'.': {'>': {'/': {'?': {'`': {'~': {' ': {'\t': {'\n':
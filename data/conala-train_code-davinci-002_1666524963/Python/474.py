def remove_chars(string, chars):
    return "".join(c for c in string if c not in chars)

remove_chars("Battle of the Vowels: Hawaii vs. Grozny", "aeiou")
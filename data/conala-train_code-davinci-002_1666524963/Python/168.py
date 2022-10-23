def is_alpha_space(string):
    return string.replace(" ", "").isalpha()

print(is_alpha_space("Hello World"))
print(is_alpha_space("HelloWorld"))
print(is_alpha_space("Hello World 123"))
def get_last_part(s, c):
    return s.rsplit(c, 1)[-1]

print(get_last_part('https://www.w3resource.com/python-exercises/string', '/'))
print(get_last_part('https://www.w3resource.com/python-exercises/string', '-'))
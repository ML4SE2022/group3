def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            yield i

my_list = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']

print(list(find_index(my_list, 'b')))
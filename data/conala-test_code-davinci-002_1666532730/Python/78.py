from operator import itemgetter

list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 17}, {'name': 'Bob', 'age': 30}]

sorted(list_of_dicts, key=itemgetter('age'))
# [{'name': 'Jane', 'age': 17}, {'name': 'John', 'age': 25}, {'name': 'Bob', 'age': 30}]

sorted(list_of_dicts, key=itemgetter('age'), reverse=True)
# [{'name': 'Bob', 'age': 30}, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 17}]
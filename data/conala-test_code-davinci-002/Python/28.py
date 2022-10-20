from operator import itemgetter

list_of_strings = ['a,b,c', 'd,e,f', 'g,h,i']

sorted_list = sorted(list_of_strings, key=lambda x: x.split(',')[1])

print(sorted_list)
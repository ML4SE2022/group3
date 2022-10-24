def max_length(list_of_lists):
    max_lengths = []
    for i in range(len(list_of_lists[0])):
        max_lengths.append(max([len(str(row[i])) for row in list_of_lists]))
    return max_lengths

def print_table(list_of_lists):
    max_lengths = max_length(list_of_lists)
    for row in list_of_lists:
        for i in range(len(row)):
            print(str(row[i]).ljust(max_lengths[i]), end=' ')
        print()

print_table([['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']])
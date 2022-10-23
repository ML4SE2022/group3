l_of_l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

flat_list = []
for x in l_of_l:
    for y in x:
        flat_list.append(y)

print(flat_list)
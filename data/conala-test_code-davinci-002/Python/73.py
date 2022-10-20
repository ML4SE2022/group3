# Create a list of lists
list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# Merge the list of lists into a single list
merged_list = [y for x in list_of_lists for y in x]

# Print the merged list
print(merged_list)
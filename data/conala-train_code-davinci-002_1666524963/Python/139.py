# Filter the list to include only those strings that contain the letter 'a'

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: 'a' in member, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)
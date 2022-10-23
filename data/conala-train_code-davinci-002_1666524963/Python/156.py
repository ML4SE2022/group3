# Create a dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Create a new dictionary with the same keys, but the values are the average of the values in the original dictionary
d_avg = {k: sum(v)/len(v) for k, v in d.items()}

# Print the new dictionary
print(d_avg)
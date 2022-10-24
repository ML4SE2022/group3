# Create a dictionary
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

# Create a function to return the value of the dictionary
def get_value(x):
    return d[x]

# Sort the dictionary by value
sorted(d, key=get_value)

# Output: ['pear', 'orange', 'banana', 'apple']
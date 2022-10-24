# Python

# Given a list of objects
objects = [
    {'name': 'John', 'age': 20},
    {'name': 'Mary', 'age': 30},
    {'name': 'Bob', 'age': 25}
]

# Extract a list of names
names = [obj['name'] for obj in objects]

# Extract a list of ages
ages = [obj['age'] for obj in objects]
# Delete all objects in a list

# Create a list of objects
objects = [
    {'name': 'object1', 'id': 1},
    {'name': 'object2', 'id': 2},
    {'name': 'object3', 'id': 3},
    {'name': 'object4', 'id': 4},
    {'name': 'object5', 'id': 5},
]

# Delete all objects in the list
for obj in objects:
    obj.delete()
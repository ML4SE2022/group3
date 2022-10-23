members = {
    'member1': {'name': 'John', 'age': '27', 'sex': 'Male'},
    'member2': {'name': 'Marie', 'age': '22', 'sex': 'Female'},
    'member3': {'name': 'Luna', 'age': '24', 'sex': 'Female'},
    'member4': {'name': 'Peter', 'age': '29', 'sex': 'Male'},
    'member5': {'name': 'Sara', 'age': '23', 'sex': 'Female'},
    'member6': {'name': 'Thomas', 'age': '24', 'sex': 'Male'},
    'member7': {'name': 'Martha', 'age': '29', 'sex': 'Female'},
    'member8': {'name': 'David', 'age': '31', 'sex': 'Male'},
    'member9': {'name': 'Nina', 'age': '26', 'sex': 'Female'},
    'member10': {'name': 'Randy', 'age': '23', 'sex': 'Male'}
}

# Create a list of all member-dict keys using a list comprehension
member_keys = [member for member in members]

print(member_keys)
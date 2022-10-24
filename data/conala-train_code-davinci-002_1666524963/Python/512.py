d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Sort by value
sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])

# Sort by key
sorted_by_key = sorted(d.items(), key=lambda kv: kv[0])

# Sort by value then by key
sorted_by_value_then_key = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
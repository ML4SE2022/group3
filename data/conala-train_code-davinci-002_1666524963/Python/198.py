import json

with open('data.json') as f:
    data = json.load(f)

sorted_data = sorted(data.items(), key=lambda x: x[1]['key'])
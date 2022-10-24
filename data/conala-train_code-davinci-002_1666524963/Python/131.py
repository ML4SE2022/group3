import json

json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(json_data)
print(text)
import json
import urllib.request

url = 'https://api.github.com/repos/jupyter/notebook/issues?state=closed'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
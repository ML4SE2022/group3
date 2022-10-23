import requests

# GET
r = requests.get('https://httpbin.org/get')
print(r.text)

# POST
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r.text)
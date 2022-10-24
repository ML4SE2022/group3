from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=java'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for meta in soup.find_all('meta'):
    if 'name' in meta.attrs and meta['name'] == 'description':
        print(meta['content'])
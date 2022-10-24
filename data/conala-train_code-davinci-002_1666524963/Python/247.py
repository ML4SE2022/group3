import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('meta', attrs={'property': 'og:title'})
description = soup.find('meta', attrs={'property': 'og:description'})
image = soup.find('meta', attrs={'property': 'og:image'})

print(title['content'])
print(description['content'])
print(image['content'])
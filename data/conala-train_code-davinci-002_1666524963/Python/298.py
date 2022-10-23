import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=python'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', attrs={'class': 'g'})

for result in results:
    link = result.find('a', href=True)
    title = result.find('h3')
    description = result.find('span', attrs={'class': 'st'})
    if link and title:
        link = link['href']
        title = title.get_text()
        if description:
            description = description.get_text()
        if link != '#':
            print('\nTitle: {}'.format(title))
            print('Link: {}'.format(link))
            print('Description: {}'.format(description))
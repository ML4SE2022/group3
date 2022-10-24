import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
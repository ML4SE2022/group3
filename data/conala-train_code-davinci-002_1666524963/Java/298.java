from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

soup.find_all(string=re.compile('Java'))
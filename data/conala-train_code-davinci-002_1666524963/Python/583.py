import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

for tag in soup.find_all(class_="story-heading"):
    if tag.a:
        print(tag.a.text.replace("\n", " ").strip())
    else:
        print(tag.contents[0].strip())
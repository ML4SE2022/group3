# Import BeautifulSoup
from bs4 import BeautifulSoup

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, 'html.parser')

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1 id="title">Hello World</h1>
        <a href="#" class="link">This is link1</a>
        <a href="# link2" class="link">This is link2</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

# Get the first element
print(soup.find('a'))

# Get the last element
print(soup.find('a').next_sibling.next_sibling)

# Get the second element
print(soup.find('a').next_sibling)
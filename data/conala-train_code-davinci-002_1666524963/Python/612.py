from bs4 import BeautifulSoup

html = """
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>John</td>
        <td>20</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>30</td>
    </tr>
</table>
"""

soup = BeautifulSoup(html, 'html.parser')

for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 2:
        print(tds[0].text, tds[1].text)
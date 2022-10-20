import re

html = '''
<script type="text/javascript" src="http://www.example.com/js/jquery.js"></script>
<script type="text/javascript" src="http://www.example.com/js/jquery.min.js"></script>
<script type="text/javascript" src="http://www.example.com/js/jquery.ui.js"></script>
<script type="text/javascript" src="http://www.example.com/js/jquery.ui.min.js"></script>
'''

regex = re.compile(r'<script.*?src="(.*?)".*?>')

for match in regex.finditer(html):
    print(match.group(1))
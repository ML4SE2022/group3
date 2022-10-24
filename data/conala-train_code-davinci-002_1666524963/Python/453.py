import urllib.parse

url = 'http://example.com/path/to/page.html#fragment'

parsed = urllib.parse.urlparse(url)

print(parsed.fragment)
# fragment

print(parsed.path)
# /path/to/page.html

print(parsed.scheme)
# http

print(parsed.netloc)
# example.com

print(parsed.geturl())
# http://example.com/path/to/page.html#fragment

print(urllib.parse.urlunparse(parsed))
# http://example.com/path/to/page.html#fragment

parsed = parsed._replace(fragment='')

print(urllib.parse.urlunparse(parsed))
# http://example.com/path/to/page.html
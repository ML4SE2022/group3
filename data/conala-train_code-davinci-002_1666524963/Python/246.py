import urllib.request

url = 'http://www.python.org/'

# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, 'python.html')
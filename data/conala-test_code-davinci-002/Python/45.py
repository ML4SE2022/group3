import urllib2

url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
response = urllib2.urlopen(url)
data = response.read()

with open('python.tar.bz2', 'wb') as f:
    f.write(data)
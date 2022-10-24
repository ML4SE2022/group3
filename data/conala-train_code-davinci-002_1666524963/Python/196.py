import urllib
import urllib2

def url_get(url, params):
    """
    url_get(url, params) -> string
    """
    return urllib2.urlopen(url + '?' + urllib.urlencode(params)).read()

def url_post(url, params):
    """
    url_post(url, params) -> string
    """
    return urllib2.urlopen(url, urllib.urlencode(params)).read()
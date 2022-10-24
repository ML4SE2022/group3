import requests

def check_website(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False

check_website('https://www.google.com')
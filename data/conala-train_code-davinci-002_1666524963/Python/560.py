from google.appengine.api import app_identity
from google.appengine.api import urlfetch
import json
import urllib

def upload_file(file_name, file_content):
    bucket_name = app_identity.get_default_gcs_bucket_name()
    url = 'https://www.googleapis.com/upload/storage/v1/b/' + bucket_name + '/o?uploadType=media&name=' + file_name
    headers = {'Content-Type': 'application/octet-stream'}
    result = urlfetch.fetch(url=url, payload=file_content, method=urlfetch.POST, headers=headers)
    if result.status_code == 200:
        return json.loads(result.content)
    else:
        return None
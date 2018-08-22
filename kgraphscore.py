import requests
import urllib
from privatekeys import google_knowledge_key

query = 'Batman vs Superman'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 1,
    'indent': True,
    'key' : google_knowledge_key
}

url = service_url + '?' + urllib.parse.urlencode(params)
movieInfo = requests.get(url).content
print(movieInfo)
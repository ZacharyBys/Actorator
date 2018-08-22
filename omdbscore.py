from privatekeys import omdb_key
import requests
import urllib

baseUrl = 'http://www.omdbapi.com/?apikey=[yourkey]&'
query = 'Batman v superman'
params = {
    'apiKey' : omdb_key,
    's' : query
}

url = baseUrl + '?' + urllib.urlencode(params)
movieInfo = requests.get(url).content
print(movieInfo)
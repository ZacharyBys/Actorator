from privatekeys import omdb_key
import requests
import urllib
import json

def findOmdbScoreFromId(imdbID):
    baseUrl = 'http://www.omdbapi.com/'
    params = {
        'apiKey' : omdb_key,
        'i' : imdbID
    }

    url = baseUrl + '?' + urllib.urlencode(params)
    result = json.loads(requests.get(url).content)

    results = {}
    if result['Ratings']:
        for rating in result['Ratings']:
            results[rating['Source']] = rating['Value']

    return convertScoresOnTen(results)

def findOmdbScore(movie):
    baseUrl = 'http://www.omdbapi.com/'
    params = {
        'apiKey' : omdb_key,
        's' : movie
    }

    url = baseUrl + '?' + urllib.parse.urlencode(params)
    searchResults = json.loads(requests.get(url).content)
    if searchResults['Search'][0]:
        return findOmdbScoreFromId(searchResults['Search'][0]['imdbID'])
    else:
        return -1

def convertScoresOnTen(movieScores):
    if movieScores['Internet Movie Database']:
        score =  movieScores['Internet Movie Database'].split('/')[0]
        movieScores['Internet Movie Database'] = score
    if movieScores['Rotten Tomatoes']:
        score = movieScores['Rotten Tomatoes'].split('%')[0]
        score = int(score)/10.0
        movieScores['Rotten Tomatoes'] = score
    if movieScores['Metacritic']:
        score = movieScores['Metacritic'].split('/')[0]
        score = int(score)/10.0
        movieScores['Metacritic'] = score

    return movieScores


print(findOmdbScore('Batman v superman'))
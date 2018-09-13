from .privatekeys import omdb_key
import requests
import urllib
import json


def find_omdb_score_from_id(imdbID):
    baseUrl = 'http://www.omdbapi.com/'
    params = {
        'apiKey' : omdb_key,
        'i' : imdbID
    }

    url = baseUrl + '?' + urllib.parse.urlencode(params)
    result = json.loads(requests.get(url).content)

    results = {}
    if result['Ratings']:
        for rating in result['Ratings']:
            results[rating['Source']] = rating['Value']

    return convert_scores_on_ten(results)


def find_omdb_score(movie):
    baseUrl = 'http://www.omdbapi.com/'
    params = {
        'apiKey' : omdb_key,
        's' : movie
    }

    url = baseUrl + '?' + urllib.parse.urlencode(params)
    searchResults = json.loads(requests.get(url).content)
    if 'Search' in searchResults and searchResults['Search'][0]:
        return find_omdb_score_from_id(searchResults['Search'][0]['imdbID'])
    else:
        return -1


def convert_scores_on_ten(movieScores):
    if 'Internet Movie Database' in movieScores:
        score =  movieScores['Internet Movie Database'].split('/')[0]
        movieScores['Internet Movie Database'] = float(score)
    if 'Rotten Tomatoes' in movieScores:
        score = movieScores['Rotten Tomatoes'].split('%')[0]
        score = int(score)/10.0
        movieScores['Rotten Tomatoes'] = score
    if 'Metacritic' in movieScores:
        score = movieScores['Metacritic'].split('/')[0]
        score = int(score)/10.0
        movieScores['Metacritic'] = score

    return movieScores

from privatekeys import tmdb_key
import json
import requests
import tmdbsimple as tmdb

tmdb.API_KEY = tmdb_key

def find_actors_movies_from_id(actorId):
    url = ('https://api.themoviedb.org/3/person/%s/movie_credits?api_key=%s&language=en-US' % (actorId, tmdb_key))
    response = json.loads(requests.get(url=url).content)
    movies = []
    if response['cast']:
        for movie in response['cast']:
            movies.append(movie['title'])
    return movies

def find_actor_id(actor):
    search = tmdb.Search()
    response = search.person(query=actor)
    if search.results:
        person = search.results[0]
        return person['id']

def find_actors_movies(actor):
    return find_actors_movies_from_id(find_actor_id(actor))

print(find_actors_movies("Tarantino"))
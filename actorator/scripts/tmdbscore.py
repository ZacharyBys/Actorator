import tmdbsimple as tmdb
import requests
import json
from privatekeys import tmdb_key

tmdb.API_KEY = tmdb_key

def find_tmdb_score(movies):
    voteTotal = 0
    for movie in movies:
        search = tmdb.Search()
        response = search.movie(query=movie)
        if search.results:
            chosenMovie = search.results[0]
            voteTotal = voteTotal + chosenMovie['vote_average']
    return voteTotal/len(movies)

def find_actor_id(actor):
    search = tmdb.Search()
    response = search.person(query=actor)
    if search.results:
        person = search.results[0]
        return person['id']

def find_actors_movies(actorId):
    url = ('https://api.themoviedb.org/3/person/%s/movie_credits?api_key=%s&language=en-US' % (actorId, tmdb_key))
    response = requests.get(url=url)
    return json.loads(response.content)

def find_score_by_person(person):
    movies = find_actors_movies(find_actor_id(person))  
    voteTotal = 0
    if movies['cast']:
        for movie in movies['cast']:
            voteTotal = voteTotal + movie['vote_average']
        return voteTotal/len(movies['cast'])
    return None

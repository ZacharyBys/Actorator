import time
from findmovies import find_actors_movies
from omdbscore import find_omdb_score
from tmdbscore import find_tmdb_score

def find_full_actor_score(actor):
    movies = find_actors_movies(actor)
    rottentomatoes = 0
    rottentomatoes_count = 0
    imdb = 0
    imdb_count = 0
    metacritic = 0
    metacritic_count = 0
    for movie in movies:
        score = find_omdb_score(movie)
        if 'Rotten Tomatoes' in score:
            rottentomatoes = rottentomatoes + score['Rotten Tomatoes']
            rottentomatoes_count = rottentomatoes_count + 1
        if 'Internet Movie Database' in score:
            imdb = imdb + score['Internet Movie Database']
            imdb_count = imdb_count + 1
        if 'Metacritic' in score:    
            metacritic = metacritic + score['Metacritic']
            metacritic_count = metacritic_count + 1

    if metacritic_count > 0:
        metacritic = metacritic / metacritic_count
    if imdb_count > 0:
        imdb = imdb / imdb_count
    if rottentomatoes_count > 0:    
        rottentomatoes = rottentomatoes / rottentomatoes_count

    return (rottentomatoes + imdb + metacritic) / 3


print(find_full_actor_score('Edgar Wright'))

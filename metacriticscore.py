from google import google
#git+https://github.com/abenassi/Google-Search-API

search_results = google.search('the dark knight rises metacritic')
for result in search_results:
    print(result.description)
from bs4 import BeautifulSoup
from googlesearch import search
import requests
from urllib.request import urlopen

movie = 'slender_man'
url = 'http://www.rottentomatoes.com/m/{}'.format(movie)

try:
	page = urlopen(url)
except:
	for url in search('{}+rotten+tomatoes'.format(movie), stop=1, num=1):
		print(url)
	page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

criticscore = soup.find('div', attrs={'class': 'critic-score meter'}).find('span', attrs={'class':'superPageFontColor'})
communityscore = soup.find('div', attrs={'class': 'audience-score meter'}).find('span', attrs={'class':'superPageFontColor'})

print('{}: Tomato score: {}'.format(movie, criticscore.text.strip()))
print('{}: Audience score: {}'.format(movie, communityscore.text.strip()))

if int(communityscore.text.strip('%')) < 30:
	print('Ouch! Tough crowd!')
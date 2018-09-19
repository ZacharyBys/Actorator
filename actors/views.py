from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.renderers import JSONRenderer
from ratings.views import get_rating
from scripts import tmdbscore
from .models import Actor, ProfileSize
from .serializers import ActorSerializer
from decimal import Decimal
import datetime



# Create your views here.
def get(request, actor_name):
	actor_id = tmdbscore.find_actor_id(actor_name)
	if actor_id == None:
		raise Http404("Invalid actor. Please try again.")
	try:
		actor = Actor.objects.get(actor_id__exact=actor_id)
		actor.birth = actor.birth.date().isoformat()
	except Actor.DoesNotExist:
		actor_score = get_rating(request, actor_name).getvalue().decode('utf-8')
		actor_response = tmdbscore.find_actor(actor_name)

		bday = datetime.datetime.strptime(actor_response["birthday"], '%Y-%m-%d')
		image_base_url = "http://image.tmdb.org/t/p/"
		image_size = ProfileSize(4).name

		actor = Actor(
			actor_id = actor_response["id"],
			imdb_id = actor_response["imdb_id"],
			name = actor_response["name"],
			score = Decimal(actor_score),
			birth = bday.date().isoformat(),
			birthplace = actor_response["place_of_birth"],
			biography = actor_response["biography"],
			picture = "{}{}{}".format(image_base_url, image_size, actor_response["profile_path"])
		)
		actor.save()
		
	serializer = ActorSerializer(actor)
	content = JSONRenderer().render(serializer.data)
	
	return HttpResponse(content)

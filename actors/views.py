from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from ratings.views import get_rating
from scripts import tmdbscore
from .models import Actor
from .serializers import ActorSerializer
from decimal import Decimal
import datetime



# Create your views here.
def get(request, actor_name):
	try:
		actor = Actor.objects.get(name__iexact=actor_name)
	except Actor.DoesNotExist:
		actor_score = get_rating(request, actor_name).getvalue().decode('utf-8')
		actor_response = tmdbscore.find_actor(actor_name)

		bday = datetime.datetime.strptime(actor_response["birthday"], '%Y-%m-%d')

		actor = Actor(
			actor_id = actor_response["id"],
			imdb_id = actor_response["imdb_id"],
			name = actor_response["name"],
			score = Decimal(actor_score),
			birth = bday.date().isoformat(),
			birthplace = actor_response["place_of_birth"],
			biography = actor_response["biography"],
			picture = actor_response["profile_path"]
		)
		actor.save()
		
	serializer = ActorSerializer(actor)
	content = JSONRenderer().render(serializer.data)
	
	return HttpResponse(content)

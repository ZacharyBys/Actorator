from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# from scripts.tmdbscore import find_actor
from .models import Actor
from .serializers import ActorSerializer
import datetime


# Create your views here.
def get(request, actor_name):
	# try:
	# 	actor = get_object_or_404(Actor, name=actor_name)
	# except Actor.DoesNotExist:
	# 	actor_response = find_actor(actor_name)
		
	# serializer = ActorSerializer(actor)
	# content = JSONRenderer().render(serializer.data)
	
	# return HttpResponse(actor_name)
	
	actor = Actor(
		actor_id = "1",
		imdb_id = "abc123",
		name = "Test Actor",
		score = 10.0,
		birth = datetime.datetime.now(),
		birthplace = "Hall 9th Floor",
		biography = "Cool Guy",
		picture = ""
	)

	serializer = ActorSerializer(actor)
	content = JSONRenderer().render(serializer.data)

	return HttpResponse(content)

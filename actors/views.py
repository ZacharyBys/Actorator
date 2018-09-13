from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

from .models import Actor
from .serializers import ActorSerializer


# Create your views here.
def get(request, actor_name):
	# actor = get_object_or_404(Actor, name=actor_name)
	# serializer = ActorSerializer(actor)
	# content = JSONRenderer().render(serializer.data)
	
	return HttpResponse(actor_name)

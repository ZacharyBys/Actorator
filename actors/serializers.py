from rest_framework import serializers
from .models import Actor

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		fields = (
			'id',
			'actor_id',
			'imdb_id',
			'name',
			'score',
			'birth',
			'birthplace',
			'biography',
			'picture'
		)
		
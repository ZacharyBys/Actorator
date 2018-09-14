from django.db import models
from enum import Enum

# Create your models here.
class Actor(models.Model):
	actor_id = models.IntegerField()
	imdb_id = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	score = models.DecimalField(max_digits=12, decimal_places=10)
	birth = models.DateTimeField(auto_now_add=False)
	birthplace = models.CharField(max_length=50)
	biography = models.CharField(max_length=1000, blank=True)
	picture = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class ProfileSize(Enum):
	w45 = 1
	w185 = 2
	h632 = 3
	original = 4
from django.db import models

# Create your models here.
class Actor(models.Model):
	actor_id = models.IntegerField()
	imdb_id = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	score = models.DecimalField(max_digits=12, decimal_places=10)
	birth = models.DateField(auto_now_add=False)
	birthplace = models.CharField(max_length=50)
	biography = models.CharField(max_length=1000)
	picture= models.CharField(max_length=50)
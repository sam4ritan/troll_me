from django.db import models

# Create your models here.
class Meme_pic(models.Model):
	description = models.CharField(max_length=200)
	ub_date = models.DateTimeField('date uploaded')
	format = models.CharField(max_length=4)
	url = models.CharField(max_length=500)

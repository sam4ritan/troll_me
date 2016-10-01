from django.db import models

# Create your models here.
class Meme_pic(models.Model):
	description = models.CharField(max_length=200)
	up_date = models.DateTimeField('date uploaded')
	format = models.CharField(max_length=4)
	mid = models.AutoField(primary_key=True)

	def __str__(self):
		return str(self.description) + str(" ") + str(self.up_date) + str(" ") + str(self.format) + str(" ") + str(self.mid)

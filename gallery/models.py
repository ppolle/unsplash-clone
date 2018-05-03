from django.db import models

# Create your models here.
class Image(models.Model):
	image_name = models.CharField(max_length = 60)
	image_description = models.TextField()
	image_location = models.ForeignKey(Location)
	image_category = models.ForeignKey(Category)
	image = models.ImageField(upload_to = 'images/')

class Location(models.Model):
	location = models.CharField(max_length = 60)


from django.db import models

# Create your models here.

class Location(models.Model):
	location = models.CharField(max_length = 60)

	def __str__(self):
		return self.location

class Category(models.Model):
	category = models.CharField(max_length = 60)

	def __str__(self):
		return self.category

class Image(models.Model):
	image_name = models.CharField(max_length = 60)
	image_description = models.TextField()
	image_location = models.ForeignKey(Location)
	image_category = models.ForeignKey(Category)
	image = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.image_name


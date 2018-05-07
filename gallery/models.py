from django.db import models

# Create your models here.

class Location(models.Model):
	location = models.CharField(max_length = 60)

	def save_location(self):
		self.save()

	def delete_location(self):
		self.delete()

	@classmethod
	def update_location(cls,id,location):
		updated_location = cls.objects.filter(pk = id).update(location = location)
		return updated_location		

	def __str__(self):
		return self.location

class Category(models.Model):
	category = models.CharField(max_length = 60)

	def save_category(self):
		self.save()

	def delete_category(self):
		self.delete()

	@classmethod
	def update_category(cls,id,category):
		category = cls.objects.filter(pk=id).update(category = category)
		return category
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

	def save_image(self):
		self.save()

	def delete_image(self):
		self.delete()

	@staticmethod
	def update_image(id,image_description,image_location,image_name,image):
		Image.objects.filter(pk=id).update(image=image,image_name=image_name,image_description=image_description,image_location = image_location)

	@classmethod
	def get_image_by_id(cls,imageId):
		image = cls.objects.get(pk = imageId)
		return image

	@classmethod
	def search_by_title(cls,search_term):
		images = cls.objects.filter(image_name__icontains = search_term)
		return images

	@classmethod
	def filter_by_location(cls,location):
		locations = cls.objects.filter(image_location = location)
		return locations
	@classmethod
	def search_image(cls,imageCategory):
		categoryImages = cls.objects.filter(image_category = imageCategory)
		return categoryImages
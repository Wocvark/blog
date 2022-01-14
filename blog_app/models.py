from django.db import models

# Create your models here.
class blog(models.Model):
	header = models.CharField(max_length=20)
	description = models.CharField(max_length=100)

	main_information = models.TextField()
	image = models.ImageField(upload_to='blog/')

	pub_date = models.DateField()

	col = models.CharField(max_length=20)

	def __str__(self):
		return self.header
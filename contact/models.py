from django.db import models

# Create your models here.
class contactForm(models.Model):

	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=500)
	message = models.CharField(max_length=10000)

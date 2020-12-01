from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class modelUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=100)
	name = models.CharField(max_length=100)


	def __str__(self):
		return f"{self.id}-{self.user}"



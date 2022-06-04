from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(max_length=255, unique=True)
	full_name = models.CharField(max_length=200, blank=True)
	avatar = models.ImageField(upload_to='accounts/avatar', null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email

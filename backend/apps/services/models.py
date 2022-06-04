from django.db import models


class Office(models.Model):
	name = models.CharField(max_length=250, unique=True)
	address = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Position(models.Model):
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Criteria(models.Model):
	position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='criterias')
	rule = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
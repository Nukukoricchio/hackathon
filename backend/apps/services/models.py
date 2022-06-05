from django.db import models


class Office(models.Model):
	name = models.CharField(max_length=250, unique=True)
	address = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Department(models.Model):
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Position(models.Model):
	department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='positions')
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def department_name(self):
		return self.department.name


class Criteria(models.Model):
	KIND_CHOICES = (
		('A', 'Phạm vi'),
		('B', 'Giá trị'),
		('C', 'Danh sách')
	)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='criterias')
	name = models.CharField(max_length=100, blank=True)
	priority = models.PositiveIntegerField(default=0)
	kind = models.CharField(max_length=5, choices=KIND_CHOICES, default='A')
	content = models.CharField(max_length=200, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.rule
from django.db import models

from apps.services.models import Position, Office


class Candidate(models.Model):
	position = models.ForeignKey(Position, on_delete=models.SET_NULL, related_name='candidates', null=True)
	# Fields can't be extracted from CV
	first_office = models.CharField(max_length=250, blank=True)
	second_office = models.CharField(max_length=250, blank=True)
	time_to_first_office = models.PositiveIntegerField(default=0)
	time_to_second_office = models.PositiveIntegerField(default=0)
	height = models.PositiveIntegerField(default=0)
	weight = models.PositiveIntegerField(default=0)
	ready_ot = models.BooleanField(default=False)
	# Fields can be extracted from CV
	info_name = models.CharField(max_length=300, blank=True)
	info_birthdate = models.CharField(max_length=50, blank=True)
	info_gender = models.CharField(max_length=20, blank=True)
	info_email = models.EmailField(max_length=255, unique=True)
	info_phone = models.CharField(max_length=20, blank=True)
	info_picture = models.ImageField(upload_to='candidate/pictures', null=True, blank=True)
	info_location_1 = models.CharField(max_length=300, blank=True)
	info_location_2 = models.CharField(max_length=300, blank=True)
	exp_period = models.CharField(max_length=200, blank=True)
	exp_company_name = models.CharField(max_length=200, blank=True)
	experience = models.JSONField(null=True, blank=True)
	exp_confident = models.CharField(max_length=100, blank=True)
	edu_school_univ = models.CharField(max_length=300, blank=True)
	edu_major = models.CharField(max_length=300, blank=True)
	education = models.JSONField(null=True, blank=True)
	others_education = models.TextField(blank=True)
	others_career_objective = models.TextField(blank=True)
	others_skills = models.TextField(blank=True)
	others_profile = models.TextField(blank=True)
	info_normalized_birthdate = models.CharField(max_length=20, blank=True)
	# Addition fields
	is_approved = models.BooleanField(default=False)
	score = models.DecimalField(max_digits=7, decimal_places=3, default=0)
	content = models.JSONField(null=True, blank=True)

	def __str__(self):
		return self.info_email

	@property
	def position_name(self):
		return self.position.name

	@property
	def gender_name(self):
		if self.info_gender == 'male':
			return 'Nam'
		elif self.info_gender == 'female':
			return 'Nữ'
		return ''


class CvFile(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='files')
	file = models.FileField(upload_to='positions/cv', null=True, blank=True)
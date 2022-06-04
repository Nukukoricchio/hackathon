from django.contrib import admin

from .models import Candidate, CvFile


class CvFileInline(admin.TabularInline):
	model = CvFile
	extra = 0


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
	list_display = ['info_email']
	inlines = [CvFileInline]


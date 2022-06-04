from django.contrib import admin

from .models import Position, Criteria, Office


class CriteriaInline(admin.TabularInline):
	model = Criteria
	extra = 0


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
	list_display = ['name']
	inlines = [CriteriaInline]


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
	list_display = ['name', 'address']

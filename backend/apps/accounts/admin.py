from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'is_active')
	list_filter = ('email', 'is_active')
	search_fields = ('email',)
	ordering = ('email',)

	fieldsets = (
	    ('Tài khoản đăng nhập', {'fields': ('email', 'password')}),
	    ('Thông tin cá nhân', {
	    	'fields': (
	    		'full_name', 'avatar'
	    	)
	    }),
	    ('Quyền và chức vụ', {
	    	'fields': (
	    		'is_superuser',  'is_active',
	    		'is_staff', 'groups', 'user_permissions'
	    	)
	    }),
	    ('Thông tin bổ sung', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
	    (None, {
	        'classes': ('wide',),
	        'fields': (
	        	'email',
	        	'password1',
	        	'password2',
	        	'full_name',
	        	'avatar'
	        ),
	    }),
	)


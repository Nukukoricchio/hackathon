from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):

	
	class Meta:
		model = User
		fields = '__all__'
		read_only_fields = ['email', 'is_superuser', 'id']


class ListUserSerializer(serializers.Serializer):
	email = serializers.EmailField()


class CustomUserListSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ['id', 'email', 'full_name']
		read_only_fields = ['id', 'email', 'full_name']

from rest_framework import serializers

from .models import Candidate, CvFile


class CandidateListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Candidate
		fields = '__all__'


class CandidateSubmitSerializer(serializers.Serializer):
	position = serializers.CharField(max_length=250)
	first_office = serializers.CharField(max_length=250)
	second_office = serializers.CharField(max_length=250)
	time_to_first_office = serializers.CharField(max_length=10, allow_blank=True)
	time_to_second_office = serializers.CharField(max_length=10, allow_blank=True)
	height = serializers.CharField(max_length=10, allow_blank=True)
	weight = serializers.CharField(max_length=10, allow_blank=True)
	ready_ot = serializers.BooleanField()
	file = serializers.FileField()


class CvFileSerializer(serializers.ModelSerializer):

	class Meta:
		model = CvFile
		fields = '__all__'


class CandidateDetailSerializer(serializers.ModelSerializer):
	files = CvFileSerializer(many=True, read_only=True)

	class Meta:
		model = Candidate
		fields = '__all__'

from rest_framework import serializers

from .models import Candidate


class CandidateListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Candidate
		fields = '__all__'


class CandidateSubmitSerializer(serializers.Serializer):
	first_office = serializers.CharField(max_length=250)
	second_office = serializers.CharField(max_length=250)
	time_to_first_office = serializers.IntegerField()
	time_to_second_office = serializers.IntegerField()
	height = serializers.IntegerField()
	weight = serializers.IntegerField()
	ready_ot = serializers.BooleanField()
	file = serializers.FileField()


class CandidateDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Candidate
		fields = '__all__'

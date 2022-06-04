from rest_framework import serializers

from .models import Office, Position, Criteria


class OfficeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Office
		fields = '__all__'


class PositionListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Position
		fields = '__all__'


class CriteriaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Criteria
		fields = '__all__'


class PositionDetailSerializer(serializers.ModelSerializer):
	criterias = CriteriaSerializer(many=True, read_only=True)

	class Meta:
		model = Position
		fields = '__all__'
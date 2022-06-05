from rest_framework import serializers

from .models import Office, Position, Criteria, Department


class OfficeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Office
		fields = '__all__'


class PositionListSerializer(serializers.ModelSerializer):
	department_name = serializers.ReadOnlyField()

	class Meta:
		model = Position
		fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
	positions = PositionListSerializer(read_only=True, many=True)

	class Meta:
		model = Department
		fields = '__all__'


class CriteriaSerializer(serializers.ModelSerializer):
	get_kind_display = serializers.ReadOnlyField()

	class Meta:
		model = Criteria
		fields = '__all__'


class PositionDetailSerializer(serializers.ModelSerializer):
	criterias = CriteriaSerializer(many=True, read_only=True)
	department_name = serializers.ReadOnlyField()

	class Meta:
		model = Position
		fields = '__all__'
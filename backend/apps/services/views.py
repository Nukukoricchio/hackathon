from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from .models import Office, Position, Criteria, Department
from .serializers import OfficeSerializer, PositionListSerializer, \
                        PositionDetailSerializer, CriteriaSerializer, DepartmentSerializer


class OfficeListView(generics.ListCreateAPIView):
	permission_classes = [AllowAny]
	queryset = Office.objects.all()
	serializer_class = OfficeSerializer


class OfficeDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Office.objects.all()
	serializer_class = OfficeSerializer


class DepartmentListView(generics.ListCreateAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer


class PositionListView(generics.ListCreateAPIView):
	permission_classes = [AllowAny]
	queryset = Position.objects.all()
	serializer_class = PositionListSerializer


class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Position.objects.all()
	serializer_class = PositionDetailSerializer


class CriteriaListView(generics.ListCreateAPIView):
	queryset = Criteria.objects.all()
	serializer_class = CriteriaSerializer


class CriteriaDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Criteria.objects.all()
	serializer_class = CriteriaSerializer
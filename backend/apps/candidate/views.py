import json
import base64

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.core.files.base import ContentFile

from .models import Position, Candidate
from .serializers import CandidateListSerializer, CandidateSubmitSerializer, CandidateDetailSerializer
from .utils import process_cv


class CandidateListView(generics.ListCreateAPIView):
	queryset = Candidate.objects.all()
	serializer_class = CandidateListSerializer


class CandidateUploadView(APIView):

	def post(self, request, format=None):
		data = request.FILES.getlist('files')
		for file in data:
			process_cv(file)
		message = {
		    'message': 'OK'
		}
		return Response(message, status=status.HTTP_200_OK)


class CandidateSubmitView(APIView):
	permission_classes = [AllowAny]

	def post(self, request, format=None):
		serializer = CandidateSubmitSerializer(data=request.data)
		if serializer.is_valid():
			data = serializer.validated_data
			first_office = data['first_office']
			second_office = data['second_office']
			time_to_first_office = data['time_to_first_office']
			time_to_second_office = data['time_to_second_office']
			height = data['height']
			weight = data['weight']
			ready_ot = data['ready_ot']
			file = data['file']
			candidate = process_cv(file)
			if candidate:
				candidate.first_office = first_office
				candidate.second_office = second_office
				candidate.time_to_first_office = time_to_first_office
				candidate.time_to_second_office = time_to_second_office
				candidate.height = height
				candidate.ready_ot = ready_ot
				candidate.height = height

			message = {
			    'message': 'OK'
			}
			return Response(message, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Candidate.objects.all()
	serializer_class = CandidateDetailSerializer

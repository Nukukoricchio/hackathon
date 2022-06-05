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
from .ranking import ITRanker, SaleRanker


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
			position = data['position']
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
				if candidate.time_to_first_office:
				    candidate.time_to_first_office = int(time_to_first_office)
				if candidate.time_to_second_office:
					candidate.time_to_second_office = int(time_to_second_office)
				if candidate.height:
					candidate.height = int(height)
				if candidate.weight:
					candidate.weight = int(weight)
				candidate.ready_ot = ready_ot

				position = get_object_or_404(Position, name=position)
				candidate.position = position

				candidate.save()

			message = {
			    'message': 'OK'
			}
			return Response(message, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Candidate.objects.all()
	serializer_class = CandidateDetailSerializer


class CandidateRankView(APIView):

	def post(self, request, format=None):
		position = request.data.get('position')
		if data:
			position = get_object_or_404(Position, name=position)
			if position.department_name == 'Phòng IT':
				sample_filter = {
			        "req_gender": {
			            "gender": "male",
			            "priority": "5"
			        },
			        "req_position": {
			            "position": "Software Engineer",
			            "priority": "4"
			        },
			        "req_seniority": {
			            "seniority": "Senior",
			            "priority": "3",
			        },
			        "req_age": {
			            "min": 18,
			            "max": 29,
			            "priority": "1"
			        },
			        "req_skills": {
			            "skills": ["English", "Planning", "API"],
			            "priority": "2"
			        },
			        "req_company": {
			            "company": ["Google", "Microsoft", "Facebook"],
			            "priority": "5"
			        },
			        "req_university": {
			            "university": ["Harvard", "Stanford", "MIT"],
			            "priority": "4"
			        }
			    }
				ranker = ITRanker(sample_filter, device="cuda:0")
				cv_list = [json.load(open("cv_14.json"))] * 100
				print([ranked[1] for ranked in ranker.rank(cv_list)])
			    
			elif position.department_name == 'Phòng Kinh doanh':
				pass
			else:
				print('ERROR!!!')

			return Response(status=status.HTTP_200_OK)

		return Response(status=status.HTTP_400_BAD_REQUEST)

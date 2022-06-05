import json
import base64

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.core.files.base import ContentFile
import torch

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
		if position:
			position = get_object_or_404(Position, name=position)
			device = 'cpu' if not torch.cuda.is_available() else 'cuda'
			if position.department_name == 'Phòng IT':
				criterias = position.criterias.all()
				sample_filter = {}
				for criteria in criterias:
					if criteria.name == 'Giới tính':
						if criteria.content == 'Nam':
							gender = 'male'
						elif criteria.content == 'Nữ':
							gender = 'female'
						else:
							gender = ''
						sample_filter["req_gender"] = {
						    "gender": gender,
						    "priority": criteria.priority
						}
					elif criteria.name == "Trình độ":
						sample_filter["req_seniority"] = {
						    "seniority": criteria.content,
			                "priority": criteria.priority,
						}
					elif criteria.name == 'Tuổi':
						sample_filter["req_age"] = {
						    "min": int(criteria.content.split(';')[0]),
						    "max": int(criteria.content.split(';')[1]),
			                "priority": criteria.priority,
						}
					elif criteria.name == "Kỹ năng":
						sample_filter["req_skills"] = {
						    "skills": criteria.content.split(';'),
			                "priority": criteria.priority,
						}
					elif criteria.name == "Công ty":
						sample_filter["req_company"] = {
						    "company": criteria.content.split(';'),
			                "priority": criteria.priority,
						}
					elif criteria.name == "Trường đại học":
						sample_filter["req_university"] = {
						    "university": criteria.content.split(';'),
			                "priority": criteria.priority,
						}
				sample_filter["req_position"] = {
				    "position": position.name,
				    "priority": 4
				}
				# sample_filters = {
				#     "req_gender": {
				#         "gender": "male",
				#         "priority": "5"
				#     },
				#     "req_position": {
				#         "position": "Software Engineer",
				#         "priority": "4"
				#     },
				#     "req_seniority": {
				#         "seniority": "Senior",
				#         "priority": "3",
				#     },
				#     "req_age": {
				#         "min": 18,
				#         "max": 29,
				#         "priority": "1"
				#     },
				#     "req_skills": {
				#         "skills": ["English", "Planning", "API"],
				#         "priority": "2"
				#     },
				#     "req_company": {
				#         "company": ["Google", "Microsoft", "Facebook"],
				#         "priority": "5"
				#     },
				#     "req_university": {
				#         "university": ["Harvard", "Stanford", "MIT"],
				#         "priority": "4"
				#     }
				# }
				# print('s1', sample_filter)
				# print('s2', sample_filters)
				ranker = ITRanker(sample_filter, device=device)
				candidates = position.candidates.all()
				if len(candidates) == 0:
					return Response(status=status.HTTP_200_OK)

				cv_list = [candidate.content for candidate in candidates]
				scores = ranker.rank(cv_list)
				print('scores ', scores)
				for i in range(len(candidates)):
					candidates[i].score = scores[i]
					candidates[i].save()
				candidates = candidates.order_by('-score')
				serializer = CandidateListSerializer(candidates, many=True)
				return Response(serializer.data, status=status.HTTP_200_OK)

			elif position.department_name == 'Phòng Kinh doanh':
				pass
			else:
				print('ERROR!!!')

			return Response(status=status.HTTP_200_OK)

		return Response(status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .serializers import CustomUserSerializer

User = get_user_model()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = CustomUserSerializer


class UserInformation(APIView):

	def get(self, request, format=None):
		if request.user:
			serializer = CustomUserSerializer(request.user)
			data = {
			    'info': serializer.data
			}
			return Response(data)

		return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, format=None):
		if request.user:
			serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)

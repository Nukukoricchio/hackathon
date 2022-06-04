from django.urls import path

from . import views


urlpatterns = [
	path('list/', views.CandidateListView.as_view()),
	path('submit/', views.CandidateSubmitView.as_view()),
	path('upload/', views.CandidateUploadView.as_view()),
	path('<int:pk>/', views.CandidateDetailView.as_view()),
]
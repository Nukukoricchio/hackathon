from django.urls import path

from . import views


urlpatterns = [
	path('office/', views.OfficeListView.as_view()),
	path('office/<int:pk>/', views.OfficeDetailView.as_view()),
	path('position/', views.PositionListView.as_view()),
	path('position/<int:pk>/', views.PositionDetailView.as_view()),
	path('criteria/', views.CriteriaListView.as_view()),
	path('criteria/<int:pk>/', views.CriteriaDetailView.as_view())
]
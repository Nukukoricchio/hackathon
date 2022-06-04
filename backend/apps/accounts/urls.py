from django.urls import path

from . import views


urlpatterns = [
    path('information/', views.UserInformation.as_view()),
    path('detail/<int:pk>/', views.UserDetailView.as_view()),
]
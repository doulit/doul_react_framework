from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
	path('<int:question_id>/', views.search),
    path('sel/<str:question_str>/', views.search),
    path('save/<str:question_str>/', views.save),	


]


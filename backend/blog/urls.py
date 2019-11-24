from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
	
    path('sel/', views.search),
    path('save/<str:question_str>/', views.save),	


]


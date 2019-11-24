from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
	
    path('index/', views.index),
    path('detail/<str:question_str>/', views.detail),
    path('save/', views.save),	


]


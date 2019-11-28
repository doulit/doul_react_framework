from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
    path('sel/', views.MasterBlog.as_view()),
    path('sel/<int:pk>/', views.DetailBlog.as_view()),
    path('save/', views.SaveBlog),	
]


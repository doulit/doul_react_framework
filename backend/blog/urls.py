from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
    path('sel/', views.search.as_view()),
    path('sel/<int:pk>/', views.DetailPost.as_view()),
    path('save/', views.save),	
]


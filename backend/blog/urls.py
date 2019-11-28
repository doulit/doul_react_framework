from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
    path('sel/all/', views.search.as_view()),
    path('detail/sel/<int:pk>/', views.DetailPost.as_view()),
    path('save/<str:question_str>/', views.save),	


]


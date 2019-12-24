from django.urls import path
from . import views

# from rest_framework import routers

app_name = 'blog'

urlpatterns = [
    path('sel/', views.MasterBlog.as_view()),
    path('sel/<int:pk>/', views.DetailBlog.as_view()),    
    path('save/', views.SaveBlog.as_view()),

    path('menu/sel/', views.MasterMenu.as_view()),
    path('menu/sel/<int:pk>/', views.DetailMenu.as_view()),
    path('menu/save/', views.SaveMenu.as_view()),

    path('category/sel/', views.MasterCategory.as_view()),
    path('category/sel/<int:pk>/', views.DetailCategory.as_view()),
    path('category/save/', views.SaveCategory.as_view()),
]



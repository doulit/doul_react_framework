#backend/blog/serializers.py
from rest_framework import serializers
from .models import Blog,Menu,Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Blog

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Menu

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
  
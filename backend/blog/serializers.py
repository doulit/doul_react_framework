#backend/blog/serializers.py
from rest_framework import serializers
from .models import Blog

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Blog

    
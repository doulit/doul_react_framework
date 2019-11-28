from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from backend.decorators import api_view
from backend.utils import errors_message
from .form import blog_Form
from .models import Blog
from backend.utils import execute,execute_and_serialize
from .serializers import PostSerializer
from rest_framework import generics


# Create your views here.
class search(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

@api_view
def save(request, question_str):
    print(request.JSON)
    form = blog_Form(request.JSON)
    if request.method == 'POST':
        if form.is_valid():
            print("save_start")
            blog = blog_Form.save(commit=False)
            requestJson = request.JSON
            blog.surname = requestJson['surname']
            blog.save()
            return ""      
        else:
            print("error2")
            return errors_message(form)
    else:
        print("error1")
        return errors_message(form)


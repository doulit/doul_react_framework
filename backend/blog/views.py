from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from backend.decorators import api_view
from backend.utils import errors_message,success_message
from .form import blog_Form
from .models import Blog
from backend.utils import execute,execute_and_serialize
from .serializers import BlogSerializer
from rest_framework import generics

# Create your views here.
class MasterBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

@api_view
def SaveBlog(request):    
    form = blog_Form(request.JSON)
    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)
    elif request.method == 'DELETE':
        if form.is_valid():            
            blog = form.delete(commit=False)
            blog.delete()
            return success_message()      
        else:
            print(errors_message(form))
            return errors_message(form)        
    else:
        return errors_message(form)

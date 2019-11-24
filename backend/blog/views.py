from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from .models import Blog
from backend.utils import execute,execute_and_serialize

# Create your views here.
def index(request):
    
    qs = Blog.objects.all()

    return execute_and_serialize(qs)

def detail(request, question_str):
    
    qs = Blog.objects.all()
    question = get_object_or_404(Blog, pk=question_str)
    print(question)
    # qs = Blog.objects.filter('Title={question_str}')

    return execute_and_serialize(qs)

def save(request):
    if request.method == 'POST':
        # Feedback 객체 생성
        fb = Blog(Title = 'Kim', Content = 'kim@test.com')
        
        # 새 객체 INSERT
        fb.save()

        qs = Blog.objects.all()

        return execute_and_serialize(qs)

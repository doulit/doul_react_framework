from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from .models import Blog
from backend.utils import execute,execute_and_serialize

# Create your views here.
def search(request):
    
    qs = Blog.objects.all()

    return execute_and_serialize(qs)


def save(request, question_str):
    print(request.method)
    # if request.method == 'POST':
    # Feedback 객체 생성
    
    # # 일괄 delete 요청
    # queryset = Blog.objects.all()
    # queryset.delete() 
    # # 일괄 delete 요청

    # fb = Blog(Title = 'Kim', Content = 'kim@test.com', name = 'Mehmet', surname = 'Baran')
    # fb2 = Blog(Title = 'Kim', Content = 'kim@test.com', name = 'Zerya Betül', surname = 'Baran')
    # # 새 객체 INSERT
    # fb.save()
    # fb2.save()

    qs = Blog.objects.all()

    return execute_and_serialize(qs)

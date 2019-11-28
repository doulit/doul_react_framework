from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from backend.decorators import api_view
from backend.utils import errors_message
from .form import blog_Form

# Create your views here.
@api_view
def search(request, question_str):
    form = blog_Form(request.POST)
    if form.is_valid():        
        return form.fetch()
    else:
        return errors_message(form)
@api_view
def save(request, question_str):
    form = blog_Form(request.JSON)
    if request.method == 'POST':
        if form.is_valid():
            return form.save()        
        else:
            return errors_message(form)
    else:
        return errors_message(form)


from django import forms
from django.shortcuts import get_object_or_404, render
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from backend.utils import execute,execute_and_serialize
from .models import Blog
import json

class blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields='__all__'        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"] = forms.CharField(
            required=False,
        )
        for field_name, field in self.fields.items():
            field.required = False
    
    def delete(self, commit=True):
        self.instance = Blog(**self.cleaned_data)
        if commit:
            self.instance.delete()
        return self.instance

    ''' 내부적으로 구현되어 있음 (멤버변수 인스턴스)
    향후 수정 기능 구현시 활용
    def save(self, commit=True):
        self.instance = Blog(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    '''
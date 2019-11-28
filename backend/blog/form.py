from django import forms
from django.shortcuts import get_object_or_404, render
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from backend.utils import execute,execute_and_serialize
from .models import Blog

class blog_Form(forms.Form):
    Title = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
                                label="Title", help_text="")
    Content = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
                                label="Content", help_text="")
    name = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
                                label="name", help_text="")
    surname = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
                                label="surname", help_text="")
    # tableData = forms.ALL_FIELDS(required=False)


    def fetch(self):
        Title = self.cleaned_data['Title']
        print("==fetch==")        
        qs = Blog.objects.all()
        # blog = get_object_or_404(Blog, pk=question_id)
        # selected_choice = blog.choice_set.get(pk=request.POST['choice'])
 

        return execute_and_serialize(qs)
    
    def save(self):
        Title = self.cleaned_data['Title']
        Content = self.cleaned_data['Content']
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        tableData = self.cleaned_data['tableData']
        print(tableData)
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
from django import forms
from django.shortcuts import get_object_or_404, render
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from backend.utils import execute,execute_and_serialize
from .models import Blog
import json

class blog_Form(forms.ModelForm):
    # Title = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
    #                             label="Title", help_text="")
    # Content = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
    #                             label="Content", help_text="")
    # name = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
    #                             label="name", help_text="")
    # surname = forms.CharField(validators=[MaxLengthValidator(50)],required=False,
    #                             label="surname", help_text="")
    
    class Meta:
        model = Blog
        fields='__all__'

    def fetch(self):
        print("==fetch==")        
        qs = Blog.objects.all()
        # blog = get_object_or_404(Blog, pk=question_id)
        # selected_choice = blog.choice_set.get(pk=request.POST['choice'])
 

        return execute_and_serialize(qs)
    
    ''' 내부적으로 구현되어 있음 (멤버변수 인스턴스)
		향후 수정 기능 구현시 활용
	def save(self, commit=True):
		self.instance = Post(**self.cleaned_data)
		if commit:
			self.instance.save()
		return self.instance
	'''

    
    '''
    def save(self, commit=True):
        Title = self.cleaned_data['Title']
        Content = self.cleaned_data['Content']
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        tableData = self.cleaned_data['tableData']
        print(tableData)
        json_data = json.dumps(tableData) #loads string as json
        json_data2 = json.loads(json_data)
        print(type(json_data))
        # print(str(json_data2["id"]))
        print(json_data2)

        # data = {'number':1}
        # json_data = json.dumps(data)
        # print(json_data['number'])
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
    '''
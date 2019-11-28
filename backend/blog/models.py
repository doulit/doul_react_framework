from django.db import models
from backend.utils import execute,execute_and_serialize,errors_message
from django.core.validators import ValidationError # validation
import re

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Blog(models.Model):
    Title = models.CharField('TITLE', max_length=50)
    Content = models.CharField('CONTENT', max_length=50)
    createDate = models.DateTimeField('createDate',auto_now=True)

    name = models.CharField('name', max_length=50, null=True)
    surname = models.CharField('surname', max_length=50, null=True)
    birthYear = models.IntegerField('birthYear', null=True)
    birthCity = models.CharField('birthCity', max_length=50, null=True)
    lnglat = models.CharField(max_length=50, blank=True, null=True,
        validators = [lnglat_validator], # 함수를 넘겨서 유효성 검사 실행
        help_text='경도, 위도 포맷으로 입력')

    def __str__(self):
        return "%s %s" %(self.name, self.text)

    def choice_set(self):
        qs_list = Blog.objects.filter(id=self.pk)
        # return execute(qs_list)
        return qs_list



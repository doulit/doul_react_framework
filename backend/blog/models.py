from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField('TITLE', max_length=50)
    Content = models.CharField('CONTENT', max_length=50)
    createDate = models.DateTimeField('createDate',auto_now=True)

    name = models.CharField('name', max_length=50, null=True)
    surname = models.CharField('surname', max_length=50, null=True)
    birthYear = models.IntegerField('birthYear', null=True)
    birthCity = models.CharField('birthCity', max_length=50, null=True)


    def __str__(self):
        return self.Title

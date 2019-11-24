from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField('TITLE', max_length=50)
    Content = models.CharField('CONTENT', max_length=50)
    createDate = models.DateTimeField('createDate',auto_now=True)


    def __str__(self):
        return self.Title

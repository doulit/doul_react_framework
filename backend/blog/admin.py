from django.contrib import admin
 
# Register your models here.
from .models import Category,Blog,Menu
from mptt.admin import DraggableMPTTAdmin    # 관리자페이지에서 카테고리를 트리형식으로
 
admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Blog)
admin.site.register(Menu)
from django.contrib import admin

# Register your models here.

# admin 페이지에 Article 모델 등록
from .models import Article
admin.site.register(Article)


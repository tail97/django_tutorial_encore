from django.contrib import admin

# Register your models here.

# admin 페이지에 Article 모델 등록, 한번은 꼭 해줘야 실행이된다
from .models import Article
admin.site.register(Article)


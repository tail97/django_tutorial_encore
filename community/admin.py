from django.contrib import admin
from django.contrib import admin
from community import models

# Register your models here.

# admin 페이지에 Article 모델 등록, 한번은 꼭 해줘야 실행이된다
class ArticleAdmin(admin.ModelAdmin):
# fields = ['name', 'title', 'contents', 'url', 'email', 'owner']
    fieldsets = [
        ('제목' , {'fields': ['title']}), 
        ('내용', {'fields':['contents']}), 
        ('작성자 정보', {'fields':['name', 'url', 'email']}),
        ('작성자 id', {'fields':['owner'], 'classes':['collapse']}), 
    ]
    list_display = ('pk', 'title', 'url', 'cdate')
    list_filter = ['cdate']
    search_fields = ['title', 'contents']


    


admin.site.register(models.Article,ArticleAdmin)


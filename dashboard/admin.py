from django.contrib import admin

# Register your models here.
from .models import CountryData


from community import models

# Register your models here.

# admin 페이지에 Article 모델 등록, 한번은 꼭 해줘야 실행이된다
class  CountryAdmin(admin.ModelAdmin):
# fields = ['name', 'title', 'contents', 'url', 'email', 'owner']
    fieldsets = [
        ('국가' , {'fields': ['country']}), 
        ('인구', {'fields':['population']}), 
        # ('작성자 정보', {'fields':['name', 'url', 'email']}),
        # ('작성자 id', {'fields':['owner'], 'classes':['collapse']}), 
    ]
    list_display = ('country','population')
    list_filter = ['country']
    search_fields = ['country', 'population']


    
# admin 페이지에 CountryData 데이터 모델 등록
admin.site.register(CountryData, CountryAdmin)
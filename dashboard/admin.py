from django.contrib import admin

# Register your models here.
from .models import CountryData

# admin 페이지에 CountryData 데이터 모델 등록
admin.site.register(CountryData)
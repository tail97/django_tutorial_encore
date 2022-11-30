from django.db import models

# Create your models here.

class Article(models.Model): #클래스를 만들어서 DB를 입력할 입력란을 구현
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    url =models.URLField()
    email = models.EmailField()
    cdate = models.DateField(auto_now_add= True)
